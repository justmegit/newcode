# Enquadramento teórico e literatura (tema A, proposta v2)

Rascunho para discussão. Todas as referências de memória estão marcadas [verificar]: confirmar autores, ano, revista e conteúdo antes de citar. A lista final deve ser construída com pesquisa sistemática (Scopus e WoS, termos abaixo).

## 1. O que precisamos que a teoria faça

O piloto mostra três padrões: (a) na pergunta geral, os LLMs substituem o produto que domina as dormidas (sol e mar) pelo cânone cultural e patrimonial; (b) quando planeiam um roteiro, concentram-se num corredor urbano Lisboa-Porto, mais do que a própria procura; (c) três modelos e quatro línguas convergem no mesmo mapa. Uma teoria útil tem de prever a direção de (a), o mecanismo de (b) e explicar (c). A tipologia de Gartner classifica o LLM mas não prevê nada disto. Precisamos de três camadas.

## 2. Camada 1: o LLM como agente de formação de imagem (posicionamento)

Gartner (1993) distingue agentes induzidos (publicidade, operadores), autónomos (jornalismo, guias, cultura popular) e orgânicos (experiência própria, boca a boca), e atribui-lhes credibilidade, custo e penetração diferentes: os autónomos têm credibilidade alta, os induzidos alcance alto. O argumento a construir: o LLM combina a credibilidade percebida de um agente autónomo (não tem anunciante visível) com o alcance, a personalização e a interatividade de um agente induzido, e, ao contrário de ambos, responde a uma pergunta direta com uma lista fechada. É um agente de "imagem solicitada sintética". O ponto não é o rótulo, é a consequência: o turista não tem o sinal comercial que lhe permite descontar a mensagem, e recebe um conjunto pequeno e estável de destinos.

Referências de base: Gartner (1993) [verificar: Journal of Travel & Tourism Marketing, 2(2/3)]; Gunn (1972) sobre imagem orgânica e induzida [verificar]; Baloglu e McCleary (1999) sobre determinantes da imagem [verificar]; Tasci e Gartner (2007) sobre imagem e relações operacionais [verificar].

## 3. Camada 2: imagem discursiva contra comportamento (prevê a direção)

As dormidas medem comportamento, e o comportamento é dominado por sol e mar, capacidade instalada, preço, acessibilidade aérea, negócios e visitas a familiares. O texto de viagens, de onde o LLM aprende, mede o que vale a pena escrever: património, paisagem, autenticidade, variedade, "joias escondidas". Um LLM é uma compressão estatística do corpo de agentes autónomos e orgânicos (guias, imprensa, blogues, fóruns, Wikipédia) e herda a sua agenda editorial. Previsão: o desvio entre recomendação e dormidas vai na direção do produto cultural e patrimonial e contra o produto sol e mar, e é mais forte onde a imagem textual e o comportamento mais divergem (Algarve: muitas dormidas, pouco texto; Évora, Coimbra, Óbidos: pouco peso nas dormidas, muito texto).

Isto liga-se à literatura sobre imagem projetada contra imagem percebida e sobre imagem de destino online, que há vinte anos compara o que as organizações e os media projetam com o que os turistas dizem e fazem. É também uma distinção entre recomendação normativa ("onde deves ir") e descrição ("onde vão as pessoas"). A hipótese inicial do projeto confundia as duas; a versão v2 faz da diferença o objeto de estudo.

Teste: termo de comparação textual (visualizações da Wikipédia por município, agregadas a NUTS III; `fetch_wikipedia.py`). Se a quota do LLM segue o textual e não o comportamental, o mecanismo fica demonstrado. Se segue ambos, o LLM é um compromisso. Se não segue nenhum, há outra coisa (por exemplo, o prompt de treino por reforço a favorecer variedade).

Referências a procurar: Mak (2017), Tourism Management, sobre imagem online projetada e percebida [verificar]; Marine-Roig e Anton Clavé sobre imagem de destino em conteúdos gerados por utilizadores [verificar]; Govers, Go e Kumar (2007) sobre imagem projetada e percebida [verificar]; Choi, Lehto e Morrison (2007) sobre representações de Macau na web [verificar]; literatura de agenda-setting aplicada ao turismo (cobertura mediática e escolha de destinos) [verificar].

## 4. Camada 3: restrições espaciais do planeamento (prevê a concentração no roteiro)

Uma lista de 10 lugares não tem custos de deslocação; um roteiro de 7 dias tem. A coerência de rota, o tempo de viagem e a entrada por aeroporto forçam uma solução canónica: Lisboa (aeroporto), Sintra (excursão), Porto (segundo aeroporto), Douro (excursão). O modelo não está a "enviesar", está a resolver um problema de itinerário com uma heurística aprendida de milhares de roteiros publicados. Previsão: a concentração aumenta quando a duração diminui (3 dias é uma cidade) e diminui quando aumenta (14 dias abre Algarve, Alentejo e ilhas), e a parte do tempo em Lisboa e Porto é maior do que a sua quota de dormidas de não residentes.

Referências: Lue, Crompton e Fesenmaier (1993) sobre padrões de viagem multi-destino [verificar: Annals of Tourism Research]; Lew e McKercher (2006) sobre modelação de movimentos turísticos [verificar: Annals]; Oppermann (1995) sobre padrões espaciais de viagem [verificar]; literatura sobre "tourist bubble" e "beaten track" [verificar]; trabalhos recentes sobre geração de itinerários por LLM (benchmark TravelPlanner, Xie et al., 2024) [verificar].

## 5. Hipótese rival: enviesamento de popularidade

Os sistemas de recomendação tendem a sobre-expor os itens populares (Abdollahpouri, Burke e Mobasher, 2017 e 2019 [verificar]; Ekstrand et al. [verificar]). Aplicado a destinos, prevê mais atenção a Lisboa e Algarve do que a sua quota de procura. O piloto rejeita isto na pergunta geral (Algarve sub-representado mesmo com medida sem teto) e aceita-o parcialmente no roteiro (Lisboa e Porto sobre-representados). Apresentar o artigo como teste entre duas previsões (imagem discursiva contra popularidade) dá-lhe a estrutura que faltava ao anterior. Andreev et al. (2025), que encontraram enviesamento de popularidade entre países ou destinos de grande escala, são o contraponto direto: a escala sub-nacional e o termo de comparação comportamental mudam a conclusão. [verificar o conteúdo exato de Andreev et al. antes de o descrever.]

## 6. Homogeneização e monocultura algorítmica

Se três modelos de três empresas, em quatro línguas, produzem o mesmo conjunto de oito regiões em 95 a 100% das respostas, a questão deixa de ser "qual é o viés de cada modelo" e passa a ser "o que acontece quando um canal de informação com alcance de massas tem uma só resposta". Kleinberg e Raghavan (2021, PNAS) formalizam a monocultura algorítmica e os seus custos de bem-estar [verificar]; Bommasani et al. (2022) discutem a homogeneização de resultados em modelos de fundação [verificar]. Em turismo, a ligação é com a literatura sobre concentração espacial e overtourism (Koens, Postma e Papp, 2018; Dodds e Butler, 2019 [verificar]) e com a política de desconcentração (Estratégia Turismo 2027, Turismo de Portugal [verificar o documento e as metas regionais]).

## 7. Viés geográfico em LLMs

Manvi et al. (2024), "Large language models are geographically biased" [verificar: ICML], mostram priors espaciais sistemáticos; há trabalhos sobre representação desigual de países e de regiões em modelos de linguagem [verificar]. O nosso contributo é levar isto à escala sub-nacional, com uma variável de resultado com significado económico (dormidas) e um desenho que separa lista de roteiro.

## 8. Termos de pesquisa para a revisão sistemática da literatura

- ("large language model*" OR ChatGPT OR "generative AI") AND (tourism OR destination OR travel) AND (recommend* OR itinerar* OR bias)
- "destination image" AND (projected OR online OR "user-generated") AND (gap OR congruence)
- "popularity bias" AND recommender AND (tourism OR "point of interest" OR POI)
- "spatial concentration" AND tourism AND (Gini OR inequality) ; overtourism AND (dispersal OR deconcentration)
- "multi-destination" AND (itinerary OR "trip pattern") ; "tourist movement" AND model
- "algorithmic monoculture" ; homogenization AND "foundation model"
- Portugal AND tourism AND (regional OR NUTS) AND concentration

## 9. Frase de tese (para o resumo)

"Os LLMs não reproduzem o mapa da procura turística; reproduzem o mapa do cânone cultural e patrimonial. Quando listam destinos, substituem o sol e mar pelo património do interior e do litoral histórico. Quando planeiam, as restrições de rota empurram-nos para um corredor urbano Lisboa-Porto, mais concentrado do que a própria procura. Modelos e línguas convergem no mesmo mapa. Para destinos com pouca capacidade, a visibilidade algorítmica chega antes da infraestrutura."
