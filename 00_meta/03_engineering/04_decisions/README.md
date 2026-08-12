# Decisões

Esta área recebe registros de decisões arquiteturais (ADRs): escolhas contextuais relevantes cujo motivo, alternativas e consequências precisam permanecer compreensíveis ao longo do tempo.

## Quando registrar

Uma decisão deve ser registrada quando:

- alterar limites, dependências ou responsabilidades arquiteturais;
- adotar tecnologia com impacto duradouro;
- estabelecer ou excepcionar um padrão;
- resolver uma divergência estrutural relevante;
- envolver alternativas plausíveis cuja rejeição deva ser preservada no histórico.

## Distinções

- Um [[../01_principles/README|princípio]] fornece fundamento duradouro para avaliar escolhas.
- Um [[../03_standards/README|padrão]] orienta uma classe recorrente de situações.
- Uma decisão registra uma escolha concreta, em determinado contexto, e suas consequências.

## Formato esperado

Cada ADR deverá registrar, no mínimo:

1. título e estado;
2. contexto;
3. alternativas consideradas;
4. decisão e justificativa;
5. consequências;
6. relações com decisões anteriores ou posteriores.

Decisões substituídas não devem ser apagadas. Seu estado deve indicar a substituição e apontar para o novo registro. ADRs retroativos somente devem ser criados quando houver contexto suficiente para reconstruir fielmente a decisão.
