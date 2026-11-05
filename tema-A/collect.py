"""Recolha: envia cada pergunta de prompts.csv a cada modelo, N repetições, e grava em data/respostas.jsonl.

Uso:
  python collect.py --ensaio      # sem APIs, respostas fictícias, para testar o circuito
  python collect.py               # recolha real (precisa da chave de API no .env)
  python collect.py --modelo claude --limite 5   # teste curto com um modelo

Só usa as línguas de "linguas" em config.json.
Retoma automaticamente: chamadas já gravadas não são repetidas.
"""
import argparse
import csv
import json
import random
import threading
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from pathlib import Path

import llm

AQUI = Path(__file__).parent

LUGARES_ENSAIO = ["Lisboa", "Porto", "Sintra", "Lagos", "Évora", "Coimbra", "Óbidos",
                  "Peso da Régua", "Monsaraz", "Ponta Delgada", "Funchal", "Aveiro", "Tavira"]


def resposta_ensaio(rng):
    escolha = rng.sample(LUGARES_ENSAIO, 10)
    return "\n".join(f"{i}. {l} - descrição." for i, l in enumerate(escolha, 1)), "ensaio"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--ensaio", action="store_true")
    ap.add_argument("--modelo", help="rótulo de um só modelo (ex.: claude)")
    ap.add_argument("--limite", type=int, help="máximo de chamadas novas")
    ap.add_argument("--saida", default=str(AQUI / "data" / "respostas.jsonl"))
    a = ap.parse_args()

    cfg = json.loads((AQUI / "config.json").read_text(encoding="utf-8"))
    with open(AQUI / "prompts.csv", encoding="utf-8") as f:
        prompts = [p for p in csv.DictReader(f) if p["lang"] in cfg["linguas"]]
    modelos = [m for m in cfg["modelos"] if not a.modelo or m["rotulo"] == a.modelo]

    saida = Path(a.saida)
    saida.parent.mkdir(exist_ok=True)
    feitos = set()
    if saida.exists():
        for linha in saida.read_text(encoding="utf-8").splitlines():
            feitos.add(json.loads(linha)["id"])

    if not a.ensaio:
        em_falta = {m["chave_env"] for m in modelos if not llm.os.environ.get(m["chave_env"])}
        if em_falta:
            raise SystemExit(f"Falta(m) a(s) chave(s): {', '.join(sorted(em_falta))}. Ver README, passo 1.")

    tarefas = [(m, p, rep) for m in modelos for p in prompts for rep in range(1, cfg["repeticoes"] + 1)
               if f"{m['rotulo']}|{p['template']}|{p['lang']}|{rep}" not in feitos]
    if a.limite is not None:
        tarefas = tarefas[:a.limite]

    rng = random.Random(cfg["semente"])
    trinco = threading.Lock()
    parar = threading.Event()
    contagem = {"novas": 0, "erros": 0}

    with open(saida, "a", encoding="utf-8") as out:
        def correr(t):
            m, p, rep = t
            if parar.is_set():
                return
            rid = f"{m['rotulo']}|{p['template']}|{p['lang']}|{rep}"
            try:
                if a.ensaio:
                    texto, versao = resposta_ensaio(rng)
                else:
                    texto, versao = llm.perguntar(m["fornecedor"], m["modelo"], m["chave_env"],
                                                  p["prompt"], cfg["max_tokens"])
            except RuntimeError as e:
                with trinco:
                    if str(e).startswith(("HTTP 401", "HTTP 402", "HTTP 403")):
                        parar.set()
                        print(f"Paragem: problema de conta/créditos. {e}", flush=True)
                    else:
                        contagem["erros"] += 1
                        print(f"[erro] {rid}: {e}", flush=True)
                return
            registo = {"id": rid, "modelo": m["rotulo"], "modelo_pedido": m["modelo"],
                       "modelo_versao": versao, "template": p["template"], "lang": p["lang"],
                       "rep": rep, "prompt": p["prompt"], "resposta": texto,
                       "data": datetime.now(timezone.utc).isoformat(timespec="seconds"),
                       "ensaio": a.ensaio}
            with trinco:
                out.write(json.dumps(registo, ensure_ascii=False) + "\n")
                out.flush()
                contagem["novas"] += 1
                if contagem["novas"] % 25 == 0:
                    print(f"{contagem['novas']}/{len(tarefas)}", flush=True)

        with ThreadPoolExecutor(max_workers=cfg["paralelo"]) as ex:
            list(ex.map(correr, tarefas))

    print(f"Concluído: {contagem['novas']} chamadas novas, {contagem['erros']} erros, em {saida}")


if __name__ == "__main__":
    main()
