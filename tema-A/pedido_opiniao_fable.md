# Pedido de opinião: artigo "The algorithmic destination image" (tema A)

Somos três docentes de turismo do ISCE (Portugal) e queremos publicar este estudo numa revista indexada em Scopus ou WoS, de preferência Q1/Q2. Pedimos uma revisão crítica, como a de um revisor exigente de uma revista de topo. Diz-nos o que está mal antes do que está bem. Responde em português.

## Contexto

- O nosso último artigo (perceções de estudantes sobre tecnologias digitais no ensino do turismo) foi rejeitado numa revista de topo por quatro razões: tema saturado, estudo descritivo, amostra só portuguesa e falta de teoria. Queremos evitar repetir estes erros.
- Restrições: não temos orçamento para painéis pagos nem para taxas de publicação. Este primeiro artigo é só dos três autores. Uma replicação noutros países, com coautores estrangeiros, fica para um segundo artigo.
- Usamos IA como apoio (código, extração, revisão), mas as decisões são nossas e registamos o uso para a declaração exigida pelas revistas.

## Pergunta e tese

Como recomendam os LLMs destinos em Portugal, e como se compara essa atenção com a procura turística real por região (NUTS III)?

- **Hipótese inicial:** os LLMs concentram a atenção nos destinos já saturados.
- **Tese atual:** surgiu depois de vermos o piloto. Os LLMs redistribuem a atenção entre regiões (sobrerrepresentam umas e subrepresentam outras face às dormidas) e concentram-na quando planeiam uma viagem.
- **Enquadramento:** formação da imagem de destino (agentes induzidos e orgânicos de Gartner, 1993), com o LLM como novo agente híbrido; enviesamento de popularidade em sistemas de recomendação; concentração espacial e overtourism.
- **Estudo mais próximo:** Andreev et al. (2025) auditaram o ChatGPT e o DeepSeek com 216 perfis de viajante e encontraram enviesamento de popularidade. Diferenciamo-nos por três pontos: análise dentro de um país, ao nível NUTS III; comparação com a procura real (dormidas); ligação à concentração turística.

## Piloto (1 de novembro de 2026)

- **Modelos**, via API do OpenRouter, sem pesquisa web nem memória e com temperatura por omissão: Claude Sonnet 5.5, GPT-6.1, Gemini 4.
- **Perguntas:** 8 tipos (geral, roteiro de 7 dias, natureza, cultura, "pouco conhecidos", família com crianças até aos 12 anos, vinho, inverno), em PT, EN, ES e FR, com 5 repetições. No total, 480 respostas.
- **Extração:** o Claude Haiku 5.5 identifica os lugares e atribui-lhes município e NUTS III, em dois níveis: destino principal e atração dentro de um destino. Ainda não houve verificação humana. Está prevista para 20% das respostas, por dois codificadores, com o kappa de Cohen.
- **Medida principal:** presença de cada NUTS III nos destinos principais de cada resposta (conta uma vez por resposta). **Medida secundária:** todas as menções.
- **Comparação:** dormidas de 2025 por NUTS III (Eurostat, tabela `tour_occ_nin3`). O site do INE não estava acessível. O total do Eurostat (89,4 milhões) é superior aos 82,1 milhões divulgados; ainda não percebemos a diferença de âmbito.

### Resultados

| Medida | Gini (IC 95% bootstrap) |
|---|---|
| Dormidas | 0,66 |
| Todas as perguntas juntas, destinos | 0,41 (0,40 a 0,43) |
| Pergunta geral | 0,63 (0,61 a 0,64) |
| Roteiro de 7 dias | 0,76 (0,74 a 0,78) |
| "Pouco conhecidos" | 0,54 (0,52 a 0,57) |
| Restantes perguntas | 0,60 a 0,63 |

- **O agregado engana.** O valor de 0,41 resulta sobretudo de juntar 8 perguntas que puxam por regiões diferentes. Dentro de cada pergunta, a concentração fica perto da das dormidas. Já tínhamos comunicado à equipa que as recomendações estavam "menos concentradas do que a procura"; corrigimos depois.
- **Rácio de enviesamento** (quota nas recomendações ÷ quota nas dormidas), na pergunta geral: Douro 13,0, Alentejo Central 7,9, Área Metropolitana do Porto 0,90, Grande Lisboa 0,47, Algarve 0,41.
- **"Pouco conhecidos":** a correlação de Spearman com as dormidas desce de 0,70 (pergunta geral) para -0,09.
- **Modelos e línguas:** diferenças pequenas. O Gini dos destinos vai de 0,41 a 0,42 entre modelos e de 0,39 a 0,43 entre línguas.
- **Inexistentes:** a marcação automática de lugares inexistentes não é fiável. Assinalou lugares reais.

## Recolha confirmatória (rascunho de pré-registo)

Fazemos uma recolha nova, igual ao piloto, pelo menos 4 semanas depois, registada no OSF antes de começar. As 480 respostas do piloto ficam como estudo exploratório.

- **H1:** na pergunta geral, o rácio é superior a 1 no Douro e no Alentejo Central e inferior a 1 na Grande Lisboa e no Algarve.
- **H2:** no roteiro de 7 dias, o Gini dos destinos é superior ao das dormidas (0,663).
- **H3:** a correlação de Spearman com as dormidas é menor em "pouco conhecidos" do que na pergunta geral.
- **Análise:** bootstrap com 10 000 reamostragens, estratificado por modelo e língua. Intervalos de 99,2% (Bonferroni para 6 testes). H1 confirma-se se os quatro intervalos ficarem todos do lado previsto de 1.
- **Não testamos** o Gini agregado.
- **Custo:** cerca de 20 a 25 USD.

## O que vos pedimos

1. **Contributo:** é suficiente para uma revista Q1 de turismo, face a Andreev et al. (2025) e à literatura de auditoria de LLMs? Se não for, o que falta?
2. **Teoria:** o enquadramento (imagem de destino e LLM como agente de formação de imagem, enviesamento de popularidade) aguenta-se? Há uma teoria melhor para explicar a redistribuição?
3. **Pré-registo:** as hipóteses foram tiradas do piloto e são testadas com os mesmos modelos e perguntas, 4 semanas depois. Isto é confirmação legítima ou só replicação? Como o devemos apresentar?
4. **Termo de comparação:** as dormidas dependem da capacidade instalada. Faz sentido comparar recomendações com dormidas? Há alternativa melhor, por exemplo por habitante, por oferta ou por atrações?
5. **Medidas e estatística:** presença por resposta, Gini sobre 26 regiões com zeros, rácios, bootstrap estratificado e Bonferroni. Há problemas, como a dependência entre repetições do mesmo modelo, ou rácios instáveis em regiões com quota de dormidas muito pequena?
6. **Validade externa:** a API sem pesquisa web não é o que um turista usa na app. Isto é fatal, ou basta reportá-lo como limitação? Vale a pena acrescentar uma condição com pesquisa web já neste artigo?
7. **Dimensão:** chegam 480 respostas (60 por pergunta)? Ou devíamos concentrar a recolha em menos perguntas, com mais repetições?
8. **Revistas:** que revistas indexadas, sem taxa de publicação, encaixam neste estudo?
9. **O que mataria o artigo** numa primeira revisão, e como o resolvemos já?
