# Estrutura-alvo

Este documento registra uma premissa arquitetural para a organização pretendida do repositório. Ele orienta sua evolução, mas não funciona como inventário autoritativo do que já existe.

## Relação com a estrutura real

A árvore real de arquivos e diretórios é a fonte da verdade factual sobre a estrutura atualmente existente. A árvore documentada abaixo representa a visão-alvo e os papéis arquiteturais pretendidos.

Uma divergência não determina automaticamente que a estrutura real esteja errada nem que este documento esteja desatualizado. Cada conjunto corrente de divergências deve ser analisado pontualmente para decidir entre:

1. adequar a estrutura real às premissas documentadas;
2. atualizar a documentação para refletir uma evolução válida da estrutura;
3. combinar ambas as ações.

Não existe uma regra genérica de precedência entre a estrutura real e a pretendida. Uma política desse tipo somente pode ser estabelecida mediante deliberação explícita do usuário.

Na ausência dessa deliberação, ferramentas e agentes não devem promover reconciliações estruturais automáticas. Quando identificarem divergências, devem, no máximo, descrevê-las, apresentar as alternativas pertinentes e solicitar deliberação do usuário antes de modificar a estrutura ou a documentação. Uma solução já autorizada pelo usuário para uma divergência específica pode ser executada diretamente.

## Visão-alvo

```text
managehub/
├── config/                 # Configuração do projeto Django
├── managehub/              # Aplicações universais em Django
│   ├── identity/           # Autenticação, perfis, papéis e permissões
│   ├── organization/       # Organizações, unidades e vínculos
│   ├── workflow/           # Processos, estados e aprovações
│   ├── work/               # Tarefas, responsáveis e prazos
│   ├── documents/          # Documentos e versões
│   ├── notifications/      # Notificações
│   ├── audit/              # Auditoria e histórico
│   └── dashboard/          # Indicadores e painéis genéricos
│
├── srohub/                 # Aplicação concreta ao SRO/4
│   ├── governance/         # Cargos, mandatos e deliberações
│   ├── membership/         # Membros e suas categorias
│   ├── operations/         # Rotinas e processos próprios
│   └── reporting/          # Relatórios e painéis SRO/4
│
├── scripts/                # Automações e utilitários auxiliares
├── integrations/           # Conectores e integrações externas
├── skills/                 # Skills operacionais do ecossistema
├── templates/              # Templates compartilhados
├── static/                 # Recursos estáticos compartilhados
├── requirements/           # Dependências por ambiente ou finalidade
├── 00_meta/                # Governança e recursos de desenvolvimento
│   ├── 01_Commit_Messages/ # Arquivo das mensagens de commit geradas
│   ├── 02_skills/          # Meta-skills de desenvolvimento e manutenção
│   └── 03_engineering/     # Premissas e documentação de engenharia
├── manage.py
└── README.md
```

As aplicações e subpastas previstas devem ser criadas somente diante de necessidade concreta, em consonância com o [[../01_principles/01_evolutionary-design|design evolutivo]]. A ausência de um componente ainda não necessário pode representar o estágio atual legítimo, e não uma falha a ser corrigida automaticamente.
