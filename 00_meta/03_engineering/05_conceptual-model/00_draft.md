# Rascunho conceitual

> Estado: exploração em andamento. Este documento consolida o entendimento atual; não constitui decisão arquitetural, modelo de dados nem especificação de implementação.

## Intenção

O núcleo do ManageHUB pode ser compreendido como um sistema que opera sobre representações persistentes de elementos relevantes de um contexto de gestão e sobre os fatos que os conectam. Pessoas, organizações, comunicações, documentos, processos, tarefas, eventos e referências possuem naturezas distintas, mas podem compartilhar uma infraestrutura comum de identidade, contexto, proveniência, histórico e relacionamento.

O núcleo não manipula diretamente pessoas, organizações ou objetos do mundo real. Ele manipula seus registros e representações informacionais. Aplicações concretas podem interagir com referentes externos por meio de apps, applets e integrações e refletir essas interações nos artefatos do núcleo.

## Artefatos

Chamamos de **artefato** a unidade universal pela qual o sistema representa, persiste e processa elementos de interesse administrativo. Sua definição, seus atributos universais e específicos, os regimes ontológicos, a ancestralidade e a instanciação estão consolidados, ainda em amadurecimento, em [[01_artifact-foundation|Fundamento dos artefatos]].

Este rascunho não duplica essas formulações. Ele preserva apenas as consequências ainda exploratórias e as questões que dependem de elaboração posterior.

## Rede de contexto

O valor do modelo não está apenas em classificar um registro como documento, tarefa ou evento, mas em tornar explícitos os vínculos entre registros. A rede resultante permite compreender o contexto e a linhagem de uma informação.

Exemplos de vínculos possíveis:

```text
solicitação ──origina──> tarefa
resposta ──satisfaz──> tarefa
anexo ──faz-parte-de──> comunicação
rascunho ──deriva-de──> solicitação
registro de evento ──refere-se-a──> processo
pessoa ──participa-de──> organização
```

Essa rede deve viabilizar, entre outras capacidades, reconstrução de narrativas, auditoria, rastreabilidade, composição de contexto, identificação de lacunas e apoio à automação. Ela é um modelo conceitual: não determina, neste estágio, a adoção de banco de grafos, RDF, event sourcing ou qualquer tecnologia de persistência específica.

## Relações como fatos de primeira classe

Relações são artefatos de primeira classe: seus definidores estabelecem semântica, polos, leituras, cardinalidade e filtros, enquanto suas instâncias registram vínculos concretos e sua proveniência. `Define` organiza uma família abstrata e não instanciável; relações concretas distinguem especialização conceitual, derivação produtiva e outras formas de fundamentação. A formulação corrente está em [[02_relationships-and-provenance|Relações e proveniência]].

Filtros também são artefatos definíveis, instanciáveis, parametrizáveis e reutilizáveis. Seus consumidores declaram persistentemente onde e em quais fases devem atuar; resolvedores determinísticos interpretam essas declarações em tempo de execução. Exceções deliberadas e inconformidades supervenientes preservam histórias distintas.

## Trabalho, obrigação e satisfação

Uma tarefa é mais que uma anotação de trabalho: representa uma obrigação contextualizada, ligada à sua origem e às evidências de satisfação. A formulação inicial e sua integração com informações normativas, resolvedores e relações multipolares estão em [[03_work-and-fulfillment|Trabalho e satisfação]].

## Identidade e representação legível

Cada artefato deve possuir uma identidade persistente, independente de reclassificações e mudanças de apresentação. Um identificador opaco, como UUID, é candidato a cumprir esse papel.

Em regra, um referente deve possuir uma única representação artefatual. Cópias deliberadas são excepcionais, recebem identidade própria e preservam sua origem por meio da relação `é copiado por`.

Representações legíveis podem incluir a classificação corrente, por exemplo `documento.comunicação.e-mail#E44AD`. Elas facilitam a leitura humana, mas não devem necessariamente constituir a identidade imutável do artefato: uma classificação pode ser corrigida, enriquecida ou substituída sem que o registro deixe de ser o mesmo.

## Classificação: uma dimensão não basta

O modelo adota classificação multidimensional e polihierárquica. Classificações intrínsecas são projetadas pelo único definidor imediato e por sua ancestralidade; papéis e classificações contextuais decorrem de relações e circunstâncias. O modelo, as consultas por ancestralidade e os estados derivados estão em [[04_typing-and-classification|Tipagem e classificação]].

Informação, campo, contêiner, portador, canal e formato são planos distintos. A promoção de informação a artefato e os resolvedores determinísticos estão em [[05_information-and-containment|Informação, continência e promoção]].

## Universalidade e especialização

O ManageHUB deve oferecer mecanismos universais para representar artefatos, relações, proveniência, histórico e fluxos de trabalho. O sroHUB — ou qualquer aplicação concreta — pode definir vocabulários, espécies documentais, papéis e regras próprios.

Exemplos específicos, como documentos ou rotinas exclusivos do SRO/4, podem ilustrar o modelo, mas não definem a semântica do núcleo. A separação deve respeitar os [[../01_principles/02_domain-language|limites de linguagem de domínio]] e a [[../02_architecture/01_system-boundaries|distinção entre ManageHUB e sroHUB]].

## IA e automação

A IA pode atuar sobre a rede de contexto para sugerir classificações, extrair relações, identificar possíveis obrigações, propor resultados esperados, encontrar evidências, compor narrativas e apontar incoerências.

Inferências automatizadas não devem ser confundidas automaticamente com fatos confirmados. Uma sugestão precisa conservar proveniência, método, data, confiança e, quando cabível, um fluxo de revisão humana antes de produzir efeitos operacionais relevantes.

Resolvedores determinísticos constituem vocabulário próprio, distinto de skills ou agentes de IA. Seus definidores e os definidores das operações consumidoras podem estabelecer se as execuções e buscas subordinadas serão persistidas, qual conteúdo será preservado e por quanto tempo.

## Unidade lógica e armazenamento físico

Todo artefato participa de um modelo lógico comum, mas isso não obriga sua materialização nem seu armazenamento em uma única tabela. Ontologia, política de materialização e arquitetura física são planos distintos. Essa separação deve orientar futuras decisões de retenção, particionamento, auditoria e desempenho sem antecipar uma tecnologia específica.

## Questões em aberto

- Que relações devem ser explicitamente modeladas e quais podem ser derivadas?
- Quais descendentes de `define` transmitem ancestralidade, estrutura, capacidades ou somente proveniência?
- Como modelar relações multipolares com quantidade variável de componentes?
- Quais condições autorizam cópias deliberadas e quais efeitos elas produzem em cada contexto?
- Uma tarefa pode ter múltiplas origens, múltiplas evidências ou soluções parciais?
- Quais dimensões classificatórias e relações-base devem integrar os axiomas?
- Como resolver conflitos entre múltiplos ancestrais?
- Quais estados e resultados determinísticos precisam ser materializados?
- Como versionar resolvedores e reproduzir decisões históricas?
- Como compor filtros e políticas de persistência herdados de múltiplos definidores?
- Qual tratamento cada consumidor deve atribuir ao resultado `indeterminado`?
- Quando revalidar exceções e como tratar inconformidades supervenientes?
- Quando uma execução efêmera deve ser promovida a artefato durável?
- Como sincronizar uma informação promovida com seu locus original e definir a fonte autoritativa?
- Como representar múltiplas fontes concordantes ou contraditórias?
- Como serão governados vocabulários universais e vocabulários específicos de cada aplicação?
- Quais direitos de acesso, retenção e auditoria acompanham artefatos e relações?
- Que decisões técnicas serão justificadas por este modelo quando houver necessidades concretas de implementação?
