"""Reprocessamento determinístico das extrações: títulos, macro-destinos e NUTS III derivada do município.

Uso: python reprocess.py [--entrada data/extracoes.jsonl] [--saida data/extracoes_v2.jsonl]

Não chama APIs. Para cada lugar extraído:
  1. marca como "titulo" os itens que são títulos ou frases introdutórias (não contam);
  2. se o nome corresponder a um macro-destino (data/macro_destinos.csv), regista nivel_geo="macro",
     nuts3_principal e nuts3_abrangidas (a análise decide como alocar);
  3. caso contrário deriva a NUTS III do município (data/municipios_nuts3_2024.csv), e regista se a
     NUTS III do extrator coincidia (taxa de erro do extrator na atribuição de NUTS III).
Imprime um resumo com as taxas. Livro de códigos: docs/livro_de_codigos.md.
"""
import argparse
import csv
import json
import re
import unicodedata
from collections import Counter
from pathlib import Path

AQUI = Path(__file__).parent

TITULO = re.compile(
    r"^(\d+\s+(lugares|places|endroits|sitios|sítios|destinos|destinations|sugest|sugg|propuestas|joyas|joias|gems|pépites)"
    r"|(roteiro|itiner|itinér|ruta|route|viagem|voyage|viaje|trip|programa|plan)\b.*\b(dias|days|jours|días)"
    r"|(top|melhores|best|meilleurs|mejores)\s+\d*\s*(lugares|places|endroits|sitios|destinos)"
    r"|^(dia|day|jour|día)\s*\d|^(resumo|summary|résumé|resumen|dicas|tips|conseils|consejos)\b"
    r"|\bportugal\s*(:|-|–)\s*\d+\b|^portugal$)", re.I)


def norm(s):
    s = unicodedata.normalize("NFKD", s or "").encode("ascii", "ignore").decode().lower().strip()
    return re.sub(r"\s+", " ", s)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--entrada", default=str(AQUI / "data" / "extracoes.jsonl"))
    ap.add_argument("--saida", default=str(AQUI / "data" / "extracoes_v2.jsonl"))
    a = ap.parse_args()

    with open(AQUI / "data" / "municipios_nuts3_2024.csv", encoding="utf-8") as f:
        mun_rows = list(csv.DictReader(f))
    mun = {}
    for r in mun_rows:
        mun.setdefault(norm(r["municipio"]), []).append(r["nuts3"])
    # grafias alternativas frequentes nas respostas
    alias = {"oporto": "porto", "lisbon": "lisboa", "lisbonne": "lisboa", "vila nova de gaia (porto)": "vila nova de gaia",
             "reguengos": "reguengos de monsaraz", "monsaraz": "reguengos de monsaraz", "nazare": "nazare",
             "obidos": "obidos", "figueira castelo rodrigo": "figueira de castelo rodrigo", "foz coa": "vila nova de foz coa",
             "vila nova de foz-coa": "vila nova de foz coa", "pinhao": "alijo", "lamego ": "lamego", "vila real de sto antonio": "vila real de santo antonio",
             "elvas ": "elvas", "fatima": "ourem", "ericeira": "mafra", "cascais ": "cascais", "guimaraes": "guimaraes",
             "angra": "angra do heroismo", "ponta delgada (sao miguel)": "ponta delgada", "funchal (madeira)": "funchal",
             "furnas": "povoacao", "porto formoso": "ribeira grande", "lagoa (algarve)": "lagoa", "lagoa (acores)": "lagoa",
             "guia": "albufeira", "armacao de pera": "silves", "quarteira": "loule", "carrapateira": "aljezur",
             "odeceixe": "aljezur", "vila nova de santo andre": "santiago do cacem", "porto da cruz": "machico",
             "aguas de moura": "palmela", "janas": "sintra", "topo": "calheta", "sete cidades": "ponta delgada",
             "vila cova a coelheira": "vila nova de paiva", "vista alegre (ilhavo)": "ilhavo", "vacarisa (vagos)": "vagos",
             "criacao velha (madalena)": "madalena", "sao jorge": "calheta", "alqueva": "reguengos de monsaraz"}
    with open(AQUI / "data" / "macro_destinos.csv", encoding="utf-8") as f:
        macros = [(r["chave"], re.compile(r["padrao"], re.I), r["nuts3_principal"], r["nuts3_abrangidas"].split("|"))
                  for r in csv.DictReader(f, delimiter=";")]
    with open(AQUI / "data" / "nuts3.csv", encoding="utf-8") as f:
        nuts = {r["nuts3"] for r in csv.DictReader(f)}

    extr = [json.loads(l) for l in Path(a.entrada).read_text(encoding="utf-8").splitlines()]
    c = Counter()
    desconhecidos = Counter()
    divergencias = Counter()
    with open(a.saida, "w", encoding="utf-8") as out:
        for e in extr:
            lugar = (e.get("lugar") or "").strip()
            e2 = dict(e)
            e2["nuts3_extrator"] = e.get("nuts3")
            if TITULO.search(lugar) or len(lugar) > 60:
                e2["nivel_geo"] = "titulo"
                e2["nuts3"] = None
                c["titulo"] += 1
            else:
                macro = next(((k, p, ab) for k, rx, p, ab in macros if rx.search(lugar)), None)
                if macro:
                    k, principal, abr = macro
                    e2["nivel_geo"] = "macro" if len(abr) > 1 else "macro_1nuts"
                    e2["macro_chave"] = k
                    e2["nuts3_principal"] = principal
                    e2["nuts3_abrangidas"] = abr
                    e2["nuts3"] = principal
                    c[e2["nivel_geo"]] += 1
                    if e.get("nuts3") not in abr:
                        divergencias[("macro", k, e.get("nuts3"))] += 1
                else:
                    m = norm(e.get("municipio"))
                    m = alias.get(m, m)
                    cands = mun.get(m)
                    if not cands:
                        # tenta o próprio nome do lugar como município (ex.: "Sintra")
                        cands = mun.get(alias.get(norm(lugar), norm(lugar)))
                    if cands:
                        if len(cands) == 1:
                            n3 = cands[0]
                        elif e.get("nuts3") in cands:
                            n3 = e.get("nuts3")
                        else:
                            lug = norm(lugar) + " " + norm(e.get("municipio"))
                            n3 = ("Região Autónoma dos Açores" if re.search(r"acores|azores|sao jorge|sao miguel|topo", lug)
                                  else "Região Autónoma da Madeira" if re.search(r"madeira|madere", lug)
                                  else "Algarve" if "Algarve" in cands else cands[0])
                        e2["nuts3"] = n3
                        e2["nivel_geo"] = "municipio"
                        c["municipio"] += 1
                        if e.get("nuts3") != n3:
                            divergencias[("municipio", e.get("municipio"), e.get("nuts3"), n3)] += 1
                            c["nuts3_extrator_errada"] += 1
                    else:
                        e2["nivel_geo"] = "municipio_desconhecido"
                        e2["nuts3"] = e.get("nuts3") if e.get("nuts3") in nuts else None
                        desconhecidos[e.get("municipio")] += 1
                        c["municipio_desconhecido"] += 1
            out.write(json.dumps(e2, ensure_ascii=False) + "\n")

    n = len(extr)
    print(f"{n} itens reprocessados -> {a.saida}")
    for k in ("municipio", "macro", "macro_1nuts", "titulo", "municipio_desconhecido", "nuts3_extrator_errada"):
        print(f"  {k:24s} {c[k]:6d}  ({100*c[k]/n:4.1f}%)")
    print("Municípios não reconhecidos (corrigir em alias ou na tabela):", desconhecidos.most_common(25))
    print("Divergências extrator vs tabela (mais frequentes):")
    for k, v in divergencias.most_common(15):
        print("  ", v, k)


if __name__ == "__main__":
    main()
