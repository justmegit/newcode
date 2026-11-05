"""Recolha v2: prompts com variantes e durações, modelos abertos e condição com pesquisa web.

Uso:
  python collect_v2.py --ensaio                 # circuito sem APIs
  python collect_v2.py --condicao confirmatorio # geral, roteiro (3/7/14 dias), pouco conhecidos; 3 variantes; todos os modelos
  python collect_v2.py --condicao exploratorio  # restantes tipos, variante 1
  python collect_v2.py --condicao pesquisa_web  # geral e roteiro de 7 dias com plugin web (só modelos fechados)
  python collect_v2.py --condicao confirmatorio --modelo claude --limite 5

Grava em data/v2/respostas_<condicao>.jsonl, com id = condicao|modelo|template|variante|duracao|lang|rep.
Retoma onde parou. Regista modelo e fornecedor devolvidos, data/hora, finish_reason e utilização de tokens.
"""
import argparse
import csv
import json
import os
import random
import threading
import time
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from pathlib import Path

import llm  # carrega .env e expõe perguntar()

AQUI = Path(__file__).parent


def perguntar_openrouter(modelo, chave_env, prompt, max_tokens, plugins=None):
    """Como llm.perguntar, mas devolve também finish_reason e usage e aceita plugins (pesquisa web)."""
    chave = os.environ.get(chave_env)
    if not chave:
        raise RuntimeError(f"Falta a variável de ambiente {chave_env}")
    body = {"model": modelo, "messages": [{"role": "user", "content": prompt}], "max_tokens": max_tokens}
    if plugins:
        body["plugins"] = plugins
    data = json.dumps(body).encode("utf-8")
    for i in range(4):
        req = urllib.request.Request("https://openrouter.ai/api/v1/chat/completions", data=data,
                                     headers={"Content-Type": "application/json", "Authorization": f"Bearer {chave}",
                                              "X-Title": "ISCE tema A v2"})
        try:
            with urllib.request.urlopen(req, timeout=180) as r:
                j = json.loads(r.read().decode("utf-8"))
            break
        except urllib.error.HTTPError as e:
            if e.code in (429, 500, 502, 503, 529) and i < 3:
                time.sleep(5 * (i + 1)); continue
            raise RuntimeError(f"HTTP {e.code}: {e.read().decode('utf-8', 'replace')[:300]}")
    if "choices" not in j:
        raise RuntimeError(f"Resposta sem conteúdo: {str(j)[:300]}")
    esc = j["choices"][0]
    texto = esc["message"].get("content") or ""
    if not texto.strip() or esc.get("finish_reason") == "length":
        raise RuntimeError(f"Resposta vazia ou cortada (finish_reason={esc.get('finish_reason')})")
    anot = esc["message"].get("annotations") or []
    return {"resposta": texto, "modelo_versao": f"{j.get('model', modelo)} via {j.get('provider', '?')}",
            "finish_reason": esc.get("finish_reason"), "usage": j.get("usage"),
            "n_citacoes_web": len(anot), "citacoes_web": [c.get("url_citation", {}).get("url") for c in anot][:20]}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--condicao", choices=["confirmatorio", "exploratorio", "pesquisa_web"], default="confirmatorio")
    ap.add_argument("--ensaio", action="store_true")
    ap.add_argument("--modelo")
    ap.add_argument("--limite", type=int)
    a = ap.parse_args()
    cfg = json.loads((AQUI / "config_v2.json").read_text(encoding="utf-8"))
    des = cfg["desenho"][a.condicao]
    with open(AQUI / "prompts_v2.csv", encoding="utf-8") as f:
        prompts = [p for p in csv.DictReader(f) if p["lang"] in cfg["linguas"] and p["template"] in des["templates"]
                   and int(p["variante"]) in des["variantes"]
                   and (not des.get("duracoes") or not p["duracao"] or int(p["duracao"]) in des["duracoes"])]
    modelos = [m for m in cfg["modelos"] if (not a.modelo or m["rotulo"] == a.modelo)
               and (not des.get("modelos") or m["rotulo"] in des["modelos"])]
    por_confirmar = [m["modelo"] for m in modelos if m["modelo"].startswith("CONFIRMAR")]
    if por_confirmar and not a.ensaio:
        raise SystemExit(f"Identificadores de modelo por confirmar em config_v2.json: {por_confirmar}")
    plugins = [des["plugin"]] if a.condicao == "pesquisa_web" else None
    reps = des.get("repeticoes", cfg["repeticoes"])

    saida = AQUI / "data" / "v2" / f"respostas_{a.condicao}.jsonl"
    saida.parent.mkdir(parents=True, exist_ok=True)
    feitos = set()
    if saida.exists():
        feitos = {json.loads(l)["id"] for l in saida.read_text(encoding="utf-8").splitlines()}
    tarefas = []
    for m in modelos:
        for p in prompts:
            for rep in range(1, reps + 1):
                rid = f"{a.condicao}|{m['rotulo']}|{p['template']}|{p['variante']}|{p['duracao'] or '-'}|{p['lang']}|{rep}"
                if rid not in feitos:
                    tarefas.append((rid, m, p, rep))
    if a.limite is not None:
        tarefas = tarefas[:a.limite]
    print(f"{len(tarefas)} chamadas a fazer ({len(prompts)} prompts × {len(modelos)} modelos × {reps} repetições, menos as feitas)")
    rng = random.Random(cfg["semente"]); trinco = threading.Lock(); parar = threading.Event(); cont = {"novas": 0, "erros": 0}
    with open(saida, "a", encoding="utf-8") as out:
        def correr(t):
            rid, m, p, rep = t
            if parar.is_set():
                return
            try:
                if a.ensaio:
                    res = {"resposta": "\n".join(f"Dia {i}: {l}" for i, l in enumerate(rng.sample(
                        ["Lisboa", "Porto", "Sintra", "Évora", "Coimbra", "Lagos", "Peso da Régua", "Funchal", "Óbidos"], 7), 1)),
                           "modelo_versao": "ensaio", "finish_reason": "stop", "usage": None, "n_citacoes_web": 0, "citacoes_web": []}
                else:
                    res = perguntar_openrouter(m["modelo"], m["chave_env"], p["prompt"], cfg["max_tokens"], plugins)
            except RuntimeError as e:
                with trinco:
                    if str(e).startswith(("HTTP 401", "HTTP 402", "HTTP 403")):
                        parar.set(); print(f"Paragem: problema de conta/créditos. {e}", flush=True)
                    else:
                        cont["erros"] += 1; print(f"[erro] {rid}: {e}", flush=True)
                return
            reg = {"id": rid, "condicao": a.condicao, "modelo": m["rotulo"], "modelo_pedido": m["modelo"],
                   "template": p["template"], "variante": int(p["variante"]), "duracao": int(p["duracao"]) if p["duracao"] else None,
                   "lang": p["lang"], "rep": rep, "prompt": p["prompt"], "pesquisa_web": bool(plugins),
                   "data": datetime.now(timezone.utc).isoformat(timespec="seconds"), "ensaio": a.ensaio, **res}
            with trinco:
                out.write(json.dumps(reg, ensure_ascii=False) + "\n"); out.flush(); cont["novas"] += 1
                if cont["novas"] % 25 == 0:
                    print(f"{cont['novas']}/{len(tarefas)}", flush=True)
        with ThreadPoolExecutor(max_workers=cfg["paralelo"]) as ex:
            list(ex.map(correr, tarefas))
    print(f"Concluído: {cont['novas']} novas, {cont['erros']} erros, em {saida}")


if __name__ == "__main__":
    main()
