# Rascunho conceitual

> Estado: exploração em andamento. Este documento consolida o entendimento atual; não constitui decisão arquitetural, modelo de dados nem especificação de implementação.

## Intenção

O ManageHUB pode ser compreendido como um sistema que opera sobre representações persistentes de elementos relevantes de um contexto de gestão e sobre os fatos que os conectam. Pessoas, organizações, comunicações, documentos, processos, tarefas, eventos e referências possuem naturezas distintas, mas podem compartilhar uma infraestrutura comum de identidade, contexto, proveniência, histórico e relacionamento.

O sistema não manipula diretamente pessoas, organizações ou objetos do mundo real. Ele manipula seus registros e representações informacionais. Essa distinção precisa permanecer explícita ao tratar identidade, duplicidade, sincronização, privacidade e auditoria.

## Artefatos

Chamamos provisoriamente de **artefato** toda representação informacional que o sistema pode identificar, contextualizar, relacionar, acompanhar ou processar.

Um artefato pode representar, por exemplo:

- uma pessoa, organização, unidade, bem ou outro referente relevante;
- uma comunicação, documento, anexo, registro ou versão;
- um processo, evento, tarefa, resultado ou evidência;
- uma regra, catálogo, configuração ou outra referência operacional;
- uma afirmação ou um vínculo entre outros artefatos.

O uso de uma unidade comum não elimina as diferenças entre esses elementos. Ele apenas permite que todos possam participar de uma mesma rede de contexto.

As propriedades candidatas compartilhadas por um artefato incluem:

- identidade persistente;
- tipo ou classificação;
- atributos próprios;
- proveniência e autoria;
- marcas temporais e histórico;
- relações com outros artefatos;
- regras de acesso, retenção e visibilidade quando aplicáveis.

A formulação inicial dessas propriedades, dos regimes ontológicos e das relações entre definições e instâncias foi registrada em [[01_artifact-foundation|Fundamento dos artefatos]]. Ela continua em amadurecimento; este rascunho preserva as questões ainda não resolvidas.

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

Uma relação não precisa ser apenas um detalhe técnico entre dois registros. Ela pode representar um fato que merece identidade, autoria, fonte, tempo, validade, confiança e histórico próprios.

Por exemplo, a afirmação de que um documento satisfaz uma tarefa pode precisar indicar:

- quem criou ou confirmou o vínculo;
- quando e com base em qual fonte;
- se ele foi inferido por automação ou confirmado por uma pessoa;
- qual seu grau de confiança;
- em que período foi válido;
- se foi corrigido, revogado ou substituído.

A expressão “relações também são artefatos” é uma hipótese importante deste modelo: relações devem poder ser tratadas como registros contextualizados sempre que isso for necessário. Ainda é preciso definir quando uma simples referência basta e quando uma relação precisa desse tratamento completo.

## Trabalho, obrigação e satisfação

Uma tarefa é mais que uma anotação de trabalho. Ela pode representar uma obrigação contextualizada: algo que precisa ser realizado porque algum evento, comunicação, regra, processo ou outro artefato a motivou.

O esquema inicial é:

```text
origem → tarefa ou obrigação → resultado ou evidência
```

- A **origem** responde por que a obrigação existe.
- A **tarefa** representa o trabalho ou resultado esperado.
- A **solução**, **resultado** ou **evidência** é o artefato que demonstra o atendimento da obrigação.

Esse encadeamento permite perguntar não apenas se uma tarefa foi marcada como concluída, mas qual registro concreto sustenta essa conclusão.

Uma tarefa pode ter uma solução esperada, mas a existência de um produto não significa automaticamente que a obrigação foi satisfeita. Será necessário distinguir, conforme o domínio, situações como produzir, submeter, aprovar, aceitar, enviar, rejeitar, substituir e satisfazer. Também permanece em aberto se toda tarefa terá exatamente uma origem ou se haverá obrigações legitimamente sustentadas por múltiplas origens.

## Identidade e representação legível

Cada artefato deve possuir uma identidade persistente, independente de reclassificações e mudanças de apresentação. Um identificador opaco, como UUID, é candidato a cumprir esse papel.

Representações legíveis podem incluir a classificação corrente, por exemplo `documento.comunicação.e-mail#E44AD`. Elas facilitam a leitura humana, mas não devem necessariamente constituir a identidade imutável do artefato: uma classificação pode ser corrigida, enriquecida ou substituída sem que o registro deixe de ser o mesmo.

## Classificação: uma dimensão não basta

O modelo inicial agrupava os artefatos por domínios como entidade, documento, processo, tarefa, evento, referencial e relação, com classes e subclasses. Esse vocabulário é um ponto de partida útil, mas não deve ainda ser tratado como uma taxonomia definitiva e mutuamente exclusiva.

Diversas propriedades pertencem a dimensões independentes:

- uma pessoa pode exercer múltiplos papéis em diferentes contextos;
- uma tarefa pode ser recorrente, ter prazo, exigir aprovação e ser complexa simultaneamente;
- um documento pode ter uma espécie documental, um formato de arquivo e versões distintas;
- uma comunicação pode ser também um evento, enquanto seu registro ou resumo é um documento;
- fornecedor, responsável e participante podem ser papéis relacionais, não espécies permanentes de entidade.

O amadurecimento da classificação deve distinguir pelo menos natureza, tipo funcional, papel contextual, estado, formato ou representação e vocabulário específico de domínio. Não está decidido se haverá uma taxonomia única, taxonomias complementares, etiquetas, tipos configuráveis ou outra composição.

## Universalidade e especialização

O ManageHUB deve oferecer mecanismos universais para representar artefatos, relações, proveniência, histórico e fluxos de trabalho. O sroHUB — ou qualquer aplicação concreta — pode definir vocabulários, espécies documentais, papéis e regras próprios.

Exemplos específicos, como documentos ou rotinas exclusivos do SRO/4, podem ilustrar o modelo, mas não definem a semântica do núcleo. A separação deve respeitar os [[../01_principles/02_domain-language|limites de linguagem de domínio]] e a [[../02_architecture/01_system-boundaries|distinção entre ManageHUB e sroHUB]].

## IA e automação

A IA pode atuar sobre a rede de contexto para sugerir classificações, extrair relações, identificar possíveis obrigações, propor resultados esperados, encontrar evidências, compor narrativas e apontar incoerências.

Inferências automatizadas não devem ser confundidas automaticamente com fatos confirmados. Uma sugestão precisa conservar proveniência, método, data, confiança e, quando cabível, um fluxo de revisão humana antes de produzir efeitos operacionais relevantes.

## Questões em aberto

- Quais outras propriedades devem ser invariantes de todo artefato, além das já propostas, e quais pertencem somente a determinadas naturezas?
- Que relações devem ser explicitamente modeladas e quais podem ser derivadas?
- Em quais casos uma relação precisa ser um registro de primeira classe?
- Como representar relações n-árias, validade temporal, versões e contradições?
- Como distinguir identidade de correspondência, duplicidade e equivalência entre representações?
- Uma tarefa pode ter múltiplas origens, múltiplas evidências ou soluções parciais?
- Quais estados são derivados da rede e quais precisam ser declarados ou confirmados?
- Como serão governados vocabulários universais e vocabulários específicos de cada aplicação?
- Quais direitos de acesso, retenção e auditoria acompanham artefatos e relações?
- Que decisões técnicas serão justificadas por este modelo quando houver necessidades concretas de implementação?
