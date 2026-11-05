# Tabelas do núcleo (esquema v1)

Cabeçalhos prontos a importar nas Data Tables do n8n (ou em Postgres com os mesmos nomes). Sem segredos. Números de telefone sempre em E.164 (+351...). Datas YYYY-MM-DD, instantes em ISO 8601 com fuso. Booleanos 0/1.

| Ficheiro | Para que serve | Linhas incluídas |
|---|---|---|
| `clientes.csv` | Registo de inquilinos: tudo o que é específico de um cliente | `lrc` (piloto) e `chr` (demonstração) |
| `kb_chr.csv` | Base de conhecimento da Clara (demonstração) | 12 entradas |
| `kb_lrc.csv` | Base de conhecimento da Vitória: migrar a partir de `kb_escola` | vazio |
| `alunos.csv` | Alunos e encarregados, mensalidade e vencimento | 3 de demonstração |
| `aulas.csv` | Horários recorrentes (dia_semana: 1=segunda … 7=domingo), lotação, exceções por data (lista `YYYY-MM-DD;...`) | 7 aulas da Clara |
| `marcacoes.csv` | Marcações por data; estados: marcada, cancelada, falta, presente | agenda fictícia de 08/11: sab10 com 4/6, sab11 cheia, sab12 com 4/6 |
| `conversas.csv` | Estado por contacto: janela 24 h, pausa humana, pedido a meio, escalação aberta | vazio |
| `escalacoes.csv` | Escalações; estados: aberta, avisada, lembrada, fechada, expirada | vazio |
| `pagamentos.csv` | Mensalidades; estados: em_falta, por_confirmar, confirmado | vazio |
| `fila_envios.csv` | Fila do expedidor; estados: pendente, enviado, falhou | vazio |
| `eventos.csv` | Registo pseudonimizado para monitor e relatório (`contacto_hash` = SHA-256 do número com sal da env var `HASH_SALT`) | vazio |
| `kb_propostas.csv` | Correções à base propostas pelo dono por voz/texto, a validar pela Blue Serenity | vazio |

## Campos de `clientes.csv` que alimentam o prompt

`secretaria_nome`, `negocio_nome`, `dono_nome`, `tratamento` (você/tu), `fuso`, `morada`, `horario_funcionamento`, `fechos`, `formas_pagamento`, `dia_vencimento`, `escala_sempre`, `f_agenda`, `f_cobrancas`, `antecedencia_min_h`, `cancelamento_min_h`, `regra_remarcacao`, `regra_experimental`. `humano_pausa_h` é o tempo de silêncio depois de um eco do dono. `silencio_inicio`/`silencio_fim` limitam lembretes e resumos, nunca respostas a clientes.

## Convenções

- `tenant_id` curto e estável (3 a 5 letras). Nunca muda.
- `numero_dono` em `clientes` é o que identifica mensagens do dono; é obrigatório antes de ativar o cliente (estado `ativo`).
- A tabela `kb_<tenant>` é a única por cliente; todas as outras levam coluna `tenant_id`.
- O workflow de "offboarding" apaga `kb_<tenant>` e todas as linhas com esse `tenant_id`, e deixa em `eventos` apenas os agregados mensais.
