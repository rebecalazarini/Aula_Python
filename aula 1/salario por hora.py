# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

salario = float(input("Digite o salario por hora: "))
hora = float(input("Digite a quantidade de horas trabalhadas no mes: "))

salario_mes = salario * hora

print("O salario mensal é igual a", salario_mes)