# Simule um do-while para fazer o usuário adivinhar um número entre 1 e 10.
import random
numero = random.randint(1, 10)

chute = 0 
while chute != numero:
    chute_str = input("Adivinhe o número (entre 1 e 10): ")
    chute = int(chute_str) # Converte para um número inteiro
    if chute < numero:
        print("Tente um número maior!")
    elif chute > numero:
        print("Tente um número menor!")
print("Parabéns! Você acertou!") 