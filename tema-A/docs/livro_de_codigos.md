# Livro de códigos: extração e codificação geográfica (tema A, v2)

Versão 2, 5 de novembro de 2026. Aplica-se à extração automática (`extract.py` + `reprocess.py`), à verificação humana (`verificacao_v2.py`) e à análise (`analyze_v2.py`). Qualquer alteração depois do pré-registo tem de ser datada e justificada neste ficheiro.

## 1. Unidades

- **Resposta**: um texto devolvido por um modelo a um prompt. Identificada por condição, modelo, tipo de pergunta, variante, duração, língua e repetição.
- **Item**: um lugar referido na resposta. Cada item tem uma posição (ordem de aparecimento), um nível de recomendação e um nível geográfico.

## 2. Nível de recomendação (`nivel`)

| Código | Definição | Exemplos |
|---|---|---|
| `destino` | Item principal da recomendação: cada entrada de uma lista numerada ou com marcadores de primeiro nível; cada título de secção dedicado a um lugar; cada paragem ou base de um dia num roteiro. | "3. Évora", "## Dia 4: Porto", "Lagos" numa lista de 10 |
| `atracao` | Lugar referido dentro de um destino principal: monumento, bairro, praia, museu, miradouro, aldeia visitada em excursão de um dia a partir da base, restaurante. Tem `destino_pai`. | "Torre de Belém" dentro de Lisboa; "Monsaraz" dentro de Évora se for excursão |
| `titulo` | Título da resposta, frase introdutória ou de fecho, rubrica sem lugar. Não conta para nada. | "10 lugares a visitar em Portugal", "Dicas práticas", "Itinéraire de 7 jours" |

Regras de desempate:
- Num roteiro, o destino do dia é o lugar onde o viajante dorme ou passa a maior parte do dia. Uma excursão de um dia a partir da base (por exemplo, Sintra a partir de Lisboa) é `destino` se ocupar um dia inteiro com cabeçalho próprio, e `atracao` se for referida dentro do dia de outra base.
- "Lisboa e Sintra" num só item são dois destinos.
- Um lugar repetido na mesma resposta conta uma vez nas medidas de destino e todas as vezes na medida de menções.

## 3. Nível geográfico (`nivel_geo`) e atribuição de NUTS III

A NUTS III é sempre derivada de forma determinística, nunca pedida ao modelo extrator. O extrator só identifica o nome do lugar e o município.

| Código | Definição | Atribuição |
|---|---|---|
| `municipio` | Lugar dentro de um único município (cidade, vila, aldeia, praia, monumento, parque urbano). | Município → NUTS III pela tabela `data/municipios_nuts3_2024.csv` (308 municípios, NUTS 2024). |
| `macro_1nuts` | Marca territorial que abrange vários municípios mas uma só NUTS III (Algarve, Madeira, Açores, Serra da Estrela, Arrábida, Ria Formosa, Montesinho). | A NUTS III única. Conta como destino normal; a percentagem destes itens é reportada. |
| `macro` | Marca territorial que abrange mais de uma NUTS III (Vale do Douro, Peneda-Gerês, Alentejo, Costa Vicentina, Minho, Trás-os-Montes, Costa de Prata, Aldeias do Xisto, Alqueva, etc.). | Tabela `data/macro_destinos.csv`: NUTS III principal e NUTS III abrangidas. A análise principal usa a principal; sensibilidade com alocação fracionária por igual e com exclusão. |
| `municipio_desconhecido` | Município não reconhecido na tabela. | Fica com a NUTS III do extrator se válida; vai para revisão manual. Meta: menos de 0,5% dos itens. |
| `titulo` | Ver secção 2. | Sem NUTS III. |

Regras:
- Os itens com `existe = false` são excluídos das medidas e contados para a taxa de erro, mas a marcação automática não é fiável: na verificação humana, confirmar sempre. Lugares em Espanha recomendados em respostas sobre Portugal são `existe = false` com nota "fora de Portugal", e não alucinações.
- Caves do vinho do Porto em Vila Nova de Gaia são `atracao` de Porto (AM Porto), não Douro.
- "Pinhão" é Alijó (Douro). "Monsaraz" é Reguengos de Monsaraz (Alentejo Central). "Fátima" é Ourém (Médio Tejo). "Ericeira" é Mafra (Grande Lisboa). "Furnas" e "Sete Cidades" são Povoação e Ponta Delgada (Açores). "Comporta" é Alcácer do Sal (Alentejo Litoral).
- Municípios homónimos: Lagoa (Algarve ou Açores) e Calheta (Madeira ou Açores) desambiguam-se pelo contexto; sem contexto, Lagoa é Algarve e Calheta é Madeira, e regista-se nota.

## 4. Macro-destinos: lista de referência

Ver `data/macro_destinos.csv` (37 entradas, com expressões regulares em PT, EN, ES e FR, NUTS III principal, NUTS III abrangidas e nota de justificação). As decisões de maior consequência:

| Marca | Principal | Abrangidas | Porquê |
|---|---|---|---|
| Vale do Douro | Douro | Douro, Tâmega e Sousa | Baixo Corgo, Cima Corgo e Douro Superior estão na NUTS III Douro; o rio passa por Baião, Resende e Cinfães. |
| Peneda-Gerês | Cávado | Alto Minho, Cávado, Alto Tâmega e Barroso | A vila do Gerês é em Terras de Bouro (Cávado); a maior área do parque é no Alto Minho. Decisão arbitrária, por isso há sensibilidade. |
| Alentejo | Alentejo Central | as 4 NUTS III do Alentejo | Évora é a capital e o destino canónico. Só a menção isolada; "Alentejo Litoral" e "Costa Alentejana" vão para Alentejo Litoral. |
| Costa Vicentina | Alentejo Litoral | Alentejo Litoral, Algarve | Odemira é Alentejo Litoral; Aljezur e Vila do Bispo são Algarve. No piloto, o extrator pôs 69 destas em Baixo Alentejo, que está errado. |
| Serra da Estrela | Beiras e Serra da Estrela | só esta | O parque natural está inteiramente nesta NUTS III. |

## 5. Noites atribuídas nos roteiros

- Cabeçalhos de dia reconhecidos: "Dia N", "Day N", "Día N", "Jour N", com ou sem intervalo ("Dias 1 a 3", "Days 1–2").
- O destino do dia é o primeiro `destino` cujo nome aparece no cabeçalho; se não houver, o primeiro que aparece no texto do dia; se não houver, o destino do dia anterior (continuação).
- Intervalos contam o número de dias do intervalo. O total de dias por resposta é normalizado a 1.
- Respostas sem pelo menos 3 cabeçalhos de dia não entram na medida de noites e são contadas.
- Na recolha v2, as variantes 2 e 3 do roteiro pedem explicitamente onde dormir cada noite, para reduzir a ambiguidade.

## 6. Exclusões (pré-registadas)

- Respostas vazias, cortadas (`finish_reason = length`) ou que recusem responder: excluídas e contadas.
- Respostas em que mais de metade dos destinos principais fica fora de Portugal: excluídas e contadas.
- Itens `titulo`: excluídos.
- Itens `existe = false` confirmados: excluídos das medidas, contados na taxa de erro.
- Açores e Madeira: incluídos na análise principal; análise de sensibilidade sem ilhas.

## 7. Verificação humana

Dois exercícios, dois codificadores (NA e AMS), cópias separadas, sem consulta mútua:

- **Exercício A, recall** (`data/verificacao_recall.xlsx`, 30 respostas estratificadas por modelo × tipo): listar os destinos principais a partir do texto, sem ver a extração. Métricas: recall e precisão do extrator contra cada codificador; Jaccard entre codificadores por resposta. Meta: recall ≥ 0,95.
- **Exercício B, precisão** (`data/verificacao_precisao.xlsx`, 96 respostas, cerca de 1 000 linhas): para cada linha extraída, três juízos s/n: destino principal, município, NUTS III. Métricas: exatidão por dimensão, acordo simples e kappa de Cohen por dimensão. Meta: exatidão ≥ 0,95 em município e NUTS III; acordo ≥ 0,90.
- Divergências entre codificadores resolvem-se por discussão depois do cálculo das métricas, e a decisão fica registada na coluna nota. As métricas reportadas são as anteriores à discussão.
- Cálculo: `python metricas_verificacao.py --recall <ficheiros> --precisao <ficheiros>`.

## 8. Registo de alterações

| Data | Alteração | Motivo |
|---|---|---|
| 2026-11-05 | v2: NUTS III derivada do município; níveis geográficos; macro-destinos; títulos; noites nos roteiros; verificação em dois exercícios | Revisão crítica do piloto (ver `revisao_fable_tema_A.md`) |
