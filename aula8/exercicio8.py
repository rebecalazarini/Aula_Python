# Instalar: pip install openpyxl

import pandas as pd
import os

arquivo = 'c:/Users/Instrutor/Desktop/transacoes.xlsx'

if os.path.exists(arquivo):
    transacoes = pd.read_excel(arquivo)
    print("Arquivo existente")
else:
    print("Nenhum arquivo encontrado. Um novo foi criado.")
    transacoes = pd.DataFrame([
        [1, 'João', 100],
        [2, 'Ana', 200],
        [3, 'Carlos', 150],
        [1, 'João', 50],
        [2, 'Ana', 300],
        [3, 'Carlos', 200]
    ], columns=['ID', 'Cliente', 'Valor'])


transacoes.to_excel(arquivo, index=False)

resumo = transacoes.groupby('Cliente').agg(Total_Transacoes=('Valor', 'sum')).reset_index()

arquivo2 = 'c:/Users/Instrutor/Desktop/resumo_transacoes.xlsx'
resumo.to_excel(arquivo2, index=False)

print(resumo.head())
