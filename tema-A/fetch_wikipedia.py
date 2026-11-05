"""Termo de comparação textual: visualizações de páginas da Wikipédia dos municípios portugueses, agregadas a NUTS III.

Uso: python fetch_wikipedia.py [--ano 2025] [--linguas pt,en] [--limite 20]

Para cada município em data/municipios_nuts3_2024.csv pede à API de pageviews da Wikimedia o total anual de
visualizações (utilizadores humanos, todos os acessos) do artigo do município em cada língua.
Gera data/wikipedia_<ano>_municipios.csv e data/wikipedia_<ano>_nuts3.csv (soma por NUTS III e quota).
Títulos ambíguos têm correspondência manual em TITULOS. Falhas são registadas para correção manual.
Nota: é um proxy da "imagem textual" (atenção discursiva), não da procura. Usa-se para distinguir se os LLMs seguem
o texto ou o comportamento. Pedidos com 1 s de intervalo e espera progressiva em 429 (a API limita a cadência; correr localmente, demora ~15 min) para respeitar a API.
"""
import argparse
import csv
import json
import time
import urllib.parse
import urllib.request
from collections import defaultdict
from pathlib import Path

AQUI = Path(__file__).parent
API = "https://wikimedia.org/api/rest_v1/metrics/pageviews/per-article/{lang}.wikipedia/all-access/user/{title}/monthly/{ini}/{fim}"
UA = "ISCE-temaA-research/1.0 (contacto: autores do estudo; uso académico)"

# título do artigo por (língua, município) quando difere do nome ou é ambíguo
TITULOS = {
    ("pt", "Lagoa|Algarve"): "Lagoa (Algarve)", ("pt", "Lagoa|Região Autónoma dos Açores"): "Lagoa (Açores)",
    ("pt", "Calheta|Região Autónoma da Madeira"): "Calheta (Madeira)", ("pt", "Calheta|Região Autónoma dos Açores"): "Calheta (Açores)",
    ("pt", "Santa Cruz"): "Santa Cruz (Madeira)", ("pt", "Porto"): "Porto", ("pt", "Lagos"): "Lagos (Portugal)",
    ("pt", "Moita"): "Moita", ("pt", "Mira"): "Mira (Portugal)", ("pt", "Cuba"): "Cuba (Portugal)", ("pt", "Fronteira"): "Fronteira (Portugal)",
    ("pt", "Nelas"): "Nelas", ("pt", "Borba"): "Borba (Portugal)", ("pt", "Avis"): "Avis (Portugal)", ("pt", "Mora"): "Mora (Portugal)",
    ("pt", "Crato"): "Crato (Portugal)", ("pt", "Horta"): "Horta (Açores)", ("pt", "Madalena"): "Madalena (Açores)",
    ("pt", "Velas"): "Velas (Açores)", ("pt", "Santana"): "Santana (Madeira)", ("pt", "Machico"): "Machico",
    ("pt", "Nordeste"): "Nordeste (Açores)", ("pt", "Povoação"): "Povoação", ("pt", "Corvo"): "Corvo (Açores)",
    ("pt", "Guarda"): "Guarda", ("pt", "Mafra"): "Mafra (Portugal)", ("pt", "Mértola"): "Mértola",
    ("en", "Lagoa|Algarve"): "Lagoa, Algarve", ("en", "Lagoa|Região Autónoma dos Açores"): "Lagoa, Azores",
    ("en", "Calheta|Região Autónoma da Madeira"): "Calheta, Madeira", ("en", "Calheta|Região Autónoma dos Açores"): "Calheta, Azores",
    ("en", "Santa Cruz"): "Santa Cruz, Madeira", ("en", "Lagos"): "Lagos, Portugal", ("en", "Lisboa"): "Lisbon",
    ("en", "Mira"): "Mira, Portugal", ("en", "Cuba"): "Cuba, Portugal", ("en", "Moita"): "Moita", ("en", "Nelas"): "Nelas",
    ("en", "Borba"): "Borba, Portugal", ("en", "Avis"): "Avis, Portugal", ("en", "Mora"): "Mora, Portugal", ("en", "Crato"): "Crato, Portugal",
    ("en", "Horta"): "Horta, Azores", ("en", "Madalena"): "Madalena, Azores", ("en", "Velas"): "Velas, Azores",
    ("en", "Santana"): "Santana, Madeira", ("en", "Nordeste"): "Nordeste, Azores", ("en", "Povoação"): "Povoação",
    ("en", "Corvo"): "Corvo Island", ("en", "Guarda"): "Guarda, Portugal", ("en", "Mafra"): "Mafra, Portugal",
    ("en", "Fronteira"): "Fronteira, Portugal", ("en", "Porto"): "Porto", ("en", "Braga"): "Braga", ("en", "Faro"): "Faro, Portugal",
    ("en", "Beja"): "Beja, Portugal", ("en", "Lagoa"): "Lagoa, Algarve", ("en", "Calheta"): "Calheta, Madeira",
    ("en", "Viana do Castelo"): "Viana do Castelo", ("en", "Setúbal"): "Setúbal", ("en", "Évora"): "Évora",
    ("en", "Santarém"): "Santarém, Portugal", ("en", "Portalegre"): "Portalegre, Portugal", ("en", "Leiria"): "Leiria",
    ("en", "Aveiro"): "Aveiro, Portugal", ("en", "Bragança"): "Bragança, Portugal", ("en", "Castelo Branco"): "Castelo Branco, Portugal",
    ("en", "Vila Real"): "Vila Real", ("en", "Coimbra"): "Coimbra", ("en", "Silves"): "Silves, Portugal",
    ("en", "Tavira"): "Tavira", ("en", "Loulé"): "Loulé", ("en", "Sines"): "Sines", ("en", "Elvas"): "Elvas",
    ("en", "Tomar"): "Tomar", ("en", "Ourém"): "Ourém", ("en", "Peniche"): "Peniche, Portugal", ("en", "Nazaré"): "Nazaré, Portugal",
    ("en", "Óbidos"): "Óbidos, Portugal", ("en", "Sintra"): "Sintra", ("en", "Cascais"): "Cascais", ("en", "Seia"): "Seia",
    ("en", "Chaves"): "Chaves, Portugal", ("en", "Lamego"): "Lamego", ("en", "Amarante"): "Amarante, Portugal",
    ("en", "Espinho"): "Espinho, Portugal", ("en", "Maia"): "Maia, Portugal", ("en", "Trofa"): "Trofa",
    ("en", "Fafe"): "Fafe", ("en", "Vizela"): "Vizela", ("en", "Ovar"): "Ovar, Portugal", ("en", "Anadia"): "Anadia, Portugal",
    ("en", "Mealhada"): "Mealhada", ("en", "Penela"): "Penela", ("en", "Soure"): "Soure, Portugal", ("en", "Pombal"): "Pombal, Portugal",
    ("en", "Batalha"): "Batalha, Portugal", ("en", "Alcobaça"): "Alcobaça, Portugal", ("en", "Alenquer"): "Alenquer, Portugal",
    ("en", "Abrantes"): "Abrantes", ("en", "Almeirim"): "Almeirim, Portugal", ("en", "Coruche"): "Coruche", ("en", "Golegã"): "Golegã",
    ("en", "Loures"): "Loures", ("en", "Oeiras"): "Oeiras, Portugal", ("en", "Amadora"): "Amadora", ("en", "Almada"): "Almada",
    ("en", "Palmela"): "Palmela", ("en", "Sesimbra"): "Sesimbra", ("en", "Montijo"): "Montijo", ("en", "Barreiro"): "Barreiro, Portugal",
    ("en", "Seixal"): "Seixal", ("en", "Alcochete"): "Alcochete", ("en", "Grândola"): "Grândola", ("en", "Odemira"): "Odemira",
    ("en", "Serpa"): "Serpa", ("en", "Moura"): "Moura, Portugal", ("en", "Ourique"): "Ourique", ("en", "Alvito"): "Alvito, Portugal",
    ("en", "Estremoz"): "Estremoz", ("en", "Redondo"): "Redondo, Portugal", ("en", "Portel"): "Portel, Portugal",
    ("en", "Mourão"): "Mourão", ("en", "Monforte"): "Monforte, Portugal", ("en", "Nisa"): "Nisa, Portugal",
    ("en", "Marvão"): "Marvão", ("en", "Gavião"): "Gavião, Portugal", ("en", "Sousel"): "Sousel", ("en", "Arronches"): "Arronches",
    ("en", "Monchique"): "Monchique", ("en", "Albufeira"): "Albufeira", ("en", "Portimão"): "Portimão", ("en", "Olhão"): "Olhão",
    ("en", "Aljezur"): "Aljezur", ("en", "Alcoutim"): "Alcoutim", ("en", "Funchal"): "Funchal", ("en", "Machico"): "Machico",
    ("en", "Porto Santo"): "Porto Santo Island", ("en", "Porto Moniz"): "Porto Moniz", ("en", "Ponta do Sol"): "Ponta do Sol, Madeira",
    ("en", "São Vicente"): "São Vicente, Madeira", ("en", "Ribeira Brava"): "Ribeira Brava, Madeira",
    ("en", "Câmara de Lobos"): "Câmara de Lobos", ("en", "Ponta Delgada"): "Ponta Delgada", ("en", "Ribeira Grande"): "Ribeira Grande, Azores",
    ("en", "Vila Franca do Campo"): "Vila Franca do Campo", ("en", "Angra do Heroísmo"): "Angra do Heroísmo",
    ("en", "Praia da Vitória"): "Praia da Vitória", ("en", "Lajes do Pico"): "Lajes do Pico", ("en", "São Roque do Pico"): "São Roque do Pico",
    ("en", "Lajes das Flores"): "Lajes das Flores", ("en", "Santa Cruz das Flores"): "Santa Cruz das Flores",
    ("en", "Santa Cruz da Graciosa"): "Santa Cruz da Graciosa", ("en", "Vila do Porto"): "Vila do Porto",
}


def pageviews(lang, title, ini, fim, tentativas=5):
    url = API.format(lang=lang, title=urllib.parse.quote(title.replace(" ", "_"), safe=""), ini=ini, fim=fim)
    for i in range(tentativas):
        req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "application/json"})
        try:
            with urllib.request.urlopen(req, timeout=60) as r:
                d = json.loads(r.read().decode("utf-8"))
            return sum(it["views"] for it in d.get("items", []))
        except urllib.error.HTTPError as e:
            if e.code == 429 and i < tentativas - 1:
                time.sleep(3 * (i + 1)); continue
            raise


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--ano", default="2025")
    ap.add_argument("--linguas", default="pt,en")
    ap.add_argument("--limite", type=int, help="só os primeiros N municípios (teste)")
    a = ap.parse_args()
    linguas = a.linguas.split(",")
    ini, fim = f"{a.ano}0101", f"{a.ano}1231"
    with open(AQUI / "data" / "municipios_nuts3_2024.csv", encoding="utf-8") as f:
        muns = list(csv.DictReader(f))
    if a.limite:
        muns = muns[:a.limite]
    saida = AQUI / "data" / f"wikipedia_{a.ano}_municipios.csv"
    feitos = {}
    if saida.exists():
        with open(saida, encoding="utf-8") as f:
            for r in csv.DictReader(f):
                feitos[(r["lang"], r["municipio"], r["nuts3"])] = r
    falhas = []
    with open(saida, "a" if feitos else "w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        if not feitos:
            w.writerow(["lang", "municipio", "nuts3", "titulo", "visualizacoes"])
        for m in muns:
            for lang in linguas:
                if (lang, m["municipio"], m["nuts3"]) in feitos:
                    continue
                titulo = (TITULOS.get((lang, f"{m['municipio']}|{m['nuts3']}")) or TITULOS.get((lang, m["municipio"]))
                          or m["municipio"])
                try:
                    v = pageviews(lang, titulo, ini, fim)
                except Exception as e:  # noqa: BLE001
                    v = ""
                    falhas.append((lang, m["municipio"], titulo, str(e)[:60]))
                w.writerow([lang, m["municipio"], m["nuts3"], titulo, v]); f.flush()
                time.sleep(1.0)
    # agregação
    with open(saida, encoding="utf-8") as f:
        rows = [r for r in csv.DictReader(f) if r["visualizacoes"]]
    agg = defaultdict(lambda: defaultdict(int))
    for r in rows:
        agg[r["lang"]][r["nuts3"]] += int(r["visualizacoes"])
    with open(AQUI / "data" / f"wikipedia_{a.ano}_nuts3.csv", "w", encoding="utf-8", newline="") as f:
        w = csv.writer(f); w.writerow(["lang", "nuts3", "visualizacoes", "quota"])
        for lang, d in agg.items():
            tot = sum(d.values())
            for n, v in sorted(d.items(), key=lambda kv: -kv[1]):
                w.writerow([lang, n, v, round(v / tot, 5)])
    print(f"{len(rows)} municípios×línguas com valor; {len(falhas)} falhas (corrigir títulos em TITULOS):")
    for fl in falhas[:30]:
        print("  ", fl)


if __name__ == "__main__":
    main()
