# Pré-registo (rascunho v2): The algorithmic destination image

Para submeter no OSF (template "OSF Preregistration") antes de iniciar a recolha confirmatória. Texto em português para discussão interna; a versão submetida será em inglês. Campos entre colchetes a preencher.

## 1. Título e autores

The algorithmic destination image: how large language models redistribute tourist attention within a country. Autores: [Alexandre Pessoa, Nuno Abranja, António Morais Santos], ISCE.

## 2. Dados já recolhidos

Sim. Um estudo exploratório (Estudo 1) com 480 respostas foi recolhido em 1 de novembro de 2026 (3 modelos, 8 tipos de pergunta, 4 línguas, 5 repetições). As hipóteses abaixo foram formuladas depois de analisar esses dados. O Estudo 1 será reportado como exploratório. Nenhum dado do Estudo 2 (confirmatório) foi recolhido à data do registo. O código, o livro de códigos e os dados do Estudo 1 estão em [repositório].

## 3. Questão de investigação

Como se distribui, entre as 26 regiões NUTS III de Portugal, a atenção que modelos de linguagem de grande dimensão dão aos destinos quando (a) listam lugares a visitar, (b) planeiam um roteiro e (c) recomendam lugares pouco conhecidos, e como se compara essa distribuição com a procura turística real (dormidas) por região?

## 4. Hipóteses

Termo de comparação: dormidas de 2025 por NUTS III (Eurostat, `tour_occ_nin3`, NACE I55.1 a I55.3), de não residentes para prompts em inglês, espanhol e francês e de residentes para prompts em português. Medida principal: exposição ponderada pela posição (peso 1/log2(ordem + 1) na primeira ocorrência de cada NUTS III entre os destinos principais de cada resposta; vetor normalizado por resposta; média entre respostas). Macro-destinos atribuídos à NUTS III principal (análise principal).

**H1 (substituição de produto, pergunta geral).** Na pergunta geral, (a) o declive da regressão de log(quota LLM) sobre log(quota de dormidas), com pseudo-contagem de 0,5, é inferior a 1; (b) o rácio quota LLM / quota de dormidas do Algarve é inferior a 0,5; (c) o rácio de pelo menos duas das três regiões do cânone patrimonial do interior e litoral histórico (Alentejo Central, Região de Coimbra, Douro) é superior a 2. No Estudo 1: declive 0,71 [0,58; 0,81]; Algarve 0,29 [0,27; 0,33]; Alentejo Central 6,4, Coimbra 3,8, Douro 12,7.

**H2 (concentração no planeamento, roteiro de 7 dias).** No roteiro de 7 dias, (a) a soma das quotas de noites atribuídas a Grande Lisboa e Área Metropolitana do Porto é superior a 60%; (b) o número efetivo de regiões das noites atribuídas é inferior ao das dormidas de não residentes (7,7). No Estudo 1: 87,7% [IC não calculado para a soma; componentes 41,7 e 46,0] e 3,1 [2,6; 3,5].

**H2b (dose-resposta, exploratória mas pré-especificada).** O número efetivo de regiões das noites atribuídas aumenta monotonicamente com a duração do roteiro (3 < 7 < 14 dias). Sem dados prévios.

**H3 (joias escondidas canónicas, "pouco conhecidos").** Em "pouco conhecidos", (a) o declive log-log é inferior a 0 (a atenção vai contra a procura); (b) a correlação de Pearson entre os vetores de exposição dos modelos, tomados dois a dois, é superior a 0,5 (os modelos concordam nas joias escondidas). No Estudo 1: declive menos 0,16 [menos 0,22; menos 0,09]; correlações 0,51 a 0,84.

**H4 (homogeneização).** Na pergunta geral e no roteiro, a correlação de Pearson entre os vetores de exposição de cada par de modelos é superior a 0,9, e o Jaccard entre os conjuntos de regiões presentes em pelo menos 50% das respostas de cada modelo é superior a 0,7. No Estudo 1: correlações 0,96 a 0,98 (geral) e 0,93 a 0,98 (roteiro); Jaccard 0,80 a 0,90 (geral) e 0,38 a 0,60 (roteiro). Nota: no roteiro o Jaccard do Estudo 1 fica abaixo do limiar; o limiar aplica-se à correlação; o Jaccard é reportado.

**Teste de mecanismo (H5, imagem discursiva contra comportamento).** Na pergunta geral, a divergência de Jensen-Shannon entre a exposição LLM e a quota de visualizações da Wikipédia por NUTS III (2025, PT e EN) é inferior à divergência entre a exposição LLM e a quota de dormidas. Sem dados prévios sobre a Wikipédia; o Estudo 1 dá JSD contra dormidas de 0,183 [0,178; 0,200].

Hipótese rival explicitada: enviesamento de popularidade (os LLMs sobre-expõem as regiões com mais dormidas) prevê declive superior a 1 e rácios superiores a 1 em Algarve e Grande Lisboa. H1 opõe-se a esta previsão.

## 5. Desenho

- **Modelos:** Claude Sonnet 5.5, GPT-6.1, Gemini 4 (os do Estudo 1, versões registadas) mais [um ou dois modelos abertos: identificadores exatos no OpenRouter a registar]. Chamadas por API via OpenRouter, sem prompt de sistema, sem memória, sem pesquisa web, temperatura por omissão de cada fornecedor (registada).
- **Prompts** (`prompts_v2.csv`): três tipos com hipóteses (geral, roteiro, pouco conhecidos), cada um com 3 paráfrases, em 4 línguas; roteiro com durações de 3, 7 e 14 dias na paráfrase 1 e de 7 dias nas paráfrases 2 e 3. Cinco tipos exploratórios (natureza, cultura, família, vinho, inverno), 1 paráfrase. 3 repetições por célula. Total confirmatório: 44 prompts × [5] modelos × 3 = 660 respostas; exploratório 300; condição com pesquisa web (geral e roteiro de 7 dias, 3 modelos fechados, plugin web): 72.
- **Janela:** todas as chamadas em 48 horas, pelo menos 4 semanas depois do Estudo 1 (a partir de 3 de dezembro de 2026). Data, modelo e fornecedor devolvidos, finish_reason e tokens registados por resposta.
- **Extração:** Claude Haiku 5.5 identifica lugares, nível (destino, atração) e município; a NUTS III é derivada de forma determinística da tabela de municípios (NUTS 2024); macro-destinos e títulos tratados por regras fixas (`docs/livro_de_codigos.md`, `data/macro_destinos.csv`, `reprocess.py`, hash do commit [a registar]).
- **Verificação humana:** dois codificadores, cópias separadas; exercício A (recall, 30 respostas às cegas) e exercício B (precisão, 20% das respostas, três juízos por linha). Metas: recall ≥ 0,95; exatidão de NUTS III ≥ 0,95; acordo ≥ 0,90. Se as metas falharem, o livro de códigos é corrigido e a extração repetida antes de qualquer teste de hipóteses; a correção é documentada.

## 6. Plano de análise

- Medidas por resposta: exposição ponderada pela posição (principal); presença; todas as menções; noites atribuídas (roteiros). Cada resposta é um vetor normalizado; as quotas de grupo são médias de vetores.
- Estatísticas: declive log-log com pseudo-contagem 0,5; número efetivo de regiões (exponencial da entropia); divergência de Jensen-Shannon; rácios suavizados com a mesma pseudo-contagem e diferença em pontos percentuais; Jaccard médio entre respostas; correlação de Pearson entre vetores de modelos.
- Incerteza: bootstrap por agrupamento, 5 000 reamostragens, células modelo × língua × paráfrase reamostradas com reposição e, dentro de cada célula, respostas com reposição; intervalos percentílicos. Cada hipótese é uma família; dentro de cada família, as componentes são testadas em conjunto (teste de interseção-união: a hipótese confirma-se se todas as componentes ficarem do lado previsto do limiar). Entre as cinco famílias, correção de Holm com alfa de 0,05 (intervalos a 99% para a componente mais exigente).
- Regras de exclusão: respostas vazias, cortadas ou recusadas; respostas com mais de metade dos destinos fora de Portugal; itens título; itens inexistentes confirmados. Todas contadas e reportadas.
- Sensibilidades pré-especificadas: macro-destinos por alocação fracionária e por exclusão; sem Açores e Madeira; termo de comparação total em vez de por língua; presença em vez de exposição ponderada. Reportadas numa tabela; não alteram a decisão sobre as hipóteses.
- Tudo o que não está acima é exploratório e será identificado como tal.

## 7. Dimensão e precisão

Justificação por precisão, não por poder (as hipóteses não são testes de nulidade). Simulação a partir do Estudo 1 (`simulacao_dimensao.py`): com 36 células e 2 a 3 respostas por célula, a largura do intervalo a 95% da divergência de Jensen-Shannon na pergunta geral é cerca de 0,013 a 0,015 e a do número efetivo de regiões cerca de 0,7 a 0,8; mais células reduzem mais a largura do que mais repetições. O desenho tem 60 células (5 modelos × 4 línguas × 3 paráfrases) com 3 respostas cada na pergunta geral. A variação por paráfrase não existe no Estudo 1, pelo que as larguras reais serão maiores; o limiar de decisão de cada hipótese foi fixado com margem (por exemplo, Algarve 0,5 contra 0,29 observado) para absorver isso.

## 8. O que mudaria a conclusão

- Se H1b falhar (Algarve ≥ 0,5) ou H1c falhar, a tese de substituição de produto não se confirma.
- Se H2a falhar (< 60%), a tese de concentração no planeamento não se confirma.
- Se H4 falhar, a homogeneização não é um resultado.
- Se H5 falhar (os LLMs seguem as dormidas tanto ou mais do que a Wikipédia), o mecanismo de imagem discursiva não se sustenta e o artigo reporta-o.

## 9. Alvo da inferência

As conclusões aplicam-se às versões de modelo testadas, às formulações de prompt testadas (três por tipo) e ao período de recolha. A generalização a outros países, a interfaces de consumo (com pesquisa, memória e localização) e a modelos futuros não é objeto deste estudo; a condição com pesquisa web é exploratória.
