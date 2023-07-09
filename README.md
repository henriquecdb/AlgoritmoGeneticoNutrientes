# Relatório de Elaboração de Cardápios Nutricionais

## Introdução
Os cardápios nutricionais desempenham um papel essencial na promoção de uma alimentação saudável e equilibrada. Eles são elaborados levando em consideração as necessidades individuais de cada pessoa, fornecendo uma variedade de alimentos que atendam aos requisitos nutricionais diários. No entanto, a criação manual de cardápios pode ser uma tarefa complexa, uma vez que requer conhecimento nutricional, consideração de restrições alimentares e a habilidade de equilibrar a ingestão de calorias.

<p>Nesse contexto, algoritmos genéticos têm sido amplamente utilizados como uma abordagem eficaz para otimizar problemas de planejamento e seleção, incluindo a elaboração de cardápios nutricionais. Os algoritmos genéticos são técnicas inspiradas na evolução biológica que utilizam uma combinação de processos de seleção, cruzamento e mutação para encontrar soluções de alta qualidade em problemas complexos.</p>

## Objetivo
O objetivo deste algoritmo é elaborar cardápios nutricionais que sejam nutricionalmente equilibrados e minimizem a quantidade de calorias consumidas. O algoritmo irá selecionar alimentos de diferentes categorias e combiná-los de maneira a fornecer uma refeição equilibrada e com baixo teor calórico.

## Modelagem
Cada indivíduo na população do algoritmo genético é representado como um cardápio, composto por uma sequência de alimentos para cada refeição do dia (café da manhã, almoço, café da tarde e jantar). A escolha dos alimentos será baseada em alimentos pré-selecionados e categorizados de acordo com a refeição do dia. As características dos alimentos são: nome, proteínas, carboidratos, gorduras e calorias.

## Referência Nutricional
De acordo com essas recomendações, o consumo de nutrientes deve se basear nas seguintes proporções:
- <b>Carboidratos</b>: É recomendado que o consumo de carboidratos seja equivalente a aproximadamente 55% das calorias totais consumidas. Os carboidratos são uma importante fonte de energia e podem ser obtidos a partir de alimentos como grãos, cereais, frutas, legumes e vegetais.
- <b>Proteínas</b>: A recomendação média é que as proteínas consumo de proteínas seja equivalente a cerca de  20% das calorias totais consumidas. As proteínas são essenciais para a construção e reparo de tecidos, além de desempenharem funções importantes no corpo. Boas fontes de proteína incluem carnes magras, peixes, ovos, laticínios, legumes, nozes e sementes.
- <b>Gorduras</b>: A recomendação é que as gorduras consumo de gorduras seja equivalente a cerca de 35% das calorias totais consumidas.

## Alimentos Disponíveis

### Café - Cereais

| Alimento                            | Proteínas | Carboidratos | Gorduras | Calorias |
|-------------------------------------|------------|-----------------|---------------|----------|
| Biscoito Recheado Chocolate         | 6          | 71              | 20            | 472      |
| Biscoito Salgado Cream Cracker      | 10         | 69              | 14            | 432      |
| Cereal Matinal                      | 7          | 84              | 1             | 382      |
| Pão Francês                         | 8          | 59              | 3             | 300      |

### Café - Frutas

| Alimento              | Proteínas | Carboidratos | Gorduras | Calorias |
|-----------------------|------------|-----------------|---------------|----------|
| Abacate               | 1          | 6               | 8             | 96       |
| Abacaxi               | 1          | 12              | 0             | 48       |
| Banana Prata          | 1          | 26              | 0             | 98       |
| Coco                  | 4          | 10              | 0             | 402      |
| Goiaba Vermelha       | 1          | 13              | 0             | 54       |
| Laranja Pêra          | 1          | 9               | 0             | 37       |
| Maçã Fuji             | 0          | 15              | 0             | 56       |
| Maracujá              | 2          | 12              | 2             | 68       |
| Melão                 | 1          | 8               | 0             | 29       |
| Morango               | 1          | 7               | 0             | 30       |

### Café - Bebidas

| Alimento              | Proteínas | Carboidratos | Gorduras | Calorias |
|-----------------------|-------------|-----------------|---------------|----------|
| Café                  | 15          | 66              | 12            | 419      |
| Água de Coco          | 0           | 5.3             | 0             | 21.5     |
| Suco Laranja Pêra     | 0.7         | 7.6             | 0.1           | 32.7     |
| Suco de Uva Néctar    | 0           | 29              | 0             | 115      |
| Leite UHT Integral    | 6           | 8.8             | 4             | 113      |
| Iogurte Natural       | 4           | 2               | 3             | 51       |

### Refeição - Cereais

| Alimento                     | Proteínas | Carboidratos | Gorduras | Calorias |
|------------------------------|------------|-----------------|---------------|----------|
| Arroz Integral Cozido        | 2.6        | 25.8            | 0.3           | 123.5    |
| Arroz Tipo 1                 | 2.5        | 28.1            | 0.2           | 128.3    |
| Macarrão Instantâneo         | 9          | 62              | 17            | 432      |
| Feijão Carioca               | 20         | 63              | 1             | 336      |
| Lentilha                     | 23         | 64              | 1             | 347      |

### Refeição - Verduras e Hortaliças

| Alimento                           | Proteínas | Carboidratos | Gorduras | Calorias |
|------------------------------------|------------|-----------------|---------------|----------|
| Abobrinha Italiana Refogada        | 1.1        | 4.2             | 0.1           | 24.4     |
| Alface Lisa                        | 2          | 2               | 0             | 14       |
| Alho Cru                           | 7          | 24              | 0             | 113      |
| Batata Doce Cozida                 | 0.6        | 18.4            | 0             | 76.8     |
| Beterraba Crua                     | 2          | 11              | 0             | 49       |
| Cará                               | 1.5        | 18.9            | 0             | 77.6     |
| Cenoura Cozida                     | 0.9        | 6.7             | 0.1           | 29.9     |
| Couve Crua                         | 3          | 4               | 1             | 27       |
| Espinafre Nova Zelândia Refogado   | 2.7        | 4.2             | 0.9           | 67.3     |
| Mandioca Frita                     | 1.4        | 50.3            | 1.7           | 300.1    |
| Nabo Cru                           | 1          | 4               | 0             | 18       |
| Tomate com Semente Cru             | 1          | 3               | 0             | 15       |
| Vagem Crua                         | 2          | 5               | 0             | 25       |

### Refeição - Pescados

| Alimento              | Proteínas | Carboidratos | Gorduras | Calorias |
|-----------------------|------------|-----------------|---------------|----------|
| Corimbata Assado      | 19         | 0               | 4.8           | 261.5    |
| Pintado Grelhado      | 30.8       | 0               | 1.1           | 152.2    |
| Filé de Merluza Frito | 26.9       | 0               | 1.4           | 191.6    |
| Atum em Conserva      | 26.2       | 0               | 1             | 165.9    |

### Refeição - Carnes

| Alimento                                  | Proteínas | Carboidratos | Gorduras | Calorias |
|-------------------------------------------|------------|-----------------|---------------|------|
| Carne Bovina Acém Moída Cozida             | 26.7       | 0               | 10.9          | 212.4    |
| Carne Bovina Contra Filé sem Gordura Grelhado  | 35.9   | 0               | 4.5           | 193.7    |
| Carne Bovina Costela Assada                | 28.8       | 0               | 27.7          | 373      |
| Filé Mignon sem Gordura Grelhado           | 33         | 0               | 9             | 220      |
| Carne Bovina Fraldinha com Gordura Cozida  | 24         | 0               | 26            | 338      |
| Carne Bovina Lagarto Cozido                | 33         | 0               | 9             | 221      |

### Refeição - Bebidas

| Alimento               | Proteínas | Carboidratos | Gorduras | Calorias |
|------------------------|-------------|-----------------|---------------|----------|
| Refrigerante Guaraná   | 0           | 10              | 0             | 38.7     |
| Suco Laranja Pêra      | 0.7         | 7.6             | 0.1           | 32.7     |
| Suco de Uva Néctar     | 0           | 29              | 0             | 115      |

## Resultados Encontrados
Após a execução do algoritmo, foram obtidos cardápios nutricionais, utilizando uma abordagem baseada na seleção e combinação de alimentos de diferentes categorias. Os resultados demonstram o potencial do algoritmo genético como uma ferramenta eficaz na elaboração de cardápios personalizados, contribuindo para uma alimentação saudável e equilibrada. A saída do programa mostra o melhor indivíduo e, em seguida, o nome dos alimentos e sua quantidade. A ordem das refeições é: café da manhã, almoço, café da tarde e jantar. Segue o exemplo de uma das execuções:
![Resultado](https://i.imgur.com/QTlNY4v.png)

## Conclusão

O algoritmo genético permite a seleção de alimentos de diferentes categorias para elaborar cardápios nutricionais com o objetivo de minimizar a ingestão de calorias. As tabelas acima apresentam os alimentos disponíveis em cada categoria, juntamente com suas informações nutricionais.

É possível utilizar o algoritmo para criar cardápios equilibrados e de baixo teor calórico, combinando alimentos de diferentes categorias. Recomenda-se o uso do algoritmo como uma ferramenta auxiliar para a elaboração de cardápios nutricionais, levando em consideração as necessidades e restrições individuais de cada pessoa.

*Observação: Os valores nutricionais fornecidos são aproximados e podem variar de acordo com a marca e o método de preparo dos alimentos.*
