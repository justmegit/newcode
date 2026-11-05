# Guião de teste da Clara (12 mensagens)

Corre-se depois de qualquer alteração ao núcleo, com o inquilino `chr`. Data de referência dos dados de demonstração: semana de 8 de novembro de 2026 (ajustar `marcacoes.csv` quando a semana passar). Cada linha tem o que se envia, o que se espera e a ferramenta que deve ter sido chamada.

| # | Enviar (como cliente, número novo) | Esperado | Ferramenta |
|---|---|---|---|
| 1 | "Olá" | Identifica-se como Clara, secretária virtual do Centro Hípico da Ribeira, e pergunta em que pode ajudar | responder |
| 2 | Nota de voz: "quais são os horários ao sábado?" | Sábado 9h às 13h, aulas de 45 min; sem inventar horas de aulas concretas, ou lista das aulas de sábado | consultar_horarios ou só KB |
| 3 | "quanto custa a aula experimental?" | 25 €, obrigatória antes da inscrição, idade mínima 6; pede nome e idade | responder |
| 4 | "é para o meu filho Tomás, tem 9 anos, sábado às 11" | Verifica vagas; 11h está cheia; propõe 10h ou lista de espera | vagas |
| 5 | "pode ser às 10" | Repete o pedido numa frase (sábado 8 de novembro, 10h, Tomás, 9 anos, experimental) e pede confirmação; **não marca ainda** | nenhuma |
| 6 | "sim" | Marca; confirma com dia da semana e dia do mês; diz que manda lembrete na véspera; o que levar | marcar |
| 7 | "posso pagar a mensalidade em três vezes?" | Diz que vai perguntar ao Ricardo; no telemóvel do dono chega uma linha com "Respondo que sim?" | escalar |
| 8 | (do número do dono) "sim" | Fecha a escalação; o cliente recebe "O Ricardo confirmou…" no tom da Clara | fechar_escalacao |
| 9 | "fazem festas de aniversário?" | Não está na base: não inventa; escala ou diz que confirma com o Ricardo; marca `nao_soube` | escalar + responder(marcar_nao_soube) |
| 10 | (do número do dono, da app, para o cliente) "Olá Ana, sou o Ricardo, as festas são aos domingos" | Eco detetado; `humano_ate` definido; a Clara cala-se nessa conversa | nenhuma (estado) |
| 11 | (cliente) "e quanto custam?" | **Sem resposta da Clara** enquanto `humano_ate` estiver no futuro; evento registado | nenhuma |
| 12 | (do número do dono) "a partir de janeiro a aula de sábado das 10 passa para as 9h30" | Regista proposta em `kb_propostas`; responde ao dono "Anotado, fica ativo depois de validado"; nada muda na base | propor_kb |

Critérios de passagem: 12 de 12 com as ferramentas certas; nenhuma resposta acima de 600 caracteres; nenhuma afirmação fora da base; tempo de resposta abaixo de 10 s por mensagem (nota de voz abaixo de 20 s).
