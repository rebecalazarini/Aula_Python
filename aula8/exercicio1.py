# Instalar: pip install openpyxl

import pandas as pd
import os

arquivo = 'c:/Users/Instrutor/Desktop/produtos.xlsx'

if os.path.exists(arquivo):
    produtos = pd.read_excel(arquivo)
    print("Arquivo existente")
else:
    print(" Nenhum arquivo encontrado. Um novo foi criado.")
    produtos = pd.DataFrame([
        [1, 'Teclado', 120.00, 30],
        [2, 'Mouse', 60.00, 50],
        [3, 'Monitor', 900.00, 12],
        [4, 'Headset', 150.00, 20],
        [5, 'Webcam', 200.00, 15]
    ], columns=['ID', 'Nome', 'Preco', 'Estoque'])

produtos.to_excel(arquivo, index=False)
print(produtos.head())