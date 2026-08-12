# Adoção de tecnologias

Python e Django formam a fundação principal do ManageHUB, sem restringir o ecossistema a uma única linguagem ou categoria de ferramenta. Tecnologias subsidiárias devem resolver necessidades concretas e permanecer compatíveis com o [[../01_principles/01_evolutionary-design|design evolutivo]].

## Critérios de adoção

Uma tecnologia deve ser introduzida quando:

- resolver uma necessidade demonstrável melhor do que as opções já adotadas;
- tiver papel e limites claramente definidos;
- não introduzir acoplamento incompatível com a arquitetura;
- puder ser instalada, configurada, testada e mantida de forma compreensível;
- tiver suas dependências, riscos operacionais e forma de uso documentados;
- trouxer benefício proporcional ao custo e à complexidade adicionais.

## Tecnologias já deliberadas

- **Python**: linguagem principal para o sistema, automações e serviços.
- **Django**: framework estruturante das aplicações web e do domínio persistente.
- **Shell**: administração, automação e implantação quando apropriado ao ambiente.
- **JavaScript**: interfaces, integrações e ferramentas auxiliares que exijam execução no navegador ou em seu ecossistema.
- **SQL**: consultas, migrações, rotinas analíticas e otimizações justificadas.
- **Playwright**: automação de navegador e testes de fluxos reais da interface.
- **Ollama**: execução local de modelos de linguagem quando privacidade, autonomia ou experimentação local justificarem seu uso.

A deliberação favorável permite o uso dessas tecnologias quando pertinente; ela não exige sua introdução antecipada nem dispensa a avaliação da necessidade concreta.

## Tecnologias eventuais ou hipotéticas

As tecnologias abaixo são possibilidades, não escolhas já aprovadas para implementação:

- **C#** ou outras linguagens, para integrações ou aplicativos específicos que as justifiquem.
- **Pandas**, para tratamento e análise tabular de dados.
- **PyTorch**, **Keras** e **TensorFlow**, para aprendizado de máquina quando houver um caso de uso definido.
- Serviços externos de inteligência artificial, dados ou automação que atendam aos critérios deste documento.

A mera menção nesta lista não autoriza a adição de uma dependência. A adoção efetiva deve decorrer de necessidade concreta e, quando tiver impacto arquitetural duradouro, ser registrada em [[../04_decisions/README|decisão própria]].
