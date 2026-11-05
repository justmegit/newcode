"""Descarrega do Eurostat as dormidas por NUTS III (2025) por residência e o âmbito NACE nacional.

Uso: python fetch_eurostat.py [--ano 2025]

Gera:
  data/dormidas_<ano>_nuts3.csv   colunas: nuts3, codigo, total, nao_residentes, residentes
  data/dormidas_<ano>_nace_pt.csv âmbito NACE nacional (I551, I552, I553), para explicar a diferença face ao INE
Fonte: tour_occ_nin3 (NUTS 3, de 2020 em diante) e tour_occ_nin2 (NACE). Só biblioteca padrão.
"""
import argparse
import csv
import json
import urllib.request
from pathlib import Path

AQUI = Path(__file__).parent
BASE = "https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/"


def jsonstat(url):
    with urllib.request.urlopen(url, timeout=120) as r:
        return json.loads(r.read().decode("utf-8"))


def valores(d, geo_prefixo="PT"):
    """Devolve {(rótulo_geo, código_geo, rótulo_nace): valor} para a primeira categoria das outras dimensões."""
    dims, size = d["id"], d["size"]
    cats = {k: d["dimension"][k]["category"] for k in dims}
    idx = {k: (dict(zip(cats[k]["index"], range(len(cats[k]["index"])))) if isinstance(cats[k]["index"], list)
               else cats[k]["index"]) for k in dims}
    out = {}
    geos = [g for g in idx["geo"] if g.startswith(geo_prefixo)]
    naces = list(idx["nace_r2"])
    for g in geos:
        for n in naces:
            pos = 0
            for k, s in zip(dims, size):
                i = idx["geo"][g] if k == "geo" else idx["nace_r2"][n] if k == "nace_r2" else 0
                pos = pos * s + i
            v = d["value"].get(str(pos))
            if v is not None:
                out[(cats["geo"]["label"][g], g, cats["nace_r2"]["label"][n])] = v
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--ano", default="2025")
    a = ap.parse_args()
    with open(AQUI / "data" / "nuts3.csv", encoding="utf-8") as f:
        nuts = [r["nuts3"] for r in csv.DictReader(f)]

    por_res = {}
    for res in ("TOTAL", "FOR", "DOM"):
        d = jsonstat(f"{BASE}tour_occ_nin3?format=JSON&lang=EN&time={a.ano}&c_resid={res}&unit=NR")
        por_res[res] = {k[0]: (k[1], v) for k, v in valores(d).items()}
    em_falta = [n for n in nuts if n not in por_res["TOTAL"]]
    if em_falta:
        raise SystemExit(f"NUTS III sem valor no Eurostat (ver nomes em data/nuts3.csv): {em_falta}")
    saida = AQUI / "data" / f"dormidas_{a.ano}_nuts3.csv"
    with open(saida, "w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(["nuts3", "codigo", "total", "nao_residentes", "residentes"])
        for n in nuts:
            w.writerow([n, por_res["TOTAL"][n][0], int(por_res["TOTAL"][n][1]),
                        int(por_res["FOR"][n][1]), int(por_res["DOM"][n][1])])
    tot = {r: sum(por_res[r][n][1] for n in nuts) for r in por_res}
    print(f"{saida.name}: total={tot['TOTAL']:,.0f} nao_residentes={tot['FOR']:,.0f} residentes={tot['DOM']:,.0f}")

    d = jsonstat(f"{BASE}tour_occ_nin2?format=JSON&lang=EN&time={a.ano}&geo=PT&c_resid=TOTAL&unit=NR")
    saida2 = AQUI / "data" / f"dormidas_{a.ano}_nace_pt.csv"
    with open(saida2, "w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(["nace_r2", "dormidas"])
        for (geo, cod, nace), v in sorted(valores(d).items(), key=lambda kv: -kv[1]):
            w.writerow([nace, int(v)])
            print(f"  {nace[:70]:70s} {v:,.0f}")
    print(f"{saida2.name} gravado. O INE exclui parques de campismo (I55.3) e colónias de férias do total de referência.")


if __name__ == "__main__":
    main()
