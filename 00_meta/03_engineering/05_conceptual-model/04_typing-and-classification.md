# Tipagem e classificação

> Estado: formulação em amadurecimento. Este documento registra o entendimento atual e não constitui, por si só, uma decisão de implementação.

## Propósito

Esta área descreve como classificações e capacidades especializam o significado e o comportamento dos artefatos sem alterar os [[01_artifact-foundation#Regime ontológico|regimes ontológicos]] fundamentais. Entre essas capacidades está a de um definidor funcionar como template para a criação orientada de novas instâncias.

## Classificação multidimensional

A taxonomia lineana inspira a ordenação por generalização e especialização, a herança de significado e a localização de um elemento dentro de uma cadeia classificatória. O ManageHUB, porém, não adota os níveis biológicos, uma quantidade fixa de níveis, uma única árvore ou a exigência de um único ancestral.

O modelo usa **dimensões classificatórias**: perspectivas semanticamente autônomas pelas quais definidores e, por projeção, suas instâncias podem ser compreendidos. Cada dimensão responde a uma pergunta diferente e pode possuir profundidade, cardinalidade e regras próprias.

| Dimensão | Pergunta respondida | Comportamento | Exemplos |
| --- | --- | --- | --- |
| Regime ontológico | Qual posição o artefato ocupa no modelo? | Universal, obrigatório e exclusivo | axioma `define`; definidor `Contrato`; instância `Contrato nº 52/2026` |
| Natureza ontológica | Que tipo fundamental de ente o definidor representa? | Intrínseca ao definidor e projetada nas instâncias | pessoa física; instrumento jurídico |
| Função administrativa | Para que o artefato serve? | Herdável ou composta | documento comprobatório; instrumento autorizativo |
| Tipologia especializada | Qual definição imediata governa a instância? | Corresponde ao único definidor instanciado | contrato administrativo; publicação em boletim |
| Papel contextual | Que papel exerce em determinada situação? | Relacional, múltiplo e possivelmente temporal | fiscal técnico titular; substituto; aprovador |
| Estado derivado | Em que condição calculável se encontra? | Resolvido em tempo de execução a partir de fatos persistidos | contrato vigente; contrato expirado |
| Proveniência | Como surgiu ou entrou no sistema? | Própria ou relacional | importado do SPED; extraído de DIEx |
| Governança | Que tratamento administrativo exige? | Herdada, própria ou contextual | ostensivo; restrito; retenção permanente |

As dimensões não precisam usar níveis equivalentes. A estrutura genérica abaixo descreve uma progressão possível, não patamares obrigatórios:

```text
Dimensão
  └── categoria geral
        └── especialização
              └── definidor aplicável
```

## Polihierarquia e família de definição

As categorias de uma dimensão podem formar uma rede dirigida acíclica com múltiplos ancestrais e múltiplos descendentes:

```text
A ──é base conceitual para──> B
A ──é base conceitual para──> C
B ──é base conceitual para──> D
C ──é base conceitual para──> D
```

`Define` é o axioma abstrato e não instanciável que organiza uma família de relações de fundamentação. As arestas classificatórias concretas usam `é base conceitual para`, cuja leitura inversa é `é especialização de`.

O fechamento classificatório abrange somente relações cujos definidores descendam de `define` e declarem transmitir ancestralidade classificatória, herança e aciclicidade. Pertencer à família não basta: `é fonte derivativa de`, por exemplo, registra proveniência produtiva e não torna o resultado uma especialização da fonte.

## Natureza projetada pelo definidor

A natureza ontológica é intrínseca aos definidores. Uma instância não escolhe nem acumula naturezas independentes: recebe sua natureza do único definidor que instancia e dos ancestrais desse definidor.

```text
Contrato nº 52/2026
  └── instancia → Contrato administrativo
                       └── é especialização de → Instrumento contratual
                                                    └── é especialização de → Instrumento jurídico
```

O contrato pode ser recuperado como `Contrato administrativo`, `Instrumento contratual` ou `Instrumento jurídico`, sem possuir três relações de instanciação.

Uma instância `X` satisfaz uma classificação `C` quando:

```text
X ──instancia──> D
```

e `D = C` ou existe um caminho válido na família de definição:

```text
C ──é base conceitual para+──> D
```

Todo caminho válido deve ser composto apenas por relações concretas que transmitam ancestralidade classificatória.

## Classificações intrínsecas e contextuais

Uma classificação **intrínseca** é declarada ou herdada pelo definidor e projetada sobre todas as suas instâncias. Ela informa o que o artefato é por definição.

Uma classificação **contextual** decorre de relações, papéis, circunstâncias temporais ou resultados determinísticos. Ela informa o que o artefato é ou faz em um contexto e pode surgir ou cessar sem alterar sua identidade ou seu definidor imediato.

```text
Ten Izabela
├── instancia → Pessoa física
├── integra o quadro pessoal de → SRO/4
└── é fiscal técnica titular em → Fiscalização técnica nº 7
```

`Pessoa física` é classificação intrínseca. `Integrante do quadro do SRO/4` e `fiscal técnica titular` são classificações contextuais produzidas por relações concretas.

## Consultas por ancestralidade

Consultas podem combinar relações concretas com o fechamento classificatório dos definidores:

```text
Instrumento jurídico
├── é base conceitual para → Instrumento contratual
│   └── é base conceitual para → Contrato
└── é base conceitual para → Publicação oficial
    └── é base conceitual para → Publicação em boletim
```

Considere a relação multipolar:

```text
Fiscalização técnica nº 7
├── tem contrato fiscalizado → Contrato nº 52/2026
├── tem fiscal técnica titular → Ten Izabela
└── tem publicação designadora → Publicação em boletim nº 17
```

A consulta “localize os instrumentos jurídicos associados à Ten Izabela” pode retornar o contrato e a publicação. Conceitualmente, o sistema:

1. resolve a identidade de Ten Izabela;
2. encontra relações bipolares e multipolares em que ela participa;
3. recupera os demais participantes relevantes;
4. identifica o definidor imediato de cada participante;
5. percorre o fechamento classificatório da família de `define`;
6. retorna as instâncias que satisfazem `Instrumento jurídico`.

## Filtros como classificação polihierárquica

O axioma `Filtro` estabelece as dimensões `polaridade`, `força` e `excepcionabilidade`. `Filtro de artefatos`, também axioma, é sua primeira especialização e transmite essas dimensões aos definidores de segunda geração:

```text
Filtro
└── é base conceitual para → Filtro de artefatos
      ├── é base conceitual para → Filtro requerido estrito
      ├── é base conceitual para → Filtro requerido excepcionável
      ├── é base conceitual para → Filtro preferencial inclusivo
      ├── é base conceitual para → Filtro preferencial exclusivo
      ├── é base conceitual para → Filtro proibitivo estrito
      └── é base conceitual para → Filtro proibitivo excepcionável
```

| Definidor de segunda geração | Polaridade | Força | Excepcionabilidade |
| --- | --- | --- | --- |
| Filtro requerido estrito | inclusão | obrigatória | estrita |
| Filtro requerido excepcionável | inclusão | obrigatória | excepcionável |
| Filtro preferencial inclusivo | inclusão | preferencial | não se aplica |
| Filtro preferencial exclusivo | exclusão | preferencial | não se aplica |
| Filtro proibitivo estrito | exclusão | obrigatória | estrita |
| Filtro proibitivo excepcionável | exclusão | obrigatória | excepcionável |

Os atributos pertencem originalmente a `Filtro`, são herdados por `Filtro de artefatos` e recebem valores constantes nos definidores de segunda geração. `Não se aplica` é um valor explícito: distingue uma dimensão semanticamente inaplicável de uma configuração ausente ou desconhecida.

A polihierarquia permite que filtros de domínio especializem esses perfis e combinem regras reutilizáveis sem transformar força, polaridade e excepcionabilidade em etiquetas independentes de suas definições. A semântica operacional completa está em [[02_relationships-and-provenance#Filtros de artefatos|Filtros de artefatos]].

## Estados persistidos e derivados

Um estado pode decorrer de atributo universal, atributo específico, relação direta, participação multipolar, cadeia de relações ou cálculo determinístico. O sistema deve persistir os fatos primários e evitar persistir como fato independente um estado que possa ser obtido de forma confiável em tempo de execução.

Para um contrato, por exemplo, o campo universal `data final` pode receber do definidor `Contrato` a semântica de `data de expiração da vigência`:

```text
Contrato nº 52/2026
  └── data final → 31/12/2026
```

Um resolvedor pode calcular, em um exemplo mínimo:

```text
vigente(contrato, instante) = instante <= contrato.data_final
```

A regra efetiva pode também considerar data inicial, prorrogações, suspensões, rescisões, encerramento antecipado e ausência de dados. Por isso, `vigente`, `ainda não iniciado`, `próximo do vencimento`, `suspenso`, `expirado`, `encerrado` ou `indeterminado` são resultados possíveis da avaliação, não necessariamente valores persistidos no contrato.

Necessidades informacionais recorrentes podem ser formalizadas como [[05_information-and-containment#Resolvedores determinísticos|resolvedores determinísticos]], preservando regras reproduzíveis sem confundi-las com inferências generativas.

## Templates e promoção de instância

Um **template** é um artefato no regime `definidor` que oferece conteúdo, estrutura, valores iniciais, metadados ou regras reutilizáveis para orientar a criação ou configuração de instâncias. Template não constitui um regime ontológico próprio: é uma capacidade de um definidor.

Todo template deve ser instanciável. A recíproca não é necessária: um definidor pode autorizar instâncias sem oferecer conteúdo ou configuração reutilizável como template.

### Tornar uma instância um template

Uma instância não pode mudar diretamente para o regime `definidor`, pois isso apagaria a distinção entre a ocorrência concreta e a abstração reutilizável. A operação de sistema apresentada ao usuário como **“tornar-se template”** é, portanto, uma promoção por criação: preserva a instância de origem e cria um novo artefato definidor.

O novo definidor possui ancestralidade múltipla:

```text
Definidor-base de template ──é base conceitual para──> Novo definidor template
Definidor da instância de origem ──é base conceitual para──> Novo definidor template
```

O primeiro ancestral transmite a capacidade e as regras gerais de template. O segundo preserva a natureza semântica da origem — documento, comunicação, tarefa ou outra definição aplicável. O novo artefato deve ser marcado como `template` e, por implicação, como `instanciável`.

A operação transfere da instância de origem:

- o conteúdo selecionado para reutilização;
- os metadados autorizados pela definição e pelo contexto;
- configurações que devam servir como valores iniciais das futuras instâncias.

Ela não copia a identidade persistente da origem. Estados operacionais, relações contextuais, dados pessoais, datas históricas e outros valores próprios daquela ocorrência somente podem ser transferidos quando houver autorização semântica e de governança explícita.

A proveniência deve ser preservada por uma relação de derivação, pois o resultado possui regime e finalidade semanticamente distintos da origem:

```text
Instância de origem ──é fonte derivativa de──> Novo definidor template
Novo definidor template ──é derivado de──> Instância de origem
```

Essa relação registra a origem da promoção, mas não torna o novo definidor uma instância da ocorrência original. O novo artefato possui identidade, regime e finalidade próprios.

### Exemplo

Considere um relatório de vistoria concreto, instância do definidor `Relatório de vistoria`. Se o usuário solicitar que ele “se torne template”, o sistema cria um novo definidor, por exemplo `Template de relatório de vistoria da unidade`, com esta fundamentação:

```text
Template ──é base conceitual para──> Template de relatório de vistoria da unidade
Relatório de vistoria ──é base conceitual para──> Template de relatório de vistoria da unidade
Relatório nº 42 ──é fonte derivativa de──> Template de relatório de vistoria da unidade
Template de relatório de vistoria da unidade ──é derivado de──> Relatório nº 42
```

O novo definidor pode conservar seções, instruções, campos iniciais e metadados reutilizáveis do relatório nº 42, enquanto exclui datas da ocorrência, assinaturas, participantes e demais informações que não devam propagar-se. As futuras instâncias criadas a partir dele continuam sendo ocorrências concretas fundamentadas por esse único definidor template.

## Questões ainda abertas

- Quais dimensões classificatórias integrarão os axiomas e quais poderão ser criadas por aplicações?
- Quais dimensões exigirão classificação única, múltipla ou obrigatória?
- Como serão combinadas regras herdadas de múltiplos ancestrais, inclusive os dois ancestrais de um template, quando houver conflito?
- Quais estados derivados devem ser materializados para auditoria ou desempenho?
- Quais atributos e relações são copiáveis por padrão e quais exigem autorização explícita?
- Que permissões autorizam a promoção e a posterior alteração de um template?
- Como versionar um template sem modificar retroativamente as instâncias já criadas?
