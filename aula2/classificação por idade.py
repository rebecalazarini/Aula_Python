# Classificação por Idade: Crie um programa que peça a idade do usuário e classifique-o como: Menor de idade (abaixo de 18) Adulto (entre 18 e 64) Idoso (65 ou mais)

idade = int(input("Digite sua idade: "))
if idade < 18:
    print("Você é menor de idade.")
elif 18 <= idade <=64:
    print("Você é adulto.")
else:
    print("Você é idoso.")