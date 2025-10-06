# Calculadora de Ano Bissexto: Escreva um programa que determine se um ano fornecido é bissexto ou não.Dica: Qualquer ano que seja uniformemente divisível por 4 é um ano bissexto: por exemplo, 1988, 1992 e 1996 são anos bissextos.
ano = int(input("Digite o ano: "))
if ano % 100 != 0 and ano % 4 == 0 or ano % 400 == 0:
   print("É um ano bissexto")
else:
    print("Não é ano bissexto")