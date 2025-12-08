# Instalar: pip install openpyxl

import pandas as pd
import os

arquivo = 'c:/Users/Instrutor/Desktop/notas_alunos.xlsx'

if os.path.exists(arquivo):
    notas = pd.read_excel(arquivo)
    print("Arquivo existente")
else:
    print("Nenhum arquivo encontrado. Um novo foi criado.")
    notas = pd.DataFrame([
        ['Ana', 8.5],
        ['Carlos', 6.0],
        ['Maria', 7.2],
        ['João', 5.8]
    ], columns=['Aluno', 'Media'])

notas.to_excel(arquivo, index=False)
notas['Situacao'] = notas['Media'].apply(lambda x: 'Aprovado' if x >= 7 else 'Reprovado')

arquivo2 = 'c:/Users/Instrutor/Desktop/notas_situacao.xlsx'
notas.to_excel(arquivo2, index=False)

print(notas.head())
