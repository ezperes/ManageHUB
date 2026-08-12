# Fundamento dos artefatos

> Estado: formulação em amadurecimento. Este documento registra o entendimento atual e não constitui, por si só, uma decisão de implementação.

## Propósito

O modelo conceitual parte da premissa de que o ManageHUB opera sobre representações informacionais de elementos relevantes de um contexto de gestão. Chamamos essas representações de **artefatos**.

Um artefato não se confunde com seu referente no mundo real. Uma pessoa, uma organização, um documento físico ou uma ocorrência existem independentemente do sistema; o artefato é o registro identificável, contextualizável e relacionável que os representa ou documenta.

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

## Regime ontológico

Todo artefato pertence a um dos seguintes regimes ontológicos:

- **Axioma** — fundamento interpretativo do sistema.
- **Definidor** — artefato abstrato que fornece ancestralidade funcional ou semântica a outros definidores.
- **Instância** — ocorrência concreta fundada em uma definição aplicável.

Os axiomas são artefatos visíveis e classificáveis, mas sua validade não depende de uma cadeia ordinária de definições internas. Eles constituem a raiz de bootstrap a partir da qual o sistema interpreta as demais definições, relações e instâncias.

Um definidor pode ter a capacidade de funcionar como **template**. Template não é um quarto regime: é uma capacidade de um definidor reutilizável para orientar a criação ou configuração de instâncias.

Todo definidor também deve declarar se é **instanciável**. Essa capacidade, que poderá corresponder a um atributo próprio do definidor, autoriza ou veda que instâncias concretas o usem como base imediata em uma relação de instanciação. Um definidor não instanciável ainda pode definir outros definidores, transmitir semântica, fornecer estrutura ou atuar como componente de um template, mas não pode receber diretamente uma relação `instancia`.

Template e instanciabilidade são capacidades distintas. Um definidor pode ser reutilizável como template, instanciável, ambos ou nenhum, conforme a semântica que sua definição determinar.

## Ancestralidade de definições

A relação axiomática `define` expressa ancestralidade funcional ou semântica entre definidores:

```text
Definição-base ──define──> Definição derivada
Definição derivada ──é definida por──> Definição-base
```

Uma definição derivada herda, especializa ou compõe significado, estrutura, capacidades, restrições ou comportamento de sua definição-base. A relação `é definido por` é a leitura inversa de `define`.

O grafo formado por `define` é uma rede dirigida acíclica (*directed acyclic graph*, ou DAG) e deve terminar em um ou mais axiomas. Não se trata, portanto, de uma árvore: um definidor pode possuir múltiplos definidores-base e, simultaneamente, definir múltiplos descendentes. O que é vedado é que um definidor se torne ancestral de si mesmo, direta ou indiretamente.

```text
A ──define──> B
A ──define──> C
B ──define──> D
C ──define──> D
```

Nesse exemplo, `A` define diretamente `B` e `C`; `B` e `C` definem `D`. Assim, `D` possui dois ancestrais diretos e `A` é seu ancestral indireto. A rede admite herança múltipla e especializações paralelas porque nenhum caminho retorna de `D` para `A`, `B`, `C` ou para o próprio `D`.

Em termos semânticos, uma definição de **comunicação oficial** pode definir, em paralelo, as definições de **comunicação recebida** e **comunicação enviada**. Uma definição de **resposta formal recebida** pode então ser definida simultaneamente por ambas: herda a estrutura comum de comunicação oficial e especializa aspectos associados ao recebimento e à resposta.

Formalmente, não pode existir caminho de tamanho positivo como:

```text
A ──define+──> A
```

## Instanciação

Instanciação relaciona o plano abstrato ao plano concreto. Uma instância materializa uma definição aplicável, de modo análogo a um objeto em relação a uma classe na programação orientada a objetos.

```text
Instância concreta ──instancia──> Definição abstrata
Definição abstrata ──é instanciada por──> Instância concreta
```

Na leitura orientada à instância, a mesma ideia pode ser expressa como: uma instância concreta **é instância de** uma definição abstrata. A escolha entre `instancia` e `é instância de` como nome canônico de armazenamento permanece aberta; ambas não devem ser tratadas como relações semânticas independentes.

Instanciação não é sinônimo de `define`:

- `define` liga uma definição a outra definição e transmite ancestralidade funcional ou semântica;
- `instancia` liga uma ocorrência concreta à definição que ela materializa.

Uma relação `instancia` somente é válida quando seu polo de origem está no regime `instância` e seu polo de destino está no regime `definidor` com a capacidade `instanciável` autorizada. A relação não é permitida apenas porque um artefato é um definidor; a autorização deve ser declarada pela própria definição.

Cada instância deve instanciar **uma e somente uma** definição. A cardinalidade imediata da relação é, portanto, `1` no polo da definição: uma instância não pode materializar diretamente múltiplos definidores. Ela pode, contudo, herdar fundamentação indireta de diversos ancestrais por meio da rede acíclica de `define` da única definição que instancia.

Uma instância pode estar diretamente ligada a uma definição especializada e, por sua cadeia de definições, possuir fundamentação indireta em múltiplos definidores e axiomas. Essa fundamentação deve poder ser percorrida e auditada sem exigir a materialização de cada vínculo indireto como um fato independente.

## Linhagem entre instâncias

Instâncias não instanciam outras instâncias. Ainda assim, uma instância pode manter relações de linhagem ou de contexto com outra instância, sem que isso altere a única definição da qual cada uma é instância.

Uma relação entre duas instâncias somente é válida quando existe um **definidor de relação** que a define e que admite artefatos do regime `instância` nos dois polos. Portanto, não basta que dois artefatos sejam instâncias para que possam ser ligados: a natureza, a direção, os polos permitidos e as regras do vínculo devem ser declarados pelo definidor da relação.

```text
Definidor de relação ──define──> Relação entre instâncias
Instância A ──[polo permitido]──> Relação definida ──[polo permitido]──> Instância B
```

As relações candidatas iniciais são:

```text
Instância derivada ──deriva de──> Instância de origem
Instância de origem ──é copiada por──> Instância copiada
Instância posterior ──serve de referência para──> Instância que a consulta
```

Essas relações têm semânticas distintas:

- **deriva de** preserva uma transformação ou continuidade: a instância derivada foi obtida a partir de outra, possivelmente com alterações;
- **é copiada por** registra a reprodução de uma instância por outra, sem afirmar que a cópia seja semanticamente uma nova definição;
- **serve de referência para** registra uso contextual, consulta ou inspiração, sem afirmar derivação nem cópia.

Por exemplo, um rascunho revisado pode derivar de um rascunho anterior, uma nova versão pode ser copiada de uma versão prévia e uma resposta pode usar uma comunicação anterior como referência. Em todos os casos, cada artefato continua sendo instância de seu definidor aplicável; as relações entre instâncias registram sua história operacional e seu contexto.

## Relações axiomáticas

As definições das relações `define`, `é definido por`, `instancia` e `é instanciada por` pertencem à base axiomática do sistema. Elas podem ser representadas e consultadas como artefatos, mas a interpretação de seu significado não depende de relações ordinárias adicionais.

```text
Axioma
  └── define → Definição-base
        └── define → Definição especializada
              └── é instanciada por → Instância concreta
```

## Questões ainda abertas

- Quais capacidades adicionais um definidor pode possuir além de funcionar como template e ser instanciável?
- Quais axiomas são estritamente necessários para iniciar o sistema e quais podem ser definições internas posteriores?
- Qual será a convenção canônica de direção e nome para a relação de instanciação?
- Como serão expressas composição, compatibilidade e conflito entre múltiplas definições-base?
