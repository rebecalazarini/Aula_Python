# Peça ao usuário para inserir números até que ele insira um número negativo. Use um loop while.

n = 0
while n >= 0:
    digite = input("Digite um numero: ")
    if n >= 0:
        print("Numero positivo")
        break
    print("Numero negativo")