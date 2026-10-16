# Atividade: padrões de projeto - Strategy

Resolução da atividade de Engenharia de Software, 4º período do Bacharelado
em Sistemas de Informação do CEFET-MG. Código refatorado a partir do projeto
didático https://github.com/brunoacre/es-code-smell.

## Executar

Extraia o ZIP e abra o terminal na pasta `atividade_strategy`:

```bash
python teste_frete.py
```

Para executar os testes automatizados:

```bash
python -m unittest -v
```

Em sistemas que utilizam o comando `python3`, substitua `python` por `python3`.
O projeto utiliza somente a biblioteca padrão do Python 3.

## Identificação do Code Smell e violação do OCP

O método original `calcular_frete(tipo_servico)` concentrava as fórmulas de
SEDEX, PAC, transportadora e motoboy em uma sequência de `if/elif` baseada
em uma string. Esse é o Code Smell de condicionais por tipo, frequentemente
chamado de *Switch Statements*, mesmo quando implementado com `if/elif`.

Para acrescentar DRONE, era necessário modificar esse método em Pedido.
Isso viola o Princípio Aberto/Fechado (OCP): a classe deveria permitir novas
modalidades por extensão, sem precisar alterar sua implementação a cada
novo algoritmo de frete.

## Solução e correspondência com os passos

1. **Interface:** `estrategia_frete.py` define `EstrategiaFrete`, classe
   abstrata com uma única operação: `calcular(self, pedido)`.
2. **Estratégias concretas:** `fretes.py` contém as quatro fórmulas originais,
   cada uma em sua classe: `FreteSedex`, `FretePac`, `FreteTransportadora` e
   `FreteMotoboy`.
3. **Contexto:** `pedido.py` mantém o atributo privado `__estrategia`, expõe
   o setter público `set_estrategia()` e delega o cálculo em
   `calcularFrete()`, sem parâmetros explícitos. O método antigo foi removido.
4. **Cliente:** `teste_frete.py` escolhe e injeta os objetos de estratégia.
   A troca pode acontecer durante a execução, sobre o mesmo pedido.
5. **Extensibilidade:** `frete_drone.py` implementa a taxa fixa de R$ 25,00.
   O cliente importa e injeta `FreteDrone()`; a classe Pedido não precisa
   ser modificada. `frete_retirada_local.py` também atende à modalidade
   gratuita citada no cenário.
6. **Explicação:** os arquivos Python têm comentários e docstrings sobre
   responsabilidades, delegação, contrato, fórmulas e escolha da estratégia.

O PDF pede o nome `calcularFrete()`, enquanto o README original sugere
`calcular_frete()`. Nesta resolução foi seguido o nome solicitado no PDF.

## Por que atende ao OCP?

Pedido depende da abstração EstrategiaFrete, e não das modalidades concretas.
Para uma nova modalidade, basta criar outra subclasse e configurá-la no
cliente. Pedido continua usando `self.__estrategia.calcular(self)`.
O código de composição do cliente pode mudar para disponibilizar a nova
opção; o ponto protegido contra alterações é o contexto Pedido.

O `if` que verifica a ausência de estratégia não escolhe uma modalidade.
Ele apenas impede o cálculo antes da configuração. Nesse caso é lançado
ValueError, evitando tratar uma configuração ausente como frete gratuito.

## Resultados esperados

| Modalidade | Pedido com 2,5 kg |
| --- | ---: |
| SEDEX | R$ 13,75 |
| PAC | R$ 7,50 |
| TRANSPORTADORA | R$ 27,50 |
| MOTOBOY | R$ 15,00 |
| DRONE | R$ 25,00 |
| RETIRADA_LOCAL | R$ 0,00 |

Para um segundo pedido de 10 kg, o PAC custa R$ 15,00. O cliente original
criava `pedido2`, mas chamava o cálculo em `pedido`; esse exemplo foi corrigido.

Os valores usam float para manter a representação do exercício original.

## Verificação da extensibilidade

Além de verificar as modalidades e a troca de estratégia, `test_strategy.py`
declara uma estratégia inédita dentro de um teste e a injeta em Pedido.
Isso demonstra que o contexto aceita outra implementação do contrato sem
conhecer previamente sua classe. Há sete métodos de teste, incluindo
subcasos para diferentes pesos e modalidades.

## Referências

- Enunciado fornecido: Cópia de Atividade Padrões de Projeto.pdf.
- Projeto original de Bruno Acre: https://github.com/brunoacre/es-code-smell.
- Refactoring.Guru. Strategy: https://refactoring.guru/pt-br/design-patterns/strategy.

## Entrega

O enunciado aceita os arquivos `.py` compactados. O ZIP contém os sete
arquivos Python e este README com a explicação da solução.
