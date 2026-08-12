# Linguagem de domínio

A linguagem usada no código e na documentação deve revelar a qual domínio cada conceito pertence. Essa clareza sustenta os [[../02_architecture/01_system-boundaries|limites entre ManageHUB e sroHUB]].

## Premissas

- Termos, siglas, regras e modelos próprios do SRO/4 permanecem no sroHUB.
- Componentes do ManageHUB usam nomes compreensíveis em contextos organizacionais independentes do SRO/4.
- Um nome aparentemente genérico não torna universal um conceito cuja regra continue específica.
- Traduções artificiais de termos específicos devem ser evitadas quando apenas ocultarem uma dependência de domínio.

## Sinais de vazamento

Há indício de vazamento de domínio quando um componente do ManageHUB:

- precisa conhecer siglas, cargos, processos ou documentos exclusivos do SRO/4;
- contém condicionais destinadas apenas à operação do sroHUB;
- usa nomes genéricos para representar regras que não fazem sentido fora da aplicação específica;
- exige alterações sempre que uma regra interna do SRO/4 muda.

Quando houver dúvida, deve-se aplicar a pergunta orientadora: a funcionalidade continua fazendo sentido sem a existência do SRO/4?
