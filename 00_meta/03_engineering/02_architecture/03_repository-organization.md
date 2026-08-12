# Organização do repositório

ManageHUB e sroHUB residem no mesmo repositório para compartilhar histórico, manutenção, sincronização e implantação, sem eliminar os [[01_system-boundaries|limites de responsabilidade]] entre eles.

## Áreas principais

- `managehub/`: aplicações e capacidades universais do produto.
- `srohub/`: especializações e regras próprias do SRO/4.
- `config/`: configuração do projeto Django.
- `scripts/`: automações e utilitários auxiliares.
- `integrations/`: conectores e integrações externas.
- `skills/`: skills operacionais executadas como capacidades do ecossistema.
- `templates/` e `static/`: recursos compartilhados da aplicação.
- `requirements/`: dependências organizadas por ambiente ou finalidade.
- `00_meta/`: governança e recursos internos de desenvolvimento e manutenção.

## Meta-skills e skills operacionais

`00_meta/02_skills/` contém meta-skills usadas para desenvolver, revisar, manter e governar o repositório. `skills/` contém skills operacionais do produto. A primeira categoria auxilia a construção do ecossistema; a segunda integra as capacidades executadas por ele.

A localização pretendida de cada área é apresentada na [[04_target-structure|estrutura-alvo]]. A existência factual de arquivos e diretórios, contudo, deve ser verificada diretamente na árvore do repositório.
