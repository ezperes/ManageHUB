# Limites do sistema

O **ManageHUB** é o núcleo universal de capacidades de gestão. O **sroHUB** é sua aplicação concreta para a gestão no SRO/4. Ambos compartilham o mesmo repositório, mas preservam responsabilidades conceituais distintas.

## Critério orientador

> Esta funcionalidade continua fazendo sentido sem a existência do SRO/4?

- Se sim, ela pode pertencer ao ManageHUB.
- Se depende da identidade, da linguagem, das regras ou da operação específica do SRO/4, ela pertence ao sroHUB.

A resposta positiva é uma condição necessária, mas não suficiente, para promover uma capacidade ao núcleo. A reutilização deve ser demonstrada conforme o princípio de [[../01_principles/01_evolutionary-design|design evolutivo]].

## Exemplos de responsabilidades

| ManageHUB | sroHUB |
| --- | --- |
| Usuários, perfis, papéis e permissões | Cargos e mandatos próprios |
| Organizações, unidades e vínculos | Estrutura organizacional do SRO/4 |
| Tarefas, prazos e responsáveis | Rotinas operacionais específicas |
| Processos, aprovações e estados | Fluxos internos do SRO/4 |
| Documentos, versões e auditoria | Documentos e relatórios próprios |
| Indicadores genéricos | Painéis e métricas do SRO/4 |

## Promoção ao núcleo

Uma capacidade originada no sroHUB pode ser promovida ao ManageHUB quando:

- possuir significado independente do SRO/4;
- atender a mais de um contexto concreto ou tiver reutilização claramente demonstrada;
- puder ser nomeada sem ocultar conceitos específicos;
- respeitar as [[02_dependency-rules|regras de dependência]].
