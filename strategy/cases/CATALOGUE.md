# Catálogo de casos (v4, 24 out 2026) — documento interno

Substitui a organização por cliente. **Uma peça = um cliente + um desafio.** Desafios parecidos em
clientes diferentes são casos diferentes. Este ficheiro é interno: é o único sítio onde o cliente
real aparece ao lado do caso.

## Regras (decididas pelo Alexandre a 24 out)

1. **Anonimato sempre**, mesmo com autorização: as administrações mudam e o texto não deve ter de ser
   reescrito. O descritor não pode identificar o cliente em 5 pesquisas. Os casos nunca remetem uns
   para os outros («the same installer» está proibido).
2. **Um desafio por caso**, dito como um diretor-geral o diria. Teste: um leitor sem contexto resume o
   desafio numa frase sem «e».
3. **De desafio a processo.** A tecnologia e a AI aparecem dentro da decisão, como meio, nunca como título.
4. **Números:** um valor absoluto só entra se for credível a qualquer escala. Se não for, usa-se um
   rácio. Se o rácio também for fraco, mede-se o processo: tempo, dono, cadência.
5. **O que falhou entra sempre**, mas ao nível de quem lê, que é um diretor-geral, financeiro ou de RH.
   Entram os desafios além do previsto: mudança de cultura e adoção, dependências de terceiros,
   variações da tecnologia e das fontes. Não entram bugs, duplicados nem detalhes de implementação.
   Antes de escrever um fracasso, confirmar com o Alexandre que ele aconteceu: o «julho nunca chegou
   ao cliente» era falso, porque o envio foi manual a partir do comunicacion@. Fica como «What did not
   work» quando é um fracasso, e como «What was harder than planned» quando é um desafio. Há casos
   inteiros sobre fracassos (o 04), e o ensaio dá depois a leitura de fundo.
6. **Nenhum número sem linha num registo de provas.** O `check_v4.py` confirma-o.

## Estrutura de cada caso

Desafio (a frase do diretor-geral) → Context → What was underneath → The decision → Process, and who
runs it → Result → What did not work → Three questions to ask your team tomorrow.

## Mapa

| # | Ficheiro | Desafio | Cliente (interno) | Camada | Estado |
|---|---|---|---|---|---|
| 01 | `case-01-scenarios-not-a-budget.md` | «Quanto devemos investir em Espanha, e o que compra cada nível?» | SOGEM | Transform | `[FILL]` em execução e resultado |
| 02 | `case-02-what-the-algorithm-learns-from.md` | «As plataformas dizem que corre bem e eu não sei o que compro.» | Conceptance | Assess | pronto para juízes |
| 03 | `case-03-what-a-lead-is-worth.md` | «Cortamos ou reforçamos a media?» | Conceptance | Assess / Advise | pronto para juízes |
| 04 | `case-04-leads-nobody-answered.md` | «Precisamos de mais leads.» (fracasso: não precisavam) | Conceptance | Assess | pronto para juízes |
| 05 | `case-05-claims-you-can-defend.md` | «A publicidade pode dizer isto?» | Conceptance | Transform | pronto para juízes |
| 06 | `case-06-a-hire-or-a-process.md` | «Preciso de substituir a pessoa da comunicação.» | ISQ España | Transform | `[FILL]` no resultado |
| 07 | `case-07-from-clipping-to-market-analysis.md` | «Recebemos um clipping todos os meses e nunca fazemos nada com ele.» | ISQ España | Transform | `[FILL]`: decisão tirada do relatório |
| 08 | `case-08-authentic-content-inside-the-rules.md` | «Queremos AI no conteúdo sem violar o AI Act nem expor clientes.» (absorve o antigo 08, afirmações) | ISQ España | Transform | pronto para juízes |
| 09 | `case-09-a-catalogue-nobody-could-update.md` | «As vendas online caíram. Vale a pena investir num canal que encolhe?» | ISQ Academy | Transform | pronto para juízes |
| 10 | `case-10-the-next-sale-is-in-the-data.md` | «Quem devíamos estar a contactar e não estamos?» | ISQ Academy | Transform | `[FILL]` no resultado aos 90 dias |
| 11 | `case-11-recruitment-as-a-routine.md` | «Cada vaga começa do zero, e as difíceis vão para uma consultora.» | ISQ España | Transform | `[FILL]`: contratações e tempo de preenchimento |
| — | caso 3 antigo, «long game» | — | por escolher | Advise | sem cliente: decisão do Alexandre |
| — | `essay-ai-built-it.md` | ensaio | Conceptance | tese | só depois do fim da relação |

## Decisões de 24 out (2.ª ronda)

- O 07 passa a ser a passagem do clipping à análise setorial, com a contratação pública como farol. O clipping manual nunca deu origem a nenhuma ação (Alexandre).
- O antigo 08 (afirmações) foi integrado no novo 08 (governação do conteúdo), por ser uma camada desse modelo.
- «LLM-agnóstico» passa a «trocar o modelo de texto é uma configuração», e «cumpre o AI Act» passa a «desenhado para». A troca de modelo nunca foi feita, o modelo de imagem está fixo e a marcação das imagens (A9) está em aberto.
- O 11 (recrutamento) é escrito como capacidade: 19 perfis recorrentes × 7 delegações, contra as cerca de 12 vagas/ano da proposta de 2 fev. O lote está em aprovação. As candidaturas (30-40) são uma contagem do Alexandre no backoffice, que eu não verifiquei.
- O 06 ficou só com a questão contratação versus processo.

## Site (30 out)

Decisão do Alexandre: os 11 casos vão para o site, em cartões curtos, agrupados por tema. Sem cliente nomeado. O texto dos cartões está em `site/copy.md` §5, e o `check_v4.py` também o verifica.

## Avaliado e não escrito (1 nov)

- **A migração do CRM da Conceptance (de HubSpot para Odoo).** Não é caso, por decisão minha com o critério do Alexandre («só se trouxer valor»). A ação foi do cliente, não há resultado conhecido, lê-se como um cliente que abandonou o que foi montado, e a relação ainda está ativa. Reavaliar daqui a 12 meses: se a mudança de ferramenta não tiver mudado o processo, é um bom argumento para um ensaio.

## O que saiu e porquê

- **A página de LinkedIn da ISQ España (visitas, seguidores, o post do inspetor).** Os números absolutos
  são pequenos e os rácios assentam em contagens de um só dígito. Um diretor-geral não compra isto.
- **Os aniversários (38 envios falhados).** São a prova de uma falha silenciosa, mas o assunto é menor.
  No caso 06 fica a falha, sem o número.
- **O envio de email rejeitado por DNS (Conceptance).** É um desafio à parte e pequeno demais.
- **«Construir antes de vender», os 30/40/30 e a garantia (ISQ Academy).** Falam de como a Bluewright
  vende, não do desafio do cliente. Servem para uma proposta, não para um caso.
- **As 40 horas do Código do Trabalho e o benchmark do site principal.** O primeiro aponta o país e o
  segundo expõe o cliente.

## Descritores públicos

| Cliente | Descritor |
|---|---|
| SOGEM | a building-products manufacturer from northern Europe, part of an industrial group |
| Conceptance | a premium outdoor-living installer, authorised partner of a European manufacturer |
| ISQ España | the Spanish subsidiary of a European technical-services group |
| ISQ Academy | a technical training provider running a branded academy for a supplier's reseller and installer network |
