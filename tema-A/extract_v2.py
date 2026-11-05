"""Extração v2: o modelo identifica lugar, nível e município; a NUTS III vem sempre da tabela (reprocess.Geocodificador).

Uso:
  python extract_v2.py --ensaio                                   # sem API, dicionário pequeno
  python extract_v2.py                                            # todas as respostas em data/v2/respostas_*.jsonl
  python extract_v2.py --entrada data/respostas.jsonl --saida data/extracoes_v2_reextr.jsonl   # reextrair o piloto
  python extract_v2.py --condicao confirmatorio                   # só uma condição

Diferenças face a extract.py (v1):
  - o prompt não pede NUTS III nem a lista de 26 regiões; pede lugar, nível (destino/atracao), destino_pai, município,
    "abrangente" (vários municípios), "existe", e um campo "contexto" curto (ilha ou região referida no texto), que serve
    para desambiguar municípios homónimos (Lagoa, Calheta);
  - pede explicitamente para ignorar títulos e frases introdutórias e para marcar como destino cada paragem de dia num roteiro;
  - a NUTS III é derivada pela tabela de municípios e pelos macro-destinos (livro de códigos), nunca pelo modelo;
  - lê as respostas v2 (com condicao, variante, duracao) e também as do piloto.
Saída: um item por linha, já geocodificado (mesmos campos que data/extracoes_v2.jsonl). A amostra de verificação humana
faz-se depois com verificacao_v2.py.
"""
import argparse
import json
import re
import threading
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

from llm import perguntar
from reprocess import Geocodificador

AQUI = Path(__file__).parent

INSTRUCAO = """És um assistente de codificação para um estudo de turismo.
Lê a resposta abaixo, dada a um turista sobre Portugal, e lista TODOS os lugares em Portugal recomendados, pela ordem em que aparecem.

Para cada lugar indica:
- "lugar": o nome tal como aparece no texto (sem descrições);
- "nivel": "destino" se for um item principal (cada entrada de lista numerada ou com marcadores de primeiro nível, cada título de secção dedicado a um lugar, cada paragem ou base de um dia num roteiro), ou "atracao" se for referido DENTRO de um destino (monumento, bairro, praia, museu, miradouro, aldeia visitada em excursão, restaurante). Atrações têm "destino_pai" com o nome exato do destino; destinos têm "destino_pai": null;
- "municipio": o município português onde fica. Se abranger vários municípios (serra, rio, região, parque natural, ilha, costa), indica o município mais associado e põe "abrangente": true; caso contrário "abrangente": false;
- "contexto": a ilha, região ou arquipélago referido no texto para esse lugar, se houver (ex.: "São Miguel, Açores", "Madeira", "Algarve"); senão "";
- "existe": false se o lugar não existir ou não ficar em Portugal (lugares em Espanha contam como false); caso contrário true.

NÃO incluas títulos da resposta, frases introdutórias ou de fecho, nem rubricas sem lugar (ex.: "10 lugares a visitar", "Dicas práticas", "Dia 3").
Num roteiro, cada dia tem pelo menos um destino: o lugar onde o viajante dorme ou passa a maior parte do dia.

Responde só com JSON, sem texto à volta, no formato:
[{{"posicao": 1, "lugar": "...", "nivel": "destino", "destino_pai": null, "municipio": "...", "abrangente": false, "contexto": "", "existe": true}}]

RESPOSTA:
{resposta}"""

ENSAIO = {"Lisboa": "Lisboa", "Porto": "Porto", "Sintra": "Sintra", "Lagos": "Lagos", "Évora": "Évora", "Coimbra": "Coimbra",
          "Óbidos": "Óbidos", "Peso da Régua": "Peso da Régua", "Funchal": "Funchal", "Vale do Douro": "Peso da Régua"}


def extrair_ensaio(texto):
    itens, pos = [], 0
    for linha in texto.splitlines():
        for nome, mun in ENSAIO.items():
            if nome in linha:
                pos += 1
                itens.append({"posicao": pos, "lugar": nome, "nivel": "destino", "destino_pai": None, "municipio": mun,
                              "abrangente": nome == "Vale do Douro", "contexto": "", "existe": True})
                break
    return itens


def ler_json(texto):
    m = re.search(r"\[.*\]", texto, re.S)
    if not m:
        raise ValueError("sem JSON na resposta de extração")
    itens = json.loads(m.group(0))
    if not isinstance(itens, list):
        raise ValueError("JSON não é uma lista")
    return itens


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--ensaio", action="store_true")
    ap.add_argument("--entrada", nargs="*", help="ficheiros de respostas; por omissão data/v2/respostas_*.jsonl")
    ap.add_argument("--condicao", help="filtra por condição (confirmatorio, exploratorio, pesquisa_web)")
    ap.add_argument("--saida", default=str(AQUI / "data" / "v2" / "extracoes_v2.jsonl"))
    ap.add_argument("--limite", type=int)
    a = ap.parse_args()

    cfg = json.loads((AQUI / ("config_v2.json" if (AQUI / "config_v2.json").exists() else "config.json")).read_text(encoding="utf-8"))
    entradas = [Path(x) for x in a.entrada] if a.entrada else sorted((AQUI / "data" / "v2").glob("respostas_*.jsonl"))
    if not entradas:
        raise SystemExit("Sem ficheiros de respostas. Indicar --entrada ou correr collect_v2.py primeiro.")
    respostas = []
    for p in entradas:
        respostas += [json.loads(l) for l in p.read_text(encoding="utf-8").splitlines()]
    if a.condicao:
        respostas = [r for r in respostas if r.get("condicao") == a.condicao]
    saida = Path(a.saida); saida.parent.mkdir(parents=True, exist_ok=True)
    feitos = set()
    if saida.exists():
        feitos = {json.loads(l)["id"] for l in saida.read_text(encoding="utf-8").splitlines()}
    pendentes = [r for r in respostas if r["id"] not in feitos]
    if a.limite is not None:
        pendentes = pendentes[:a.limite]
    print(f"{len(respostas)} respostas lidas; {len(pendentes)} por extrair.")

    ex = cfg["extracao"]
    geo = Geocodificador()
    trinco = threading.Lock()
    erros = [0]
    with open(saida, "a", encoding="utf-8") as out:
        def correr(r):
            for tentativa in range(3):
                try:
                    if a.ensaio:
                        itens = extrair_ensaio(r["resposta"])
                    else:
                        txt, _ = perguntar(ex["fornecedor"], ex["modelo"], ex["chave_env"],
                                           INSTRUCAO.format(resposta=r["resposta"]), max_tokens=8000, esforco="desligado")
                        itens = ler_json(txt)
                    break
                except (RuntimeError, ValueError, json.JSONDecodeError) as e:
                    if tentativa == 2:
                        with trinco:
                            erros[0] += 1
                        print(f"[erro] {r['id']}: {e}", flush=True)
                        return
            meta = {k: r.get(k) for k in ("id", "condicao", "modelo", "template", "variante", "duracao", "lang", "rep", "pesquisa_web")}
            with trinco:
                for it in itens:
                    it.setdefault("existe", True); it.setdefault("abrangente", False); it.setdefault("contexto", "")
                    it.setdefault("nivel", "destino"); it.setdefault("destino_pai", None)
                    out.write(json.dumps({**meta, **geo.item(it)}, ensure_ascii=False) + "\n")
                out.flush()

        with ThreadPoolExecutor(max_workers=cfg["paralelo"]) as pool:
            list(pool.map(correr, pendentes))

    total = sum(1 for _ in saida.open(encoding="utf-8"))
    print(f"Extração concluída: {total} itens em {saida}; {erros[0]} respostas com erro.")
    geo.resumo(sum(geo.contagem[k] for k in ("municipio", "macro", "macro_1nuts", "titulo", "municipio_desconhecido")))
    if geo.desconhecidos:
        print("Rever os municípios não reconhecidos antes da análise (ALIAS em reprocess.py ou tabela de municípios).")


if __name__ == "__main__":
    main()
