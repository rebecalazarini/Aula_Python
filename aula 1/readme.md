# Itrodução 
## Tipos de dados em Python

- Numeros inteiros (int): 1, 2, 3, -4, -5
- Numeros reais (float): 1.5, 2.0, -3.4, -0.5
- Texto (str): "Olá", 'Mundo', "123", 'True'
- Booleano (bool): True, False
- Litas (list): [1, 2, 3], ['a', 'b', 'c'], [1, 'a', True]
- Tuplas (tuple): (1, 2, 3), ('a', 'b', 'c'), (1, 'a', True)
- Dicionarios (dict): {'chave': 'valor'}, {'nome': 'João', 'idade': 30}
- Conjuntos (set): {1, 2, 3}, {'a', 'b', 'c'}

## Variaveis
Variáveis são espaços reservados na memória do computador para armazenar dados. Elas podem ser usadas para armazenar diversos tipos de dados, como inteiros, strings, listas e dicionários.
Em Python, você não precisa declarar o tipo de uma variável explicitamente. O tipo é inferido automaticamente com base no valor atribuído a ela.

## Constantes
A regra de nomeação das constantes no Python segue um padrão parecido com as de variáveis, com a diferença de que todas as letras são maiúsculas e separadas por underline “_”. Porém, por possuir tipagem dinâmica, os valores atribuídos à constantes podem ser alterados sem problemas: 

- MINHA_CONSTANTE = 10 
- print(MINHA_CONSTANTE) # 10 
- MINHA_CONSTANTE = 15 
- print(MINHA_CONSTANTE) # 10
