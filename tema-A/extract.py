"""Extração: identifica os lugares de cada resposta e atribui município e NUTS III.

Uso:
  python extract.py --ensaio   # sem API (dicionário pequeno), para testar o circuito
  python extract.py            # extração com o modelo definido em config.json

Gera data/extracoes.jsonl (um lugar por linha) e data/verificacao_humana.csv
(amostra para os dois codificadores humanos preencherem).
"""
import argparse
import csv
import json
import random
import re
import threading
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

from llm import perguntar

AQUI = Path(__file__).parent

ENSAIO = {"Lisboa": ("Lisboa", "Grande Lisboa"), "Porto": ("Porto", "Área Metropolitana do Porto"),
          "Sintra": ("Sintra", "Grande Lisboa"), "Lagos": ("Lagos", "Algarve"),
          "Évora": ("Évora", "Alentejo Central"), "Coimbra": ("Coimbra", "Região de Coimbra"),
          "Óbidos": ("Óbidos", "Oeste"), "Peso da Régua": ("Peso da Régua", "Douro"),
          "Monsaraz": ("Reguengos de Monsaraz", "Alentejo Central"),
          "Ponta Delgada": ("Ponta Delgada", "Região Autónoma dos Açores"),
          "Funchal": ("Funchal", "Região Autónoma da Madeira"), "Aveiro": ("Aveiro", "Região de Aveiro"),
          "Tavira": ("Tavira", "Algarve")}

INSTRUCAO = """És um assistente de codificação para um estudo de turismo.
Lê a resposta abaixo, dada a um turista sobre Portugal, e lista TODOS os lugares em Portugal recomendados, pela ordem em que aparecem.
Para cada lugar indica o município português onde fica e a NUTS III (versão 2024), escolhida EXATAMENTE desta lista:
{nuts}
Se um lugar abranger vários municípios (ex.: uma serra, um rio, uma região), usa o município principal e marca "abrangente": true.
Se um lugar não existir ou não ficar em Portugal, marca "existe": false.
Classifica cada lugar num de dois níveis:
- "destino": um dos itens principais recomendados (cada entrada da lista numerada, cada título, ou cada paragem de um dia num roteiro);
- "atracao": um lugar referido DENTRO de um destino principal (monumento, bairro, praia, miradouro, museu, etc.). Indica em "destino_pai" o nome exato do destino principal a que pertence.
Os destinos têm "destino_pai": null.
Responde só com JSON, sem texto à volta, no formato:
[{{"posicao": 1, "lugar": "...", "nivel": "destino", "destino_pai": null, "municipio": "...", "nuts3": "...", "abrangente": false, "existe": true}}]

RESPOSTA:
{resposta}"""


def extrair_ensaio(texto):
    itens, pos = [], 0
    for linha in texto.splitlines():
        for nome, (mun, n3) in ENSAIO.items():
            if nome in linha:
                pos += 1
                itens.append({"posicao": pos, "lugar": nome, "nivel": "destino", "destino_pai": None,
                              "municipio": mun, "nuts3": n3,
                              "abrangente": False, "existe": True})
                break
    return itens


def ler_json(texto):
    m = re.search(r"\[.*\]", texto, re.S)
    if not m:
        raise ValueError("sem JSON na resposta de extração")
    return json.loads(m.group(0))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--ensaio", action="store_true")
    ap.add_argument("--entrada", default=str(AQUI / "data" / "respostas.jsonl"))
    ap.add_argument("--saida", default=str(AQUI / "data" / "extracoes.jsonl"))
    a = ap.parse_args()

    cfg = json.loads((AQUI / "config.json").read_text(encoding="utf-8"))
    with open(AQUI / "data" / "nuts3.csv", encoding="utf-8") as f:
        nuts = [r["nuts3"] for r in csv.DictReader(f)]
    respostas = [json.loads(l) for l in Path(a.entrada).read_text(encoding="utf-8").splitlines()]

    saida = Path(a.saida)
    feitos = set()
    if saida.exists():
        feitos = {json.loads(l)["id"] for l in saida.read_text(encoding="utf-8").splitlines()}

    ex = cfg["extracao"]
    invalidos = [0]
    trinco = threading.Lock()
    pendentes = [r for r in respostas if r["id"] not in feitos]
    with open(saida, "a", encoding="utf-8") as out:
        def correr(r):
            for tentativa in range(3):
                try:
                    if a.ensaio:
                        itens = extrair_ensaio(r["resposta"])
                    else:
                        txt, _ = perguntar(ex["fornecedor"], ex["modelo"], ex["chave_env"],
                                           INSTRUCAO.format(nuts="\n".join(nuts), resposta=r["resposta"]),
                                           max_tokens=8000, esforco="desligado")
                        itens = ler_json(txt)
                    break
                except (RuntimeError, ValueError, json.JSONDecodeError) as e:
                    if tentativa == 2:
                        print(f"[erro] {r['id']}: {e}", flush=True)
                        return
            with trinco:
                for it in itens:
                    if it.get("nuts3") not in nuts:
                        invalidos[0] += 1
                        it["nuts3_invalida"] = True
                    out.write(json.dumps({"id": r["id"], "modelo": r["modelo"], "template": r["template"],
                                          "lang": r["lang"], "rep": r["rep"], **it}, ensure_ascii=False) + "\n")
                out.flush()

        with ThreadPoolExecutor(max_workers=cfg["paralelo"]) as pool:
            list(pool.map(correr, pendentes))

    # Amostra para verificação humana (por resposta, não por lugar)
    extr = [json.loads(l) for l in saida.read_text(encoding="utf-8").splitlines()]
    ids = sorted({e["id"] for e in extr})
    if not ids:
        raise SystemExit("Nenhum lugar extraído; ver os erros acima.")
    rng = random.Random(cfg["semente"])
    amostra = set(rng.sample(ids, max(1, round(len(ids) * cfg["amostra_verificacao"]))))
    texto = {r["id"]: r["resposta"] for r in respostas}
    with open(saida.parent / "verificacao_humana.csv", "w", encoding="utf-8-sig", newline="") as f:
        w = csv.writer(f, delimiter=";")
        w.writerow(["id", "posicao", "lugar", "nivel", "destino_pai", "municipio", "nuts3", "existe",
                    "codificador_1_correto (s/n)", "codificador_2_correto (s/n)", "nota", "resposta_original"])
        for e in extr:
            if e["id"] in amostra:
                w.writerow([e["id"], e["posicao"], e["lugar"], e.get("nivel"), e.get("destino_pai") or "",
                            e["municipio"], e["nuts3"], e.get("existe"),
                            "", "", "", texto.get(e["id"], "") if e["posicao"] == 1 else ""])
    print(f"Extração concluída: {len(extr)} lugares de {len(ids)} respostas; "
          f"{invalidos[0]} com NUTS III fora da lista; {len(amostra)} respostas na amostra humana.")


if __name__ == "__main__":
    main()
