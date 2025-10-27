# Crie uma lista com os números de 1 a 10 e remova todos os números pares.

numeros = [1,2,3,4,5,6,7,8,9,10]
numeros = [num for num in numeros if num % 2 != 0]
print(numeros)