"""Chamadas mínimas às APIs de OpenAI, Anthropic e Google (só biblioteca padrão)."""
import json
import os
import time
import urllib.error
import urllib.request
from pathlib import Path

# Chaves opcionalmente num ficheiro .env ao lado dos scripts (NOME=valor por linha); não partilhar este ficheiro.
_ENV = Path(__file__).parent / ".env"
if _ENV.exists():
    for _l in _ENV.read_text(encoding="utf-8-sig").splitlines():
        if "=" in _l and not _l.lstrip().startswith("#"):
            _k, _v = _l.split("=", 1)
            os.environ.setdefault(_k.strip(), _v.strip().strip('"'))
if "OPEN_ROUTER_API_KEY" in os.environ:
    os.environ.setdefault("OPENROUTER_API_KEY", os.environ["OPEN_ROUTER_API_KEY"])


def _post(url, headers, body, tentativas=4):
    data = json.dumps(body).encode("utf-8")
    for i in range(tentativas):
        req = urllib.request.Request(url, data=data, headers={"Content-Type": "application/json", **headers})
        try:
            with urllib.request.urlopen(req, timeout=120) as r:
                return json.loads(r.read().decode("utf-8"))
        except urllib.error.HTTPError as e:
            if e.code in (429, 500, 502, 503, 529) and i < tentativas - 1:
                time.sleep(5 * (i + 1))
                continue
            raise RuntimeError(f"HTTP {e.code}: {e.read().decode('utf-8', 'replace')[:300]}")


def perguntar(fornecedor, modelo, chave_env, prompt, max_tokens=2000, esforco=None):
    """Devolve (texto, versao_do_modelo_reportada)."""
    chave = os.environ.get(chave_env)
    if not chave:
        raise RuntimeError(f"Falta a variável de ambiente {chave_env}")
    msgs = [{"role": "user", "content": prompt}]
    if fornecedor == "openrouter":
        r = _post("https://openrouter.ai/api/v1/chat/completions",
                  {"Authorization": f"Bearer {chave}", "X-Title": "ISCE tema A"},
                  {"model": modelo, "messages": msgs, "max_tokens": max_tokens,
                   **({"reasoning": {"enabled": False}} if esforco == "desligado" else {})})
        if "choices" not in r:
            raise RuntimeError(f"Resposta sem conteúdo: {str(r)[:300]}")
        esc = r["choices"][0]
        texto = esc["message"].get("content") or ""
        if not texto.strip() or esc.get("finish_reason") == "length":
            raise RuntimeError(f"Resposta vazia ou cortada (finish_reason={esc.get('finish_reason')})")
        return texto, f"{r.get('model', modelo)} via {r.get('provider', '?')}"
    if fornecedor == "anthropic":
        r = _post("https://api.anthropic.com/v1/messages",
                  {"x-api-key": chave, "anthropic-version": "2023-06-01"},
                  {"model": modelo, "max_tokens": max_tokens, "messages": msgs})
        return "".join(b.get("text", "") for b in r["content"]), r.get("model", modelo)
    if fornecedor == "openai":
        r = _post("https://api.openai.com/v1/chat/completions",
                  {"Authorization": f"Bearer {chave}"},
                  {"model": modelo, "messages": msgs})
        return r["choices"][0]["message"]["content"], r.get("model", modelo)
    if fornecedor == "google":
        r = _post(f"https://generativelanguage.googleapis.com/v1beta/models/{modelo}:generateContent",
                  {"x-goog-api-key": chave},
                  {"contents": [{"parts": [{"text": prompt}]}]})
        partes = r["candidates"][0]["content"]["parts"]
        return "".join(p.get("text", "") for p in partes), r.get("modelVersion", modelo)
    raise ValueError(f"Fornecedor desconhecido: {fornecedor}")
