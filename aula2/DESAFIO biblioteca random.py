# Jogo de Adivinhação: Escreva um programa que escolhe aleatoriamente um número entre 1 e 100. O usuário deve tentar adivinhar o número, e o programa deve dar dicas se o número é maior ou menor a cada tentativa.
# Dica: importar uma biblioteca que se chama "random". Busque como funciona a biblioteca. Dica: Utilizara um laço de repetição... Verifique qual melhor se enquadra
import random
numero_secreto = random.randint(1, 100)
tentativas = 0
print("Bem-vindo ao jogo de adivinhação!")
while True:
    palpite = int(input("Digite seu palpite (entre 1 e 100): "))
    tentativas += 1
    if palpite < numero_secreto:
        print("Tente um número maior.")
    elif palpite > numero_secreto:
        print("Tente um número menor.")
    else:
        print(f"Parabéns! Você adivinhou o número {numero_secreto} em {tentativas} tentativas.")
        break