"""Tabela de sensibilidade: compara os números de cabeçalho entre as variantes de análise em results_v2/."""
import csv
from pathlib import Path

AQUI = Path(__file__).parent
VARS = {"principal": "results_v2", "fracionaria": "results_v2/sens_fracionaria", "excluir": "results_v2/sens_excluir",
        "sem ilhas": "results_v2/sens_sem_ilhas"}
REG = ["Algarve", "Grande Lisboa", "Área Metropolitana do Porto", "Alentejo Central", "Região de Coimbra", "Douro"]


def ler(d, nome):
    p = AQUI / d / nome
    if not p.exists():
        return []
    with open(p, encoding="utf-8-sig") as f:
        return list(csv.DictReader(f, delimiter=";"))


linhas = []
for var, d in VARS.items():
    met = ler(d, "metricas.csv"); quo = ler(d, "quotas.csv"); noi = ler(d, "roteiro_noites.csv")
    if not met:
        continue
    def m(medida, grupo, col):
        r = next((x for x in met if x["medida"] == medida and x["benchmark"] == "lingua" and x["grupo"] == grupo), None)
        return r[col] if r else ""
    def rac(grupo, n):
        r = next((x for x in quo if x["medida"] == "posicao" and x["benchmark"] == "lingua" and x["grupo"] == grupo and x["nuts3"] == n), None)
        return r["racio"] if r else ""
    lp = sum(float(x["quota_noites_llm"]) for x in noi if x["grupo"] == "roteiro" and x["nuts3"] in ("Grande Lisboa", "Área Metropolitana do Porto"))
    linhas.append([var, m("posicao", "geral", "declive"), m("posicao", "geral", "effN"), m("posicao", "geral", "jsd")]
                  + [rac("geral", n) for n in REG] + [m("posicao", "pouco_conhecidos", "declive"),
                     m("noites", "roteiro", "effN"), round(100 * lp, 1)])
cab = ["variante", "declive geral", "effN geral", "JSD geral"] + [f"rácio {n} (geral)" for n in REG] + \
      ["declive pouco conhecidos", "effN noites roteiro", "Lisboa+Porto % noites"]
with open(AQUI / "results_v2" / "sensibilidade.csv", "w", encoding="utf-8-sig", newline="") as f:
    w = csv.writer(f, delimiter=";"); w.writerow(cab); w.writerows(linhas)
print("| " + " | ".join(cab) + " |"); print("|" + "---|" * len(cab))
for l in linhas:
    print("| " + " | ".join(str(x) for x in l) + " |")
