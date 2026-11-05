# Casos da Bluewright: ponto de partida (handoff v4, 24 out 2026)

Ler `CATALOGUE.md` primeiro: tem as regras, o mapa caso → cliente (interno) e o que saiu e porquê.

## O que mudou na v4

- **Uma peça = um cliente + um desafio.** Os 4 casos antigos (2, 4, 5, 6), que juntavam vários
  desafios, deram 10 casos. Desafios parecidos em clientes diferentes ficam em casos separados.
- **Anonimato sempre**, mesmo com autorização. A regra 4 do `CLAUDE.md` foi alterada.
- **Os fracassos entram.** O caso 04 é inteiro sobre um fracasso; todos têm «What did not work».
- **Números:** saíram os absolutos pequenos (visitas no LinkedIn, aniversários, lugares, plugins,
  encomendas).
- **Esta sessão (Opus) decide o enquadramento.** Os agentes só fazem verificação: registo, números,
  equipa vermelha, leitura a frio.
- As versões v3 estão em `archive/cases-v3/`. As versões para LinkedIn ficam para depois.

## Ficheiros

| Ficheiro | O que é |
|---|---|
| `case-01` … `case-11` | Os casos v4, em inglês (07, 08 e 11 refeitos na 2.ª ronda; versões anteriores em `archive/cases-v4/`) |
| `essay-ai-built-it.md` | Ensaio v3, sem alterações. Só se publica depois do fim da relação com o cliente |
| `check_v4.py` | Juiz 1: cada número de cada caso tem de existir num dos três registos. **Passa** |
| `evidence-ledger-v4.csv` | Registo dos casos 07, 08 e 11 (2.ª ronda) |
| `evidence-ledger.csv` | Registo dos casos 02–05 e do ensaio (`build_ledger.py`) |
| `../../cases/evidence-ledger-isq.csv`, `evidence-ledger-case06.csv` | Registos dos casos 06–10 |
| `judges/` | Memorandos adversariais e reidentificação da v3, e a leitura a frio da v4 |

`check_ledger.py` (o da v3) procura os ficheiros antigos e já não serve; usar `check_v4.py`.

## Por fazer

- Os `[FILL]` do Alexandre: o 11 (contratações e
  tempo de preenchimento), o 09 e o 10 (resultados aos 90 dias, a
  22 jan 2027). Dependem do tempo: não há mais nada a perguntar agora.
- ~~Equipa vermelha e reidentificação da v4~~: feitas a 24 out, ver `judges/reid-redteam-v4.md`. Ninguém identificou os clientes pela web; quem conhece o setor reconhece-os.
- **Site (decidido a 30 out): os 11 casos, agrupados em 4 temas**, em `site/index.html` e `site/copy.md`. Está só local. O 01 fechou sem decisão da administração, com perguntas ao leitor (1 nov). O 06 está completo desde 1 nov. Nos cartões, os `[FILL]` dos outros casos ficaram de fora. O cartão «long game» saiu, por não ter cliente, e o Advise fica sem caso no site.
- O teste com 5 leitores do público-alvo, que o Alexandre tem de nomear.
- O caso «long game» (Advise): ainda não há cliente escolhido.
- Ensaio sobre os desafios: rascunho v1 em `essay-the-part-that-takes-longest.md`, por rever pelo Alexandre.
