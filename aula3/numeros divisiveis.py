# Faça um programa que conte quantos números entre 100 e 999 são divisíveis por 3 e 7 simultaneamente.

contador = 0

for numero in range(100, 1000):
    if numero % 3 == 0 and numero % 7 == 0:
        contador += 1
    print(f"Existem {contador} números entre 100 e 999 que são divisíveis por 3 e 7 simultaneamente.")