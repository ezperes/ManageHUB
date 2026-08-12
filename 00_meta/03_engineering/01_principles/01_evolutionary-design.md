# Design evolutivo

O ManageHUB deve crescer a partir de necessidades concretas. Aplicações, módulos, diretórios e abstrações são introduzidos quando seu papel puder ser demonstrado, e não apenas para antecipar uma possibilidade futura.

## Premissas

- O núcleo universal deve ser funcional, não uma coleção de abstrações vazias.
- Uma capacidade específica do sroHUB somente deve migrar para o ManageHUB quando sua reutilização fora do contexto do SRO/4 estiver demonstrada.
- Aplicações Django devem ser criadas conforme a necessidade, usando os mecanismos próprios do framework.
- Estruturas previstas na [[../02_architecture/04_target-structure|estrutura-alvo]] não precisam existir antes de serem necessárias.
- A evolução deve preservar código compreensível e evitar complexidade especulativa.

## Estado inicial

O ManageHUB começa como um núcleo de gestão universal aplicado inicialmente ao SRO/4. Esse estágio embrionário não reduz sua intenção de universalidade, mas exige que a generalização seja comprovada pela prática.

A visão futura descreve uma direção, não uma declaração de que todos os componentes já estejam implementados. O estado efetivo deve sempre ser constatado na árvore real do repositório.
