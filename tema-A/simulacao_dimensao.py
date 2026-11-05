"""Justificação da dimensão da recolha confirmatória por precisão (largura dos intervalos), simulada a partir do piloto.

Uso: python simulacao_dimensao.py [--iteracoes 500]

Para a pergunta geral, o roteiro e "pouco conhecidos", reamostra do piloto desenhos com diferentes números de
células (modelo × língua) e de repetições por célula, e calcula a largura do intervalo a 95% (bootstrap por
agrupamento) do declive log-log, do número efetivo de regiões e da divergência de Jensen-Shannon, na medida de
exposição ponderada pela posição. A variação por paráfrase não existe no piloto (uma formulação por pergunta), por
isso a largura real será maior: este é um limite inferior, útil para escolher repetições e células, não para prometer precisão.
Saída: results_v2/simulacao_dimensao.csv e tabela no terminal.
"""
import argparse
import csv
import json
import random
from collections import defaultdict
from pathlib import Path

import analyze_v2 as A

AQUI = Path(__file__).parent


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--iteracoes", type=int, default=300, help="reamostragens por cenário")
    ap.add_argument("--semente", type=int, default=2026)
    a = ap.parse_args()
    rng = random.Random(a.semente)
    with open(AQUI / "data" / "dormidas_2025_nuts3.csv", encoding="utf-8") as f:
        dl = list(csv.DictReader(f))
    nuts = [r["nuts3"] for r in dl]
    def q(col):
        tot = sum(float(r[col]) for r in dl); return {r["nuts3"]: float(r[col]) / tot for r in dl}
    qT, qF, qD = q("total"), q("nao_residentes"), q("residentes")
    resps = [json.loads(l) for l in (AQUI / "data" / "respostas.jsonl").read_text(encoding="utf-8").splitlines()]
    extr = [json.loads(l) for l in (AQUI / "data" / "extracoes_v2.jsonl").read_text(encoding="utf-8").splitlines()]
    por = defaultdict(list)
    for e in extr:
        por[e["id"]].append(e)
    vet = {r["id"]: A.medidas_resposta(por.get(r["id"], []), r["resposta"], "principal") for r in resps}

    cenarios = [(12, 1), (12, 2), (12, 3), (12, 5), (20, 2), (20, 3), (36, 2), (36, 3)]  # (células, repetições por célula)
    out = AQUI / "results_v2"; out.mkdir(exist_ok=True)
    linhas = []
    print(f"{'pergunta':17s} {'células':>7s} {'reps':>4s} {'n':>4s} | largura IC95: declive  effN   JSD")
    for t in ("geral", "roteiro", "pouco_conhecidos"):
        rs = [r for r in resps if r["template"] == t and "posicao" in vet[r["id"]]]
        cel = defaultdict(list)
        for r in rs:
            cel[(r["modelo"], r["lang"])].append(r)
        chaves = list(cel)
        for n_cel, reps in cenarios:
            larg = defaultdict(list)
            for _ in range(a.iteracoes):
                # desenho simulado: n_cel células (com reposição a partir das 12 reais), reps respostas por célula
                amostra = []
                for c in rng.choices(chaves, k=n_cel):
                    amostra.extend(rng.choices(cel[c], k=reps))
                # bootstrap por agrupamento dentro do desenho simulado (50 reamostragens para a largura)
                grupos = [amostra[i:i + reps] for i in range(0, len(amostra), reps)]
                ests = defaultdict(list)
                for _ in range(50):
                    bs = []
                    for g in rng.choices(grupos, k=len(grupos)):
                        bs.extend(rng.choices(g, k=len(g)))
                    vs = [vet[r["id"]]["posicao"] for r in bs]
                    qb = A.bench_grupo(bs, qF, qD, qT, "lingua", nuts)
                    m = A.metricas(vs, nuts, qb, len(vs), com_jaccard=False)
                    for k in ("declive", "effN", "jsd"):
                        ests[k].append(m[k])
                for k in ests:
                    lo, hi = A.ic(ests[k]); larg[k].append(hi - lo)
            med = {k: sorted(v)[len(v) // 2] for k, v in larg.items()}
            n = n_cel * reps
            print(f"{t:17s} {n_cel:7d} {reps:4d} {n:4d} |                  {med['declive']:6.3f} {med['effN']:6.2f} {med['jsd']:6.4f}")
            linhas.append([t, n_cel, reps, n, round(med["declive"], 3), round(med["effN"], 2), round(med["jsd"], 4)])
    with open(out / "simulacao_dimensao.csv", "w", encoding="utf-8-sig", newline="") as f:
        w = csv.writer(f, delimiter=";")
        w.writerow(["pergunta", "celulas", "repeticoes_por_celula", "n_respostas", "largura_ic_declive", "largura_ic_effN", "largura_ic_jsd"])
        w.writerows(linhas)
    print("Nota: larguras medianas; limite inferior porque o piloto não tem variação por paráfrase.")


if __name__ == "__main__":
    main()
