# Crie uma lista com 10 números aleatórios entre 1 e 100 e encontre o maior e o menor valor.

import random
numeros = [random.randint(1, 100) for _ in range(10)]
maior = max(numeros)
menor = min(numeros)
print("Números:", numeros)
print("Maior número:", maior)