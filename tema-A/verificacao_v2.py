"""Verificação humana v2: dois exercícios separados (recall às cegas e precisão por dimensão).

Uso:
  python verificacao_v2.py            # gera data/verificacao_recall.xlsx e data/verificacao_precisao.xlsx
  python verificacao_v2.py --n-recall 30 --n-precisao 96

Exercício A (recall): N respostas estratificadas por modelo e tipo de pergunta. Cada codificador lê a resposta e lista,
sem ver a extração, os destinos principais (nome e município). Mede o que o extrator perdeu.
Exercício B (precisão): amostra de linhas extraídas (destinos principais). Cada codificador avalia, em separado,
se o lugar é destino principal, se o município está certo e se a NUTS III está certa. Mede o que o extrator inventou ou trocou.
Os dois codificadores preenchem cópias separadas. Métricas: python metricas_verificacao.py
"""
import argparse
import csv
import json
import random
from collections import defaultdict
from pathlib import Path

from openpyxl import Workbook
from openpyxl.styles import Alignment, Font, PatternFill
from openpyxl.worksheet.datavalidation import DataValidation

AQUI = Path(__file__).parent
FUNDO = PatternFill("solid", fgColor="FFF2CC")

INSTR_A = [
    "Exercício A: recall dos destinos principais (tema A)",
    "",
    "Objetivo: saber se o extrator automático perde destinos. Por isso NÃO vê a extração; lista os destinos a partir do texto.",
    "",
    "Como fazer:",
    "1. Guardar uma cópia só sua, com as suas iniciais no nome. Não combinar com a outra pessoa.",
    "2. Na folha Respostas, ler cada resposta pela ordem.",
    "3. Na folha Destinos, escrever uma linha por destino principal, com o id da resposta, a ordem em que aparece,",
    "   o nome tal como está no texto e o município (ou 'macro' se for uma região, serra, parque ou ilha sem município único).",
    "",
    "Destino principal é: cada entrada da lista numerada, cada título de secção, ou cada paragem/base de um dia num roteiro.",
    "Não é destino principal: um monumento, bairro, praia, museu ou restaurante referido dentro de um destino (isso é atração).",
    "Títulos e frases introdutórias ('10 lugares a visitar') não contam.",
    "Em caso de dúvida, registar e explicar na coluna nota.",
]
INSTR_B = [
    "Exercício B: precisão da extração (tema A)",
    "",
    "Objetivo: saber se cada linha extraída está certa, dimensão a dimensão. Está em causa a extração, não a recomendação.",
    "",
    "Como fazer:",
    "1. Guardar uma cópia só sua, com as suas iniciais no nome. Não combinar com a outra pessoa.",
    "2. Para cada linha, procurar o id na folha Respostas e ler o texto.",
    "3. Preencher as três colunas amarelas com s ou n:",
    "   - destino_principal_ok: o lugar é mesmo um destino principal na resposta (não atração, não título)?",
    "   - municipio_ok: o município está certo? Para macro-destinos (serra, região, parque, ilha), 's' se o município indicado for razoável.",
    "   - nuts3_ok: a NUTS III está certa (lista na folha NUTS III)? Para macro-destinos, 's' se for uma das NUTS III abrangidas.",
    "4. Se o lugar não existir ou não for em Portugal, pôr 'n' em municipio_ok e explicar na nota.",
    "Não combinar respostas com a outra pessoa; em caso de dúvida, escolher e explicar na nota.",
]


def folha_instrucoes(wb, titulo, linhas):
    ws = wb.active; ws.title = "Instruções"; ws.column_dimensions["A"].width = 115
    for t in linhas:
        ws.append([t])
    for c in ws["A"]:
        c.alignment = Alignment(wrap_text=True, vertical="top")
    ws["A1"].font = Font(bold=True, size=14)


def folha_respostas(wb, respostas):
    ws = wb.create_sheet("Respostas")
    ws.append(["id", "modelo", "tipo", "língua", "resposta original"])
    for c in ws[1]:
        c.font = Font(bold=True)
    for r in respostas:
        ws.append([r["id"], r["modelo"], r["template"], r["lang"], r["resposta"]])
    for col, w in zip("ABCDE", (26, 10, 16, 8, 120)):
        ws.column_dimensions[col].width = w
    for c in ws["E"]:
        c.alignment = Alignment(wrap_text=True, vertical="top")
    ws.freeze_panes = "A2"


def folha_nuts(wb, nuts):
    ws = wb.create_sheet("NUTS III")
    ws.append(["NUTS III (versão 2024)"]); ws["A1"].font = Font(bold=True)
    for n in nuts:
        ws.append([n])
    ws.column_dimensions["A"].width = 36


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--n-recall", type=int, default=30)
    ap.add_argument("--n-precisao", type=int, default=96, help="número de respostas na amostra de precisão")
    ap.add_argument("--semente", type=int, default=2026)
    a = ap.parse_args()
    rng = random.Random(a.semente)

    resps = [json.loads(l) for l in (AQUI / "data" / "respostas.jsonl").read_text(encoding="utf-8").splitlines()]
    extr = [json.loads(l) for l in (AQUI / "data" / "extracoes_v2.jsonl").read_text(encoding="utf-8").splitlines()]
    with open(AQUI / "data" / "nuts3.csv", encoding="utf-8") as f:
        nuts = [r["nuts3"] for r in csv.DictReader(f)]

    # A: estratificado por modelo × tipo (24 células); distribui n pelas células
    cel = defaultdict(list)
    for r in resps:
        cel[(r["modelo"], r["template"])].append(r)
    chaves = sorted(cel)
    amostra_a = []
    i = 0
    while len(amostra_a) < a.n_recall:
        c = chaves[i % len(chaves)]
        cand = [r for r in cel[c] if r not in amostra_a]
        if cand:
            amostra_a.append(rng.choice(cand))
        i += 1
    wb = Workbook()
    folha_instrucoes(wb, "A", INSTR_A)
    ws = wb.create_sheet("Destinos")
    ws.append(["id", "ordem", "nome no texto", "município (ou 'macro')", "nota"])
    for c in ws[1]:
        c.font = Font(bold=True)
    for r in amostra_a:
        for k in range(12):
            ws.append([r["id"], k + 1, "", "", ""])
    for col, w in zip("ABCDE", (26, 7, 36, 30, 50)):
        ws.column_dimensions[col].width = w
    for linha in ws.iter_rows(min_row=2, min_col=3, max_col=4):
        for c in linha:
            c.fill = FUNDO
    ws.freeze_panes = "A2"
    folha_respostas(wb, amostra_a)
    folha_nuts(wb, nuts)
    wb.save(AQUI / "data" / "verificacao_recall.xlsx")

    # B: amostra de respostas (por resposta, estratificada por modelo × tipo), linhas = destinos principais extraídos
    ids_a = {r["id"] for r in amostra_a}
    amostra_b = []
    i = 0
    while len(amostra_b) < a.n_precisao:
        c = chaves[i % len(chaves)]
        cand = [r for r in cel[c] if r not in amostra_b and r["id"] not in ids_a]
        if cand:
            amostra_b.append(rng.choice(cand))
        i += 1
    ids_b = {r["id"] for r in amostra_b}
    linhas = [e for e in extr if e["id"] in ids_b and e.get("nivel") == "destino" and e.get("nivel_geo") != "titulo"]
    wb = Workbook()
    folha_instrucoes(wb, "B", INSTR_B)
    ws = wb.create_sheet("Verificação")
    ws.append(["id", "posicao", "lugar", "tipo_geo", "municipio", "nuts3", "destino_principal_ok (s/n)",
               "municipio_ok (s/n)", "nuts3_ok (s/n)", "nota"])
    for c in ws[1]:
        c.font = Font(bold=True)
    for e in sorted(linhas, key=lambda e: (e["id"], e.get("posicao", 0))):
        ws.append([e["id"], e.get("posicao"), e.get("lugar"), e.get("nivel_geo"), e.get("municipio"), e.get("nuts3"),
                   "", "", "", ""])
    for col, w in zip("ABCDEFGHIJ", (26, 8, 32, 12, 26, 30, 14, 14, 14, 50)):
        ws.column_dimensions[col].width = w
    for linha in ws.iter_rows(min_row=1, min_col=7, max_col=9):
        for c in linha:
            c.fill = FUNDO
    sn = DataValidation(type="list", formula1='"s,n"', allow_blank=True)
    ws.add_data_validation(sn)
    sn.add(f"G2:I{len(linhas) + 1}")
    ws.freeze_panes = "A2"; ws.auto_filter.ref = ws.dimensions
    folha_respostas(wb, amostra_b)
    folha_nuts(wb, nuts)
    wb.save(AQUI / "data" / "verificacao_precisao.xlsx")
    print(f"verificacao_recall.xlsx: {len(amostra_a)} respostas. verificacao_precisao.xlsx: {len(linhas)} linhas de {len(amostra_b)} respostas.")


if __name__ == "__main__":
    main()
