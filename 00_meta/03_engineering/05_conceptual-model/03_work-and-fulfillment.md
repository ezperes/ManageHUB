# Trabalho e satisfação

> Estado: formulação inicial. Este documento registra conexões já identificadas com o modelo conceitual; a ontologia específica do trabalho permanece em amadurecimento.

## Propósito

Uma tarefa pode representar uma obrigação contextualizada: algo precisa ser realizado porque um evento, comunicação, regra, processo ou outro artefato o motivou. O esquema inicial é:

```text
origem → tarefa ou obrigação → resultado ou evidência
```

A origem explica por que a obrigação existe; a tarefa representa o trabalho ou resultado esperado; a evidência permite avaliar se a obrigação foi satisfeita. Produzir um artefato não implica necessariamente aprovação, aceitação, envio ou satisfação final.

## Fundamentação informacional

Procedimentos e decisões podem ser fundamentados por informações promovidas a artefatos:

```text
DIEx nº XXX/DOM
  └── dá amparo normativo a → Informação sobre limites de competência
        └── fundamenta → Procedimento de aprovação de termo aditivo
```

Essa cadeia separa a fonte documental, a informação normativa individualizada e o procedimento que a utiliza.

## Estados e resultados determinísticos

Estados de tarefas, processos e obrigações podem decorrer de atributos, relações, evidências e cálculos em tempo de execução. Um [[05_information-and-containment#Resolvedores determinísticos|resolvedor determinístico]] pode identificar, por exemplo:

- a autoridade competente para aprovar um termo aditivo;
- a vigência de um contrato no instante de referência;
- a elegibilidade atual de uma pessoa para exercer determinado papel;
- a existência de evidência suficiente para satisfazer uma obrigação.

Resolvedores de busca localizam e qualificam candidatos sem produzir, por padrão, efeitos administrativos. Resolvedores de ação validam precondições, aplicam filtros e produzem mutações controladas. Qualquer filtro do qual dependa uma ação deve ser reavaliado imediatamente antes da persistência.

O definidor da tarefa, workflow, ação ou resolvedor consumidor declara se sua execução e as buscas subordinadas devem ser persistidas, quais dados devem ser conservados e por quanto tempo. Quando o resultado fundamentar decisão relevante, exceção ou alteração de estado, a política pode exigir materialização com versões das regras, fatos utilizados, resultados e justificativas, permitindo auditoria e reprodução histórica.

Filtros obrigatórios excepcionáveis podem admitir uma escolha inconforme mediante confirmação e justificativa persistida. A exceção constitui artefato auditável; se a escolha era conforme e apenas se tornou inconforme posteriormente, registra-se uma inconformidade superveniente, e não uma exceção retroativa.

## Relações multipolares no trabalho

Fatos administrativos complexos podem ser representados por [[02_relationships-and-provenance#Relações multipolares por agregação|relações multipolares]]. Uma aprovação, por exemplo, pode agregar solicitante, autoridade competente, objeto aprovado, fundamento normativo e documento decisório, além de campos próprios como data e resultado.

## Questões ainda abertas

- Uma tarefa pode possuir múltiplas origens ou uma origem multipolar agregada?
- Como representar soluções parciais, concorrentes, rejeitadas ou substituídas?
- Qual relação distingue produção, submissão, aprovação, aceitação e satisfação?
- Quais estados devem ser persistidos e quais devem ser resolvidos em tempo de execução?
- Quais definidores de trabalho exigem retenção das execuções e de suas buscas subordinadas?
- Quando a evidência deve ser um artefato autônomo e quando pode permanecer incorporada?
