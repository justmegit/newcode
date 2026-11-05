"""Gera data/verificacao_destinos.xlsx: só os destinos principais da amostra, para cada codificador preencher."""
import csv
from pathlib import Path

from openpyxl import Workbook
from openpyxl.styles import Alignment, Font, PatternFill
from openpyxl.worksheet.datavalidation import DataValidation

AQUI = Path(__file__).parent
FUNDO = PatternFill("solid", fgColor="FFF2CC")

INSTRUCOES = [
    "Verificação dos destinos principais (tema A)",
    "",
    "O que é: um modelo de IA leu 96 respostas de ChatGPT, Claude e Gemini e extraiu os destinos recomendados em cada uma. "
    "Esta verificação confirma se essa extração está certa. Está em causa a extração, não a qualidade da recomendação.",
    "",
    "Como fazer:",
    "1. Guardar uma cópia só sua, com as suas iniciais no nome do ficheiro. Duas pessoas verificam em separado, sem ver as respostas uma da outra.",
    "2. Na folha Verificação, procurar o id da linha na folha Respostas e ler o texto original.",
    "3. Preencher as colunas amarelas: s se a linha estiver toda certa, n se algo estiver errado. Em n, explicar na coluna nota.",
    "",
    "A linha está certa (s) se:",
    "- o lugar é recomendado na resposta como item principal (entrada da lista, título ou paragem do roteiro);",
    "- o município está certo (num lugar que abrange vários municípios, como uma serra ou um rio, aceita-se o principal);",
    "- a NUTS III está certa (lista na folha NUTS III);",
    "- o lugar existe e fica em Portugal. A coluna existe é a resposta do modelo, que pode falhar, por isso confirmar sempre.",
    "",
    "Se faltar um destino recomendado na resposta, registar na coluna nota da linha anterior.",
    "Em caso de dúvida, escolher a opção que parecer melhor e explicar na nota. Não combinar respostas com a outra pessoa.",
]


def main():
    with open(AQUI / "data" / "verificacao_humana.csv", encoding="utf-8-sig", newline="") as f:
        linhas = list(csv.DictReader(f, delimiter=";"))
    with open(AQUI / "data" / "nuts3.csv", encoding="utf-8") as f:
        nuts = [r["nuts3"] for r in csv.DictReader(f)]
    respostas = {r["id"]: r["resposta_original"] for r in linhas if r["resposta_original"]}
    destinos = [r for r in linhas if r["nivel"] == "destino"]

    wb = Workbook()
    ws = wb.active
    ws.title = "Instruções"
    ws.column_dimensions["A"].width = 110
    for t in INSTRUCOES:
        ws.append([t])
    for c in ws["A"]:
        c.alignment = Alignment(wrap_text=True, vertical="top")
    ws["A1"].font = Font(bold=True, size=14)

    ws = wb.create_sheet("Verificação")
    colunas = ["id", "posicao", "lugar", "municipio", "nuts3", "existe"]
    ws.append(colunas + ["correto (s/n)", "nota"])
    for r in destinos:
        ws.append([r[c] for c in colunas] + ["", ""])
    for c, largura in zip("ABCDEFGH", (24, 8, 32, 26, 32, 8, 13, 50)):
        ws.column_dimensions[c].width = largura
    for c in ws[1]:
        c.font = Font(bold=True)
    for linha in ws.iter_rows(min_row=1, min_col=7, max_col=8):
        for c in linha:
            c.fill = FUNDO
    sn = DataValidation(type="list", formula1='"s,n"', allow_blank=True)
    ws.add_data_validation(sn)
    sn.add(f"G2:G{len(destinos) + 1}")
    ws.freeze_panes = "A2"
    ws.auto_filter.ref = ws.dimensions

    ws = wb.create_sheet("Respostas")
    ws.append(["id", "resposta original"])
    ws["A1"].font = ws["B1"].font = Font(bold=True)
    for i, t in sorted(respostas.items()):
        ws.append([i, t])
    ws.column_dimensions["A"].width = 24
    ws.column_dimensions["B"].width = 120
    for c in ws["B"]:
        c.alignment = Alignment(wrap_text=True, vertical="top")
    ws.freeze_panes = "A2"

    ws = wb.create_sheet("NUTS III")
    ws.append(["NUTS III (versão 2024)"])
    ws["A1"].font = Font(bold=True)
    for n in nuts:
        ws.append([n])
    ws.column_dimensions["A"].width = 36

    saida = AQUI / "data" / "verificacao_destinos.xlsx"
    wb.save(saida)
    print(f"{saida.name}: {len(destinos)} linhas, {len(respostas)} respostas, "
          f"maior resposta {max(map(len, respostas.values()))} caracteres, {saida.stat().st_size} bytes")


if __name__ == "__main__":
    main()
