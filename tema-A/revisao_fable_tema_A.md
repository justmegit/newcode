# Revisão crítica do tema A: "The algorithmic destination image"

Revisão a pedido dos autores, no papel de revisor exigente de uma revista Q1 de turismo. Data: 5 de novembro de 2026. Baseia-se no pedido de opinião, nos scripts, nas 480 respostas, nas 15 665 extrações e nos resultados em `results/`. Recalculei várias medidas a partir de `data/extracoes.jsonl` e descarreguei do Eurostat as dormidas de 2025 por residência (não residentes e residentes) para as 26 NUTS III. Onde cito literatura de memória, marco [verificar].

---

## Veredicto

A ideia é boa, a pergunta é oportuna e o pipeline está limpo e reprodutível. Mas, tal como está, o artigo repete duas das quatro razões da rejeição anterior (descritivo, sem teoria que preveja alguma coisa) e tem três problemas de medida que explicam, em parte, os resultados principais. Verifiquei os três nos vossos dados. A boa notícia é que, depois das correções, há uma história mais forte e mais simples do que a atual.

Os três factos que mudam a leitura dos resultados:

1. **O rácio de enviesamento na pergunta geral é um artefacto da medida de presença.** Cada resposta nomeia em média 9,45 NUTS III distintas. Como uma região só conta uma vez por resposta, nenhuma região pode ter mais de 10,6% da "atenção". Seis regiões aparecem em 100% das respostas (Grande Lisboa, AM Porto, Madeira, Região de Coimbra, Alentejo Central, Douro) e têm por isso exatamente a mesma quota, 10,6%. Os rácios de 0,47 (Lisboa) e 13,0 (Douro) são a mesma presença dividida por quotas de dormidas diferentes. H1 está decidida pela construção da medida, não pelos modelos.

2. **O termo de comparação está errado para três das quatro línguas.** Quem pergunta em inglês, espanhol ou francês é um turista estrangeiro. As dormidas de não residentes (Eurostat, `c_resid=FOR`, 2025) têm Gini 0,763, não 0,663. O Gini do roteiro de 7 dias (0,76) deixa de ser "superior ao das dormidas". H2 cai com o termo de comparação certo.

3. **O roteiro de 7 dias conta uma história diferente da que contam.** Extraí de forma aproximada os dias que os modelos atribuem a cada paragem: AM Porto 46%, Grande Lisboa 42%, Douro 6%, Algarve e Madeira 0%. Gini 0,90. A concentração do planeamento não é "a mesma da procura", é muito maior, e está noutro sítio: um corredor urbano Lisboa-Porto, sem sol e mar. Isto é o resultado mais interessante do piloto e ainda não está no artigo.

A estrutura de resultados que emerge depois das correções: os LLMs reproduzem o cânone do turismo cultural e patrimonial (Lisboa, Sintra, Porto, Douro, Coimbra, Évora, Óbidos, Madeira, Açores) com uma uniformidade quase total entre modelos e línguas, e omitem o produto que domina as dormidas, o sol e mar (Algarve, Península de Setúbal, Alentejo Litoral). Não é redistribuição aleatória, é substituição de um produto por outro. E quando planeiam, concentram-se no eixo urbano. Isso é uma tese com mecanismo, testável e ligada à política de desconcentração.

---

## 1. O que mata o artigo numa primeira revisão, por ordem de gravidade

### 1.1 Teto mecânico da medida de presença

Verificado nos dados: `nuts_distintas` por resposta na pergunta geral é 9,4 (min 8, max 13). O teto de quota é 1/9,45 = 10,6%. A Grande Lisboa tem 27% das dormidas de não residentes; mesmo presente em todas as respostas, o rácio máximo é 0,39. O Algarve, 29%; rácio máximo 0,37. Os rácios "inferiores a 1" de H1 são impossíveis de falhar.

Correção. Usar medidas em que uma região possa absorver uma quota grande:

- **Noites atribuídas nos roteiros.** Os 60 roteiros têm todos marcadores de dia (média 7,5 por resposta). Extraiam quantos dias cada paragem recebe. É a única medida do estudo com a mesma natureza das dormidas e é a mais barata de obter. A minha extração aproximada por expressões regulares deu os números acima; façam-na bem, com o extrator.
- **Exposição ponderada pela posição** nas listas de 10 (pesos 1/log2(posição+1), como no DCG). Com esta medida e o termo de comparação certo, o rácio da Grande Lisboa nas línguas estrangeiras passa de 0,39 para 0,84 e o da AM Porto para 1,17. O Algarve fica em 0,30 e o Alentejo Central em 11. Ou seja, a sub-representação de Lisboa quase desaparece; a do Algarve e a sobre-representação de Évora, Coimbra e Óbidos ficam. Isso é a história real.
- **Primeira menção** não serve como medida principal: é Lisboa em 92% das respostas gerais e em 100% dos roteiros. Serve como indicador de "porta de entrada".
- Presença e "todas as menções" ficam como medidas secundárias, sempre acompanhadas do número de regiões distintas por resposta, por modelo e língua. As respostas do Gemini têm o dobro do comprimento das do Claude (5 200 contra 2 600 caracteres), o que infla a medida de menções.

### 1.2 Gini contra Gini não compara o que pensam que compara

O Gini das dormidas é calculado sobre 26 regiões todas com valores positivos. O Gini das recomendações é calculado sobre contagens de presença com muitos zeros (10 a 14 regiões a zero em cada pergunta). Esse Gini mede sobretudo quantas regiões cada resposta cobre e quanto consenso há entre respostas. Se todas as respostas nomeiam as mesmas 9 regiões, o Gini é (26 menos 9)/26 = 0,65, seja qual for a relação com as dormidas. O 0,63 da pergunta geral é isso: cobertura de 9 regiões e Jaccard médio entre respostas de 0,86.

Correção. Substituir a comparação de Ginis por medidas que relacionem diretamente as duas distribuições:

- **Declive log-log** da quota nas recomendações sobre a quota nas dormidas. Calculei sobre as regiões com quota positiva: 0,59 na pergunta geral, 0,09 no roteiro, menos 0,22 em "pouco conhecidos". Declive menor do que 1 é achatamento. Tem de ser estimado com os zeros incluídos (pseudo-contagem ou modelo Tobit), senão há seleção.
- **Número efetivo de regiões** (exponencial da entropia). Dormidas totais: 10,8; não residentes: 7,7; pergunta geral: 11,1; roteiro em presença: 7,9; "pouco conhecidos": 15,4. Diz em quantas regiões "cabe" a atenção, sem o problema dos zeros.
- **Consenso** (Jaccard médio entre pares de respostas): geral 0,86, vinho 0,83, cultura 0,79, roteiro 0,58, "pouco conhecidos" 0,50. Separa "poucas regiões" de "sempre as mesmas".
- **Divergência** (Jensen-Shannon ou variação total) entre a distribuição das recomendações e a das dormidas, com intervalo por bootstrap.
- Se mantiverem um Gini, que seja sobre as noites atribuídas nos roteiros, que têm a mesma natureza das dormidas.

### 1.3 Termo de comparação: residência, âmbito e versão NUTS

- **Residência.** Para EN, ES e FR usem `c_resid=FOR`; para PT, `DOM` ou total; reportem ambos. Os números de 2025 que descarreguei: total 89,4 milhões (Gini 0,663), não residentes 60,0 milhões (Gini 0,763), residentes 29,4 milhões (Gini 0,471). As quotas mudam muito: Grande Lisboa 27,0% (FOR) contra 13,1% (DOM); Alentejo Central 0,8% contra 2,5%. Os valores completos estão na secção 5 desta revisão.
- **Âmbito Eurostat contra INE.** Resolvido: a tabela `tour_occ_nin2` de 2025 para Portugal dá 89 427 522 no total NACE I55.1 a I55.3, dos quais 6 955 104 em parques de campismo (I55.3). Sem campismo: 82,47 milhões, que bate com os 82,1 milhões do INE a menos de 0,5%, diferença atribuível a colónias de férias e pousadas de juventude. Escrevam uma frase e escolham: ou excluem o campismo em ambos os lados ou declaram que incluem. O campismo pesa no Algarve e no Alentejo Litoral.
- **Versão NUTS.** Confirmei: o ficheiro Eurostat que usaram está na NUTS 2024 (códigos PT1A0 Grande Lisboa, PT1B0 Península de Setúbal, PT1C* Alentejo, PT1D* Oeste e Vale do Tejo, PT19* Centro). As séries NUTS 2021 aparecem vazias para 2025. Está correto; digam-no no artigo, porque muitos leitores portugueses ainda pensam em AM Lisboa como uma unidade.

### 1.4 Extração: menções supra-municipais, títulos e consistência

Metade dos destinos extraídos (2 435 em 4 967) está marcada como abrangente ou tem nome de região, serra, parque ou ilha. Isso não é erro do extrator, é como os LLMs recomendam. Mas obriga a regras explícitas, e encontrei problemas concretos:

- "Vale do Douro" (e variantes) foi mapeado 251 vezes para Douro, 19 para AM Porto e 17 para Terras de Trás-os-Montes. O mesmo nome, três NUTS III. Na pergunta geral, 100% da presença do Douro vem de "Vale do Douro"; não há um único município. O rácio de 13 é defensável (o Alto Douro vinhateiro está maioritariamente na NUTS III Douro), mas tem de ser declarado como mapeamento de uma marca territorial.
- "Peneda-Gerês" foi mapeado 143 vezes para Cávado. O parque tem a maior área no Alto Minho (Arcos de Valdevez, Ponte da Barca, Melgaço) e toca Alto Tâmega e Barroso. A escolha é arbitrária e decide o rácio de três regiões.
- "Costa Vicentina" ficou 43 vezes em Baixo Alentejo (Odemira), 40 no Algarve e 7 em Alentejo Litoral. Odemira é Alentejo Litoral, não Baixo Alentejo [verificar: na NUTS 2024 Odemira continua no Alentejo Litoral]. Isto parece erro sistemático.
- "Alentejo" genérico apareceu 61 vezes, todas mapeadas para Alentejo Central, mas quase todas nas perguntas de vinho (28) e inverno (25). Na pergunta geral, o Alentejo Central é Évora. O resultado do Alentejo Central na pergunta geral sobrevive a este teste.
- Títulos extraídos como destinos: "Itinéraire de 7 jours au Portugal" ficou como único destino de um roteiro (Grande Lisboa), e "10 lugares menos conhecidos em Portugal" foi extraído como lugar inexistente. Precisam de um filtro para títulos e de uma verificação de que cada roteiro tem pelo menos as paragens dos dias.
- Lugares reais marcados como inexistentes: Costa de Prata, Estuário do Tejo, Poça da Dona Beija, Torneiros, Pousadas de Portugal. Os inexistentes verdadeiros são sobretudo lugares espanhóis (Sanlúcar de Guadiana, Lobios, Rihonor), que são respostas válidas a "longe das multidões" e não alucinações. A taxa de alucinação é quase zero (20 em 15 665). Retirem a RQ4 do centro e reportem-na numa frase.

Correção. Livro de códigos com três regras: (a) títulos e frases introdutórias não são destinos; (b) menções supra-municipais recebem um nível próprio, "macro-destino", e são excluídas da análise principal por NUTS III, com análise de sensibilidade por alocação fracionária (ponderada por dormidas e por igual); (c) tabela fixa de correspondência para as 30 marcas territoriais mais frequentes (Vale do Douro, Gerês, Serra da Estrela, Costa Vicentina, Arrábida, Ria Formosa, Alentejo, Aldeias do Xisto, Bairrada, Dão), aplicada de forma determinística depois da extração, e não deixada ao Haiku em cada chamada. Reportem a percentagem de destinos que são macro-destinos por pergunta: é um resultado em si.

### 1.5 Validação humana: o desenho atual não mede o que falta

O ficheiro de verificação pede aos codificadores para confirmar linhas já extraídas (s/n). Isso mede precisão, não recall: um destino que o extrator não apanhou só aparece se o codificador se lembrar de o escrever na nota. E o kappa sobre uma variável com 95% de "s" vai sair baixo, como já antecipam.

Correção. Dois exercícios distintos: (1) para 30 respostas estratificadas, dois codificadores listam os destinos principais a partir do texto, às cegas, e comparam-se com o extrator (precisão e recall do extrator; concordância entre codificadores com Krippendorff ou Jaccard); (2) para as 964 linhas já preparadas, verificação de município e NUTS III (precisão por dimensão). Reportem as três coisas em separado: recall de destinos, exatidão da NUTS III, exatidão do nível destino/atração.

### 1.6 Inferência: a confirmação está garantida à partida

As 5 repetições não são duplicados (zero pares iguais, similaridade textual de 0,2 a 0,3), o que é bom. Mas os conjuntos de regiões são quase idênticos (Jaccard 0,86), e as 12 células modelo × língua, com uma formulação por pergunta, são as unidades reais. O bootstrap estratificado por célula reamostra o ruído de amostragem do modelo e ignora a incerteza que importa: formulação do prompt, versão e escolha dos modelos. Os intervalos de 0,74 a 0,78 são sintoma disso. Com os mesmos modelos e prompts, 4 semanas depois, H1 a H3 confirmam-se quase de certeza; um revisor vai perguntar o que podia ter falhado.

Correção. Paráfrases (3 por pergunta nos três tipos com hipóteses), um ou dois modelos abertos (Llama, Mistral, Qwen, DeepSeek via OpenRouter, custo de cêntimos), decomposição de variância por modelo, língua, paráfrase e repetição, e bootstrap por agrupamento ao nível modelo × língua × paráfrase (intervalos BCa). Registem no pré-registo o que fazem se um modelo for descontinuado. O registo de versão e fornecedor que já gravam (`modelo_versao`) é exatamente o que um revisor pede; mantenham-no e reportem a janela de recolha (as 480 chamadas correram em 25 minutos, o que é ótimo).

### 1.7 Teoria descritiva, estudo descritivo

Dizer que o LLM é um "agente híbrido" de Gartner classifica, não explica. E a literatura de enviesamento de popularidade prevê o contrário do que encontraram. Ver secção 2.2.

### 1.8 Novidade face a Andreev et al. (2025)

Tal como está, a diferença é de escala e de termo de comparação. O que vos distingue está nos dados e ainda não está no texto: noites atribuídas nos roteiros, substituição de produto (património em vez de sol e mar), concentração no eixo urbano quando planeiam, e homogeneização total entre modelos.

---

## 2. Respostas às nove perguntas

### 2.1 Contributo

Não chega para Q1 tal como está; chega para Q2 com as correções de 1.1 a 1.6. Chega para Q1 com pelo menos duas destas quatro adições:

1. **Teste de mecanismo com um termo textual.** Comparem as quotas do LLM com as dormidas (comportamento) e com um proxy da imagem textual (visualizações ou dimensão das páginas da Wikipédia em EN e PT dos municípios e destinos, agregadas a NUTS III; ou listagens de "coisas para fazer" por município). Se o LLM segue o textual e não o comportamental, têm um mecanismo demonstrado.
2. **Dose-resposta no planeamento.** Roteiros de 3, 7 e 14 dias. Os vossos 7 dias dão 88% dos dias em Lisboa e Porto. A previsão: 3 dias é uma cidade; 14 dias abre Algarve, Alentejo e ilhas. Uma curva vale mais do que um ponto.
3. **Homogeneização.** Na pergunta geral, os três modelos dão o mesmo conjunto de 8 regiões em 95 a 100% das respostas; só divergem no Oeste (GPT 35%, os outros 95 a 100%) e no Cávado. Meçam a sobreposição entre modelos e entre línguas e discutam monocultura algorítmica (Kleinberg e Raghavan, 2021, PNAS [verificar]; Bommasani et al., 2022 [verificar]). É um contributo conceptual, não só empírico.
4. **Política.** A Estratégia Turismo 2027 quer alargar a atividade ao território. Os LLMs fazem isso no discurso (Évora, Coimbra, Douro) mas não no planeamento (Lisboa e Porto). E deslocam atenção para regiões com pouca capacidade (Douro, com saturação pontual no Pinhão; Évora, Capital Europeia da Cultura em 2027, o que pode estar a inflacionar a atenção no corpo de treino). Isto dá uma secção de implicações que um editor reconhece.

Sobre "amostra só portuguesa": aqui a amostra são respostas de modelos; Portugal é o caso. Justifiquem-no (concentração muito elevada, política explícita de desconcentração, debate sobre overtourism em Lisboa e Porto, NUTS III estáveis) e apresentem o método como protocolo portátil com código aberto, de que Portugal é a primeira aplicação.

### 2.2 Teoria

Gartner (1993) serve para posicionar, e há um argumento melhor do que "híbrido": os agentes autónomos (guias, jornalismo, cultura popular) têm credibilidade alta; os induzidos têm alcance alto. O LLM junta a credibilidade percebida de um agente autónomo ao alcance e à personalização de um induzido, sem a assinatura comercial que permite ao turista descontar a mensagem. Isso é um argumento.

Mas Gartner não prevê a direção do desvio. Para isso, três camadas compatíveis:

- **Imagem discursiva contra comportamento.** As dormidas medem comportamento, dominado por sol e mar, capacidade, preço, negócios e visitas a familiares. O texto de viagens, de onde o LLM aprende, mede o que vale a pena escrever: património, paisagem, "joias escondidas". O LLM é uma compressão do corpo de agentes autónomos e orgânicos e herda a sua agenda. Previsão: o desvio vai na direção do produto cultural e contra o produto sol e mar. É exatamente o que os vossos dados mostram (Algarve 0,30, Évora 11, Coimbra 6,5). Âncoras: a literatura de imagem projetada contra percebida online (Mak, 2017, Tourism Management [verificar]; Marine-Roig [verificar]).
- **Normativo contra descritivo.** "Onde devo ir" não é "onde vão as pessoas". A hipótese inicial confundia as duas; reconheçam-no e façam disso o objeto.
- **Restrições espaciais do planeamento.** Para o roteiro, o mecanismo é geográfico: coerência de rota e tempo de deslocação forçam a rota canónica Lisboa-Sintra-Porto-Douro. Âncoras: Lue, Crompton e Fesenmaier (1993) sobre viagens multi-destino; Lew e McKercher (2006) sobre modelação de movimentos turísticos [verificar anos].

Deixem o enviesamento de popularidade dos sistemas de recomendação como hipótese rival, rejeitada na pergunta geral e aceite no planeamento. Para viés geográfico em LLMs, Manvi et al. (2024) [verificar].

### 2.3 Pré-registo

É confirmação legítima no sentido estrito (hipóteses fixas antes dos dados), mas fraca, porque o alvo inferencial é "as mesmas versões, os mesmos prompts, 4 semanas depois". Como apresentar:

- "Estudo 1, exploratório (n = 480, 1 de novembro de 2026), gerou as hipóteses. Estudo 2, confirmatório, pré-registado no OSF em [data], testa-as em dados novos recolhidos em [janela]." No formulário do OSF, declarem o piloto sem rodeios.
- Digam qual é o alvo: estabilidade temporal e robustez à formulação, com estas versões. Não generalização a outros países ou modelos futuros.
- Tornem a confirmação não trivial: paráfrases, modelos novos, e uma condição em que a vossa teoria prevê algo que a rival não prevê (termo textual ou dose-resposta).
- Reescrevam as hipóteses com as medidas de 1.1 e 1.2. Proposta:
  - H1: na pergunta geral, o declive log-log entre exposição ponderada por posição e quota de dormidas de não residentes é inferior a 1; e a quota do Algarve é inferior a metade da sua quota de dormidas.
  - H2: no roteiro de 7 dias, a quota de noites atribuídas a Grande Lisboa mais AM Porto excede 70%; o número efetivo de regiões das noites atribuídas é inferior ao das dormidas de não residentes (7,7).
  - H3: em "pouco conhecidos", pelo menos 70% dos destinos ficam em regiões do tercil inferior de intensidade turística (dormidas por residente); e a sobreposição entre modelos no conjunto de regiões é superior a 0,4 (as joias escondidas são as mesmas para todos).
- Pré-registem também: exclusão de títulos, regra para macro-destinos, tabela de correspondência de marcas territoriais, tratamento de zeros, sensibilidade sem ilhas, versão do pipeline (hash do commit).
- Correção múltipla: H1 com componentes em que exigem que todas passem é um teste de interseção-união e já controla o erro ao nível nominal; não precisa de Bonferroni nas componentes. Tratem H1, H2 e H3 como três famílias, com Holm. Diferenças entre correlações sobre as mesmas 26 regiões são dependentes: bootstrap da diferença, não dois intervalos.

### 2.4 Termo de comparação

Dormidas são o termo certo para pressão e concentração; a dependência da capacidade é o que gera saturação, não um defeito. Mas um termo só não chega para interpretar o desvio. Três, com papéis definidos a priori:

1. Comportamental (primário): dormidas 2025 por NUTS III, não residentes para EN/ES/FR, residentes ou total para PT, com o âmbito NACE declarado.
2. Pressão (interpretação): dormidas por residente e por km2, para dizer se a atenção vai para regiões de baixa ou alta pressão.
3. Textual (mecanismo): Wikipédia, como em 2.1.

Por habitante e por camas são normalizações da camada 2, não termos primários. "Por atrações" é difícil de operacionalizar e acaba por ser um proxy textual pior do que a Wikipédia.

### 2.5 Medidas e estatística

Resumo das correções, por ordem: noites atribuídas e exposição ponderada por posição como medidas principais; presença e menções como secundárias com k reportado; declive log-log com zeros, número efetivo de regiões, consenso Jaccard e divergência em vez de Gini contra Gini; rácios em escala logarítmica com suavização (pseudo-contagem ou Dirichlet-multinomial), acompanhados da diferença em pontos percentuais, e destacados só nas regiões com mais de 1% das dormidas; lista das regiões nunca recomendadas (há 9 na pergunta geral) como resultado; sensibilidade sem Açores e Madeira; bootstrap por agrupamento ou modelo hierárquico; reportar comprimento das respostas por modelo e língua.

### 2.6 Validade externa

Não é fatal, se enquadrarem e acrescentarem uma condição pequena. Sem pesquisa, medem o prior paramétrico do modelo, que está presente em todas as interfaces e responde quando a pesquisa não é acionada. Mas acrescentem já uma condição com pesquisa web para a pergunta geral e o roteiro: 3 modelos × 4 línguas × 5 repetições × 2 perguntas, 120 chamadas. Se converge, a objeção cai; se diverge (a pesquisa puxa para conteúdo otimizado para motores de busca, provavelmente Algarve e Lisboa), têm um segundo resultado. Declarem o que a API não tem: prompt de sistema do produto, memória, localização do utilizador, conversa com seguimento. Registem a temperatura efetiva por fornecedor.

### 2.7 Dimensão

A restrição não são as 480 respostas; são as 12 células e a formulação única. Proposta para a recolha confirmatória: três tipos com hipóteses (geral, roteiro, pouco conhecidos), 3 paráfrases cada, 3 durações no roteiro (3, 7, 14 dias), 4 línguas, 4 ou 5 modelos, 3 repetições. Cerca de 900 respostas mais 120 com pesquisa web; 40 a 60 USD. Os outros cinco tipos ficam exploratórios ou saem para o segundo artigo. Justifiquem a dimensão por precisão (largura do intervalo do declive e da divergência, simulada a partir do piloto), não por poder.

### 2.8 Revistas

Todas as híbridas publicam sem taxa na via de subscrição; a taxa só existe se escolherem acesso aberto. Confirmem a política atual na página de cada revista.

| Revista | Editora | Porquê encaixa | Nota |
|---|---|---|---|
| Tourism Geographies | T&F | Concentração espacial, escala sub-nacional, geografia da visibilidade | Primeira escolha se o ângulo espacial e de política dominar |
| Information Technology & Tourism | Springer | Casa natural das auditorias de tecnologia em turismo; valoriza método e reprodutibilidade | Primeira escolha se o ângulo de auditoria e protocolo dominar |
| Journal of Sustainable Tourism | T&F | Overtourism, desconcentração | Exige a secção de implicações bem feita |
| Journal of Destination Marketing & Management | Elsevier | Imagem de destino é o tema da revista | Exige a camada teórica de 2.2 |
| Current Issues in Tourism | T&F | Temas emergentes; formatos curtos | Boa segunda opção |
| Tourism Management | Elsevier | Alcance máximo | Só com teste de mecanismo e homogeneização |
| Annals of Tourism Research | Elsevier | Contributo conceptual | Só se a teoria for o centro; considerar nota de investigação |
| Journal of Travel Research | SAGE | Rigor metodológico | Vai pedir mais modelos e mecanismo |
| Tourism Review | Emerald | Aberta a IA generativa | Opção mais acessível |
| European Journal of Tourism Research | Varna | Acesso aberto sem taxa, Scopus | Rede de segurança |

Evitem Annals of Tourism Research Empirical Insights e outras de acesso aberto com taxa obrigatória.

### 2.9 O que fazer nas próximas duas semanas

1. Filtro de títulos, tabela de marcas territoriais e regra para macro-destinos; reextração determinística da NUTS III a partir do município.
2. Validação humana em dois exercícios (recall às cegas em 30 respostas; precisão nas 964 linhas).
3. Recalcular o piloto com noites atribuídas, exposição ponderada, declive log-log, número efetivo de regiões e consenso, contra dormidas de não residentes. Ver se a história sobrevive; pelos meus cálculos, sobrevive numa forma mais forte.
4. Reescrever as hipóteses, acrescentar paráfrases, modelos abertos, durações de roteiro e condição com pesquisa web. Pré-registar.
5. Escrever a teoria como oposição entre duas previsões (imagem discursiva contra enviesamento de popularidade) e acrescentar o termo textual que as distingue.
6. Preparar código, dados e livro de códigos para publicação no OSF e no GitHub no momento da submissão.

---

## 3. Tese sugerida para o resumo

"Os LLMs não reproduzem o mapa da procura turística; reproduzem o mapa do cânone cultural e patrimonial. Quando listam destinos, substituem o sol e mar, que domina as dormidas, pelo património do interior e do litoral histórico. Quando planeiam, as restrições de rota empurram-nos para um corredor urbano Lisboa-Porto, mais concentrado do que a própria procura. Três modelos e quatro línguas convergem no mesmo mapa. Para destinos com pouca capacidade, a visibilidade algorítmica chega antes da infraestrutura."

---

## 4. Problemas menores no código

- `extract.py`: a NUTS III é pedida ao Haiku em cada chamada. Peçam só o município e derivem a NUTS III de uma tabela município → NUTS III (CAOP 2024). Elimina a inconsistência "Vale do Douro" em três regiões e a NUTS inválida "Beira Interior Norte".
- `extract.py`: a amostra de verificação é por resposta, o que está certo, mas o CSV só permite confirmar linhas; ver 1.5.
- `analyze.py`: o Gini não tem correção de pequena amostra (n/(n menos 1)); com 26 unidades vale 4%. Irrelevante se abandonarem o Gini contra Gini, mas reportem a fórmula.
- `analyze.py`: `existe` em falta é tratado como verdadeiro; tornem explícito.
- `collect.py`: `finish_reason == "length"` levanta erro, bem; registem também `usage` (tokens) para controlar o comprimento.
- README: diz "comparação com as dormidas (INE)" em `analyze.py`, mas a fonte é o Eurostat. Corrijam.

---

## 5. Dormidas 2025 por NUTS III e residência (Eurostat, tour_occ_nin3, descarregado em 2026-11-05)

Total 89 427 522; não residentes 60 022 455; residentes 29 405 067. Gini: total 0,663; não residentes 0,763; residentes 0,471.

| NUTS III | Total % | Não residentes % | Residentes % |
|---|---|---|---|
| Algarve | 25,7 | 28,8 | 19,3 |
| Grande Lisboa | 22,4 | 27,0 | 13,1 |
| Área Metropolitana do Porto | 11,7 | 12,7 | 9,6 |
| Região Autónoma da Madeira | 11,1 | 13,7 | 5,8 |
| Região Autónoma dos Açores | 3,5 | 3,4 | 3,7 |
| Península de Setúbal | 2,7 | 1,6 | 4,9 |
| Alentejo Litoral | 2,5 | 1,3 | 4,9 |
| Oeste | 2,5 | 1,6 | 4,3 |
| Região de Coimbra | 2,3 | 1,4 | 4,2 |
| Médio Tejo | 1,9 | 1,6 | 2,4 |
| Cávado | 1,5 | 1,1 | 2,3 |
| Alto Minho | 1,4 | 0,9 | 2,4 |
| Alentejo Central | 1,3 | 0,8 | 2,5 |
| Região de Aveiro | 1,3 | 0,9 | 2,3 |
| Beiras e Serra da Estrela | 1,2 | 0,3 | 3,1 |
| Região de Leiria | 1,0 | 0,4 | 2,3 |
| Ave | 0,8 | 0,5 | 1,5 |
| Douro | 0,8 | 0,5 | 1,4 |
| Viseu Dão Lafões | 0,8 | 0,2 | 1,9 |
| Baixo Alentejo | 0,7 | 0,3 | 1,5 |
| Alto Alentejo | 0,6 | 0,2 | 1,5 |
| Tâmega e Sousa | 0,6 | 0,3 | 1,2 |
| Alto Tâmega e Barroso | 0,5 | 0,2 | 1,1 |
| Terras de Trás-os-Montes | 0,4 | 0,2 | 0,9 |
| Beira Baixa | 0,4 | 0,2 | 0,9 |
| Lezíria do Tejo | 0,4 | 0,1 | 0,9 |

Comando para reproduzir: `https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/tour_occ_nin3?format=JSON&lang=EN&time=2025&c_resid=FOR&unit=NR` (e `c_resid=DOM`). Âmbito NACE em `tour_occ_nin2?geo=PT&time=2025`: I551 67 656 449; I552 14 815 969; I553 (campismo) 6 955 104.

## 6. Números recalculados do piloto que cito acima

| Medida | Valor |
|---|---|
| NUTS III distintas por resposta, pergunta geral | 9,4 (teto de quota 10,6%) |
| NUTS III distintas por resposta, roteiro | 4,9 |
| Regiões presentes em 100% das respostas gerais | Grande Lisboa, AM Porto, Madeira, Coimbra, Alentejo Central, Douro |
| Jaccard médio entre respostas, geral / roteiro / pouco conhecidos | 0,86 / 0,58 / 0,50 |
| Declive log-log (regiões com quota positiva), geral / roteiro / pouco conhecidos | 0,59 / 0,09 / menos 0,22 |
| Número efetivo de regiões, geral / roteiro / pouco conhecidos / dormidas FOR | 11,1 / 7,9 / 15,4 / 7,7 |
| Dias atribuídos nos roteiros (aproximado): AM Porto / Grande Lisboa / Douro / Algarve | 46% / 42% / 6% / 0% (Gini 0,90) |
| Exposição ponderada por posição, línguas estrangeiras, rácio contra FOR: Lisboa / Porto / Algarve / Alentejo Central / Coimbra | 0,84 / 1,17 / 0,30 / 11,0 / 6,5 |
| Destinos abrangentes ou com nome de região | 2 435 de 4 967 |
| Pares de respostas idênticas dentro da mesma célula | 0 de 960 |
| Comprimento médio: Claude / GPT / Gemini | 2 660 / 3 600 / 5 400 caracteres |
| Lugares marcados inexistentes | 20 de 15 665, vários errados |
