#  Instalar: pip install openpyxl

import pandas as pd
import os

arquivo = 'c:/Users/Instrutor/Desktop/estoque.xlsx'

if os.path.exists(arquivo):
    estoque = pd.read_excel(arquivo)
    print("Arquivo existente")
else:
    print(" Nenhum arquivo encontrado. Um novo foi criado.")
    estoque = pd.DataFrame([
        [1, 'Teclado', 45.00, 30 ],
        [2, 'Mouse', 17.00, 45],
        [3, 'Monitor', 300.00, 38],
        [4, 'Headset', 150.00, 2],
        [5, 'Webcam', 20.00, 25]
    ], columns=['ID', 'Nome', 'Preco', 'Estoque'])

estoque.to_excel(arquivo, index=False)

estoque = pd.DataFrame(estoque)
estoque['Total'] = estoque['Preco'] * estoque['Estoque']

arquivo2 = 'c:/Users/Instrutor/Desktop/estoque_alterados.xlsx'
estoque.to_excel(arquivo2, index=False)

print(estoque.head())