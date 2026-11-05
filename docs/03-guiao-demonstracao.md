# Guião da demonstração de 5 minutos (v1)

Objetivo: o dono vê a secretária a responder-lhe **a ele**, no telemóvel dele, em menos de 5 minutos, e sai com a sessão de arranque marcada. Nada de slides, nada de portátil.

## Antes de ir

- Número de demonstração da Blue Serenity com a secretária "Clara" da escola fictícia **Centro Hípico da Ribeira** (base de conhecimento na secção 4), no segundo canal grátis da YCloud. Enquanto não existir, usar o número 938 da Vitória com a base do Lisbon Riding Club, com autorização do Mike, ou o plano B da secção 3.
- O telemóvel do Alexandre com o número de demonstração gravado como "Clara · Centro Hípico" e um QR impresso no verso da folha de venda que abre a conversa (`https://wa.me/351XXXXXXXXX?text=Olá`).
- Três capturas de ecrã impressas ou no telemóvel (plano B).
- Folha de venda em PDF no telemóvel e duas impressas.

## 1. Guião, minuto a minuto

**0:00 · Abertura (30 s).** "Posso mostrar-lhe uma coisa no seu telemóvel? Leva cinco minutos." Lê o QR ou envia o contacto. Não explicar nada ainda.

**0:30 · Primeira pergunta (1 min).** Pedir ao dono que **mande uma nota de voz** como se fosse um cliente: "pergunte-lhe os horários de sábado, ou quanto custa uma aula experimental". A resposta chega em segundos, em texto. Deixar o dono ler em silêncio. Depois: "Isto é a Clara. Só sabe o que está na folha que o dono do centro nos deu. Era assim consigo: a sua, com o seu nome, só sabe o que você nos disser."

**1:30 · Marcação (1 min).** "Agora peça-lhe para marcar uma aula experimental para o seu filho no sábado." A Clara pergunta nome e idade, propõe um horário com vaga, confirma e diz que vai mandar um lembrete na véspera. Ponto a sublinhar: "Ela só marca onde há vaga e dentro das suas regras. Se a aula é às 10h e só aceita até 6 cavaleiros, ela sabe."

**2:30 · Escalação (1 min).** "Pergunte-lhe uma coisa que ela não pode saber: se pode pagar em três vezes, ou se o cavalo do João está melhor." A Clara responde: "Isso é com o Ricardo, vou perguntar-lhe e já lhe digo." No telemóvel do Alexandre chega, à vista do dono, a mensagem de escalação: "O [nome do dono] pergunta se pode pagar em 3 vezes. Respondo que sim?" Alexandre responde "sim" e a Clara fecha a conversa com o dono. Frase-chave: **"Foi isto que o incomodou. Uma linha. Um sim."**

**3:30 · O resumo (30 s).** Mostrar no telemóvel do Alexandre o resumo semanal de exemplo (secção 2). "Isto chega-lhe à segunda de manhã. Quem faltou, quem está por pagar, o que ela não soube responder. É tudo o que tem de ler."

**4:00 · Preço e fecho (1 min).** Abrir a folha de venda no telemóvel na página dos preços. Dizer só duas frases: "Uma rececionista a meio tempo custa mais de 700 € e falta. Isto são 89 € por mês e nos primeiros cinco negócios 49 € para sempre, sem arranque." Depois a pergunta de fecho: **"Quer que a sua comece a atender na próxima semana? Preciso de 30 minutos consigo para os horários e as regras, e 15 minutos ao seu lado para ligar o número. Quando lhe dá jeito?"**

Se hesitar: não insistir no preço, oferecer a conversa de 30 minutos como passo seguinte sem compromisso. Nunca prometer chamadas de voz nem datas para funcionalidades que não existem.

## 2. Resumo semanal de exemplo (guardar como mensagem no telemóvel)

```
Bom dia, Ricardo. Semana de 27 out a 2 nov no Centro Hípico:

Aulas: 42 dadas, 3 canceladas com antecedência, 2 faltas sem aviso (Matilde S., Pedro A.).
Novos: 1 aula experimental marcada (sábado 10h, Tomás, 9 anos).
Mensalidades de novembro: 31 pagas, 6 por pagar. Já lembrei 4; os pais da Inês e do Duarte pediram para falar consigo.
Não soube responder a 2 perguntas: "fazem festas de aniversário?" e "há desconto para irmãos?". Diga-me o que responder e passo a saber.
Tenha uma boa semana.
```

## 3. Plano B: sem rede ou sem a demonstração a funcionar

Nunca pedir desculpa pela tecnologia. Dizer "deixe-me mostrar-lhe como foi na semana passada com outro cliente" e passar três capturas de ecrã, pela mesma ordem do guião: pergunta por nota de voz e resposta; marcação confirmada; escalação com o "sim" e a resposta final. Depois o resumo semanal e o fecho iguais.

As capturas fazem-se a partir das conversas de teste com a Clara, com nomes fictícios. Tirá-las assim que a Cloud API estiver a funcionar.

## 4. Base de conhecimento da escola fictícia (para montar a Clara)

Centro Hípico da Ribeira, dono Ricardo. Desenhada para a demonstração correr nos quatro passos. Formato pensado para a tabela `kb_escola` (tema, pergunta, resposta); adaptar ao esquema real.

| Tema | O que a Clara sabe |
|---|---|
| Horários | Terça a sexta 16h às 20h; sábado 9h às 13h; domingo e segunda fechado. Aulas de 45 min em grupo, 30 min individuais. |
| Grupos | Iniciação (6 a 10 anos), Jovens (11 a 16), Adultos. Máximo 6 cavaleiros por aula de grupo. |
| Preços | Aula experimental 25 €. Mensalidade 1 aula/semana 95 €, 2 aulas/semana 160 €. Aula individual 40 €. Seguro anual 30 €. |
| Mensalidades | Pagas até dia 8 por transferência ou MB WAY. Lembrete no dia 5 e no dia 9. |
| Marcações | Marcar com 24 h de antecedência; cancelar até 12 h antes sem perder a aula; remarcar na mesma semana se houver vaga. |
| O que levar | Calças compridas, botas com salto pequeno ou ténis fechados; capacete emprestado pelo centro. |
| Morada | Estrada da Ribeira 12, Sintra. Estacionamento à porta. Ponto de referência: depois da escola primária, à esquerda. |
| Idade mínima | 6 anos. Abaixo disso, passeio de pónei ao sábado, 15 €. |
| Chuva | Com chuva forte há picadeiro coberto; aulas mantêm-se salvo aviso. |
| Feriados | Fechado a 1 nov, 1 dez, 8 dez, 25 dez, 1 jan. |
| Escala sempre | Pagamentos fracionados ou descontos; estado de saúde de cavalos ou alunos; reclamações; pedidos para falar com o Ricardo; qualquer coisa fora desta lista. |
| Tom | Trata por "você", simpática, frases curtas, nunca inventa, nunca promete o que não está na lista. |

Agenda fictícia para a demonstração de marcação: sábado 10h Iniciação com 4 de 6 vagas ocupadas; sábado 11h Iniciação cheia; sábado 12h Jovens com 2 vagas. Assim a Clara propõe as 10h e, se o dono insistir nas 11h, oferece lista de espera.

## 5. O que falta para a demonstração estar pronta

1. Segundo canal na YCloud (plano grátis tem 2) com um número da Blue Serenity; o Embedded Signup já se sabe fazer (feito a 05/11 para o 926).
2. Montar a Clara: copiar o workflow da Vitória, trocar a base de conhecimento pela tabela acima, agenda fictícia em Data Table.
3. Gravar o contacto, fazer o QR, tirar as três capturas do plano B.
4. Ensaiar o guião duas vezes com alguém que não seja do ramo e cronometrar.
