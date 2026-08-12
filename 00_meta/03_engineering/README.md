# Engenharia

Esta área reúne a documentação interna que orienta a arquitetura e o desenvolvimento do sistema. Seu papel é registrar a filosofia de engenharia do projeto: princípios, premissas, padrões e decisões que dão coerência à evolução do código.

Esses documentos não são destinados ao usuário final. Eles servem de referência para quem projeta, implementa, revisa e mantém o sistema e poderão fundamentar, futuramente, a documentação formal do próprio sistema.

## Organização

1. [[01_principles/README|Princípios]] — fundamentos e valores duradouros que orientam as escolhas de engenharia.
2. [[02_architecture/README|Arquitetura]] — limites, dependências, organização e visão estrutural do sistema.
3. [[03_standards/README|Padrões]] — critérios recorrentes aplicáveis ao desenvolvimento.
4. [[04_decisions/README|Decisões]] — registros contextuais de escolhas arquiteturais relevantes.

## Critério de inclusão

Um documento pertence a esta área quando explica por que o sistema é concebido ou desenvolvido de determinada maneira ou quando estabelece critérios duradouros para futuras decisões técnicas.

Documentação operacional, instruções de uso e descrições voltadas ao usuário devem permanecer fora desta área. Detalhes transitórios de implementação também não devem ser tratados como princípios ou decisões permanentes.

Os documentos devem evoluir junto com o sistema. Quando uma premissa ou decisão deixar de ser válida, seu histórico e sua substituição devem ser registrados, preservando o contexto da mudança.

## Convenções

- Diretórios de categoria usam o padrão `NN_categoria`.
- Documentos ordenados usam o padrão `NN_nome-descritivo.md`.
- `README.md` permanece sem numeração e funciona como índice do diretório.
- Relações entre conceitos e documentos usam WikiLinks na primeira ocorrência pertinente de cada documento; repetições não recebem novos links, salvo quando isso for necessário à compreensão.
