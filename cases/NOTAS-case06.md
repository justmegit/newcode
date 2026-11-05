# Caso 6, ISQ Academy (Academia RubisGás): notas para o Alexandre

Rascunho v1, de 24 out 2026. Segue o método da Bluewright (ver `strategy/cases/HANDOFF.md`): registo de provas, rascunho, juiz numérico e, depois, um memorando adversarial.

## Ficheiros

| Ficheiro | O que é |
|---|---|
| `case-06-the-catalogue-nobody-could-sell.md` | O caso, em inglês e no formato dos casos 4 e 5. Inclui a versão para LinkedIn |
| `evidence-ledger-case06.csv` | 20 afirmações, cada uma com numerador, denominador, fonte, data, confiança e proveniência |
| `build_ledger_case06.py` | Gera o registo |
| `check_case06.py` | Juiz 1: confere os rácios e verifica que cada número do texto tem linha no registo. **Passa** |

Para correr: `python -I build_ledger_case06.py` e depois `python -I check_case06.py`.

## Ângulo escolhido

O caso não é sobre a loja nova. É sobre um catálogo que deixou de se vender porque ninguém o conseguia manter vivo, e sobre o histórico de inscrições, que passou de lixo a lista de pessoas a contactar.

Mantém as três ideias de negócio do projeto:
- a plataforma foi construída antes de ser vendida, por isso o cliente comprou uma entrega e não uma promessa;
- foram aceites todas as proteções que o cliente pediu, mas com a redação feita por nós;
- o SAP ficou fora do âmbito, por escrito.

## Números recalculados a partir dos dados brutos (não da proposta)

As vendas foram consultadas na base de dados de produção a 24/10:
- 2025 ficou 60% abaixo de 2024;
- de 1/1 a 20/7/2026, as vendas ficaram 57% abaixo do mesmo período de 2025.

Os números da proposta (11.800 €, 4.700 € e 1.600 €) conferem, mas sem IVA.

**Atenção:** entre 21/7 e 21/10/2026 o site antigo faturou 5,7 vezes mais do que no mesmo período de 2025, muito por causa do curso de Évora. Isto aconteceu **antes** da plataforma nova, por isso não pode ser atribuído a ela. O caso não o faz.

## Decisões que são tuas (bloqueiam a publicação)

1. **Resultado aos 90 dias (`[FILL]`)**: data proposta 22/01/2027. Métricas:
   - faturação online face ao mesmo trimestre de 2025;
   - inscrições vindas de contactos do Radar;
   - edições publicadas pela equipa sem pedir apoio;
   - encomendas corrigidas depois da venda.

   O plano da 2.ª vaga diz que este caso não se publica sem dados de antes e depois. Mantém-se.
2. **Nomes**: o ISQ aparece nomeado (é público e está permitido no `CLAUDE.md`). A RubisGás aparece como «a gas distribution brand». Nomear a marca exige autorização escrita da Joana ou da Paula Fiúza. Quem aprova a nomeação do ISQ?
3. **Só rácios?** Segui a regra mais estrita: não há euros em valor absoluto, nem o preço do projeto. Ficaram três números de volume (47 e cinco plugins, 23 lugares, 31 empresas), que não revelam a faturação. Confirma se a regra «só rácios» também se aplica a clientes nomeados (é a pergunta 10 do plano).
4. **«What did not work»** inclui dois erros meus, descritos sem dramatismo: as 35 encomendas expiradas por engano e o Radar vazio em produção. Dão credibilidade, mas decide se ficam.

## Juízes que faltam

- **Juiz 2, memorando adversarial** (diretor financeiro cético ou short seller), feito por um agente separado e sem o contexto deste projeto. Posso lançá-lo se pedires.
- **Juiz 3**: como o cliente é nomeado, a pesquisa de reidentificação é substituída pela **aprovação escrita do ISQ**.
- **Juiz 4, 5 leitores do público-alvo**: precisa dos nomes. Critério: pelo menos 3 em 5 marcariam uma conversa.

## Corrigido em produção enquanto recolhia as provas

- **35 encomendas antigas** não pagas foram marcadas como «Expirada» na madrugada de 23/10 pela tarefa automática. Foi efeito da ligação do histórico (plugin 0.8.4). Repus as 35 em «Aguarda confirmação de pagamento», com uma nota em cada uma, e não saiu nenhum e-mail. O plugin 0.8.5 impede que se repita.
- **Radar vazio em produção**: os pares de renovação e progressão e as validades só tinham sido definidos no site local, e a reparação do histórico nunca tinha corrido em produção. Ficou reposto: 30 renovações (todas caducadas), 31 progressões e 55 formandos abaixo das 40 horas, em 31 empresas.

## v2 (24 out), depois do memorando adversarial e das tuas decisões

- **Resultado:** publica-se a viragem: a venda cruzada deixou de depender de memória e folhas de cálculo e passou a ser uma lista permanente, atualizada a cada venda. O resultado comercial mede-se mais tarde, contra uma base acordada com o cliente. Já não bloqueia a publicação.
- **Diagnóstico** («a procura não desapareceu»): passa a ser a leitura da própria equipa, e não um dado. Verifica-se mais tarde.
- **Radar:** já não se diz «no dia do lançamento». O Radar aparece no resultado como «na primeira semana», e a falha dos primeiros dias está em «What did not work», com a causa: o histórico arquivado ainda não estava ligado às edições novas.
- **Números:** saíram os 57% (seletivos), os 95% do preço do projeto (potencial) e o «terço da faturação do ano» (revelava a escala). Os «três dias» passaram a «under 48 hours».
- **Falhas antigas:** saem sem dono. Retirei a frase do servidor por corrigir e a do projeto anterior que falhou por causa da integração com a faturação.
- **Outros problemas importantes já tratados:** a lei das 40 horas tem a ressalva «counting only hours done at the academy», a adoção já não é afirmada, e o demo é descrito como «on the client's own catalogue».
- **Por resolver:** a aprovação escrita do texto pelo ISQ (substitui o juiz 3), a decisão de nomear a marca parceira, e os 5 leitores (juiz 4). O memorando adversarial da v1 está em `judges/redteam-case06.md`. A v2 ainda não teve uma segunda volta.
