# Tema A — Imagem de destino algorítmica (piloto)

*The algorithmic destination image: how large language models redistribute tourist attention in Portugal*

Protocolo completo e decisões em aberto: documento partilhado "Agenda de Investigação ISCE 2026/27".

## Pergunta do piloto

Que regiões ficam sobre e sub-representadas nas recomendações de ChatGPT, Claude e Gemini face às
dormidas por NUTS III, e a concentração muda com o tipo de pedido?

A hipótese inicial (recomendações mais concentradas do que a procura) não se confirmou no agregado.
A tese de redistribuição surgiu depois de ver os dados: estas 480 respostas são exploratórias, e o teste
confirmatório exige uma nova recolha com hipóteses pré-registadas.

## Ficheiros

| Ficheiro | Conteúdo | Quem decide / preenche |
|---|---|---|
| `prompts.csv` | 8 tipos de pergunta × 5 línguas; só correm as de `linguas` em `config.json` (PT, EN, ES, FR; DE quando as traduções forem verificadas) | Equipa valida as traduções |
| `config.json` | Modelos, línguas, repetições (5), amostra de verificação (20%) | Equipa |
| `data/nuts3.csv` | 26 NUTS III (versão 2024) + coluna `dormidas` | Dormidas de 2025 do Eurostat (`tour_occ_nin3`, total, todos os alojamentos; cópia em `data/eurostat_tour_occ_nin3_2026-10-20.json`). O site do INE não respondeu em 2026-11-01 |
| `collect.py` | Recolha das respostas → `data/respostas.jsonl` | Script |
| `extract.py` | Extração de lugares, município e NUTS III → `data/extracoes.jsonl` + amostra `data/verificacao_humana.csv` | Script + 2 codificadores humanos |
| `ficheiro_verificacao.py` | Gera `data/verificacao_destinos.xlsx`: só os destinos principais da amostra (964 linhas), com instruções, para cada codificador preencher | Script |
| `analyze.py` | Quotas, Gini, HHI, top-3, rácio de enviesamento, kappa → `results/` | Script; interpretação pela equipa |

## Como correr

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
