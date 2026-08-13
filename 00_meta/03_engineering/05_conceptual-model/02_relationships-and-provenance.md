# Relações e proveniência

> Estado: formulação em amadurecimento. Este documento registra o entendimento atual e não constitui, por si só, uma decisão de implementação.

## Propósito

Relações tornam explícitos os fatos que conectam artefatos. Elas permitem preservar não apenas que dois artefatos estão associados, mas o significado do vínculo, os papéis exercidos por seus participantes, sua origem, sua validade e as regras que autorizam sua existência.

Toda relação concreta é tratada como artefato de primeira classe: um vínculo identificável, validável, consultável e auditável. O modelo distingue:

- **definidor de relação** — artefato que estabelece a semântica, os polos, as leituras, a cardinalidade e as restrições de uma natureza de relação;
- **instância relacional** — vínculo concreto que instancia exatamente um definidor de relação e conecta artefatos admitidos em seus polos.

## Relações axiomáticas

`define` e `instancia` são definidores de relação no regime ontológico `axioma`. Sua interpretação integra a base mínima do sistema:

- `define` estabelece ancestralidade funcional ou semântica entre axiomas e definidores;
- `instancia` liga uma ocorrência concreta ao único definidor instanciável que ela materializa.

Os polos dessas relações obedecem a restrições axiomáticas:

- em `define`, um axioma pode ocupar o polo ativo diante de outro axioma ou de um definidor; um definidor pode definir outro definidor, mas nunca um axioma;
- em `instancia`, o polo ativo é obrigatoriamente uma instância e o polo passivo é obrigatoriamente um definidor com capacidade `instanciável`;
- cada instância participa como polo ativo de uma e somente uma relação `instancia`.

As leituras `é definido por` e `é instanciada por` são projeções inversas desses mesmos fatos. Elas não criam relações adicionais.

Para interromper a regressão de relações que precisariam instanciar a si próprias, ocorrências de `define` e `instancia` são reconhecidas pelo núcleo como vínculos axiomáticos. As demais relações concretas obedecem ao mecanismo ordinário de instanciação relacional.

## Polos e leituras

Toda relação possui um polo ativo e um polo passivo. Na leitura direta, o polo ativo fica à esquerda e o polo passivo à direita:

```text
Polo ativo ──label forward──> Polo passivo
```

Quando o definidor admitir leitura inversa, invertem-se a ordem dos polos e o rótulo utilizado:

```text
Polo passivo ──label backward──> Polo ativo
```

A leitura inversa apresenta outra perspectiva linguística do mesmo fato. Ela não cria uma segunda instância relacional nem altera qual artefato ocupa cada polo na relação armazenada.

## Contrato semântico do definidor de relação

Um definidor de relação deve declarar, ao menos, os seguintes campos ou propriedades conceituais:

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

## Filtros dos polos

Cada polo possui filtros próprios de admissibilidade ou inadmissibilidade. Esses filtros podem considerar, isolada ou conjuntamente:

- regime ontológico;
- definidor imediato instanciado pelo artefato;
- ancestralidade desse definidor na rede de `define`;
- classificações e atributos do artefato;
- relações já mantidas pelo artefato;
- pertencimento a organização, aplicação ou contexto determinado;
- outras condições declaradas pelo definidor da relação.

Uma instância relacional somente pode ser criada quando os artefatos de ambos os polos satisfizerem todos os filtros aplicáveis.

### Exemplo no sroHUB

A relação específica `fiscaliza` pode ser definida no sroHUB com a seguinte leitura direta:

```text
Pessoa física vinculada ao SRO/4 ──fiscaliza──> Contrato
```

Nesse exemplo:

- o polo ativo deve ser uma instância de pessoa física;
- essa pessoa deve possuir uma relação de pertencimento válida ao SRO/4;
- o polo passivo deve ser uma instância da definição de contrato ou de um definidor descendente dela;
- qualquer regra adicional de vigência, impedimento ou exclusividade deve ser declarada pelo definidor de `fiscaliza`.

O exemplo pertence à linguagem do sroHUB. O ManageHUB fornece o mecanismo universal de filtros, polos e validação, sem incorporar as regras específicas do SRO/4.

## Cardinalidade e unicidade do vínculo

A cardinalidade é uma restrição operacional sobre a criação de instâncias relacionais:

- **`1:1`** — cada artefato do polo ativo pode relacionar-se com, no máximo, um artefato do polo passivo, e cada passivo pode relacionar-se com, no máximo, um ativo;
- **`1:n`** — um artefato do polo ativo pode relacionar-se com vários passivos, mas cada passivo pode relacionar-se com, no máximo, um ativo;
- **`n:1`** — vários artefatos ativos podem relacionar-se com um passivo, mas cada ativo pode relacionar-se com, no máximo, um passivo;
- **`n:n`** — múltiplos artefatos podem relacionar-se em ambos os polos.

Em todas as modalidades, é vedada a repetição da mesma relação entre o mesmo par de artefatos. Restrições adicionais podem tornar a cardinalidade mais estreita em determinado contexto, mas não ampliá-la além do que o definidor autoriza.

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

## Cópia deliberada

Em regra, o sistema veda representações duplicadas do mesmo referente. Quando uma cópia deliberada for autorizada, sua proveniência deve ser preservada pela relação canônica:

```text
Artefato de origem ──é copiado por──> Artefato copiado
Artefato copiado ──é cópia de──> Artefato de origem
```

`É copiado por` é a leitura *forward* e `é cópia de` sua leitura *backward*. Ambas representam uma única instância relacional. Não deve existir outro definidor concorrente que expresse a mesma semântica de duplicação.

A cópia recebe identidade própria e pode divergir de sua origem. A relação registra de onde ela proveio, mas não afirma, por si só, que origem e cópia continuam semanticamente equivalentes.

## Questões ainda abertas

- Qual é o significado operacional exato de bidirecionalidade obrigatória e facultativa?
- Quais propriedades de proveniência serão universais e quais serão exigidas apenas por determinados definidores de relação?
- Como representar relações com mais de dois participantes sem reduzir artificialmente sua semântica a pares?
- Como compor filtros herdados de múltiplos ancestrais e resolver eventuais conflitos?
- Em quais circunstâncias uma relação inferida pode produzir efeitos antes de confirmação humana?
