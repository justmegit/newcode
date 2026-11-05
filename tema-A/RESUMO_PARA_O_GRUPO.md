# Tema A: ponto de situação e proposta v2 (para Nuno e António)

5 de novembro de 2026. Tudo o que está aqui referido está no ramo `papers-fable`, pasta `tema-A/`. Leitura sugerida por ordem: este resumo, `results_v2/relatorio.md`, `docs/pre_registo_v2.md`, `docs/plano_trabalho.md`. A revisão crítica completa que originou isto está em `revisao_fable_tema_A.md`.

## 1. Em duas frases

O piloto está bem feito mas as três medidas que sustentavam a tese (presença por resposta, Gini contra Gini, dormidas totais) estavam a esconder o resultado real. Com as medidas corrigidas, a história é mais forte e mais simples: os LLMs trocam o produto que domina a procura (sol e mar) pelo cânone cultural e patrimonial, concentram o planeamento num corredor Lisboa-Porto, e fazem-no todos da mesma maneira.

## 2. O que estava mal e porquê (verificado nos dados)

| Problema | O que acontecia | Consequência |
|---|---|---|
| Presença por resposta tem teto | Cada resposta nomeia 9,4 NUTS III; nenhuma região pode ter mais de 10,6% da atenção | Lisboa, Porto, Madeira, Coimbra, Évora e Douro estavam em 100% das respostas e tinham a mesma quota; os rácios 0,47 (Lisboa) e 13 (Douro) eram a mesma presença dividida por dormidas diferentes. H1 estava decidida pela medida |
| Gini contra Gini | O Gini das recomendações mede cobertura e consenso, não semelhança com a procura | O 0,63 "parecido com 0,66" não dizia nada; o 0,76 do roteiro comparado com 0,66 falha quando se usa o termo certo |
| Dormidas totais | Quem pergunta em EN/ES/FR é estrangeiro; as dormidas de não residentes têm Gini 0,763, não 0,663 | H2 cai com o termo de comparação certo |
| Macro-destinos | Metade dos destinos são marcas territoriais ("Vale do Douro", "Gerês", "Alentejo"); o extrator mapeou o mesmo nome para NUTS III diferentes e pôs Costa Vicentina e Odemira em Baixo Alentejo | Rácios de regiões pequenas dependiam de decisões não declaradas |
| Validação humana | O ficheiro só permitia confirmar linhas extraídas | Media precisão, não recall |
| Inferência | 12 células independentes, 1 formulação por pergunta, bootstrap sobre repetições | Intervalos estreitos demais; a confirmação com os mesmos prompts estava garantida |
| Eurostat vs INE | 89,4 contra 82,1 milhões | Resolvido: são os 6,96 milhões de dormidas em campismo (NACE I55.3); sem campismo, 82,47 milhões |

## 3. O que os dados dizem com as medidas corrigidas (`results_v2/relatorio.md`)

Medida: exposição ponderada pela posição na lista (sem teto). Termo: dormidas 2025 de não residentes para EN/ES/FR e de residentes para PT. Intervalos a 95% por bootstrap por agrupamento modelo × língua.

**Pergunta geral (n = 60).** Declive log-log 0,71 [0,58; 0,81]: a atenção cresce com a procura, mas menos do que proporcionalmente. Rácios: Algarve 0,29 [0,27; 0,33]; Madeira 0,56; Grande Lisboa 0,84 [0,70; 1,04]; AM Porto 1,05; Coimbra 3,8; Alentejo Central 6,4; Douro 12,7. Lisboa deixa de estar "sub-representada"; o Algarve e a Madeira continuam. Doze regiões nunca aparecem como destino principal.

**Roteiro de 7 dias (n = 59 com dias legíveis).** Noites atribuídas: AM Porto 46%, Grande Lisboa 42%, Douro 6%, Algarve e Madeira 0%. Lisboa + Porto: 87,7% das noites contra 35,4% das dormidas de não residentes. Número efetivo de regiões 3,1 [2,6; 3,5] contra 7,7 nas dormidas. Gini 0,90.

**"Pouco conhecidos" (n = 60).** Declive menos 0,16 [menos 0,22; menos 0,09]: a atenção vai contra a procura, como pedido. Mas os três modelos concordam: Terras de Trás-os-Montes, Beira Baixa, Beiras e Serra da Estrela, Baixo Alentejo e Douro aparecem em 65 a 88% das respostas. As joias escondidas são canónicas.

**Homogeneização.** Correlação entre os vetores de exposição dos modelos: 0,96 a 0,98 na pergunta geral, 0,93 a 0,98 no roteiro, 0,51 a 0,84 em "pouco conhecidos". Entre línguas: 0,98 a 0,99 na pergunta geral.

**Extração.** NUTS III do extrator errada em 2,0% dos itens com município (Arouca, Odemira, Aljezur, Mealhada, Freixo); 14 títulos extraídos como lugares; 4 municípios não reconhecidos em 15 665 itens. Tudo corrigido de forma determinística em `reprocess.py`. Alucinações: 20 itens, vários errados; não é um resultado.

## 4. A tese proposta

"Os LLMs não reproduzem o mapa da procura turística; reproduzem o mapa do cânone cultural e patrimonial. Quando listam destinos, substituem o sol e mar pelo património do interior e do litoral histórico. Quando planeiam, as restrições de rota empurram-nos para um corredor urbano Lisboa-Porto, mais concentrado do que a própria procura. Modelos e línguas convergem no mesmo mapa. Para destinos com pouca capacidade, a visibilidade algorítmica chega antes da infraestrutura."

Teoria em três camadas (`docs/enquadramento_teorico.md`): o LLM como agente de imagem com credibilidade de agente autónomo e alcance de agente induzido (Gartner); imagem discursiva contra comportamento, que prevê a direção do desvio e se testa com um termo textual (Wikipédia); restrições espaciais do planeamento, que explicam o corredor. Hipótese rival explícita: enviesamento de popularidade. Resultado transversal: homogeneização (monocultura algorítmica).

## 5. O que já está feito no ramo

| Ficheiro | O que é |
|---|---|
| `fetch_eurostat.py` → `data/dormidas_2025_nuts3.csv`, `data/dormidas_2025_nace_pt.csv` | Dormidas 2025 por NUTS III, total, não residentes e residentes; âmbito NACE nacional |
| `data/municipios_nuts3_2024.csv` | 308 municípios → NUTS III 2024 (feito de memória; verificar contra a CAOP) |
| `data/macro_destinos.csv` | 37 marcas territoriais com NUTS III principal e abrangidas |
| `reprocess.py` → `data/extracoes_v2.jsonl` | Reprocessamento determinístico das extrações do piloto |
| `analyze_v2.py` → `results_v2/` | Medidas novas, termo por língua, bootstrap por agrupamento, relatório, homogeneização, noites nos roteiros, sensibilidades |
| `simulacao_dimensao.py` → `results_v2/simulacao_dimensao.csv` | Largura dos intervalos por número de células e repetições |
| `verificacao_v2.py` → `data/verificacao_recall.xlsx`, `data/verificacao_precisao.xlsx`; `metricas_verificacao.py` | Verificação humana em dois exercícios e métricas |
| `prompts_v2.csv`, `config_v2.json`, `collect_v2.py` | Recolha confirmatória: 3 paráfrases, roteiros de 3/7/14 dias, modelos abertos, condição com pesquisa web |
| `fetch_wikipedia.py` | Termo de comparação textual (correr localmente; a API limita a cadência) |
| `docs/livro_de_codigos.md` | Regras de extração, macro-destinos, noites, exclusões, verificação |
| `docs/pre_registo_v2.md` | Hipóteses H1 a H5 com limiares, desenho, plano de análise, dimensão |
| `docs/enquadramento_teorico.md` | Três camadas, hipótese rival, literatura a verificar, termos de pesquisa |
| `docs/revistas.md` | Revistas sem taxa, por ordem, com riscos |
| `docs/plano_trabalho.md` | 4 semanas, tarefas por pessoa, decisões para reunião |

## 6. O que precisamos de decidir (reunião)

1. Aceitar a tese v2 e as hipóteses H1 a H5 (com os limiares propostos) ou ajustar.
2. Macro-destinos: NUTS III principal como análise principal, com fracionária e exclusão como sensibilidade.
3. Modelos abertos: quais e quantos (custo marginal baixo).
4. Condição com pesquisa web: 72 chamadas, só pergunta geral e roteiro.
5. Revista: Tourism Geographies ou Information Technology & Tourism.
6. Divisão da escrita (proposta em `docs/plano_trabalho.md`).

## 7. O que vos pedimos esta semana

- Nuno e António: os dois exercícios de verificação (`data/verificacao_recall.xlsx`, 30 respostas; `data/verificacao_precisao.xlsx`, cerca de 1 000 linhas), cada um na sua cópia, sem consulta. São 3 a 4 horas cada.
- Nuno e António: ler o livro de códigos e marcar o que discordam, sobretudo Peneda-Gerês (Cávado) e Alentejo (Alentejo Central).
- António: rever as traduções ES e FR de `prompts_v2.csv`; Nuno: EN.
- Alexandre: verificar a tabela de municípios, confirmar os identificadores dos modelos abertos e do plugin web, correr a Wikipédia localmente, submeter o pré-registo depois da reunião.

## 8. Avisos de honestidade

- A tabela de municípios e as referências bibliográficas foram feitas de memória e estão marcadas para verificação.
- A medida de noites nos roteiros é lida por expressões regulares dos cabeçalhos de dia; funciona em 59 dos 60 roteiros do piloto, mas as variantes 2 e 3 da v2 pedem explicitamente onde dormir para reduzir ambiguidade.
- As larguras de intervalo da simulação são um limite inferior: o piloto não tem variação por paráfrase.
- O pré-registo com os mesmos modelos é um teste de estabilidade e robustez, não de generalização; é assim que deve ser apresentado.
