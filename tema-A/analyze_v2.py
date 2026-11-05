"""Análise v2: medidas sem teto mecânico, termo de comparação por residência, bootstrap por agrupamento.

Uso:
  python analyze_v2.py                       # análise principal (macro-destinos -> NUTS III principal)
  python analyze_v2.py --alocacao fracionaria # macro-destinos repartidos por igual pelas NUTS III abrangidas
  python analyze_v2.py --alocacao excluir     # macro-destinos fora da análise por NUTS III
  python analyze_v2.py --sem-ilhas            # sensibilidade sem Açores e Madeira
  python analyze_v2.py --bootstrap 5000       # reamostragens (por omissão 2000)

Entradas: data/extracoes_v2.jsonl (de reprocess.py), data/respostas.jsonl, data/dormidas_2025_nuts3.csv (de fetch_eurostat.py).
Saídas em results_v2/: metricas.csv, quotas.csv, roteiro_noites.csv, homogeneizacao.csv, relatorio.md.

Medidas por resposta (cada resposta é um vetor de quotas que soma 1):
  presenca  : 1 por NUTS III presente nos destinos principais (medida do piloto; tem teto 1/k)
  posicao   : exposição ponderada pela posição, 1/log2(ordem+1) na primeira ocorrência de cada NUTS III (sem teto)
  mencoes   : todas as menções (destinos e atrações)
  noites    : só roteiros; dias atribuídos a cada paragem, lidos dos cabeçalhos "Dia N"
Termo de comparação: dormidas 2025 de não residentes para EN/ES/FR e de residentes para PT ("lingua"), e total ("total").
Incerteza: bootstrap por agrupamento (células modelo × língua reamostradas com reposição; dentro de cada célula, respostas
com reposição). Intervalos percentílicos a 95%.
"""
import argparse
import csv
import json
import math
import random
import re
from collections import Counter, defaultdict
from pathlib import Path

AQUI = Path(__file__).parent
RES = AQUI / "results_v2"
ILHAS = {"Região Autónoma dos Açores", "Região Autónoma da Madeira"}
DIA = re.compile(r"^\W*(?:\*\*|#+\s*)?\s*(?:dia|day|d[ií]a|jour)s?\s*(\d+)(?:\s*(?:[-–—a]|to|à|al|et|y|e|and)\s*(\d+))?\b[^\n]*",
                 re.I | re.M)


# ---------- utilitários ----------
def gini(v, corrigido=False):
    v = sorted(v); n = len(v); s = sum(v)
    if n == 0 or s == 0:
        return float("nan")
    g = sum((2 * (i + 1) - n - 1) * x for i, x in enumerate(v)) / (n * s)
    return g * n / (n - 1) if corrigido else g


def entropia_eff(p):
    return math.exp(-sum(x * math.log(x) for x in p if x > 0))


def ranks(v):
    s = sorted(range(len(v)), key=lambda i: v[i]); r = [0.0] * len(v); i = 0
    while i < len(v):
        j = i
        while j + 1 < len(v) and v[s[j + 1]] == v[s[i]]:
            j += 1
        for k in range(i, j + 1):
            r[s[k]] = (i + j) / 2 + 1
        i = j + 1
    return r


def pearson(x, y):
    mx, my = sum(x) / len(x), sum(y) / len(y)
    sxy = sum((a - mx) * (b - my) for a, b in zip(x, y))
    sxx = sum((a - mx) ** 2 for a in x); syy = sum((b - my) ** 2 for b in y)
    return sxy / math.sqrt(sxx * syy) if sxx > 0 and syy > 0 else float("nan")


def spearman(x, y):
    return pearson(ranks(x), ranks(y))


def declive_loglog(p, q, n_resp):
    """Elasticidade da quota LLM face à quota de dormidas, com pseudo-contagem para os zeros."""
    k = len(p)
    ps = [(x * n_resp + 0.5) / (n_resp + 0.5 * k) for x in p]
    xs = [math.log(b) for b in q]; ys = [math.log(a) for a in ps]
    mx, my = sum(xs) / k, sum(ys) / k
    return sum((a - mx) * (b - my) for a, b in zip(xs, ys)) / sum((a - mx) ** 2 for a in xs)


def jsd(p, q):
    m = [(a + b) / 2 for a, b in zip(p, q)]
    def kl(a, b):
        return sum(x * math.log2(x / y) for x, y in zip(a, b) if x > 0)
    return 0.5 * kl(p, m) + 0.5 * kl(q, m)


def tvd(p, q):
    return 0.5 * sum(abs(a - b) for a, b in zip(p, q))


def media_vetores(vs, nuts):
    n = len(vs)
    return [sum(v.get(x, 0.0) for v in vs) / n for x in nuts] if n else [0.0] * len(nuts)


def normaliza(d):
    s = sum(d.values())
    return {k: v / s for k, v in d.items()} if s > 0 else {}


# ---------- construção das medidas por resposta ----------
def alocacao(item, modo):
    """Devolve {nuts3: peso} para um item extraído, segundo o modo de tratamento dos macro-destinos."""
    ng = item.get("nivel_geo")
    if ng == "titulo" or not item.get("existe", True) or item.get("nuts3") is None:
        return {}
    if ng == "macro":
        if modo == "excluir":
            return {}
        if modo == "fracionaria":
            abr = item["nuts3_abrangidas"]
            return {n: 1 / len(abr) for n in abr}
    return {item["nuts3"]: 1.0}


def medidas_resposta(itens, texto, modo):
    """itens: extrações de uma resposta, por ordem de posição. Devolve {medida: {nuts3: quota}}."""
    itens = sorted(itens, key=lambda e: e.get("posicao", 0))
    dest = [e for e in itens if e.get("nivel", "destino") == "destino"]
    pres, pos, men = defaultdict(float), defaultdict(float), defaultdict(float)
    ordem = 0; vistos = set()
    for e in dest:
        al = alocacao(e, modo)
        if not al:
            continue
        ordem += 1
        for n, w in al.items():
            pres[n] = max(pres[n], w)
            if n not in vistos:
                pos[n] += w / math.log2(ordem + 1)
        vistos.update(al)
    for e in itens:
        for n, w in alocacao(e, modo).items():
            men[n] += w
    out = {"presenca": normaliza(pres), "posicao": normaliza(pos), "mencoes": normaliza(men)}
    noites = noites_roteiro(dest, itens, texto, modo)
    if noites:
        out["noites"] = noites
    return out


def noites_roteiro(dest, itens, texto, modo):
    cab = list(DIA.finditer(texto))
    if len(cab) < 3:
        return {}
    nomes = [(e["lugar"].lower(), alocacao(e, modo)) for e in dest if alocacao(e, modo)]
    todos = [(e["lugar"].lower(), alocacao(e, modo)) for e in itens if alocacao(e, modo)]
    dias = defaultdict(float); ultimo = None
    for k, h in enumerate(cab):
        fim = cab[k + 1].start() if k + 1 < len(cab) else min(len(texto), h.end() + 600)
        cabecalho = h.group(0).lower(); segmento = texto[h.start():fim].lower()
        d1 = int(h.group(1)); d2 = int(h.group(2)) if h.group(2) else d1
        nd = max(1, min(d2, 21) - d1 + 1)
        al = next((a for nm, a in nomes if nm and nm in cabecalho), None) \
            or next((a for nm, a in nomes if nm and nm in segmento), None) \
            or next((a for nm, a in todos if nm and nm in cabecalho), None) or ultimo
        if not al:
            continue
        for n, w in al.items():
            dias[n] += nd * w
        ultimo = al
    return normaliza(dias)


# ---------- métricas de grupo ----------
def jaccard_medio(vs, limite=150):
    """Jaccard médio entre pares de respostas (conjuntos de NUTS III). Acima de `limite` respostas usa uma amostra de pares."""
    conj = [frozenset(k for k, v in d.items() if v > 0) for d in vs]
    n = len(conj)
    if n < 2:
        return float("nan")
    if n <= limite:
        pares = [(i, j) for i in range(n) for j in range(i + 1, n)]
    else:
        rng = random.Random(7)
        pares = [(rng.randrange(n), rng.randrange(n)) for _ in range(limite * limite // 2)]
        pares = [(i, j) for i, j in pares if i != j]
    jac = [len(conj[i] & conj[j]) / len(conj[i] | conj[j]) for i, j in pares if conj[i] | conj[j]]
    return sum(jac) / len(jac) if jac else float("nan")


def metricas(vs, nuts, q_bench, n_resp, com_jaccard=True):
    p = media_vetores(vs, nuts); q = [q_bench[n] for n in nuts]
    return {"effN": entropia_eff(p), "gini": gini(p), "gini_corr": gini(p, True),
            "top3": sum(sorted(p, reverse=True)[:3]),
            "jaccard": jaccard_medio(vs) if com_jaccard else float("nan"),
            "declive": declive_loglog(p, q, n_resp), "spearman": spearman(p, q),
            "jsd": jsd(p, q), "tvd": tvd(p, q), "n_regioes_zero": sum(1 for x in p if x == 0)}


def bench_grupo(resps, qF, qD, qT, modo_bench, nuts):
    if modo_bench == "total":
        return qT
    n = len(resps); w_pt = sum(1 for r in resps if r["lang"] == "pt") / n
    return {x: w_pt * qD[x] + (1 - w_pt) * qF[x] for x in nuts}


def bootstrap(resps, vetores, medida, nuts, qF, qD, qT, modo_bench, B, rng, regioes):
    """Reamostra células modelo×língua e, dentro delas, respostas. Devolve distribuições de métricas e rácios."""
    celulas = defaultdict(list)
    for r in resps:
        if medida in vetores[r["id"]]:
            celulas[(r["modelo"], r["lang"])].append(r)
    chaves = list(celulas)
    dist = defaultdict(list)
    for _ in range(B):
        amostra = []
        for c in rng.choices(chaves, k=len(chaves)):
            lst = celulas[c]
            amostra.extend(rng.choices(lst, k=len(lst)))
        vs = [vetores[r["id"]][medida] for r in amostra]
        q = bench_grupo(amostra, qF, qD, qT, modo_bench, nuts)
        m = metricas(vs, nuts, q, len(vs), com_jaccard=len(vs) <= 100)
        for k in ("effN", "declive", "jsd", "jaccard", "top3", "spearman"):
            dist[k].append(m[k])
        p = media_vetores(vs, nuts)
        for n in regioes:
            i = nuts.index(n)
            dist[("racio", n)].append(((p[i] * len(vs) + 0.5) / (len(vs) + 0.5 * len(nuts))) / q[n])
            dist[("quota", n)].append(p[i])
    return dist


def ic(xs, a=0.025):
    s = sorted(x for x in xs if not (isinstance(x, float) and math.isnan(x)))
    if not s:
        return (float("nan"), float("nan"))
    return s[int(a * (len(s) - 1))], s[int((1 - a) * (len(s) - 1))]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--alocacao", choices=["principal", "fracionaria", "excluir"], default="principal")
    ap.add_argument("--sem-ilhas", action="store_true")
    ap.add_argument("--bootstrap", type=int, default=2000)
    ap.add_argument("--semente", type=int, default=2026)
    ap.add_argument("--dormidas", default=str(AQUI / "data" / "dormidas_2025_nuts3.csv"))
    ap.add_argument("--saida", default=str(RES))
    a = ap.parse_args()
    out = Path(a.saida); out.mkdir(exist_ok=True)
    rng = random.Random(a.semente)

    with open(a.dormidas, encoding="utf-8") as f:
        dl = list(csv.DictReader(f))
    nuts = [r["nuts3"] for r in dl if not (a.sem_ilhas and r["nuts3"] in ILHAS)]
    def q(col):
        tot = sum(float(r[col]) for r in dl if r["nuts3"] in nuts)
        return {r["nuts3"]: float(r[col]) / tot for r in dl if r["nuts3"] in nuts}
    qT, qF, qD = q("total"), q("nao_residentes"), q("residentes")

    resps = [json.loads(l) for l in (AQUI / "data" / "respostas.jsonl").read_text(encoding="utf-8").splitlines()]
    extr = [json.loads(l) for l in (AQUI / "data" / "extracoes_v2.jsonl").read_text(encoding="utf-8").splitlines()]
    if a.sem_ilhas:
        extr = [e for e in extr if e.get("nuts3") not in ILHAS]
    por_resp = defaultdict(list)
    for e in extr:
        por_resp[e["id"]].append(e)
    vetores = {r["id"]: medidas_resposta(por_resp.get(r["id"], []), r["resposta"], a.alocacao) for r in resps}

    templates = sorted({r["template"] for r in resps})
    grupos = [("total", "todos", resps)] + [("template", t, [r for r in resps if r["template"] == t]) for t in templates]
    for t in templates:
        for m in sorted({r["modelo"] for r in resps}):
            grupos.append((f"template_modelo", f"{t}|{m}", [r for r in resps if r["template"] == t and r["modelo"] == m]))
        for l in sorted({r["lang"] for r in resps}):
            grupos.append((f"template_lang", f"{t}|{l}", [r for r in resps if r["template"] == t and r["lang"] == l]))
    medidas = ["presenca", "posicao", "mencoes", "noites"]
    regioes_destaque = ["Grande Lisboa", "Algarve", "Área Metropolitana do Porto", "Região Autónoma da Madeira",
                        "Douro", "Alentejo Central", "Região de Coimbra", "Oeste"]
    regioes_destaque = [n for n in regioes_destaque if n in nuts]

    fm = open(out / "metricas.csv", "w", encoding="utf-8-sig", newline="")
    fq = open(out / "quotas.csv", "w", encoding="utf-8-sig", newline="")
    wm, wq = csv.writer(fm, delimiter=";"), csv.writer(fq, delimiter=";")
    wm.writerow(["medida", "benchmark", "dimensao", "grupo", "n_respostas", "k_medio", "effN", "effN_lo", "effN_hi",
                 "gini", "gini_corr", "top3", "top3_lo", "top3_hi", "jaccard", "jaccard_lo", "jaccard_hi",
                 "declive", "declive_lo", "declive_hi", "spearman", "jsd", "jsd_lo", "jsd_hi", "tvd",
                 "n_regioes_zero", "effN_dormidas", "gini_dormidas"])
    wq.writerow(["medida", "benchmark", "dimensao", "grupo", "nuts3", "quota_llm", "quota_llm_lo", "quota_llm_hi",
                 "quota_dormidas", "racio", "racio_lo", "racio_hi", "diferenca_pp", "pct_respostas_presente"])
    relatorio = {}
    for medida in medidas:
        for dim, g, rs in grupos:
            rs_m = [r for r in rs if medida in vetores[r["id"]]]
            if len(rs_m) < 5:
                continue
            vs = [vetores[r["id"]][medida] for r in rs_m]
            k_medio = sum(len(v) for v in vs) / len(vs)
            p = media_vetores(vs, nuts)
            pres_pct = {n: sum(1 for v in vs if v.get(n, 0) > 0) / len(vs) for n in nuts}
            for bench in ("lingua", "total"):
                qb = bench_grupo(rs_m, qF, qD, qT, bench, nuts)
                m = metricas(vs, nuts, qb, len(vs))
                faz_boot = dim in ("total", "template") or (dim == "template_modelo" and medida in ("posicao", "noites"))
                d = bootstrap(rs_m, vetores, medida, nuts, qF, qD, qT, bench, a.bootstrap if faz_boot else 0, rng,
                              nuts if dim == "template" else regioes_destaque) if faz_boot else defaultdict(list)
                wm.writerow([medida, bench, dim, g, len(vs), round(k_medio, 2),
                             round(m["effN"], 2), *[round(x, 2) for x in ic(d["effN"])],
                             round(m["gini"], 3), round(m["gini_corr"], 3),
                             round(m["top3"], 3), *[round(x, 3) for x in ic(d["top3"])],
                             round(m["jaccard"], 3), *[round(x, 3) for x in ic(d["jaccard"])],
                             round(m["declive"], 3), *[round(x, 3) for x in ic(d["declive"])],
                             round(m["spearman"], 3), round(m["jsd"], 4), *[round(x, 4) for x in ic(d["jsd"])],
                             round(m["tvd"], 3), m["n_regioes_zero"],
                             round(entropia_eff([qb[n] for n in nuts]), 2), round(gini([qb[n] for n in nuts]), 3)])
                for i, n in enumerate(nuts):
                    rac = ((p[i] * len(vs) + 0.5) / (len(vs) + 0.5 * len(nuts))) / qb[n]
                    lo, hi = ic(d[("racio", n)]) if ("racio", n) in d else ("", "")
                    qlo, qhi = ic(d[("quota", n)]) if ("quota", n) in d else ("", "")
                    wq.writerow([medida, bench, dim, g, n, round(p[i], 4),
                                 round(qlo, 4) if qlo != "" else "", round(qhi, 4) if qhi != "" else "",
                                 round(qb[n], 4), round(rac, 2), round(lo, 2) if lo != "" else "",
                                 round(hi, 2) if hi != "" else "", round(100 * (p[i] - qb[n]), 1),
                                 round(100 * pres_pct[n])])
                if bench == "lingua" and dim in ("total", "template"):
                    relatorio[(medida, g)] = (m, d, p, qb, pres_pct, len(vs), k_medio)
    fm.close(); fq.close()

    # homogeneização: sobreposição entre modelos e línguas dos conjuntos de regiões (presença >= 50% das respostas)
    with open(out / "homogeneizacao.csv", "w", encoding="utf-8-sig", newline="") as f:
        w = csv.writer(f, delimiter=";")
        w.writerow(["template", "dimensao", "a", "b", "jaccard_conjuntos_50pct", "correlacao_quotas_posicao"])
        for t in templates:
            for dim in ("modelo", "lang"):
                vals = sorted({r[dim] for r in resps})
                conj = {}; vec = {}
                for v in vals:
                    rs = [r for r in resps if r["template"] == t and r[dim] == v and "posicao" in vetores[r["id"]]]
                    pv = media_vetores([vetores[r["id"]]["presenca"] for r in rs], nuts)
                    pres = [sum(1 for r in rs if vetores[r["id"]]["presenca"].get(n, 0) > 0) / len(rs) for n in nuts]
                    conj[v] = {n for n, x in zip(nuts, pres) if x >= 0.5}
                    vec[v] = media_vetores([vetores[r["id"]]["posicao"] for r in rs], nuts)
                for i, x in enumerate(vals):
                    for y in vals[i + 1:]:
                        w.writerow([t, dim, x, y, round(len(conj[x] & conj[y]) / len(conj[x] | conj[y]), 3),
                                    round(pearson(vec[x], vec[y]), 3)])

    # roteiro: noites por NUTS III
    with open(out / "roteiro_noites.csv", "w", encoding="utf-8-sig", newline="") as f:
        w = csv.writer(f, delimiter=";")
        w.writerow(["grupo", "nuts3", "quota_noites_llm", "lo", "hi", "quota_dormidas_lingua", "quota_dormidas_total", "racio_lingua"])
        for (medida, g), (m, d, p, qb, pres_pct, n_resp, k) in relatorio.items():
            if medida != "noites":
                continue
            for i, n in enumerate(nuts):
                lo, hi = ic(d[("quota", n)]) if ("quota", n) in d else (float("nan"), float("nan"))
                w.writerow([g, n, round(p[i], 4), round(lo, 4), round(hi, 4), round(qb[n], 4), round(qT[n], 4),
                            round(((p[i] * n_resp + 0.5) / (n_resp + 0.5 * len(nuts))) / qb[n], 2)])

    escreve_relatorio(out, relatorio, nuts, qT, qF, qD, templates, a)
    print(f"Resultados em {out} (alocação={a.alocacao}, sem_ilhas={a.sem_ilhas}, bootstrap={a.bootstrap})")


def escreve_relatorio(out, rel, nuts, qT, qF, qD, templates, a):
    L = []
    L.append(f"# Relatório automático v2 (alocação de macro-destinos: {a.alocacao}; sem ilhas: {a.sem_ilhas}; "
             f"bootstrap: {a.bootstrap} reamostragens por agrupamento modelo × língua)\n")
    L.append("Termo de comparação: dormidas 2025 de não residentes para EN/ES/FR e de residentes para PT, ponderadas pela composição "
             "linguística do grupo. Intervalos a 95%.\n")
    L.append(f"Número efetivo de regiões das dormidas: total {entropia_eff([qT[n] for n in nuts]):.1f}, "
             f"não residentes {entropia_eff([qF[n] for n in nuts]):.1f}, residentes {entropia_eff([qD[n] for n in nuts]):.1f}. "
             f"Gini: {gini([qT[n] for n in nuts]):.3f} / {gini([qF[n] for n in nuts]):.3f} / {gini([qD[n] for n in nuts]):.3f}.\n")
    for medida, titulo in (("posicao", "Exposição ponderada pela posição (medida principal proposta)"),
                           ("presenca", "Presença por resposta (medida do piloto, com teto 1/k)"),
                           ("noites", "Noites atribuídas nos roteiros"), ("mencoes", "Todas as menções")):
        L.append(f"\n## {titulo}\n")
        L.append("| Grupo | n | k médio | nº efetivo regiões [IC] | top-3 | Jaccard | declive log-log [IC] | Spearman | JSD [IC] | regiões a zero |")
        L.append("|---|---|---|---|---|---|---|---|---|---|")
        for g in ["todos"] + templates:
            if (medida, g) not in rel:
                continue
            m, d, p, qb, pres, n, k = rel[(medida, g)]
            def f(key, nd=2):
                lo, hi = ic(d[key]); return f"{m[key]:.{nd}f} [{lo:.{nd}f}; {hi:.{nd}f}]"
            L.append(f"| {g} | {n} | {k:.1f} | {f('effN',1)} | {m['top3']:.2f} | {m['jaccard']:.2f} | {f('declive')} | "
                     f"{m['spearman']:.2f} | {f('jsd',3)} | {m['n_regioes_zero']} |")
    L.append("\n## Quotas e rácios por região (exposição ponderada pela posição), perguntas com hipóteses\n")
    for g in ("geral", "roteiro", "pouco_conhecidos"):
        if ("posicao", g) not in rel:
            continue
        m, d, p, qb, pres, n, k = rel[("posicao", g)]
        L.append(f"\n### {g} (n = {n})\n")
        L.append("| NUTS III | quota dormidas (língua) % | quota LLM % [IC] | rácio [IC] | diferença pp | presente em % das respostas |")
        L.append("|---|---|---|---|---|---|")
        for i in sorted(range(len(nuts)), key=lambda i: -qb[nuts[i]]):
            n3 = nuts[i]; lo, hi = ic(d[("quota", n3)]); rlo, rhi = ic(d[("racio", n3)])
            rac = ((p[i] * n + 0.5) / (n + 0.5 * len(nuts))) / qb[n3]
            L.append(f"| {n3} | {100*qb[n3]:.1f} | {100*p[i]:.1f} [{100*lo:.1f}; {100*hi:.1f}] | {rac:.2f} [{rlo:.2f}; {rhi:.2f}] | "
                     f"{100*(p[i]-qb[n3]):+.1f} | {100*pres[n3]:.0f} |")
    if ("noites", "roteiro") in rel:
        m, d, p, qb, pres, n, k = rel[("noites", "roteiro")]
        L.append(f"\n## Roteiro de 7 dias: noites atribuídas por NUTS III (n = {n} roteiros com dias legíveis)\n")
        L.append("| NUTS III | quota de noites LLM % [IC] | dormidas não residentes % | rácio |")
        L.append("|---|---|---|---|")
        for i in sorted(range(len(nuts)), key=lambda i: -p[i])[:12]:
            n3 = nuts[i]; lo, hi = ic(d[("quota", n3)])
            L.append(f"| {n3} | {100*p[i]:.1f} [{100*lo:.1f}; {100*hi:.1f}] | {100*qb[n3]:.1f} | {p[i]/qb[n3]:.2f} |")
        il = [i for i, n3 in enumerate(nuts) if n3 in ("Grande Lisboa", "Área Metropolitana do Porto")]
        L.append(f"\nGrande Lisboa + AM Porto: {100*sum(p[i] for i in il):.1f}% das noites atribuídas; "
                 f"nas dormidas de não residentes: {100*sum(qb[nuts[i]] for i in il):.1f}%. Gini das noites LLM: {m['gini']:.3f}.\n")
    L.append("\n## Regiões nunca recomendadas como destino principal (presença 0% na pergunta geral)\n")
    if ("presenca", "geral") in rel:
        pres = rel[("presenca", "geral")][4]
        L.append(", ".join(n for n in nuts if pres[n] == 0) or "nenhuma")
    (out / "relatorio.md").write_text("\n".join(L) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
