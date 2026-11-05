# Tema A — Imagem de destino algorítmica

*The algorithmic destination image: how large language models redistribute tourist attention in Portugal*

**Ponto de situação (5 de novembro de 2026):** o piloto (v1, 480 respostas) está analisado e revisto; a proposta de desenho confirmatório (v2) está pronta para discussão. Começar por `RESUMO_PARA_O_GRUPO.md`. A revisão crítica está em `revisao_fable_tema_A.md`; os resultados com as medidas corrigidas em `results_v2/relatorio.md`.

## Estrutura (v1 = piloto, v2 = proposta confirmatória)

| Ficheiro | Conteúdo | Versão |
|---|---|---|
| `RESUMO_PARA_O_GRUPO.md` | Ponto de situação, tese v2, o que está feito, decisões a tomar | v2 |
| `revisao_fable_tema_A.md` | Revisão crítica do piloto, com números recalculados | v2 |
| `docs/pre_registo_v2.md` | Rascunho do pré-registo OSF: hipóteses H1 a H5, desenho, análise, dimensão | v2 |
| `docs/livro_de_codigos.md` | Regras de extração e codificação geográfica; verificação humana | v2 |
| `docs/enquadramento_teorico.md` | Teoria em três camadas, hipótese rival, literatura a verificar | v2 |
| `docs/revistas.md` | Revistas sem taxa, por ordem de encaixe | v2 |
| `docs/plano_trabalho.md` | 4 semanas, tarefas por pessoa | v2 |
| `prompts.csv`, `config.json`, `collect.py` | Recolha do piloto (8 tipos × 4 línguas × 3 modelos × 5 repetições) | v1 |
| `prompts_v2.csv`, `config_v2.json`, `collect_v2.py` | Recolha confirmatória: 3 paráfrases, roteiros de 3/7/14 dias, modelos abertos, condição com pesquisa web | v2 |
| `extract.py` | Extração de lugares com Claude Haiku 5.5 → `data/extracoes.jsonl` | v1 (a adaptar: pedir só município) |
| `reprocess.py` | Títulos, macro-destinos e NUTS III derivada do município → `data/extracoes_v2.jsonl` | v2 |
| `fetch_eurostat.py` | Dormidas por NUTS III por residência e âmbito NACE → `data/dormidas_2025_nuts3.csv` | v2 |
| `fetch_wikipedia.py` | Termo de comparação textual (visualizações da Wikipédia por município) | v2 (correr localmente) |
| `analyze.py` → `results/` | Análise do piloto (presença, Gini, rácios) | v1 |
| `analyze_v2.py` → `results_v2/` | Exposição ponderada, noites nos roteiros, declive log-log, número efetivo de regiões, JSD, bootstrap por agrupamento, homogeneização, sensibilidades | v2 |
| `simulacao_dimensao.py` | Largura dos intervalos por número de células e repetições | v2 |
| `ficheiro_verificacao.py` | Verificação v1 (só precisão) | v1 |
| `verificacao_v2.py`, `metricas_verificacao.py` | Verificação em dois exercícios (recall às cegas e precisão por dimensão) e métricas | v2 |
| `resumo_sensibilidade.py` | Tabela que compara as variantes de análise | v2 |
| `data/nuts3.csv` | 26 NUTS III (2024) com dormidas totais 2025 | v1 |
| `data/municipios_nuts3_2024.csv` | 308 municípios → NUTS III (verificar contra a CAOP) | v2 |
| `data/macro_destinos.csv` | 37 marcas territoriais → NUTS III principal e abrangidas | v2 |
| `data/teste-2026-10/` | Dados do teste de outubro | v1 |

## Como correr a cadeia v2 sobre o piloto

```
python fetch_eurostat.py            # dormidas por residência (já feito; refazer se o Eurostat atualizar)
python reprocess.py                 # extrações do piloto → extracoes_v2.jsonl
python analyze_v2.py                # análise principal (cerca de 6 min com 2000 reamostragens)
python analyze_v2.py --alocacao fracionaria --bootstrap 300 --saida results_v2/sens_fracionaria
python analyze_v2.py --alocacao excluir --bootstrap 300 --saida results_v2/sens_excluir
python analyze_v2.py --sem-ilhas --bootstrap 300 --saida results_v2/sens_sem_ilhas
python resumo_sensibilidade.py      # tabela comparativa
python simulacao_dimensao.py        # precisão esperada por desenho
python verificacao_v2.py            # ficheiros para os codificadores
python metricas_verificacao.py --recall <xlsx NA> <xlsx AMS> --precisao <xlsx NA> <xlsx AMS>
```

## Como correr a recolha confirmatória (depois do pré-registo)

1. Preencher em `config_v2.json` os identificadores dos modelos abertos e confirmar a sintaxe do plugin web no OpenRouter.
2. `python collect_v2.py --ensaio` para testar o circuito; `python collect_v2.py --condicao confirmatorio --limite 5` para um teste real.
3. Na janela de recolha (48 h): `--condicao confirmatorio` (660), `--condicao exploratorio` (300), `--condicao pesquisa_web` (72).
4. Extração (adaptar `extract.py` para ler `data/v2/respostas_*.jsonl` e pedir só o município), `reprocess.py`, `analyze_v2.py` com os ficheiros v2.

## Como correr o piloto (v1)

1. Criar o ficheiro `.env` nesta pasta com a linha `OPENROUTER_API_KEY=...` (uma só chave dá acesso aos três modelos).
   Nunca partilhar este ficheiro. Modelos escolhidos no mesmo escalão de preço (2 $/10 $ por milhão de tokens):
   `anthropic/claude-sonnet-5.5`, `openai/gpt-6.1-sol`, `google/gemini-4-argon`. Extração com `anthropic/claude-haiku-5.5` (sem raciocínio), para reduzir custos: em 5 respostas coincidiu com o Sonnet em 50 de 52 presenças; as divergências foram lugares que abrangem vários municípios.
2. Teste do circuito sem custos: `python collect.py --ensaio`, `python extract.py --ensaio`, `python analyze.py`
   (apagar depois `data/respostas.jsonl`, `data/extracoes.jsonl` e `results/`).
3. Teste curto real: `python collect.py --modelo claude --limite 5`.
4. Recolha completa: `python collect.py` (480 chamadas; retoma onde parou se for interrompida).
5. `python extract.py`, depois os dois codificadores preenchem `data/verificacao_humana.csv` (s/n) às cegas, um sem ver o outro.
6. `python analyze.py`. Meta: kappa ≥ 0,80. Com acordo quase total o kappa pode sair baixo (paradoxo do kappa): reportar também o acordo simples.

## Notas metodológicas

- Chamadas por API, sem memória nem pesquisa web: mede o conhecimento "de base" do modelo. A pesquisa web fica como variável no estudo completo.
- Dois níveis na extração: `destino` (cada item principal da lista, título ou paragem do roteiro) e `atracao` (lugar dentro de um destino, com `destino_pai`).
  Ambas em `results/` (coluna `medida`):
  - `destinos` (principal): presença de uma NUTS III por resposta, só com destinos principais (conta no máximo uma vez por resposta);
  - `mencoes` (secundária): todas as menções, destinos e atrações, cada uma conta. Mede a "profundidade" de atenção dada a cada região.
- Dados do teste de outubro arquivados em `data/teste-2026-10/`: a recolha final corre toda na mesma janela temporal.
- Teste com 5 respostas (Claude, pergunta geral em PT): Gini 0,59 em destinos e 0,72 em menções. Grande Lisboa tem 25% das menções.
- Rácio de enviesamento = quota da NUTS III nas recomendações ÷ quota nas dormidas. > 1 = sobre-representada.
- Lugares inexistentes ou fora de Portugal são excluídos da análise e contam para a taxa de erro (RQ4).
- Registar a data e a versão de cada modelo (já gravadas em `respostas.jsonl`): os modelos mudam e o estudo tem de ser replicável.

## Registo de uso de IA (para a declaração na submissão)

| Data | Tarefa | Ferramenta | Validado por |
|---|---|---|---|
| 2026-10-16 | Rascunho do protocolo, perguntas e scripts | Claude (Anthropic) | Nuno Abranja e António Morais Santos (perguntas) |
| 2026-11-01 | Alterações às perguntas Família e Inverno, por proposta do António | Claude (Anthropic) | por validar |
| 2026-11-01 | Recolha, extração e análise preliminar | Claude (Anthropic) | por validar |
| 2026-11-03 | Rascunho do pré-registo da recolha confirmatória (separador no documento partilhado) | Claude (Anthropic) | por validar |
| 2026-11-05 | Revisão crítica do piloto; reprocessamento determinístico; análise v2; tabelas de municípios e macro-destinos; verificação v2; prompts v2; pré-registo v2; enquadramento; plano | Claude (Anthropic) | por validar (AP, NA, AMS) |
