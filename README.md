# ManageHUB

O **ManageHUB** é um ecossistema modular de gestão universal, desenvolvido principalmente em **Python**, tendo o **Django** como seu framework estruturante.

O ecossistema pode incluir scripts, serviços, automações e pequenos aplicativos subsidiários, criados conforme a necessidade em outras linguagens e tecnologias — por exemplo, Shell, JavaScript, SQL e C#. Também pode integrar ferramentas e bibliotecas especializadas, como Ollama, Pandas, PyTorch e TensorFlow.

Este repositório contém também o **sroHUB**, a primeira aplicação concreta desse núcleo: a gestão **no SRO/4**. Ambos residem no mesmo repositório, compartilham histórico, manutenção, sincronização e implantação, mas preservam responsabilidades bem definidas.

## Conceito

O ManageHUB reúne capacidades de gestão que fazem sentido em diferentes contextos organizacionais. O sroHUB combina e especializa essas capacidades para as necessidades, regras e linguagem próprias do SRO/4.

> **ManageHUB** é o núcleo universal de capacidades de gestão.  
> **sroHUB** é sua aplicação concreta para a gestão no SRO/4.

A pergunta que orienta a separação é:

> Esta funcionalidade continua fazendo sentido sem a existência do SRO/4?

- Se sim, pertence ao **ManageHUB**.
- Se depende da identidade, das regras ou da operação específica do SRO/4, pertence ao **sroHUB**.

## Arquitetura

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
├── scripts/                # Automações e utilitários ad hoc
├── integrations/           # Conectores e integrações externas
├── skills/                 # Skills operacionais do ecossistema
├── templates/              # Templates compartilhados
├── static/                 # Recursos estáticos compartilhados
├── requirements/           # Arquivos de dependências por ambiente
├── 00_meta/                # Governança e recursos de desenvolvimento
│   ├── 01_Commit_Messages/ # Arquivo das mensagens de commit geradas
│   └── 02_skills/          # Meta-skills para desenvolvimento e manutenção
├── manage.py
└── README.md
```

### Skills

As skills são separadas de acordo com seu papel no repositório:

- `00_meta/02_skills/` contém **meta-skills**, usadas durante o desenvolvimento, a manutenção e a governança do repositório. Elas apoiam atividades como compor mensagens de commit, revisar alterações e documentar decisões.
- `skills/` contém **skills operacionais**, usadas durante a execução do ecossistema ManageHUB e de suas aplicações. Elas implementam capacidades do produto e não ferramentas para desenvolver o próprio repositório.

As subpastas de aplicações Django devem ser criadas conforme a necessidade, usando `manage.py startproject` e `manage.py startapp`; a árvore acima representa a organização-alvo, não a criação antecipada de todos os módulos.

## Tecnologias e integrações

Python e Django formam a base principal do ManageHUB, sem restringir o ecossistema a essas tecnologias.

Conforme a necessidade, o repositório pode incorporar:

- Scripts de Shell para administração, automação e implantação.
- JavaScript para interfaces, integrações ou ferramentas auxiliares.
- SQL para consultas, migrações, rotinas analíticas e otimizações.
- C# ou outras linguagens para integrações e aplicativos específicos.
- Ferramentas locais ou externas de inteligência artificial, análise de dados e aprendizado de máquina, como Ollama, Pandas, PyTorch e TensorFlow.

Cada tecnologia subsidiária deve ser introduzida para resolver uma necessidade concreta, mantendo a arquitetura compreensível e evitando dependências sem finalidade definida.

## Regra de dependência

As dependências devem seguir uma única direção:

```text
sroHUB → ManageHUB
ManageHUB ↛ sroHUB
```

Os módulos do sroHUB podem usar as capacidades do ManageHUB. Em contrapartida, o ManageHUB não deve importar nem depender de conceitos, regras, siglas ou modelos específicos do SRO/4.

## Exemplos de responsabilidades

| ManageHUB | sroHUB |
| --- | --- |
| Usuários, perfis, papéis e permissões | Cargos e mandatos próprios |
| Organizações, unidades e vínculos | Estrutura organizacional do SRO/4 |
| Tarefas, prazos e responsáveis | Rotinas operacionais específicas |
| Processos, aprovações e estados | Fluxos internos do SRO/4 |
| Documentos, versões e auditoria | Documentos e relatórios próprios |
| Indicadores genéricos | Painéis e métricas do SRO/4 |

## Princípios

- Um único repositório, um único histórico e uma única base de manutenção.
- Python e Django como fundação principal, com abertura a componentes subsidiários adequados à necessidade.
- Núcleo universal funcional, e não apenas abstrações vazias.
- Especializações do SRO/4 isoladas no sroHUB.
- Crescimento orientado pela prática: um conceito específico só migra para o ManageHUB quando se mostrar realmente reutilizável.
- Linguagem de domínio explícita: termos próprios do SRO/4 permanecem no sroHUB.
- Integrações e tecnologias adicionais devem ter propósito claro, documentação e manutenção compatível com o ecossistema.

## Estado inicial

O ManageHUB começa como um embrião de gestão universal, aplicado inicialmente ao SRO/4 por meio do sroHUB. A arquitetura permite futuras aplicações em outros contextos sem exigir a separação do código, do histórico ou da operação.
