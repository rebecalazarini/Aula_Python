#  Instalar: pip install openpyxl

import pandas as pd
import os

arquivo = 'c:/Users/Instrutor/Desktop/funcionarios.xlsx'

if os.path.exists(arquivo):
    funcionarios = pd.read_excel(arquivo)
    print("Arquivo existente")
else:
    print(" Nenhum arquivo encontrado. Um novo foi criado.")
    funcionarios = pd.DataFrame([
        [1, 'Marcelo', 'Vendas', 2000],
        [2, 'Carlos', 'TI', 3200],
        [3, 'Luiza', 'TI', 3200],
        [4, 'Hector', 'RH', 1990],
        [5, 'Maria', 'Vendas', 2000]
    ], columns=['ID', 'Nome', 'Setor', 'Salario'])

funcionarios.to_excel(arquivo, index=False)

vendas = funcionarios[funcionarios['Setor'] == 'Vendas'].copy()
vendas['Salario'] = vendas['Salario'] * 1.15

arquivo2 = 'c:/Users/Instrutor/Desktop/funcionarios_alterados.xlsx'
vendas.to_excel(arquivo2, index=False)

print(vendas.head())