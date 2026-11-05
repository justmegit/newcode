# Juiz 3: teste de reidentificação (24 out 2026)

Três agentes independentes, um por texto, sobre cópias limpas (sem registo de provas nem HANDOFF). Máximo de 5 pesquisas web cada. Cada agente escreveu um palpite às cegas antes de pesquisar e declarou contaminação. Critério: cliente não identificado em 5 pesquisas.

| Texto | Pesquisas | Contaminação | Cliente identificado | Resultado |
|---|---|---|---|---|
| Caso 4 | 5 de 5 | nenhuma declarada | não (falso positivo plausível, ~10%, que o texto não confirma) | **passa** |
| Caso 5 | 5 de 5 | nenhuma declarada | não (país não determinado; fabricante ~10%, não confirmado) | **passa** |
| Ensaio | 3 de 5 | nenhuma declarada | não (nem o país) | **passa** |

Limite: os agentes herdam o ambiente do projeto, por isso a ausência de contaminação é declarada por eles, não provada. O risco residual é reconhecimento por conhecimento interno (concorrente, fabricante, equipa do cliente), que a pesquisa web não mede.

## Ajustes sugeridos (NÃO aplicados; decisão do Alexandre; correr `check_ledger.py` depois)

**Caso 4**
- «exclusive distributor» -> «authorised partner» / «specialist installer»
- datas absolutas (28 August, 20 October) -> relativas
- retirar «catalogue requests» e a linguagem de «corridor»
- «southern Europe» -> «Europe»

**Caso 5**
- «a national technical body» -> «an independent technical assessment»
- «another country's design standard» -> «a standard other than the one in the market where the ads ran»
- «salt-fog» -> «a corrosion test»
- «a structure made by a European manufacturer» -> «a product»
- retirar «tested on a single size»

**Ensaio**
- «configurator», «journal» -> «interactive tools», «editorial section»
- arredondar ou retirar os tempos de resposta exatos
- retirar «a client portal», «three weeks», «that month»
- «premium home-improvement» -> «premium consumer-services»
- não juntar «código parece gerado por IA» com «texto parece traduzido»
