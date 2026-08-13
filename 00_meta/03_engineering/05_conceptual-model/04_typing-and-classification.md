# Tipagem e classificação

> Estado: formulação em amadurecimento. Este documento registra o entendimento atual e não constitui, por si só, uma decisão de implementação.

## Propósito

Esta área descreve como classificações e capacidades especializam o significado e o comportamento dos artefatos sem alterar os [[01_artifact-foundation#Regime ontológico|regimes ontológicos]] fundamentais. Entre essas capacidades está a de um definidor funcionar como template para a criação orientada de novas instâncias.

## Templates e promoção de instância

Um **template** é um artefato no regime `definidor` que oferece conteúdo, estrutura, valores iniciais, metadados ou regras reutilizáveis para orientar a criação ou configuração de instâncias. Template não constitui um regime ontológico próprio: é uma capacidade de um definidor.

Todo template deve ser instanciável. A recíproca não é necessária: um definidor pode autorizar instâncias sem oferecer conteúdo ou configuração reutilizável como template.

### Tornar uma instância um template

Uma instância não pode mudar diretamente para o regime `definidor`, pois isso apagaria a distinção entre a ocorrência concreta e a abstração reutilizável. A operação de sistema apresentada ao usuário como **“tornar-se template”** é, portanto, uma promoção por criação: preserva a instância de origem e cria um novo artefato definidor.

O novo definidor possui ancestralidade múltipla:

```text
Definidor-base de template ──define──> Novo definidor template
Definidor da instância de origem ──define──> Novo definidor template
```

O primeiro ancestral transmite a capacidade e as regras gerais de template. O segundo preserva a natureza semântica da origem — documento, comunicação, tarefa ou outra definição aplicável. O novo artefato deve ser marcado como `template` e, por implicação, como `instanciável`.

A operação copia da instância de origem:

- o conteúdo selecionado para reutilização;
- os metadados autorizados pela definição e pelo contexto;
- configurações que devam servir como valores iniciais das futuras instâncias.

Ela não copia a identidade persistente da origem. Estados operacionais, relações contextuais, dados pessoais, datas históricas e outros valores próprios daquela ocorrência somente podem ser transferidos quando houver autorização semântica e de governança explícita.

A proveniência deve ser preservada pela relação canônica definida em [[02_relationships-and-provenance#Cópia deliberada|Cópia deliberada]]:

```text
Instância de origem ──é copiada por──> Novo definidor template
```

Essa relação registra a origem da promoção, mas não torna o novo definidor uma instância da ocorrência original. O novo artefato possui identidade, regime e finalidade próprios.

### Exemplo

Considere um relatório de vistoria concreto, instância do definidor `Relatório de vistoria`. Se o usuário solicitar que ele “se torne template”, o sistema cria um novo definidor, por exemplo `Template de relatório de vistoria da unidade`, com esta fundamentação:

```text
Template ──define──> Template de relatório de vistoria da unidade
Relatório de vistoria ──define──> Template de relatório de vistoria da unidade
Relatório nº 42 ──é copiado por──> Template de relatório de vistoria da unidade
```

O novo definidor pode conservar seções, instruções, campos iniciais e metadados reutilizáveis do relatório nº 42, enquanto exclui datas da ocorrência, assinaturas, participantes e demais informações que não devam propagar-se. As futuras instâncias criadas a partir dele continuam sendo ocorrências concretas fundamentadas por esse único definidor template.

## Questões ainda abertas

- Quais atributos e relações são copiáveis por padrão e quais exigem autorização explícita?
- Como regras herdadas dos dois ancestrais são combinadas quando houver conflito?
- Que permissões autorizam a promoção e a posterior alteração de um template?
- Como versionar um template sem modificar retroativamente as instâncias já criadas?
