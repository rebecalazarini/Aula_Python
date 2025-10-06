# Verificação de Positivo/Negativo/Zero: Escreva um programa que peça um número e informe se ele é positivo, negativo ou zero.
num = int(input("Digite um numero: "))
if num > 0:
    print("O numero", num, "é positivo")
elif num < 0:
    print("O numero", num, "é negativo")
else:
    print("O numero é zero")