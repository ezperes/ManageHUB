# Regras de dependência

As dependências entre as duas áreas de produto seguem uma única direção:

```text
sroHUB → ManageHUB
ManageHUB ↛ sroHUB
```

O sroHUB pode consumir capacidades universais do ManageHUB. O ManageHUB não pode importar nem depender de conceitos, regras, siglas ou modelos específicos do SRO/4, conforme os [[01_system-boundaries|limites do sistema]].

## Dependências permitidas

- Um fluxo do sroHUB usar tarefas, documentos ou auditoria fornecidos pelo ManageHUB.
- Um relatório específico compor dados a partir de serviços universais.
- Uma aplicação concreta especializar pontos de extensão definidos pelo núcleo.

## Dependências proibidas

- O ManageHUB importar módulos do sroHUB.
- Um modelo universal conter campos ou regras exigidos somente pelo SRO/4.
- Serviços do núcleo condicionarem seu comportamento à existência da aplicação específica.
- Uma interface universal expor terminologia exclusiva do SRO/4.

## Tratamento de violações

Uma violação deve ser analisada para separar a capacidade universal da regra específica. A correção pode mover a regra para o sroHUB, introduzir um ponto de extensão neutro ou redefinir a responsabilidade do componente. Alterações de limite com impacto duradouro devem ser registradas em [[../04_decisions/README|decisões arquiteturais]].
