# Escreva um programa que peça um número ao usuário e imprima todos os números primos menores ou iguais a esse número usando um loop for.

def primo(n):

    if n <= 1:
        return False
    for i in range (2, n):
     if n % i == 0:
        return False
    return True
numero = int(input("Digite um numero: "))
print ("Os numeros primos menores ou iguais são:")
for i in range (2, numero + 1):
    if primo(i):
     print(i)
