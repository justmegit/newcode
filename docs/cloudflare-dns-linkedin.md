# DNS no Cloudflare para a verificação da página Blue Serenity no LinkedIn

O LinkedIn prova a posse do site com um registo TXT no domínio. O valor exato só
aparece durante o pedido de verificação (página Blue Serenity > Settings >
Verification controls > Request verification). Copia-o de lá, não inventes.

## Registo a adicionar

| Tipo | Nome | Conteúdo | TTL | Proxy |
|------|------|----------|-----|-------|
| TXT | @ | linkedin-site-verification=VALOR_DADO_PELO_LINKEDIN | Auto | não se aplica |

Mantém os registos TXT já existentes no domínio (SPF, google-site-verification,
ppkey). Um domínio pode ter vários TXT na raiz.

Se o LinkedIn oferecer em alternativa uma meta tag ou ficheiro HTML, isso vai no
site blueserenity.pt e não no DNS. O TXT é a opção mais simples.

## Passos no Cloudflare

1. Entra em dash.cloudflare.com e escolhe o domínio blueserenity.pt.
2. Menu lateral: DNS > Records.
3. Botão "Add record".
4. Type: TXT. Name: @ (o Cloudflare mostra "blueserenity.pt"). Content: cola
   `linkedin-site-verification=...` completo, incluindo o prefixo. TTL: Auto.
5. "Save".
6. Confirma a propagação (normalmente minutos, o LinkedIn fala em até 48 h):
   abre https://dns.google/resolve?name=blueserenity.pt&type=TXT e procura a linha
   linkedin-site-verification. Ou no terminal: `dig TXT blueserenity.pt +short`.
7. Volta ao LinkedIn e clica em "Verify" / "Confirm". O estado fica "Pending" até
   o LinkedIn aprovar.
8. Depois de "Verified", em Verification controls: "+ Add domains" > blueserenity.pt.
   Só então a Maria pode verificar o local de trabalho por email.

## Estado atual do DNS (2026-11-05)

- MX: mail.blueserenity.pt (correio próprio).
- TXT: SPF (inclui outlook.com, google, ipzmarketing, mailersend),
  ppkey-..., google-site-verification=...
- Sem registo linkedin-site-verification: a página ainda não foi verificada.
