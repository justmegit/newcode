"""Análise: concentração das recomendações por NUTS III e comparação com as dormidas (INE).

Uso: python analyze.py
Lê data/extracoes.jsonl e data/nuts3.csv (coluna dormidas preenchida a partir do INE).
Grava results/quotas_nuts3.csv, results/concentracao.csv e, se a verificação humana
estiver preenchida, imprime o kappa de Cohen entre os dois codificadores.
"""
import csv
import json
from collections import Counter, defaultdict
from pathlib import Path

AQUI = Path(__file__).parent
RES = AQUI / "results"


def gini(valores):
    v = sorted(valores)
    n, s = len(v), sum(v)
    if n == 0 or s == 0:
        return float("nan")
    return sum((2 * (i + 1) - n - 1) * x for i, x in enumerate(v)) / (n * s)


def hhi(quotas):
    return sum(q * q for q in quotas)


def kappa(a, b):
    n = len(a)
    if n == 0:
        return float("nan")
    po = sum(x == y for x, y in zip(a, b)) / n
    cats = set(a) | set(b)
    pe = sum((a.count(c) / n) * (b.count(c) / n) for c in cats)
    return (po - pe) / (1 - pe) if pe < 1 else 1.0


def main():
    with open(AQUI / "data" / "nuts3.csv", encoding="utf-8") as f:
        linhas = list(csv.DictReader(f))
    nuts = [r["nuts3"] for r in linhas]
    dorm = {r["nuts3"]: float(r["dormidas"]) for r in linhas if r["dormidas"].strip()}
    tem_dorm = len(dorm) == len(nuts)
    if tem_dorm:
        tot = sum(dorm.values())
        q_dorm = {n: dorm[n] / tot for n in nuts}

    extr = [json.loads(l) for l in (AQUI / "data" / "extracoes.jsonl").read_text(encoding="utf-8").splitlines()]
    validos = [e for e in extr if e.get("existe", True) and not e.get("nuts3_invalida")]
    erros = len(extr) - len(validos)

    # Medida principal: destinos principais, por presença (uma NUTS III conta no máximo uma vez por resposta).
    # Medida secundária: todas as menções (destinos + atrações), cada uma conta.
    medidas = {"destinos": [e for e in validos if e.get("nivel", "destino") == "destino"], "mencoes": validos}

    RES.mkdir(exist_ok=True)
    with open(RES / "quotas_nuts3.csv", "w", encoding="utf-8-sig", newline="") as fq, \
         open(RES / "concentracao.csv", "w", encoding="utf-8-sig", newline="") as fc:
        wq, wc = csv.writer(fq, delimiter=";"), csv.writer(fc, delimiter=";")
        wq.writerow(["medida", "dimensao", "grupo", "nuts3", "contagem", "quota_llm", "quota_dormidas",
                     "racio_enviesamento"])
        wc.writerow(["medida", "dimensao", "grupo", "contagem", "nuts3_presentes", "gini_llm", "hhi_llm",
                     "top3_quota", "gini_dormidas", "hhi_dormidas"])
        totais = {}
        for medida, itens in medidas.items():
            grupos = defaultdict(Counter)
            vistos = set()
            for e in itens:
                if medida == "destinos" and (e["id"], e["nuts3"]) in vistos:
                    continue
                vistos.add((e["id"], e["nuts3"]))
                for g in [("total", "todos"), ("modelo", e["modelo"]), ("lang", e["lang"]),
                          ("template", e["template"]), ("modelo_lang", f"{e['modelo']}_{e['lang']}")]:
                    grupos[g][e["nuts3"]] += 1
            totais[medida] = grupos[("total", "todos")]
            for (dim, grp), cont in sorted(grupos.items()):
                tot = sum(cont.values())
                quotas = {n: cont.get(n, 0) / tot for n in nuts}
                for n in nuts:
                    qd = q_dorm[n] if tem_dorm else ""
                    racio = (quotas[n] / qd) if tem_dorm and qd > 0 else ""
                    wq.writerow([medida, dim, grp, n, cont.get(n, 0), round(quotas[n], 4),
                                 round(qd, 4) if qd != "" else "", round(racio, 2) if racio != "" else ""])
                top3 = sum(sorted(quotas.values(), reverse=True)[:3])
                wc.writerow([medida, dim, grp, tot, len(cont), round(gini(list(quotas.values())), 3),
                             round(hhi(quotas.values()), 3), round(top3, 3),
                             round(gini(list(q_dorm.values())), 3) if tem_dorm else "",
                             round(hhi(q_dorm.values()), 3) if tem_dorm else ""])

    n_dest = len(medidas["destinos"])
    print(f"{len(extr)} lugares extraídos ({n_dest} destinos principais, {len(validos) - n_dest} atrações); "
          f"{erros} excluídos (inexistentes ou NUTS III inválida).")
    for medida, tot in totais.items():
        print(f"[{medida}] {len(tot)} de {len(nuts)} NUTS III presentes; top 5:",
              ", ".join(f"{n} {c}" for n, c in tot.most_common(5)))
    if not tem_dorm:
        print("[aviso] Coluna 'dormidas' de data/nuts3.csv por preencher: sem rácio de enviesamento.")

    ver = AQUI / "data" / "verificacao_humana.csv"
    if ver.exists():
        with open(ver, encoding="utf-8-sig") as f:
            rows = [r for r in csv.DictReader(f, delimiter=";")
                    if r["codificador_1_correto (s/n)"].strip() and r["codificador_2_correto (s/n)"].strip()]
        if rows:
            a = [r["codificador_1_correto (s/n)"].strip().lower() for r in rows]
            b = [r["codificador_2_correto (s/n)"].strip().lower() for r in rows]
            acordo = sum(x == y for x, y in zip(a, b)) / len(a)
            print(f"Kappa de Cohen ({len(rows)} itens): {kappa(a, b):.2f}; acordo simples: {acordo:.0%}; "
                  f"exatidão da extração (codificador 1): {a.count('s') / len(a):.0%}")
        else:
            print("Verificação humana ainda por preencher.")
    print(f"Resultados em {RES}")


if __name__ == "__main__":
    main()
