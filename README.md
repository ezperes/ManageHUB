# ManageHUB

O **ManageHUB** é um ecossistema modular de gestão universal, desenvolvido principalmente em **Python**, tendo o **Django** como seu framework estruturante.

Este repositório também contém o **sroHUB**, sua primeira aplicação concreta, voltada à gestão no SRO/4. A relação entre [[00_meta/03_engineering/02_architecture/01_system-boundaries|ManageHUB e sroHUB]] preserva responsabilidades distintas dentro de um único repositório.

## Conceito

O ManageHUB reúne capacidades de gestão aplicáveis a diferentes contextos organizacionais. O sroHUB combina e especializa essas capacidades para as necessidades, regras e linguagem próprias do SRO/4.

> **ManageHUB** é o núcleo universal de capacidades de gestão.  
> **sroHUB** é sua aplicação concreta para a gestão no SRO/4.

A pergunta que orienta a separação é:

> Esta funcionalidade continua fazendo sentido sem a existência do SRO/4?

- Se sim, pertence ao **ManageHUB**.
- Se depende da identidade, das regras ou da operação específica do SRO/4, pertence ao **sroHUB**.

As dependências seguem a direção `sroHUB → ManageHUB`; os detalhes e critérios estão nas [[00_meta/03_engineering/02_architecture/02_dependency-rules|regras de dependência]].

## Estado atual

O ManageHUB começa como um núcleo de gestão universal aplicado inicialmente ao SRO/4 por meio do sroHUB. Seu [[00_meta/03_engineering/01_principles/01_evolutionary-design|crescimento é orientado por necessidades concretas]], permitindo futuras aplicações em outros contextos sem exigir a separação do código, do histórico ou da operação.

Python e Django constituem a fundação tecnológica. Outras tecnologias podem ser incorporadas quando resolverem necessidades demonstráveis e atenderem aos [[00_meta/03_engineering/03_standards/01_technology-adoption|critérios internos de adoção]].

## Engenharia

As premissas, os princípios, os padrões e as decisões que orientam a evolução técnica do projeto estão reunidos na [documentação interna de engenharia](00_meta/03_engineering/README.md).

Essa documentação descreve a visão pretendida e os critérios de desenvolvimento. A árvore real do repositório permanece como fonte da verdade factual sobre os arquivos e diretórios existentes.
