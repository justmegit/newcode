# Estado do produto e registo de decisões

Ficheiro vivo. Sem credenciais, nunca. Última atualização: 05/11/2026.

## Estado a 05/11/2026

| Item | Estado |
|---|---|
| Bloqueio da Meta | **Resolvido** a 05/11. WABA nova ativa no portfólio "Secretária Virtual" `388612488295788`. O portfólio não estava marcado; o problema era a WABA antiga `28321972994162691`, que fica abandonada em "Revisão em curso" (tal como a duplicada `1405854064471551`). |
| Plataforma | **YCloud**, plano grátis (2 canais, API + webhooks, sem margem sobre a Meta, carteira pré-paga; saldo 0,50 $). App YCloud `2892949377516980` subscrita aos webhooks. |
| WABA nova | `1648511630107490` "Secretária Virtual - YCloud", `can_send_message: AVAILABLE`. |
| Número 926 | `phone_number_id` `1436224236241306`, CONNECTED, VERIFIED, CLOUD_API, TIER_250. Envio LIMITED até a Meta aprovar o nome de apresentação "Lisbon Riding Club" (`name_status NON_EXISTS`). |
| Número 938 (Mike) | Continua na Evolution. Não se toca até a Vitória estar testada no 926. |
| Vitória | Em produção na Evolution. Ligação à YCloud por fazer (passos abaixo). |
| Templates | `escalacao_aviso` e `onboarding_pergunta_utilidade` têm de ser recriados na WABA nova, pela YCloud. |
| Monitor `O0Q9FqGuDEJQ8RTA` | Ainda lê o `phone_number_id` antigo, que já não existe. Corrigir. |
| Documentos do produto | 01 oferta e preço · 02 folha de venda (md + pdf) · 03 guião de demonstração · 04 sessão de arranque · 05 arquitetura técnica. Todos atualizados a 05/11 para a via YCloud e para a coexistência como predefinição. |
| Núcleo (pasta `nucleo/`) | `prompt-sistema.md` (prompt do cérebro + prompt do dono) · `ferramentas.json` (10 ferramentas + 2 do dono) · `tabelas/` (12 CSV com esquema, piloto e demonstração) · `guiao-teste-clara.md` (12 mensagens). |

## Próximos passos técnicos (fase 1 da arquitetura)

1. Pôr saldo na carteira da YCloud.
2. Recriar os dois templates UTILITY na WABA nova, pela YCloud; esperar aprovação.
3. Gerar a chave de API da YCloud e guardá-la em `YCLOUD_API_KEY` no Coolify.
4. Adaptar o gateway `gwKc8toftwSRD7G8` (envio por `POST /v2/whatsapp/messages`) e o adaptador `GpJxyM42Psl8Zy7c` (webhook `whatsapp.inbound_message.received`, verificar `YCloud-Signature`, descarregar média com a chave). Criar o endpoint de webhook na YCloud a apontar para o n8n.
5. Atualizar o monitor com o `phone_number_id` novo e as env vars `META_*`; acrescentar o saldo da carteira ao monitor.
6. Teste com o número do Alexandre. Depois corte pela env var `EVOLUTION_URL`. Evolution e 938 ficam ligados até o teste passar.
7. Segundo canal grátis da YCloud: a Clara de demonstração.

## Decisões

| Data | Decisão | Porquê |
|---|---|---|
| 05/11 | Produto chama-se "Secretária Virtual by Blue Serenity"; cada instância tem nome próprio | O público entende "secretária"; o nome do portfólio já é esse |
| 05/11 | Tabela v1: base 350 € + 89 €/mês; cobranças +30 €; presença 450 € + 40 €; Solo 190 € + 49 €; fundador 0 € + 49 €/mês para 5 clientes | Âncora na rececionista a part-time; validar em 3 conversas antes de imprimir |
| 05/11 | Foco em escolas de 50 a 200 alunos nos primeiros 6 meses | Arranque custa o mesmo tempo que um Solo |
| 05/11 | Cliente nunca põe cartão: taxas Meta pela carteira YCloud da Blue Serenity | Resolvido pela via YCloud |
| 05/11 | Presença digital: até 2 publicações/mês incluídas; extra em pacote de 12 por 120 € | Publicações são o que mais consome tempo |
| 05/11 | Mike gratuito até estabilizar na Cloud API; depois preço de fundador | Piloto e embaixador |
| 05/11 | Pagamentos fase 2: fornecedor decidido ao primeiro pedido de links (Ifthenpay, EuPago, Stripe) | Sem cliente a pedir, não vale a hora |
| 05/11 | Plataforma YCloud para o piloto e a demonstração; ao terceiro número, Chakra (favorita) ou YCloud paga. Cloud API direta excluída | A coexistência só existe em Tech Providers aprovados; YCloud grátis até 2 canais |
| 05/11 | Número: coexistência no número atual do negócio é a predefinição; híbrido (SIM dedicado + app no telemóvel do dono) se o número for misto; dedicado puro só se o dono não quiser ver nada | Sem mudança de número para os clientes do negócio e o dono vê tudo na app |
| 05/11 | Onboarding: Modelo 1 (tudo no portfólio Blue Serenity, cliente só confirma o QR) é o predefinido **se** a Meta aprovar o nome "Lisbon Riding Club"; senão Modelo 2 (portfólio do cliente + parceiro) | O Modelo 1 é o único em que o cliente não toca na Meta |
| 05/11 | Arquitetura: um núcleo multi-cliente em n8n, formato interno neutro, LLM com ferramentas, base inteira no prompt, sem painel para o dono | 30 cópias de 62 nós não se mantêm |

## Hipóteses em aberto

- A Meta aprova um nome de apresentação de outro negócio numa WABA da SPRINGBREEZE? Veredicto do 926 decide o modelo de onboarding.
- Ligar coexistência a um número já registado na Cloud API (o 926) sem desregistar: possível? Perguntar à YCloud antes de pôr a app no telemóvel do Mike.
- A YCloud reencaminha os ecos do dono em coexistência? A documentação diz que as mensagens da app aparecem no histórico da API; confirmar no webhook antes de depender disso.
