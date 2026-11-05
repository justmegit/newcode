# Briefing para o agente local (Chrome, sessão LinkedIn do super admin)

Contexto: Maria Pessoa (Blue Serenity, mariapessoa@blueserenity.pt) tem de gerir
publicações e anúncios da página ISQ España (linkedin.com/company/106941249).
Adicioná-la como Content admin falha com "This member could not be added as a page
admin. Ask the member to verify their account". Não há regra publicada do LinkedIn
que exija admins verificados; é um bloqueio de confiança sobre a conta nova dela.

Regras: nunca iniciar verificação de identidade (Persona, CLEAR, passaporte,
selfie). Nunca comprar nada (Premium Company Page, Premium, anúncios). Não alterar
DNS. Não desligar nem religar canais no Postiz. Em cada passo, registar o texto
exato de erros e tirar captura.

## Tarefas por ordem

1. ISQ España, vista de admin > Settings > Manage admins.
   a. Pending admin requests: se houver pedido da Maria, Assign role > Content admin.
      Registar se aceita ou dá erro.
   b. Se não houver pedido, Add admin > Maria Pessoa > Content admin. Registar o
      erro exato e se há link "verify" com destino (anotar o URL, não seguir).
2. Blue Serenity, vista de admin > Settings. Procurar "Verification controls".
   a. Se não existir: reportar e parar este ponto.
   b. Se existir só "Ask about verifying": clicar, reportar.
   c. Se existir "Request verification": preencher nome legal, site
      https://blueserenity.pt, morada. Quando pedir prova de posse do site, copiar
      o valor TXT `linkedin-site-verification=...` e reportar. Não confirmar ainda.
      O utilizador adiciona o TXT no Cloudflare (ver docs/cloudflare-dns-linkedin.md)
      e depois confirma-se no LinkedIn.
   d. Se a página já estiver "Verified": Verification controls > + Add domains >
      blueserenity.pt > guardar. Reportar.
3. Campaign Manager (campaignmanager.linkedin.com), conta de anúncios do ISQ ES.
   a. Account settings: confirmar que a página associada é ISQ España.
   b. Manage access > Add user > Maria Pessoa > papel Campaign Manager. Reportar
      se o convite sai ou se dá o mesmo erro de verificação.
4. Postiz: https://postiz2.blueserenity.pt > Settings > Teams > Add member >
   mariapessoa@blueserenity.pt (papel User ou Admin). Reportar se diz "invitation
   sent" e se existe provider de email configurado (Settings/Email ou .env do
   servidor). Se não houver email, reportar o link de convite se a UI o mostrar.
5. Postiz > Analytics > ISQ España: confirmar que mostra dados (seguidores,
   impressões). Reportar.

## Reportar no fim

- Resultado de cada ponto com texto exato dos erros.
- Valor TXT do ponto 2c, se obtido.
- Se Verification controls não existir na página Blue Serenity.
- Estado do convite da Maria no Campaign Manager e no Postiz.
