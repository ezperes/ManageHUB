# Informação, continência e promoção

> Estado: formulação em amadurecimento. Este documento registra o entendimento atual e não constitui, por si só, uma decisão de implementação.

## Propósito

Este documento distingue a informação de sua posição semântica, do contêiner em que está inscrita, do portador que a transporta, do canal pelo qual circula e do formato que a codifica. Também descreve quando uma informação incorporada deve ganhar identidade própria e como necessidades informacionais recorrentes podem ser satisfeitas por rotinas determinísticas.

## Planos de mediação informacional

| Plano | Definição | Exemplos |
| --- | --- | --- |
| Informação | Conteúdo semanticamente relevante | data de expiração; limite de competência |
| Campo ou posição semântica | Lugar estruturado que atribui significado ao valor | `data final` interpretada como expiração da vigência |
| Contêiner | Estrutura na qual a informação está inscrita | corpo de contrato; corpo de e-mail |
| Portador | Artefato que transporta ou apresenta o contêiner | mensagem de e-mail; arquivo digital |
| Canal | Meio pelo qual o portador circula | e-mail; WhatsApp; SPED |
| Endpoint | Ponto institucional concreto do canal | conta corporativa; caixa de entrada do SPED |
| Formato | Codificação técnica de um contêiner digital | PDF; DOCX; XLSX; CSV |

Esses planos não devem ser confundidos. Um relatório pode ser documento técnico por natureza, estar materializado em arquivo digital, usar PDF como formato, ser anexado a uma mensagem e circular pelo canal e-mail.

## Cadeias de continência

Uma informação recebida por e-mail pode ser percorrida assim:

```text
Informação
  └── está contida em → Corpo do e-mail
        └── integra → Mensagem de e-mail
              └── foi recebida por → Conta corporativa
                    └── opera no canal → E-mail
```

Quando estiver em anexo:

```text
Informação
  └── está contida em → Corpo documental
        └── é materializado em → Arquivo digital
              ├── possui formato → PDF
              └── está anexado a → Mensagem de e-mail
                    └── foi recebida por → Conta corporativa
```

Uma informação contratual pode permanecer como valor de atributo sem se tornar artefato autônomo:

```text
Contrato nº 52/2026
  └── data final → 31/12/2026
```

O definidor `Contrato` atribui a `data final` o significado de `data de expiração da vigência`. Uma consulta pode partir de Ten Izabela, atravessar uma fiscalização técnica, localizar os contratos fiscalizados e recuperar suas datas finais com a semântica correta.

## Informação incorporada

Uma informação incorporada permanece em uma estrutura hospedeira, como:

- atributo universal;
- atributo específico;
- campo JSON estruturado;
- corpo textual;
- relação persistida;
- resultado obtido durante processamento em tempo de execução.

Ela é recuperável por meio do hospedeiro, mas não possui necessariamente identidade, definidor ou relações autônomas. Esse é o estado presumido de toda informação: usar a estrutura mais simples que preserve seu significado e sua utilidade.

## Promoção de informação a artefato

O usuário pode promover deliberadamente uma informação incorporada a artefato quando reconhecer relevância suficiente para integrá-la explicitamente a cadeias de informação e relações que necessitem ou mereçam rastreio.

A promoção:

1. mantém a informação no locus original, salvo decisão explícita de substituição;
2. cria uma instância com identidade persistente própria;
3. atribui-lhe um único definidor imediato;
4. copia ou referencia o conteúdo relevante;
5. registra obrigatoriamente sua proveniência;
6. permite denominação, validade, relações e histórico próprios conforme a definição;
7. estabelece, quando necessário, qual representação é autoritativa e como serão sincronizadas.

Promoção não é cópia. A cópia reproduz deliberadamente um artefato; a promoção individualiza uma unidade semântica que antes estava incorporada em outro artefato. A operação pode produzir uma relação de extração, derivação ou fundamentação, conforme a semântica do caso.

### Critérios de promoção

Uma informação torna-se candidata à promoção quando precisar de uma ou mais destas capacidades:

- identidade própria;
- denominação ou descrição própria;
- proveniência específica;
- combinação de múltiplas fontes;
- confiança, validação ou confirmação;
- validade temporal própria;
- histórico independente;
- contestação ou contradição;
- relações próprias;
- recuperação direta, independente da busca no hospedeiro;
- reutilização em múltiplos processos;
- atuação como fundamento de decisões ou automações.

### Exemplo de informação normativa

Considere um DIEx cujo conteúdo estruturado registra limites de competência para aprovação de termos aditivos:

```text
DIEx nº XXX/DOM
  └── informações contidas
        └── limites de competência para aprovação de termos aditivos
```

Se a informação fosse ordinária, poderia permanecer apenas nesse campo. Como ela orienta decisões importantes e precisa participar de outros fluxos, o usuário a promove:

```text
DIEx nº XXX/DOM
  ──dá amparo normativo a──>
Informação normativa sobre limites de competência
```

```text
Informação normativa sobre limites de competência
  ──fundamenta──>
Procedimento de aprovação de termo aditivo
```

A informação continua no DIEx e passa a possuir identidade e vida relacional próprias. Pelo [[02_relationships-and-provenance#Princípio da especialidade relacional|princípio da especialidade]], `dá amparo normativo a` deve prevalecer sobre uma relação genérica quando ela representar integralmente o fato que se pretende registrar.

## Extração, derivação, cópia e promoção

| Operação | Significado | Exemplo |
| --- | --- | --- |
| Extração | Conteúdo já existente em um locus passa a existir também ou em substituição em outro | individualizar a data de expiração contida no contrato |
| Derivação | Algo novo é criado usando uma fonte como base | produzir resumo analítico a partir de relatório |
| Cópia | Um artefato é deliberadamente reproduzido em outro | duplicar documento para edição independente |
| Promoção | Informação incorporada recebe identidade e vida relacional próprias | tornar limite normativo do DIEx um artefato consultável |

Promoção pode envolver extração ou derivação, mas não é sinônimo de nenhuma delas. `É copiado por` permanece reservado à reprodução de artefatos, conforme [[02_relationships-and-provenance#Cópia deliberada|Cópia deliberada]].

## Resolvedores determinísticos

Um **resolvedor determinístico** é uma rotina formal, não generativa e reproduzível que satisfaz uma necessidade informacional recorrente por meio de atributos, relações, ancestralidade classificatória e regras previamente definidas. Ele não é uma skill de agente de IA.

O vocabulário axiomático inicial distingue:

```text
Resolvedor determinístico [axioma]
├── é base conceitual para → Resolvedor determinístico de busca [axioma]
└── é base conceitual para → Resolvedor determinístico de ação [axioma]
```

Definidores concretos especializam esses axiomas; uma execução concreta instancia exatamente um definidor de resolvedor. O resolvedor pode consumir [[02_relationships-and-provenance#Filtros de artefatos|filtros de artefatos]] declarados por seu próprio definidor ou pelo definidor da operação que o consome.

Um resolvedor deve declarar:

- denominação e pergunta satisfeita;
- parâmetros e tipos admissíveis de entrada;
- instante de referência, quando aplicável;
- campos e caminhos relacionais consultados;
- regra determinística e dependências;
- tipo de saída;
- condições de indeterminação;
- versão da regra;
- filtros consumidos e fases em que atuam;
- política de registro de suas execuções e buscas subordinadas.

### Resolvedor determinístico de busca

Um resolvedor de busca deve ser reprodutível e, por padrão, livre de efeitos administrativos. Além do contrato comum, declara escopo, candidatos, filtros, ordenação, motivos de conformidade, instante de avaliação e forma de apresentação dos resultados `conforme`, `inconforme` e `indeterminado`.

Sua saída pode orientar outro resolvedor ou uma ação. Quando a busca fundamentar uma seleção ou decisão relevante, o consumidor pode exigir a preservação da execução, de seus parâmetros, da versão das regras e da fotografia dos resultados utilizados.

### Resolvedor determinístico de ação

Um resolvedor de ação produz efeitos administrativos ou altera estado persistente. Deve declarar também:

- precondições e filtros;
- validações imediatamente anteriores à mutação;
- efeitos e pós-condições;
- atomicidade e idempotência esperadas;
- política de exceção;
- requisitos de auditoria;
- estratégia de compensação ou recuperação, quando aplicável.

O definidor do resolvedor de ação pode exigir que suas buscas subordinadas sejam persistidas para demonstrar quais candidatos, conformidades e justificativas sustentaram a decisão.

### Vigência contratual

```text
vigencia_do_contrato(contrato, instante)
```

O resolvedor recebe uma instância cujo definidor satisfaça `Contrato` e um instante de referência, com padrão `agora()`. Ele pode consultar data inicial, data final, termos aditivos, suspensões, rescisões e encerramentos. Sua saída pode ser:

```text
vigente | ainda não iniciado | próximo do vencimento |
suspenso | expirado | encerrado | indeterminado
```

O estado nasce em tempo de execução; os fatos primários permanecem nos campos e relações que o sustentam.

### Quadro atual de uma organização

```text
quadro_atual(organização, instante)
```

Para responder “quem integra atualmente o quadro pessoal do SRO/4?”, o resolvedor:

1. seleciona relações da família `integra o quadro pessoal de`;
2. filtra as que possuem o SRO/4 como organização;
3. avalia a validade de cada vínculo no instante informado;
4. retorna as pessoas participantes;
5. exclui vínculos expirados, revogados ou ainda não iniciados.

## Materialização de resultados

O resultado de um resolvedor nasce em tempo de execução. Nem toda execução precisa ser materializada, mas a decisão não deve ficar dispersa em comportamento implícito da aplicação. O próprio definidor do resolvedor ou o definidor da operação que o consome deve declarar:

- se a execução será persistida;
- se suas buscas subordinadas também serão persistidas;
- quais entradas, candidatos, resultados, motivos e efeitos serão conservados;
- o prazo de retenção, inclusive a possibilidade de prazo indeterminado;
- condições que promovam um registro efêmero a durável;
- requisitos de auditoria, imutabilidade, anonimização ou descarte;
- política aplicável a exceções e inconformidades supervenientes.

Quando houver mais de uma política aplicável, prevalece a que imponha maior preservação, salvo regra de governança mais específica que autorize outro tratamento. A política efetiva usada em cada execução deve ser identificável e versionada.

| Natureza da execução | Política inicial indicativa |
| --- | --- |
| Busca transitória sem efeito administrativo | não materializar ou manter telemetria efêmera |
| Busca usada em decisão relevante | materializar resumo reproduzível ou fotografia dos resultados |
| Ação que altera estado | persistir a execução e seus efeitos |
| Exceção ou decisão auditável | persistência obrigatória |
| Execução sujeita a requisito de *compliance* | memória durável e, quando exigido, imutável |

### Execução como artefato

Quando materializada, a execução é um artefato lógico com identidade, definidor imediato e proveniência próprios:

```text
Execução nº 884
├── instancia → Execução de resolvedor de busca
├── executa → Resolvedor “Quadro atual”
├── utiliza → Filtro configurado para SRO/4
├── foi consumida por → Operação ou resolvedor de ação
├── instante e parâmetros
├── versões das regras
├── resultado
└── política e justificativa de materialização
```

O definidor da operação consumidora pode determinar a persistência tanto do registro de sua própria execução quanto das execuções dos resolvedores de busca que utilizou. Dessa forma, a cadeia decisória permanece recuperável sem impor retenção uniforme a todas as buscas do sistema.

Um resultado materializado não se torna automaticamente a fonte autoritativa. A regra versionada e os fatos utilizados no cálculo continuam necessários para explicar e, quando possível, reproduzir o resultado.

## Unidade lógica e topologia física

Ser artefato no modelo lógico não significa ocupar uma linha na mesma tabela física de todos os demais artefatos. Ontologia, materialização e persistência são planos relacionados, mas distintos:

- a **ontologia** determina o que a coisa é e como participa do modelo;
- a **política de materialização** determina se, com que conteúdo e por quanto tempo uma ocorrência será preservada;
- a **arquitetura de persistência** determina onde e como os registros serão armazenados.

Essas distinções lançam requisitos para a implementação futura sem antecipar DBMS, ORM ou estratégia definitiva:

- identidade lógica uniforme entre famílias fisicamente separadas;
- tabelas, partições ou mecanismos próprios para execuções e eventos de alto volume;
- retenção diferenciada entre memória efêmera, registro operacional e evidência durável;
- consultas conceituais independentes da distribuição física;
- preservação de proveniência, versão e contexto quando um registro efêmero for promovido a durável;
- índices adequados a ancestralidade, filtros, relações e validade temporal;
- possibilidade de cache ou projeção materializada sem substituir automaticamente a fonte autoritativa;
- reconstrução auditável de decisões quando a política aplicável assim exigir.

A implementação deverá evitar tanto uma tabela central monolítica por obrigação ontológica quanto fragmentação que impeça tratar todos esses registros como artefatos no modelo lógico.

## Questões ainda abertas

- A promoção será exclusivamente manual ou poderá ser proposta por automação?
- Como escolher o definidor imediato de uma informação promovida?
- Qual locus será autoritativo após a promoção e como ocorrerá a sincronização?
- Como representar múltiplas fontes concordantes ou contraditórias?
- Como versionar resolvedores e reproduzir decisões históricas?
- Como compor políticas de persistência herdadas de vários definidores consumidores quando houver conflito?
- Quais condições devem promover automaticamente uma execução efêmera a registro durável?
- Quais famílias exigirão armazenamento físico ou particionamento próprio?
