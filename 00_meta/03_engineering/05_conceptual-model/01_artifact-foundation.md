# Fundamento dos artefatos

> Estado: formulação em amadurecimento. Este documento registra o entendimento atual e não constitui, por si só, uma decisão de implementação.

## Propósito

O modelo conceitual do ManageHUB apoia-se em dois conceitos complementares: **artefatos**, que tornam elementos de interesse administrativo persistentes e processáveis, e **axiomas de sistema**, que fornecem a base mínima para interpretá-los. Juntos, eles permitem que o sistema represente informações diversas sem perder a semântica que lhes dá sentido.

Todo elemento tratado pelo sistema entra e permanece nele como artefato. Os axiomas também são artefatos, mas ocupam uma posição fundacional: estabelecem os significados e as regras elementares pelos quais os demais artefatos, suas definições, suas instâncias e suas relações podem ser compreendidos.

### Artefato

No ManageHUB, **artefato** é a unidade universal de representação, persistência e processamento de tudo aquilo que possa ser relevante para a gestão de um usuário ou organização.

Um artefato não é necessariamente uma coisa material nem uma ocorrência concreta. Ele é a forma pela qual o sistema torna uma entidade — material, informacional, conceitual, normativa, relacional ou operacional — identificável, armazenável, recuperável, inteligível e processável ao longo do tempo.

O núcleo do ManageHUB opera sobre essas representações informacionais persistentes, e não diretamente sobre seus referentes externos. Aplicações concretas, como o sroHUB, podem interagir com pessoas, organizações, dispositivos, serviços ou outros referentes por meio de seus próprios apps, applets e integrações. Essas interações produzem, consultam ou atualizam os artefatos por meio dos quais o núcleo preserva e processa o contexto administrativo.

O conceito abrange dois planos complementares:

- No plano **definidor**, artefatos formalizam como outras entidades devem ser compreendidas e tratadas pelo sistema: seus significados, estruturas, atributos, capacidades, restrições, relações permitidas e formas de processamento. São a base semântica pela qual o sistema recebe, armazena e interpreta novas informações.
- No plano das **instâncias**, artefatos representam ocorrências individualizadas de interesse administrativo: uma pessoa, organização, documento, comunicação, evento, obrigação, decisão, relação ou qualquer outro ente identificável no contexto do usuário.

Os exemplos seguintes são ilustrativos e não esgotam os elementos representáveis. Os ancestrais indicados para os definidores também são exemplos de uma possível especialização futura, e não um vocabulário já estabelecido.

| Elemento representado | Regime ontológico | Ancestral ou definidor imediato |
| --- | --- | --- |
| Definição de pessoa | Definidor | Definição-base de entidade |
| Pessoa individualizada | Instância | Definição de pessoa |
| Definição de organização | Definidor | Definição-base de entidade coletiva |
| Organização individualizada | Instância | Definição de organização |
| Definição de contrato | Definidor | Definição-base de instrumento contratual |
| Contrato específico | Instância | Definição de contrato |
| Definição de e-mail recebido | Definidor | Definição-base de comunicação |
| E-mail específico | Instância | Definição de e-mail recebido |
| Definição de documento técnico | Definidor | Definição-base de documento |
| Documento técnico específico | Instância | Definição de documento técnico |
| Definição de tarefa | Definidor | Definição-base de item de trabalho |
| Tarefa individualizada | Instância | Definição de tarefa |
| Definição de processo administrativo | Definidor | Definição-base de processo |
| Processo administrativo específico | Instância | Definição de processo administrativo |
| Definição de reunião | Definidor | Definição-base de evento |
| Reunião ocorrida ou agendada | Instância | Definição de reunião |
| Definição de arquivo digital | Definidor | Definição-base de recurso informacional |
| Arquivo anexado específico | Instância | Definição de arquivo digital |
| Definição de fiscalização técnica de contrato | Definidor | Definição-base de relação multipolar |
| Fiscalização técnica nº 7 | Instância relacional | Definição de fiscalização técnica de contrato |
| Definição de workflow | Definidor | Definição-base de processo executável |
| Execução específica de workflow | Instância | Definição de workflow |

Ser imaterial não torna uma entidade menos apta a ser instância. Uma tarefa concreta é uma instância operacional; uma obrigação assumida é uma instância normativa; uma reunião ocorrida é uma instância de evento; e o vínculo específico entre duas pessoas ou entre um documento e uma tarefa é uma instância relacional. Todos são reais e relevantes para o domínio administrativo, ainda que não sejam objetos físicos.

Assim, o artefato é tanto o ponto de entrada de uma entidade no armazenamento persistente quanto sua unidade permanente de inteligibilidade operacional. A qualquer tempo, ele e suas relações devem poder ser recuperados e interpretados para gerar valor por meio de consultas ou processamentos, previamente definidos ou formulados *ad hoc*.

### Axioma de sistema

Um **axioma de sistema** é um artefato que integra a base interpretativa mínima do ManageHUB. Ele estabelece um significado, uma distinção ou uma regra fundamental necessária para que o sistema possa compreender suas próprias definições, relações e instâncias.

Os axiomas-raiz são definidos fora da cadeia ordinária de definições internas: sua validade não depende de outro artefato que os defina. Um axioma também pode descender de um ou mais axiomas, mas nunca de um definidor comum. Desse modo, a camada axiomática pode ser composta e especializada sem perder sua separação em relação às definições ordinárias.

Os axiomas-raiz constituem o ponto de *bootstrap* do modelo, interrompendo a regressão infinita de definições e fornecendo o fundamento semântico a partir do qual os demais artefatos se tornam inteligíveis.

Embora os axiomas-raiz sejam fundamentados externamente, todos os axiomas permanecem visíveis, identificáveis, classificáveis e consultáveis como artefatos. Isso permite que a base do sistema seja explícita, auditável e passível de evolução deliberada, sem confundir sua função fundacional com a de um definidor comum.

## Propriedades candidatas universais

Todo artefato deve poder possuir, no mínimo:

- identidade persistente;
- regime ontológico;
- classificação em uma ou mais dimensões;
- proveniência mínima;
- temporalidade mínima;
- contexto de acesso e governança;
- capacidade de participar de relações com outros artefatos.

Essas propriedades não tornam todos os artefatos equivalentes. Conteúdo documental, participantes de uma comunicação, prazo, responsável, formato de arquivo, estado de workflow, polos de uma relação e regras específicas de validação pertencem somente às naturezas ou definições a que se aplicam.

## Atributos estruturais e semântica especializada

Todo artefato possui uma quantidade fixa de **atributos generalistas universais**. Eles existem em todos os artefatos por integrarem sua estrutura comum, mas não carregam necessariamente o mesmo significado operacional em todas as tipologias. A tipologia do artefato define como cada atributo deve ser compreendido, exibido, preenchido, validado e processado.

Entre os atributos generalistas candidatos estão `denominação`, `data inicial`, `data final` e uma quantidade fixa de datas universais de interesse. A existência desses campos não implica que todos sejam aplicáveis ou obrigatórios em toda tipologia. Por exemplo, em uma pessoa, `denominação` pode significar o nome de referência interna na organização e `data inicial` pode significar a data de nascimento; em um documento, `denominação` pode significar seu título e `data inicial` sua data de emissão; em um contrato, as datas podem significar o início e o término de sua vigência.

Para cada atributo generalista, a tipologia deve declarar, quando aplicável:

- **rótulo** (*label*) apresentado ao usuário;
- **descrição** de seu significado semântico;
- aplicabilidade;
- obrigatoriedade;
- tipo de valor;
- cardinalidade;
- regras de validação;
- visibilidade e regras de processamento.

Além dos atributos generalistas, uma tipologia pode introduzir **atributos específicos**, necessários apenas à sua própria semântica. Um contrato pode possuir atributos próprios para condições ou cláusulas contratuais; uma nota de empenho pode possuir atributos próprios para sua identificação e execução. Esses atributos não precisam existir em artefatos de outras tipologias.

Há também **atributos relacionais**, cujo valor é outro artefato ou um conjunto de artefatos. Eles devem ser definidos pela tipologia como referências individuais ou múltiplas e submetidos às regras das relações permitidas entre os polos envolvidos.

### Família de valores

Quando uma tipologia precisar representar valor, ela deve usar uma família fixa de atributos estruturais, em vez de um único campo universal com tipos de dados incompatíveis. A família inicial é composta por:

- valor numérico;
- unidade;
- moeda;
- valor textual, quando necessário.

A tipologia define quais atributos dessa família são aplicáveis e obrigatórios. Um contrato ou uma nota de empenho pode exigir valor numérico e moeda; um bem pode exigir valor numérico e uma unidade de mensuração ou moeda; uma pessoa pode tornar todos esses atributos não aplicáveis. Essa composição preserva persistência e consultas previsíveis, sem reduzir a capacidade de especialização semântica.

Em síntese, a tipologia não apenas classifica o artefato: ela estabelece o contrato semântico de seus atributos universais e introduz os atributos específicos e relacionais requeridos por sua natureza.

## Identidade e unicidade representacional

Todo artefato possui identidade persistente. Em regra, um mesmo referente material, informacional, conceitual, normativo, relacional ou operacional deve possuir uma única representação artefatual no sistema. A criação acidental de artefatos distintos para o mesmo referente é vedada e deve ser prevenida ou reconciliada pelos mecanismos de identidade aplicáveis.

Uma cópia deliberada pode ser admitida por necessidade circunstancial, desde que resulte de uma ação consciente e preserve sua proveniência. Nesses casos, a origem deve ser registrada pela relação canônica:

```text
Artefato de origem ──é copiado por──> Artefato copiado
```

A cópia passa a possuir identidade própria e não deve ser confundida com uma segunda representação independente do mesmo referente. Ela pode, por exemplo, ser adaptada para servir de referência operacional. A criação de um definidor template a partir de uma instância é uma derivação semanticamente distinta, não uma cópia. As condições de autorização e os efeitos de cada operação pertencem à definição da relação e às regras do contexto em que ela é usada.

## Regime ontológico

Todo artefato pertence a um dos seguintes regimes ontológicos:

- **Axioma** — fundamento interpretativo do sistema.
- **Definidor** — artefato abstrato que fornece ancestralidade funcional ou semântica a outros definidores.
- **Instância** — ocorrência concreta fundada em uma definição aplicável.

Um axioma pode não possuir ancestral. Quando possuir um ou mais, todos devem estar igualmente no regime `axioma`. Todo definidor, por sua vez, deve possuir pelo menos um ancestral imediato, que pode ser um axioma ou outro definidor. Essas regras asseguram que nenhum definidor comum exista sem fundamentação e que toda cadeia possa ser percorrida até um ou mais axiomas-raiz.

Um definidor pode ter a capacidade de funcionar como **template**. Template não é um quarto regime: é uma capacidade de um definidor reutilizável para orientar a criação ou configuração de instâncias.[^promocao-template]

[^promocao-template]: Uma instância pode sofrer uma operação de sistema apresentada ao usuário como “tornar-se template”. A instância original não muda de regime: o sistema cria outro artefato, no regime `definidor`, descendente tanto do definidor-base de template quanto do definidor instanciado pela origem, transfere da instância seu conteúdo e os metadados autorizados, registra a derivação e marca o novo definidor como template — e, necessariamente, como instanciável. Consulte [[04_typing-and-classification#Templates e promoção de instância|Templates e promoção de instância]].

Todo definidor também deve declarar se é **instanciável**. Essa capacidade, que poderá corresponder a um atributo próprio do definidor, autoriza ou veda que instâncias concretas o usem como base imediata em uma relação de instanciação. Um definidor não instanciável ainda pode definir outros definidores, transmitir semântica, fornecer estrutura ou atuar como componente de um template, mas não pode receber diretamente uma relação `instancia`.

Template e instanciabilidade são capacidades distintas, mas não independentes: todo definidor com capacidade de template deve ser instanciável. Um definidor instanciável não precisa ser template, e um definidor sem nenhuma dessas capacidades ainda pode definir ou compor outros definidores.

## Ancestralidade de definições

A relação axiomática `define` organiza a família de vínculos capazes de expressar fundamentação funcional ou semântica entre definições. Ela é **abstrata e não instanciável**: não deve existir vínculo concreto cujo definidor imediato seja `define`. Toda ligação persistida nessa família instancia um descendente mais específico.

O primeiro descendente classificatório adotado pelo modelo possui as seguintes leituras:

```text
Definição-base ──é base conceitual para──> Definição especializada
Definição especializada ──é especialização de──> Definição-base
```

`É base conceitual para` transmite ancestralidade classificatória: a definição especializada herda, restringe, especializa ou compõe significado, estrutura, capacidades, restrições ou comportamento de sua base. `É especialização de` é a leitura inversa do mesmo fato.

Outros descendentes de `define` podem estabelecer fundamentação sem transmitir classificação. `É fonte derivativa de`, por exemplo, registra que um artefato novo foi produzido a partir de outro, mas não torna o resultado uma especialização ontológica da fonte. Por isso, cada definidor concreto pertencente à família de `define` deve declarar se transmite ancestralidade classificatória, estrutura, capacidades e restrições ou se preserva apenas proveniência.

Na prosa e nas consultas, `define` pode designar a família inteira ou o predicado genérico inferido de seus descendentes. Essa conveniência não autoriza sua instanciação direta.

O grafo formado pelas relações da família de `define` que transmitam ancestralidade classificatória é uma rede dirigida acíclica (*directed acyclic graph*, ou DAG). Percorrida no sentido inverso, toda cadeia deve alcançar um ou mais axiomas-raiz. Não se trata, portanto, de uma árvore: um definidor pode possuir múltiplas bases conceituais e, simultaneamente, servir de base para múltiplos descendentes. O que é vedado é que um artefato se torne ancestral de si mesmo, direta ou indiretamente.

```text
A ──é base conceitual para──> B
A ──é base conceitual para──> C
B ──é base conceitual para──> D
C ──é base conceitual para──> D
```

Nesse exemplo, `A` é base conceitual direta para `B` e `C`; `B` e `C` são bases conceituais para `D`. Assim, `D` possui dois ancestrais diretos e `A` é seu ancestral indireto. A rede admite herança múltipla e especializações paralelas porque nenhum caminho retorna de `D` para `A`, `B`, `C` ou para o próprio `D`.

Em termos semânticos, uma definição de **comunicação oficial** pode ser base conceitual, em paralelo, para **comunicação recebida** e **comunicação enviada**. Uma definição de **resposta formal recebida** pode então ser especialização simultânea de ambas: herda a estrutura comum de comunicação oficial e especializa aspectos associados ao recebimento e à resposta.

Formalmente, não pode existir caminho de tamanho positivo como:

```text
A ──é base conceitual para+──> A
```

## Instanciação

Instanciação relaciona o plano abstrato ao plano concreto. Uma instância materializa uma definição aplicável, de modo análogo a um objeto em relação a uma classe na programação orientada a objetos.

```text
Instância concreta ──instancia──> Definição abstrata
Definição abstrata ──é instanciada por──> Instância concreta
```

Na leitura orientada à instância, a mesma ideia pode ser expressa como: uma instância concreta **é instância de** uma definição abstrata. A escolha entre `instancia` e `é instância de` como nome canônico de armazenamento permanece aberta; ambas não devem ser tratadas como relações semânticas independentes.

Instanciação não é sinônimo de `define`:

- a família de `define` organiza vínculos de fundamentação entre definições; somente seus descendentes classificatórios transmitem ancestralidade funcional ou semântica;
- `instancia` liga uma ocorrência concreta à definição que ela materializa.

Uma relação `instancia` somente é válida quando seu polo de origem está no regime `instância` e seu polo de destino está no regime `definidor` com a capacidade `instanciável` autorizada. A relação não é permitida apenas porque um artefato é um definidor; a autorização deve ser declarada pela própria definição.

Cada instância deve instanciar **uma e somente uma** definição. A cardinalidade imediata da relação é, portanto, `1` no polo da definição: uma instância não pode materializar diretamente múltiplos definidores. Ela pode, contudo, herdar fundamentação indireta de diversos ancestrais por meio da rede acíclica classificatória da única definição que instancia.

Uma instância pode estar diretamente ligada a uma definição especializada e, por sua cadeia de definições, possuir fundamentação indireta em múltiplos definidores e axiomas. Essa fundamentação deve poder ser percorrida e auditada sem exigir a materialização de cada vínculo indireto como um fato independente.

## Classificação intrínseca e contexto

Toda instância possui um único definidor imediato. Suas **classificações intrínsecas** decorrem desse definidor e da rede de ancestralidade formada pela família semântica da relação axiomática `define`; elas não são atribuídas à instância como classificações independentes.

Uma instância satisfaz uma classificação quando seu definidor imediato é a própria classificação ou quando a classificação é ancestral desse definidor. A travessia considera somente relações concretas descendentes de `define` que declarem transmitir ancestralidade classificatória e preservem aciclicidade.

```text
Contrato nº 52/2026
  └── instancia → Contrato administrativo
                       └── é especialização de → Instrumento contratual
                                                    └── é especialização de → Instrumento jurídico
```

O contrato satisfaz as três classificações, embora instancie imediatamente apenas `Contrato administrativo`.

Classificações **contextuais**, em contraste, decorrem dos papéis, relações, circunstâncias ou inferências temporais em que a instância participa. `Pessoa física` pode ser uma classificação intrínseca de Ten Izabela; `fiscal técnica titular do Contrato nº 52/2026` é um papel contextual produzido por uma relação concreta. A distinção entre classificação intrínseca e contextual é axiomática no modelo; seus efeitos sobre consultas estão detalhados em [[04_typing-and-classification#Classificações intrínsecas e contextuais|Tipagem e classificação]].

## Fatos persistidos e informações derivadas

Nem todo predicado verdadeiro sobre um artefato precisa residir em um campo próprio. Uma informação pode decorrer de:

- atributo universal semanticamente especializado;
- atributo específico introduzido pelo definidor;
- relação bipolar direta;
- participação em relação multipolar;
- cadeia de relações;
- classificação herdada;
- cálculo determinístico em tempo de execução;
- inferência composta por campos, relações e classificações.

O contrato persistir `data final` com a semântica de `data de expiração da vigência`, por exemplo, não exige persistir também o estado `vigente`. Esse estado pode ser resolvido em tempo de execução pela comparação da data com o instante de referência e por outras condições aplicáveis.

## Informação incorporada e promoção

Uma informação deve nascer na forma estrutural mais simples capaz de preservar seu significado e sua utilidade: valor de atributo, conteúdo estruturado ou relação. Ela somente deve tornar-se artefato autônomo quando sua relevância justificar identidade, proveniência ou vida relacional próprias.

O usuário pode promover deliberadamente uma informação incorporada a artefato. A promoção preserva a informação em seu locus original, salvo decisão explícita em contrário, e cria uma instância com identidade persistente, um único definidor imediato e relação obrigatória de proveniência com a origem. Denominação, validade, relações e histórico próprios são exigidos conforme a definição aplicável.

A promoção não é cópia: individualiza uma unidade informacional que antes estava incorporada em outro artefato. Seus critérios e seu ciclo de vida estão detalhados em [[05_information-and-containment#Promoção de informação a artefato|Informação, continência e promoção]].

## Linhagem entre instâncias

Instâncias não instanciam outras instâncias. Ainda assim, uma instância pode manter relações de linhagem ou de contexto com outra instância, sem que isso altere a única definição da qual cada uma é instância.

Uma relação bipolar entre duas instâncias somente é válida quando existe um **definidor de relação** concreto, instanciável e que admita artefatos do regime `instância` nos dois polos. Portanto, não basta que dois artefatos sejam instâncias para que possam ser ligados: a natureza, a direção, os polos permitidos e as regras do vínculo devem ser declarados pelo definidor da relação. Relações multipolares são artefatos agregadores ligados a seus participantes por duas ou mais relações bipolares definidas.

```text
Relação bipolar ──é base conceitual para──> Definidor concreto de relação
Instância relacional ──instancia──> Definidor concreto de relação
Instância A ──[polo permitido]──> Instância relacional ──[polo permitido]──> Instância B
```

As relações candidatas iniciais são:

```text
Instância de origem ──é fonte derivativa de──> Instância derivada
Instância derivada ──é derivado de──> Instância de origem
Instância de origem ──é copiada por──> Instância copiada
Instância posterior ──serve de referência para──> Instância que a consulta
```

Essas relações têm semânticas distintas:

- **é derivado de** preserva uma transformação ou continuidade: a instância derivada foi obtida a partir de outra, possivelmente com alterações;
- **é copiada por** registra a reprodução de uma instância por outra, sem afirmar que a cópia seja semanticamente uma nova definição;
- **serve de referência para** registra uso contextual, consulta ou inspiração, sem afirmar derivação nem cópia.

Por exemplo, um rascunho revisado pode derivar de um rascunho anterior, uma nova versão pode ser copiada de uma versão prévia e uma resposta pode usar uma comunicação anterior como referência. Em todos os casos, cada artefato continua sendo instância de seu definidor aplicável; as relações entre instâncias registram sua história operacional e seu contexto.

As regras detalhadas para definidores de relação, polos, leituras, cardinalidade, admissibilidade e proveniência estão registradas em [[02_relationships-and-provenance|Relações e proveniência]].

## Relações axiomáticas

As definições das relações `define` e `instancia` pertencem à base axiomática do sistema. `Define` é abstrata e não instanciável; `é definido por` é sua leitura inversa genérica. `Instancia` é interpretada diretamente pelo núcleo; `é instanciada por` é sua leitura inversa. Leituras inversas não constituem relações semanticamente independentes.

```text
define [axioma abstrato]
├── é base conceitual para / é especialização de
└── é fonte derivativa de / é derivado de

Axioma ──é base conceitual para──> Definição-base
Definição-base ──é base conceitual para──> Definição especializada
Definição especializada ──é instanciada por──> Instância concreta
```

## Unidade lógica e persistência física

Todo artefato possui identidade e comportamento no modelo lógico comum, mas isso não exige que todas as famílias ocupem uma única tabela física. A ontologia determina o que cada artefato é; a política de materialização determina se e por quanto tempo uma ocorrência deve ser persistida; a arquitetura de persistência determina onde e como armazená-la. Essas camadas devem permanecer distinguíveis para permitir estratégias próprias de retenção, particionamento, auditoria e desempenho sem romper a unidade conceitual do artefato.

## Questões ainda abertas

- Quais capacidades adicionais um definidor pode possuir além de funcionar como template e ser instanciável?
- Quais axiomas são estritamente necessários para iniciar o sistema e quais podem ser definições internas posteriores?
- Qual será a convenção canônica de direção e nome para a relação de instanciação?
- Como serão expressas composição, compatibilidade e conflito entre múltiplas definições-base?
