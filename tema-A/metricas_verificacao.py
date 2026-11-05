"""Métricas da verificação humana v2: recall e precisão do extrator, concordância entre codificadores.

Uso:
  python metricas_verificacao.py --recall data/verificacao_recall_NA.xlsx data/verificacao_recall_AMS.xlsx \
                                 --precisao data/verificacao_precisao_NA.xlsx data/verificacao_precisao_AMS.xlsx

Recall: para cada resposta, compara a lista de cada codificador com os destinos extraídos (correspondência por nome,
sem acentos, com tolerância a prefixos como "Vila Nova de"). Reporta recall e precisão do extrator contra cada
codificador e contra a união/interseção, e a concordância entre codificadores (Jaccard por resposta).
Precisão: kappa de Cohen e acordo simples por dimensão (destino principal, município, NUTS III), e taxa de exatidão do extrator.
"""
import argparse
import json
import re
import unicodedata
from collections import defaultdict
from pathlib import Path

from openpyxl import load_workbook

AQUI = Path(__file__).parent


def norm(s):
    s = unicodedata.normalize("NFKD", str(s or "")).encode("ascii", "ignore").decode().lower()
    s = re.sub(r"\(.*?\)", " ", s)
    s = re.sub(r"[^a-z0-9 ]+", " ", s)
    return re.sub(r"\s+", " ", s).strip()


def iguais(a, b):
    a, b = norm(a), norm(b)
    return a == b or (len(a) > 3 and (a in b or b in a))


def kappa(x, y):
    n = len(x)
    po = sum(i == j for i, j in zip(x, y)) / n
    cats = set(x) | set(y)
    pe = sum((x.count(c) / n) * (y.count(c) / n) for c in cats)
    return (po - pe) / (1 - pe) if pe < 1 else 1.0, po


def ler(path, folha):
    ws = load_workbook(path, read_only=True)[folha]
    rows = list(ws.iter_rows(values_only=True))
    cab = [str(c) for c in rows[0]]
    return [dict(zip(cab, r)) for r in rows[1:] if any(v not in (None, "") for v in r)]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--recall", nargs="*", default=[])
    ap.add_argument("--precisao", nargs="*", default=[])
    a = ap.parse_args()
    extr = [json.loads(l) for l in (AQUI / "data" / "extracoes_v2.jsonl").read_text(encoding="utf-8").splitlines()]
    dest = defaultdict(list)
    for e in extr:
        if e.get("nivel") == "destino" and e.get("nivel_geo") != "titulo":
            dest[e["id"]].append(e["lugar"])

    if a.recall:
        listas = []
        for p in a.recall:
            d = defaultdict(list)
            for r in ler(p, "Destinos"):
                if r.get("nome no texto"):
                    d[r["id"]].append(r["nome no texto"])
            listas.append(d)
        print("== Recall do extrator (destinos principais)")
        for ci, d in enumerate(listas, 1):
            tp = fn = fp = 0
            for rid, humanos in d.items():
                ex = dest.get(rid, [])
                tp += sum(1 for h in humanos if any(iguais(h, x) for x in ex))
                fn += sum(1 for h in humanos if not any(iguais(h, x) for x in ex))
                fp += sum(1 for x in ex if not any(iguais(h, x) for h in humanos))
            print(f"  codificador {ci}: recall={tp/(tp+fn):.2%} precisão={tp/(tp+fp):.2%} (n humanos={tp+fn}, n extraídos={tp+fp})")
        if len(listas) >= 2:
            jac = []
            for rid in set(listas[0]) & set(listas[1]):
                A, B = listas[0][rid], listas[1][rid]
                inter = sum(1 for x in A if any(iguais(x, y) for y in B))
                uni = len(A) + len(B) - inter
                jac.append(inter / uni if uni else 1)
            print(f"  concordância entre codificadores (Jaccard médio por resposta): {sum(jac)/len(jac):.2f} em {len(jac)} respostas")

    if a.precisao:
        tabs = [ler(p, "Verificação") for p in a.precisao]
        print("== Precisão do extrator e concordância, por dimensão")
        for col in ("destino_principal_ok (s/n)", "municipio_ok (s/n)", "nuts3_ok (s/n)"):
            vals = []
            for t in tabs:
                vals.append({(r["id"], r["posicao"]): str(r.get(col) or "").strip().lower() for r in t})
            chaves = [k for k in vals[0] if all(k in v and v[k] in ("s", "n") for v in vals)]
            if not chaves:
                print(f"  {col}: por preencher"); continue
            x = [vals[0][k] for k in chaves]
            linha = f"  {col:28s} n={len(chaves):4d} exatidão(cod.1)={x.count('s')/len(x):.1%}"
            if len(vals) >= 2:
                y = [vals[1][k] for k in chaves]
                kp, po = kappa(x, y)
                linha += f" exatidão(cod.2)={y.count('s')/len(y):.1%} acordo={po:.1%} kappa={kp:.2f}"
            print(linha)
        print("Nota: com exatidão perto de 100% o kappa é instável (paradoxo do kappa); reportar sempre o acordo simples e as prevalências.")


if __name__ == "__main__":
    main()
