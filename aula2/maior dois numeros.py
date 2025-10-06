# Maior de Dois Números: Peça dois números ao usuário e determine qual é o maior.
a = int(input("Digite um numero: "))
b = int(input("Digite outro numero: "))

resultado = a if a > b else b

print("O maior numero entre", a, "e", b, "é", resultado)