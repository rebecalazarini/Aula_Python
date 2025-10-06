# Verificação de Paridade: Escreva um programa que peça ao usuário para inserir um número e imprima se ele é par ou ímpar.
x = int (input("Digite um numero pra verficar se é par ou impar: "))
if x % 2 == 0:
    print("O numero", x, "é par")
else:
    print("O numero", x, "é impar")