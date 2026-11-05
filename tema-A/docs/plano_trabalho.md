# Plano de trabalho: do piloto à recolha confirmatória (tema A)

Horizonte: 4 semanas a partir de 5 de novembro de 2026. Pessoas: Alexandre (AP), Nuno (NA), António (AMS). O que está marcado "feito" já está no ramo `papers-fable`.

## Semana 1 (6 a 12 de novembro): fechar a medida

| # | Tarefa | Quem | Entrega | Estado |
|---|---|---|---|---|
| 1.1 | Rever e aprovar o livro de códigos v2 (`docs/livro_de_codigos.md`), em especial a tabela de macro-destinos | NA, AMS | Comentários no ficheiro; decisão sobre Peneda-Gerês e Alentejo | por fazer |
| 1.2 | Verificar a tabela município → NUTS III 2024 contra a CAOP ou o INE (308 linhas) | AP | `data/municipios_nuts3_2024.csv` validada | por fazer (feita de memória; dois homónimos: Lagoa, Calheta) |
| 1.3 | Exercício A de verificação (recall): 30 respostas às cegas | NA, AMS (em separado) | `verificacao_recall_NA.xlsx`, `verificacao_recall_AMS.xlsx` | ficheiro gerado |
| 1.4 | Exercício B de verificação (precisão): cerca de 1 000 linhas, três juízos por linha | NA, AMS (em separado) | `verificacao_precisao_NA.xlsx`, `verificacao_precisao_AMS.xlsx` | ficheiro gerado |
| 1.5 | Calcular métricas de verificação e corrigir o livro de códigos onde falhar | AP | saída de `metricas_verificacao.py` no README | depende de 1.3 e 1.4 |
| 1.6 | Confirmar identificadores no OpenRouter dos dois modelos abertos (Llama, DeepSeek ou Qwen/Mistral) e a sintaxe do plugin de pesquisa web | AP | `config_v2.json` sem "CONFIRMAR" | por fazer |
| 1.7 | Rever as paráfrases e traduções de `prompts_v2.csv` (3 variantes × 4 línguas; roteiro 3/7/14 dias) | AMS (ES, FR), NA (EN) | ficheiro aprovado | por fazer |

## Semana 2 (13 a 19 de novembro): pré-registo

| # | Tarefa | Quem | Entrega | Estado |
|---|---|---|---|---|
| 2.1 | Discutir o relatório v2 (`results_v2/relatorio.md`) e decidir a tese: substituição de produto + corredor urbano + homogeneização | todos | ata curta no README | por fazer |
| 2.2 | Fechar as hipóteses H1 a H4 e os limiares (`docs/pre_registo_v2.md`) | todos | texto final | rascunho feito |
| 2.3 | Descarregar o termo textual (Wikipédia 2025, PT e EN) localmente; corrigir títulos em falta | AP | `data/wikipedia_2025_nuts3.csv` | script feito; correr fora da nuvem (limite de cadência) |
| 2.4 | Submeter o pré-registo no OSF (template "Preregistration", com o piloto declarado) e guardar o DOI | AP | DOI no README | por fazer |
| 2.5 | Criar o repositório público (GitHub) com código, livro de códigos e dados do piloto; ligar ao OSF | AP | ligação no README | por fazer |

## Semana 3 (20 a 26 de novembro): ensaio da recolha

| # | Tarefa | Quem | Entrega | Estado |
|---|---|---|---|---|
| 3.1 | Ensaio de 5 chamadas por modelo com `collect_v2.py` (inclui os abertos e a condição web) e extração | AP | log sem erros | por fazer |
| 3.2 | Verificar que os roteiros das variantes 2 e 3 dizem onde dormir cada noite e que a medida de noites os lê (≥ 95% das respostas com dias legíveis) | AP | nota no README | por fazer |
| 3.3 | Estimar custo real por resposta e confirmar orçamento (previsão: 40 a 60 USD para cerca de 1 030 respostas) | AP | número no README | por fazer |

## Semana 4 (a partir de 3 de dezembro, ≥ 4 semanas depois do piloto): recolha confirmatória

| # | Tarefa | Quem | Entrega | Estado |
|---|---|---|---|---|
| 4.1 | Recolha completa em janela de 48 horas: confirmatório (660), exploratório (300), pesquisa web (72) | AP | `data/v2/respostas_*.jsonl` | por fazer |
| 4.2 | Extração (`extract.py` adaptado a v2) + `reprocess.py` | AP | `data/v2/extracoes_v2.jsonl` | por fazer |
| 4.3 | Verificação humana da recolha v2 (mesmos dois exercícios, 20%) | NA, AMS | ficheiros preenchidos | por fazer |
| 4.4 | Análise pré-registada (`analyze_v2.py` com os ficheiros v2) e sensibilidades | AP | `results_v2/` da recolha v2 | por fazer |

## Dezembro e janeiro: escrita

| # | Tarefa | Quem |
|---|---|---|
| 5.1 | Introdução e enquadramento (camadas 1 a 3 de `docs/enquadramento_teorico.md`), revisão sistemática da literatura com os termos listados | NA |
| 5.2 | Método (protocolo, livro de códigos, verificação, medidas, pré-registo) e resultados | AP |
| 5.3 | Discussão e implicações (política de desconcentração, capacidade, Évora 2027, homogeneização) | AMS |
| 5.4 | Escolha da revista (`docs/revistas.md`) e formatação | todos |
| 5.5 | Declaração de uso de IA (registo no README) e disponibilização de dados e código | AP |

## Decisões que precisam de reunião

1. Macro-destinos: aceitar a NUTS III principal como análise principal e as outras duas como sensibilidade, ou excluir macro-destinos da análise principal?
2. Hipótese H3 ("pouco conhecidos"): manter a versão com intensidade turística, ou substituir pela sobreposição entre modelos (as joias escondidas são as mesmas para todos)?
3. Modelos abertos: dois ou um? Qual?
4. Condição com pesquisa web: só pergunta geral e roteiro de 7 dias (72 chamadas), ou também "pouco conhecidos"?
5. Revista alvo: Tourism Geographies ou Information Technology & Tourism.
