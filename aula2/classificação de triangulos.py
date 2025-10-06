# Classificação de Triângulos: Escreva um programa que peça os três lados de um triângulo e determine se ele é equilátero, isósceles ou escaleno.

a = int(input("Digite o primeiro lado do triângulo: "))
b = int(input("Digite o segundo lado do triângulo: "))
c = int(input("Digite o terceiro lado do triângulo: "))
if a == b == c:
    print("O triângulo é equilátero.")
elif a == b or b == c or a == c:
    print("O triângulo é isósceles.")
else:
    print("O triângulo é escaleno.")
