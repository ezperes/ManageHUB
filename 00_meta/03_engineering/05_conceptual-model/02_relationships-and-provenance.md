# Relações e proveniência

> Estado: formulação em amadurecimento. Este documento registra o entendimento atual e não constitui, por si só, uma decisão de implementação.

## Propósito

Relações tornam explícitos os fatos que conectam artefatos. Elas permitem preservar não apenas que dois artefatos estão associados, mas o significado do vínculo, os papéis exercidos por seus participantes, sua origem, sua validade e as regras que autorizam sua existência.

Toda relação concreta é tratada como artefato de primeira classe: um vínculo identificável, validável, consultável e auditável. O modelo distingue:

- **definidor de relação** — artefato que estabelece a semântica, os polos, as leituras, a cardinalidade e as restrições de uma natureza de relação;
- **instância relacional** — vínculo concreto que instancia exatamente um definidor de relação e conecta artefatos admitidos em seus polos.

O axioma geral `Relação` fundamenta duas formas estruturais:

```text
Relação
├── é base conceitual para → Relação bipolar
└── é base conceitual para → Relação multipolar
```

Uma relação bipolar representa diretamente um fato entre dois polos. Uma relação multipolar é um artefato agregador que reúne duas ou mais relações bipolares semanticamente nomeadas e pode possuir campos, regras, cardinalidades e leituras gerais próprios.

## Relações axiomáticas

`define` e `instancia` são definidores de relação no regime ontológico `axioma`. Sua interpretação integra a base mínima do sistema:

- `define` organiza a família de relações que estabelecem fundamentação funcional, semântica ou produtiva entre artefatos;
- `instancia` liga uma ocorrência concreta ao único definidor instanciável que ela materializa.

`Define` é abstrata e não instanciável. Nenhum vínculo persistido pode tê-la como definidor imediato: deve instanciar um descendente concreto que refine a natureza da fundamentação. O vocabulário inicial distingue:

```text
define / é definido por [axioma abstrato]
├── é base conceitual para / é especialização de
└── é fonte derivativa de / é derivado de
```

`É base conceitual para` transmite ancestralidade classificatória. Seu polo ativo é uma definição-base e o passivo, uma especialização. `É fonte derivativa de` preserva proveniência produtiva: seu polo ativo é a fonte e o passivo, o resultado criado a partir dela. Esta última não transmite classificação intrínseca por padrão.

Cada definidor concreto da família deve declarar:

- se é instanciável;
- se transmite ancestralidade classificatória;
- se transmite estrutura, capacidades ou restrições;
- se estabelece somente proveniência;
- quais regimes admite em cada polo;
- se sua rede deve ser acíclica.

Pertencer à família de `define` não basta para participar do fechamento classificatório. Somente descendentes que declarem preservar ancestralidade classificatória podem projetar classificações sobre instâncias.

Os polos dessas relações obedecem a restrições axiomáticas:

- em `é base conceitual para`, um axioma pode ocupar o polo ativo diante de outro axioma ou de um definidor; um definidor pode servir de base para outro definidor, mas nunca para um axioma;
- em `instancia`, o polo ativo é obrigatoriamente uma instância e o polo passivo é obrigatoriamente um definidor com capacidade `instanciável`;
- cada instância participa como polo ativo de uma e somente uma relação `instancia`.

As leituras inversas são projeções dos mesmos fatos e não criam relações adicionais.

Para interromper a regressão de relações que precisariam instanciar a si próprias, o núcleo reconhece `define`, `instancia` e o vocabulário relacional axiomático inicial. As relações concretas ordinárias obedecem ao mecanismo de instanciação relacional; relações abstratas organizam famílias, mas não recebem instâncias diretamente.

Também integram a base axiomática os definidores universais necessários para distinguir `é copiado por`, `é derivado de`, `é extraído de`, continência e fundamentação. A decomposição exata desse vocabulário ainda pode ser refinada, mas essas diferenças semânticas devem existir na camada axiomática. Relações específicas de aplicação descendem dessas bases sem se tornarem axiomas. `Dá amparo normativo a`, por exemplo, pode descender da relação axiomática geral `fundamenta`.

## Nomenclatura das relações

Todo rótulo de relação deve formar uma proposição completa e inequívoca quando inserido entre os polos. Deve-se evitar a preposição `de` na leitura direta quando ela puder sugerir posse, composição nominal ou direção diferente da relação pretendida. A substituição não é automática: `de` permanece adequado quando sua função relacional é clara.

```text
Filtro ──é base conceitual para──> Filtro de artefatos
Filtro de artefatos ──é especialização de──> Filtro

Relatório ──é fonte derivativa de──> Resumo
Resumo ──é derivado de──> Relatório
```

`É base conceitual para`, e não `é base conceitual de`, torna explícita a direção para a especialização. Em `é fonte derivativa de`, a preposição permanece porque a construção identifica a fonte do resultado sem ambiguidade relevante.

As leituras *forward* e *backward*, no singular e no plural, devem ser testadas com exemplos concretos. Se não for possível identificar pela frase quem exerce cada papel, o rótulo ainda não é suficientemente preciso.

## Polos e leituras bipolares

Toda relação bipolar possui um polo ativo e um polo passivo. Na leitura direta, o polo ativo fica à esquerda e o polo passivo à direita:

```text
Polo ativo ──label forward──> Polo passivo
```

Quando o definidor admitir leitura inversa, invertem-se a ordem dos polos e o rótulo utilizado:

```text
Polo passivo ──label backward──> Polo ativo
```

A leitura inversa apresenta outra perspectiva linguística do mesmo fato. Ela não cria uma segunda instância relacional nem altera qual artefato ocupa cada polo na relação armazenada.

## Contrato semântico do definidor de relação bipolar

Um definidor de relação bipolar deve declarar, ao menos, os seguintes campos ou propriedades conceituais:

- significado do polo ativo;
- significado do polo passivo;
- direcionalidade: unidirecional, bidirecional obrigatória ou bidirecional facultativa;
- indicação de que admite leitura *backward*;
- `label` de leitura *forward* no singular;
- `label` de leitura *forward* no plural;
- `label` de leitura *backward* no singular;
- `label` de leitura *backward* no plural;
- cardinalidade;
- filtros de admissibilidade e inadmissibilidade para cada polo;
- regras adicionais de unicidade, criação e validação.

Se a leitura *backward* for admitida e o rótulo correspondente não tiver sido definido, o sistema deve usar como *fallback* o rótulo *forward* correspondente seguido de “inversa”. Essa composição é uma salvaguarda de apresentação; um rótulo inverso semanticamente próprio continua preferível.

Os rótulos no singular e no plural permitem formular textos conforme o número gramatical do polo que ocupa a posição de sujeito: o polo ativo na leitura *forward* e o polo passivo na leitura *backward*.

Direcionalidade e possibilidade de leitura inversa são propriedades distintas. A direcionalidade descreve a reciprocidade semântica prevista pelo definidor; a leitura inversa determina se o mesmo fato pode ser apresentado a partir do polo passivo. O significado operacional exato das modalidades bidirecionais ainda deverá ser refinado antes de sua implementação.

## Filtros de artefatos

Um **filtro** é uma definição determinística reutilizável que avalia um candidato em determinado contexto e instante. Filtros não se limitam à construção dos polos de uma relação: podem orientar descoberta, ordenação, seleção, validação, persistência, execução, leitura posterior e auditoria.

O vocabulário axiomático inicial começa por:

```text
Filtro [axioma]
└── é base conceitual para → Filtro de artefatos [axioma]
```

`Filtro` define originalmente três dimensões, herdadas por `Filtro de artefatos` e por seus descendentes:

| Dimensão | Valores admitidos | Pergunta respondida |
| --- | --- | --- |
| Polaridade | `inclusão`, `exclusão` | O filtro favorece ou afasta o subconjunto delimitado? |
| Força | `obrigatória`, `preferencial` | O resultado vincula ou apenas orienta o consumidor? |
| Excepcionabilidade | `estrita`, `excepcionável`, `não se aplica` | Uma inconformidade obrigatória pode ser deliberadamente superada? |

`Não se aplica` é valor semântico explícito, distinto de ausência ou desconhecimento. Força `obrigatória` exige excepcionabilidade `estrita` ou `excepcionável`; força `preferencial` exige `não se aplica`, pois afastar uma preferência não constitui exceção.

### Perfis de filtro

Os perfis iniciais de segunda geração herdam as três dimensões e fixam seus valores:

| Perfil | Polaridade | Força | Excepcionabilidade |
| --- | --- | --- | --- |
| Filtro requerido estrito | inclusão | obrigatória | estrita |
| Filtro requerido excepcionável | inclusão | obrigatória | excepcionável |
| Filtro preferencial inclusivo | inclusão | preferencial | não se aplica |
| Filtro preferencial exclusivo | exclusão | preferencial | não se aplica |
| Filtro proibitivo estrito | exclusão | obrigatória | estrita |
| Filtro proibitivo excepcionável | exclusão | obrigatória | excepcionável |

Essa composição aproveita a polihierarquia classificatória sem confundir dimensões independentes. Novos perfis somente devem ser criados quando representarem uma combinação coerente e necessária.

### Definidor e instância de filtro

Um perfil pode servir de base conceitual para definidores de filtro de domínio. Cada ocorrência concreta instancia exatamente um desses definidores e contém seus parâmetros de aplicação:

```text
Filtro requerido estrito
  └── é base conceitual para → Integra atualmente o quadro pessoal de uma organização
        └── é instanciado por → Integra atualmente o quadro pessoal do SRO/4
```

O definidor estabelece a regra reutilizável; a instância configurada informa organização, contexto, instante de referência, versão, parâmetros e outras condições aplicáveis. Uma mesma instância pode ser reutilizada por diferentes consumidores.

Filtros de artefatos podem considerar, isolada ou conjuntamente:

- regime ontológico;
- definidor imediato instanciado pelo candidato;
- ancestralidade classificatória desse definidor;
- classificações e atributos do artefato;
- relações já mantidas pelo artefato;
- integração ao quadro pessoal de organização, aplicação ou contexto determinado;
- validade temporal dos fatos consultados;
- outras condições declaradas pelo definidor do filtro.

Uma relação de quadro pessoal, por exemplo, pode usar a leitura direta `Pessoa ──integra o quadro pessoal de──> Organização` e a leitura inversa `Organização ──possui em seu quadro pessoal──> Pessoa`. O vínculo é relacional e temporal; não deve ser reduzido a uma propriedade booleana da pessoa.

### Resultado da avaliação

Uma avaliação retorna um dos seguintes resultados:

```text
conforme | inconforme | indeterminado
```

O resultado deve ser acompanhado, quando cabível, de motivos, fatos consultados, parâmetros, instante, versão do filtro, dependências e indicação de erro ou insuficiência informacional. `Indeterminado` não equivale silenciosamente a `conforme`: em filtro obrigatório, não autoriza por si só persistência ou ação; em filtro preferencial, deve permanecer distinguível dos outros resultados. O consumidor pode refinar esse tratamento dentro dos limites autorizados pelo perfil.

### Comportamento dos perfis

| Perfil | Seleção inconforme | Confirmação expressa | Justificativa |
| --- | --- | --- | --- |
| Requerido estrito | vedada | não se aplica | não se aplica |
| Requerido excepcionável | admitida excepcionalmente | obrigatória | obrigatória |
| Preferencial inclusivo | admitida | dispensada | dispensada |
| Preferencial exclusivo | admitida | dispensada | dispensada |
| Proibitivo estrito | vedada | não se aplica | não se aplica |
| Proibitivo excepcionável | admitida excepcionalmente | obrigatória | obrigatória |

Filtros estritos devem excluir candidatos inelegíveis da descoberta ordinária e impedir sua persistência. Filtros obrigatórios excepcionáveis também ocultam inconformes por padrão, mas podem permitir que o usuário os revele e selecione mediante alerta, confirmação expressa e justificativa persistida. Filtros preferenciais orientam exibição ou ordenação sem exigir confirmação nem justificativa para seu afastamento.

Quando um resultado inconforme tiver sido admitido, leituras posteriores devem tornar a inconformidade e, se existente, sua justificativa acessíveis. Um texto exibido ao passar o ponteiro pode ser um recurso de interface, mas a exigência conceitual é não ocultar do usuário o afastamento relevante.

## Consumidores e fases de aplicação

O **consumidor de filtro** é o descritor persistido do campo, polo, ação, workflow, consulta ou outra operação que declara utilizar determinada instância de filtro:

```text
Descritor do consumidor ──aplica──> Instância de filtro
```

O resolvedor determinístico não escolhe arbitrariamente a regra. Em tempo de execução, ele lê o definidor do artefato ou da operação, encontra o descritor consumidor, recupera a instância de filtro associada e a executa no contexto corrente.

Podem consumir filtros, inicialmente:

- polos de relações bipolares;
- componentes de relações multipolares;
- campos universais semanticamente especializados;
- campos específicos;
- definidores de artefato;
- etapas de workflow;
- resolvedores determinísticos de busca ou ação;
- validadores anteriores à persistência;
- consultas preconcebidas ou *ad hoc* parametrizadas.

O consumidor pode declarar uma ou mais fases de atuação: descoberta, enumeração, ordenação, recomendação, seleção, validação, persistência, execução de ação, leitura posterior, auditoria e revalidação. O filtro deve ser reavaliado imediatamente antes de qualquer persistência ou ação cujas consequências dependam de sua conformidade.

## Exceções e inconformidades supervenientes

Uma seleção contrária a filtro obrigatório excepcionável produz um **artefato de exceção** auditável. Ele pode ser modelado como relação multipolar que reúne, ao menos:

```text
Exceção de filtro
├── excepciona → Filtro aplicado
├── autoriza seleção de → Artefato inconforme
├── aplica-se a → Consumidor, relação ou ação resultante
├── foi decidida por → Usuário do sistema
├── justificativa → Texto
├── resultado original → inconforme
├── instante da avaliação
├── instante da decisão
├── versão do filtro
└── contexto e parâmetros da avaliação
```

Seu descritor textual de exibição deve seguir a forma:

> Exceção do filtro 18 aplicado ao artefato X, criada em `<data>` por `<usuário do sistema>`.

O descritor é calculado a partir dos campos estruturados e não os substitui como fonte da informação.

Uma **inconformidade superveniente** é diferente: a seleção era conforme quando realizada, mas tornou-se inconforme após mudança dos fatos, do contexto ou da validade temporal. Ela não cria retroativamente uma exceção praticada pelo usuário. Seu registro deve preservar a avaliação original, o fato superveniente, os instantes relevantes, o filtro e sua versão, os efeitos administrativos e eventual necessidade de regularização.

## Cardinalidade e unicidade do vínculo

A cardinalidade é uma restrição operacional sobre a criação de instâncias relacionais:

- **`1:1`** — cada artefato do polo ativo pode relacionar-se com, no máximo, um artefato do polo passivo, e cada passivo pode relacionar-se com, no máximo, um ativo;
- **`1:n`** — um artefato do polo ativo pode relacionar-se com vários passivos, mas cada passivo pode relacionar-se com, no máximo, um ativo;
- **`n:1`** — vários artefatos ativos podem relacionar-se com um passivo, mas cada ativo pode relacionar-se com, no máximo, um passivo;
- **`n:n`** — múltiplos artefatos podem relacionar-se em ambos os polos.

Em todas as modalidades, é vedada a repetição da mesma relação entre o mesmo par de artefatos. Restrições adicionais podem tornar a cardinalidade mais estreita em determinado contexto, mas não ampliá-la além do que o definidor autoriza.

## Relações multipolares por agregação

Uma relação multipolar é uma instância relacional com identidade própria que agrega duas ou mais instâncias de relações bipolares. Cada componente liga o artefato agregador a um participante do fato administrativo. A agregação instancia exatamente um definidor multipolar; cada componente bipolar instancia seu respectivo definidor e é persistido como relação real, consultável e validável.

```text
Definidor de relação multipolar
├── agrega → Definidor bipolar A
├── agrega → Definidor bipolar B
├── declara → campos próprios
├── declara → regras conjuntas
└── declara → leitura geral
```

O definidor multipolar deve declarar:

- quais definidores bipolares compõem a agregação;
- nome, significado, obrigatoriedade e cardinalidade de cada componente;
- filtros de admissibilidade de seus participantes;
- campos próprios da agregação;
- regras conjuntas entre componentes;
- template textual da leitura geral;
- leituras alternativas por participante focal;
- regras de omissão e ordenação de componentes facultativos.

### Exemplo de fiscalização técnica

No sroHUB, `Fiscalização técnica de contrato` pode ser um definidor de relação multipolar. Uma instância concreta agrega componentes bipolares:

```text
Fiscalização técnica nº 7
├── tem contrato fiscalizado → Contrato nº 52/2026
├── tem fiscal técnica titular → Ten Izabela
├── tem fiscal técnico substituto → Ten Fulano
└── tem publicação designadora → Publicação nº 17
```

| Componente bipolar | Cardinalidade indicativa | Filtro principal |
| --- | ---: | --- |
| contrato fiscalizado | `1` | instância de `Contrato` ou de definidor descendente |
| fiscal técnico titular | `1` | instância de `Pessoa física` elegível |
| fiscal técnico substituto | `0..n` | instância de `Pessoa física` elegível |
| publicação designadora | `1..n` | instância de `Publicação em boletim` ou descendente |

A publicação mantém uma relação própria com seu contêiner institucional:

```text
Publicação nº 17 ──está publicada em──> Boletim regional nº 24
```

A fiscalização também pode possuir campos que não pertencem isoladamente a nenhum participante ou componente, como data inicial, data final e observações. Seu estado atual pode ser calculado em tempo de execução a partir desses campos e de eventos como revogação ou substituição.

Regras conjuntas pertencem ao definidor multipolar. Ele pode vedar que titular e substituto sejam a mesma pessoa, exigir que fiscais integrem atualmente o quadro da organização e assegurar que a publicação designadora tenha vigência compatível.

### Leituras componentes e leitura geral

Cada componente pode ser lido isoladamente:

```text
Fiscalização técnica nº 7 ──tem fiscal técnica titular──> Ten Izabela
Ten Izabela ──é fiscal técnica titular em──> Fiscalização técnica nº 7
```

O definidor multipolar oferece uma leitura geral que combina componentes e campos:

> Ten Izabela atua como fiscal técnica titular do Contrato nº 52/2026, tendo Ten Fulano como substituto, conforme a Publicação nº 17.

Relações convenientes entre participantes podem ser projeções determinísticas da agregação. `Ten Izabela ──fiscaliza──> Contrato nº 52/2026`, por exemplo, pode ser calculada a partir dos dois componentes correspondentes, sem persistência redundante como outro fato.

O exemplo pertence à linguagem do sroHUB. O ManageHUB fornece o mecanismo universal de agregação, filtros, cardinalidades e leituras, sem incorporar as regras específicas do SRO/4.

## Proveniência e ciclo de vida

Uma instância relacional deve poder preservar, conforme sua definição e relevância administrativa:

- identidade persistente;
- autoria ou agente responsável pela criação;
- fonte e método de obtenção;
- data de criação e período de validade;
- confiança ou grau de certeza;
- indicação de inferência automática ou confirmação humana;
- histórico de revisão, substituição, revogação ou encerramento.

Essas propriedades permitem distinguir um fato vigente, uma afirmação histórica, uma hipótese inferida e um vínculo posteriormente invalidado sem apagar o contexto em que cada um existiu.

## Continência e proveniência informacional

O vocabulário axiomático inicial distingue relações-base de continência, extração, derivação, cópia e fundamentação. Relações específicas podem descendê-las conforme a família semântica aplicável.

Relações candidatas de continência incluem:

```text
Informação ──está contida em──> Contêiner
Contêiner ──integra──> Portador
Arquivo ──está anexado a──> Mensagem
Portador ──circula por──> Canal
Mensagem ──é recebida por──> Endpoint
Arquivo ──possui formato──> Formato
Publicação ──está publicada em──> Boletim
```

Relações candidatas de proveniência e fundamentação incluem:

```text
Informação ──é extraída de──> Fonte
Fonte ──é fonte derivativa de──> Novo artefato
Novo artefato ──é derivado de──> Fonte
Fonte ──fundamenta──> Artefato fundamentado
Informação normativa ──fundamenta──> Procedimento
```

**Extração** significa que algo já contido em um locus passa a existir, em substituição ou complementação, em outro locus. O conteúdo pode permanecer nos dois lugares. **Derivação** significa que algo novo é criado usando uma fonte como base; o resultado não estava necessariamente contido nela.

```text
Informação “data de expiração” ──é extraída de──> Contrato
Relatório original ──é fonte derivativa de──> Resumo analítico
Resumo analítico ──é derivado de──> Relatório original
```

Todo artefato resultante de promoção informacional deve manter ao menos uma relação explícita de proveniência com o artefato hospedeiro ou com a fonte que permitiu sua individualização.

## Princípio da especialidade relacional

Quando mais de uma relação puder descrever um vínculo, deve prevalecer o definidor semanticamente mais específico que represente integralmente o fato pretendido.

```text
DIEx nº XXX/DOM ──dá amparo normativo a──> Informação normativa
```

Essa relação é preferível a `é extraída de` quando a intenção é registrar a autoridade normativa do DIEx. As duas relações podem coexistir somente quando expressarem fatos materialmente distintos e ambos forem relevantes: uma registra a localização original da informação; a outra, sua força de fundamentação. Não se devem persistir relações redundantes apenas para repetir o mesmo significado em diferentes graus de generalidade.

## Cópia deliberada

Em regra, o sistema veda representações duplicadas do mesmo referente. Quando uma cópia deliberada for autorizada, sua proveniência deve ser preservada pela relação canônica:

```text
Artefato de origem ──é copiado por──> Artefato copiado
Artefato copiado ──é cópia de──> Artefato de origem
```

`É copiado por` é a leitura *forward* e `é cópia de` sua leitura *backward*. Ambas representam uma única instância relacional. Não deve existir outro definidor concorrente que expresse a mesma semântica de duplicação.

A cópia recebe identidade própria e pode divergir de sua origem. A relação registra de onde ela proveio, mas não afirma, por si só, que origem e cópia continuam semanticamente equivalentes.

`É copiado por` aplica-se exclusivamente à reprodução deliberada de um artefato em outro. Não representa extração, derivação, promoção informacional, mudança de tipologia ou criação de artefato semanticamente distinto a partir de parte do conteúdo de outro.

```text
Documento A ──é copiado por──> Documento B       ✓
DIEx ──é copiado por──> Informação normativa      ✗
```

Promoção é uma operação do sistema, não uma relação única. Ela cria um artefato e registra a relação de proveniência mais específica aplicável, como `é extraído de`, `é derivado de` ou `é amparado por`.

## Questões ainda abertas

- Qual é o significado operacional exato de bidirecionalidade obrigatória e facultativa?
- Quais propriedades de proveniência serão universais e quais serão exigidas apenas por determinados definidores de relação?
- Quais descendentes concretos adicionais devem integrar a família axiomática de `define` e quais propriedades cada um transmite?
- Como compor filtros herdados de múltiplos ancestrais e resolver eventuais conflitos?
- Qual tratamento padrão deve ser aplicado a `indeterminado` em cada fase e perfil de filtro?
- Como versionar filtros sem alterar retroativamente a interpretação das avaliações e exceções já registradas?
- Quando uma inconformidade superveniente exige apenas alerta, regularização obrigatória ou invalidação do vínculo?
- Em quais circunstâncias uma relação inferida pode produzir efeitos antes de confirmação humana?
- Quais outros definidores formarão o vocabulário axiomático mínimo de continência e fundamentação?
- Como definir relações multipolares com número variável de componentes sem perder validação e legibilidade?
