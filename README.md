# Secretária Virtual by Blue Serenity

Produto da Blue Serenity (SPRINGBREEZE - UNIPESSOAL, LDA): uma secretária virtual por WhatsApp para pequenos negócios de serviços recorrentes (escolas de equitação, explicadores, ginásios, academias). Este repositório guarda o que é durável: documentação do produto, o núcleo técnico (prompts, ferramentas, esquema das tabelas) e os workflows n8n exportados. **Nunca contém segredos**: tokens, chaves e PINs vivem só nas variáveis de ambiente do Coolify.

## Estrutura

| Pasta | Conteúdo |
|---|---|
| `docs/00-estado-e-decisoes.md` | **Começar aqui.** Estado atual, IDs (não secretos), próximos passos e registo de decisões |
| `docs/01-oferta-e-preco.md` | Posicionamento, pacote, tabela de preços, economia unitária |
| `docs/02-folha-de-venda.md` + `.pdf` | Folha de venda de duas páginas para mostrar no telemóvel |
| `docs/03-guiao-demonstracao.md` | Demonstração de 5 minutos e a escola fictícia "Centro Hípico da Ribeira" (secretária Clara) |
| `docs/04-sessao-de-arranque.md` | Onboarding por cliente, de D0 a D37, com os dois modelos de arranque e as opções de número |
| `docs/05-arquitetura-tecnica.md` | Núcleo multi-cliente em n8n: módulos, tabelas, migração a partir da Vitória |
| `nucleo/prompt-sistema.md` | Prompt do cérebro e prompt do dono |
| `nucleo/ferramentas.json` | Ferramentas (function calling) do cérebro e do prompt do dono |
| `nucleo/tabelas/` | Esquema das 12 tabelas em CSV, com o piloto (`lrc`) e a demonstração (`chr`) |
| `nucleo/guiao-teste-clara.md` | As 12 mensagens que validam qualquer alteração ao núcleo |
| `workflows/` | Workflows n8n exportados em JSON, sem credenciais |

## Estado (05/11/2026)

Piloto: Lisbon Riding Club, secretária Vitória, em produção na Evolution API (número 938). Cloud API ligada pela YCloud no número 926, à espera de aprovação do nome de apresentação e do corte. Detalhe em `docs/00-estado-e-decisoes.md`.
