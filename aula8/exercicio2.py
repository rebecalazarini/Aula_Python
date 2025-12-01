#  Instalar: pip install openpyxl

import pandas as pd
import os

arquivo = 'c:/Users/Instrutor/Desktop/produtos_normal.xlsx'

if os.path.exists(arquivo):
    produtos = pd.read_excel(arquivo)
    print("Arquivo existente")
else:
    print(" Nenhum arquivo encontrado. Um novo foi criado.")
    produtos = pd.DataFrame([
        [1, 'Teclado', 45.00, 30],
        [2, 'Mouse', 17.00, 50],
        [3, 'Monitor', 300.00, 12],
        [4, 'Headset', 150.00, 20],
        [5, 'Webcam', 20.00, 15]
    ], columns=['ID', 'Nome', 'Preco', 'Estoque'])

produtos.to_excel(arquivo, index=False)

produtos = produtos[produtos['Preco'] > 50]

arquivo2 = 'c:/Users/Instrutor/Desktop/produtos_acima_50.xlsx'
produtos.to_excel(arquivo2, index=False)

print(produtos.head())