#  Instalar: pip install openpyxl

import pandas as pd
import os

arquivo = 'c:/Users/Instrutor/Desktop/clientes_normal.xlsx'

if os.path.exists(arquivo):
    clientes = pd.read_excel(arquivo)
    print("Arquivo existente")
else:
    print(" Nenhum arquivo encontrado. Um novo foi criado.")
    clientes = pd.DataFrame([
        [1, 'Marcelo', 19],
        [2, 'Carlos', 12],
        [3, 'Luiza', 17],
        [4, 'Hector', 22],
        [5, 'Maria', 34]
    ], columns=['ID', 'Nome', 'Idade'])

clientes.to_excel(arquivo, index=False)

clientes = clientes[clientes['Idade'] > 18]

arquivo2 = 'c:/Users/Instrutor/Desktop/clientes_adultos.xlsx'
clientes.to_excel(arquivo2, index=False)

print(clientes.head())