# Instalar: pip install openpyxl

import pandas as pd
import os

arquivo = 'c:/Users/Instrutor/Desktop/vendas.xlsx'
if os.path.exists(arquivo):
    vendas = pd.read_excel(arquivo)
    print("Arquivo existente")
else:
    print("Nenhum arquivo encontrado. Um novo foi criado.")
    vendas = pd.DataFrame([
        [1, 'Lapis', 10, 0.10],
        [2, 'Borracha', 15, None],
        [3, 'Agenda', 8, 0.15],
        [4, 'Fichario', 20, None]
    ], columns=['ID', 'Produto', 'Quantidade', 'Comissao'])

vendas.to_excel(arquivo, index=False)

media_comissao = vendas['Comissao'].mean()
vendas['Comissao'] = vendas['Comissao'].fillna(media_comissao)

arquivo2 = 'c:/Users/Instrutor/Desktop/vendas_comissao.xlsx'
vendas.to_excel(arquivo2, index=False)

print(vendas.head())
