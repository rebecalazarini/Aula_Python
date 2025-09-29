# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.

salario_hora = float(input("Digite o quanto voce ganha por hora: "))
horas_trabalhadas = float(input("Digite a quantidade de horas trabalhadas no mes: "))



salario_bruto = salario_hora * horas_trabalhadas
ir = salario_bruto * 0.11
inss = salario_bruto * 0.08
sindicato = salario_bruto * 0.05
salario_liquido = salario_bruto - ir - inss - sindicato
salario_bruto = salario_hora * horas_trabalhadas

print("O salario bruto é igual a", salario_bruto)
print("O valor do IR é igual a", ir)
print("O valor do INSS é igual a", inss)
print("O valor do Sindicato é igual a", sindicato)
print("O salario liquido é igual a", salario_liquido)