# LinkedIn ISQ ES: acesso da Maria Pessoa sem verificação biométrica

Página: linkedin.com/company/106941249 (ISQ España). Data: 2026-11-05.

## O que o LinkedIn diz de facto (páginas de ajuda oficiais)

- Não existe nenhuma regra publicada que exija membro verificado para ser admin de página.
  A ajuda "Add, edit or remove admins" só diz que o membro pode ter de seguir a página.
  O erro "Ask the member to verify their account" é um bloqueio de confiança da conta
  (conta nova), não uma regra documentada "desde 2025".
- Verificação de local de trabalho por email: gratuita, sem documento nem selfie, mas
  só funciona se (a) a página Blue Serenity for uma **Verified Page** e (b) o super admin
  dessa página adicionar o domínio blueserenity.pt em Settings > Verification controls.
  Só verifica a empresa listada como emprego atual no perfil.
- Verificação da página (Page verification): pedido pelo super admin, só em desktop,
  Settings > Verification controls > Request verification. Elegibilidade por "engagement"
  e relação comercial (Ads, Jobs, Premium Company Page são exemplos, não requisitos).
  Exige provar a posse do site (registo TXT no DNS). Hoje o DNS de blueserenity.pt
  não tem `linkedin-site-verification=`, logo a página Blue Serenity ainda não está verificada.
- Anúncios: para criar Sponsored Content ou patrocinar posts são precisos OS DOIS:
  papel na página (super admin, content admin ou Sponsored Content poster) E
  Creative manager ou superior na conta de anúncios. Só utilizador da conta de anúncios
  não chega. O papel Sponsored Content poster é um papel de admin de página.
- Microsoft Entra Verified ID: sem biometria, mas exige tenant Entra com o domínio,
  configuração Verified ID e submissão manual à Microsoft (onboarding relatado como
  pausado/irregular em 2025-2026). O DNS de blueserenity.pt não mostra um tenant
  Microsoft 365 (sem autodiscover/enterpriseregistration). Via de último recurso.
- Verificação de identidade (Persona, passaporte NFC + selfie) continua excluída.

## Ordem de ataque

1. Conta da Maria (5 min): confirmar email e telefone em Settings > Sign in & security;
   garantir que o perfil lista Blue Serenity como emprego atual; foto e algumas ligações.
2. Caminho inverso (5 min): em vez de o super admin a adicionar, a Maria pede acesso
   na página ISQ ES (menu "..." > Request admin access, ou via Campaign Manager
   "Request Sponsored Content poster"). O super admin aprova em Pending admin requests.
   O bloqueio pode aplicar-se só ao fluxo "adicionar".
3. Verificação por email (depende de 2 passos na página Blue Serenity):
   a. Página Blue Serenity > Settings > Verification controls. Se existir, Request
      verification (nome legal, site, morada; publicar o TXT no DNS de blueserenity.pt).
   b. Depois de verificada, + Add domains > blueserenity.pt.
   c. Maria: perfil > Add verification > Workplace > código enviado para
      mariapessoa@blueserenity.pt (expira em 15 min). Revalidar a cada 365 dias.
   d. Repetir o passo de adicionar como Content admin.
   Se "Verification controls" não aparecer, a opção 1 original está fechada por agora.
4. Se nada do anterior funcionar, usar o circuito sem papel na página (abaixo).

## Circuito sem papel na página

Publicações: Postiz (postiz2.blueserenity.pt) já tem "ISQ España" ligada
(id cmrckez130001oa7hooxfcw5y, platform linkedin-page), além de DMC, dBwave.i,
Conceptance e Blue Serenity. Passos:
- Settings > Teams > Add member com mariapessoa@blueserenity.pt (Postiz self-hosted
  inclui Teams; o convite por email exige provider de email configurado no Postiz).
- Ela agenda para "ISQ España" com login próprio; o token LinkedIn continua a ser
  o da conta do super admin (reautorizar quando expirar, ~60 dias).
- Limitação: não há "customers" configurados (groupList vazio), por isso ela vê as
  5 páginas. Se isso for problema, criar customers e agrupar.
- Verificar o separador Analytics do Postiz para a página: cobre parte das métricas
  que a credencial n8n não dá.
- n8n (instância autoisq.*) mantém-se como via alternativa de publicação.

Anúncios: adicioná-la à conta de anúncios (Campaign Manager > Manage access,
papel Campaign Manager ou Creative manager). Ela monta campanhas, públicos e
orçamentos; o passo de criar o criativo de Sponsored Content ou patrocinar um post
fica com quem tem papel na página (o super admin), até ela conseguir o papel
Sponsored Content poster. Formatos sem ligação à página (Text Ads) não estão
confirmados na ajuda como isentos do papel na página.

Fica por cobrir sem papel na página: responder a comentários e mensagens como página.

## Fontes

- https://www.linkedin.com/help/linkedin/answer/a541981
- https://www.linkedin.com/help/linkedin/answer/a1423367
- https://www.linkedin.com/help/linkedin/answer/a568484/
- https://www.linkedin.com/help/recruiter/answer/a6278544
- https://www.linkedin.com/help/linkedin/answer/a7174627
- https://www.linkedin.com/help/lms/answer/a1481243
- https://www.linkedin.com/help/linkedin/answer/a425628
- https://www.linkedin.com/help/linkedin/answer/a1453679
- https://www.linkedin.com/help/linkedin/answer/a1359065
- https://docs.postiz.com/general/settings/team
