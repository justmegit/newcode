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


ALIAS = {"oporto": "porto", "lisbon": "lisboa", "lisbonne": "lisboa", "vila nova de gaia (porto)": "vila nova de gaia",
         "reguengos": "reguengos de monsaraz", "monsaraz": "reguengos de monsaraz",
         "figueira castelo rodrigo": "figueira de castelo rodrigo", "foz coa": "vila nova de foz coa",
         "vila nova de foz-coa": "vila nova de foz coa", "pinhao": "alijo", "vila real de sto antonio": "vila real de santo antonio",
         "fatima": "ourem", "ericeira": "mafra", "angra": "angra do heroismo", "ponta delgada (sao miguel)": "ponta delgada",
         "funchal (madeira)": "funchal", "furnas": "povoacao", "porto formoso": "ribeira grande", "lagoa (algarve)": "lagoa",
         "lagoa (acores)": "lagoa", "guia": "albufeira", "armacao de pera": "silves", "quarteira": "loule",
         "carrapateira": "aljezur", "odeceixe": "aljezur", "vila nova de santo andre": "santiago do cacem",
         "porto da cruz": "machico", "aguas de moura": "palmela", "janas": "sintra", "topo": "calheta",
         "sete cidades": "ponta delgada", "vila cova a coelheira": "vila nova de paiva", "vista alegre (ilhavo)": "ilhavo",
         "vacarisa (vagos)": "vagos", "criacao velha (madalena)": "madalena", "sao jorge": "calheta",
         "alqueva": "reguengos de monsaraz", "comporta": "alcacer do sal", "nazare": "nazare", "obidos": "obidos"}


class Geocodificador:
    """Aplica o livro de códigos a um item extraído: títulos, macro-destinos e NUTS III derivada do município."""

    def __init__(self):
        with open(AQUI / "data" / "municipios_nuts3_2024.csv", encoding="utf-8") as f:
            self.mun = {}
            for r in csv.DictReader(f):
                self.mun.setdefault(norm(r["municipio"]), []).append(r["nuts3"])
        with open(AQUI / "data" / "macro_destinos.csv", encoding="utf-8") as f:
            self.macros = [(r["chave"], re.compile(r["padrao"], re.I), r["nuts3_principal"], r["nuts3_abrangidas"].split("|"))
                           for r in csv.DictReader(f, delimiter=";")]
        with open(AQUI / "data" / "nuts3.csv", encoding="utf-8") as f:
            self.nuts = {r["nuts3"] for r in csv.DictReader(f)}
        self.contagem = Counter()
        self.desconhecidos = Counter()
        self.divergencias = Counter()

    def item(self, e):
        """Devolve uma cópia do item com nivel_geo, nuts3 (derivada) e nuts3_extrator."""
        lugar = (e.get("lugar") or "").strip()
        e2 = dict(e)
        e2["nuts3_extrator"] = e.get("nuts3")
        if TITULO.search(lugar) or len(lugar) > 60:
            e2["nivel_geo"] = "titulo"; e2["nuts3"] = None
            self.contagem["titulo"] += 1
            return e2
        macro = next(((k, pr, ab) for k, rx, pr, ab in self.macros if rx.search(lugar)), None)
        if macro:
            k, principal, abr = macro
            e2["nivel_geo"] = "macro" if len(abr) > 1 else "macro_1nuts"
            e2["macro_chave"] = k; e2["nuts3_principal"] = principal; e2["nuts3_abrangidas"] = abr; e2["nuts3"] = principal
            self.contagem[e2["nivel_geo"]] += 1
            if e.get("nuts3") and e.get("nuts3") not in abr:
                self.divergencias[("macro", k, e.get("nuts3"))] += 1
            return e2
        m = norm(e.get("municipio")); m = ALIAS.get(m, m)
        cands = self.mun.get(m) or self.mun.get(ALIAS.get(norm(lugar), norm(lugar)))
        if not cands:
            e2["nivel_geo"] = "municipio_desconhecido"
            e2["nuts3"] = e.get("nuts3") if e.get("nuts3") in self.nuts else None
            self.desconhecidos[e.get("municipio")] += 1
            self.contagem["municipio_desconhecido"] += 1
            return e2
        if len(cands) == 1:
            n3 = cands[0]
        elif e.get("nuts3") in cands:
            n3 = e.get("nuts3")
        else:
            lug = norm(lugar) + " " + norm(e.get("municipio")) + " " + norm(e.get("contexto"))
            n3 = ("Região Autónoma dos Açores" if re.search(r"acores|azores|sao jorge|sao miguel|topo", lug)
                  else "Região Autónoma da Madeira" if re.search(r"madeira|madere", lug)
                  else "Algarve" if "Algarve" in cands else cands[0])
        e2["nuts3"] = n3; e2["nivel_geo"] = "municipio"
        self.contagem["municipio"] += 1
        if e.get("nuts3") and e.get("nuts3") != n3:
            self.divergencias[("municipio", e.get("municipio"), e.get("nuts3"), n3)] += 1
            self.contagem["nuts3_extrator_errada"] += 1
        return e2

    def resumo(self, n):
        print(f"{n} itens geocodificados")
        for k in ("municipio", "macro", "macro_1nuts", "titulo", "municipio_desconhecido", "nuts3_extrator_errada"):
            print(f"  {k:24s} {self.contagem[k]:6d}  ({100*self.contagem[k]/max(n,1):4.1f}%)")
        if self.desconhecidos:
            print("Municípios não reconhecidos (corrigir em ALIAS ou na tabela):", self.desconhecidos.most_common(25))
        if self.divergencias:
            print("Divergências extrator vs tabela (mais frequentes):")
            for k, v in self.divergencias.most_common(15):
                print("  ", v, k)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--entrada", default=str(AQUI / "data" / "extracoes.jsonl"))
    ap.add_argument("--saida", default=str(AQUI / "data" / "extracoes_v2.jsonl"))
    a = ap.parse_args()
    geo = Geocodificador()
    extr = [json.loads(l) for l in Path(a.entrada).read_text(encoding="utf-8").splitlines()]
    with open(a.saida, "w", encoding="utf-8") as out:
        for e in extr:
            out.write(json.dumps(geo.item(e), ensure_ascii=False) + "\n")
    print(f"-> {a.saida}")
    geo.resumo(len(extr))


if __name__ == "__main__":
    main()
