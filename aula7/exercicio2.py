# função .mean(): calcula a média aritmética (soma dos valores dividido pela quantidade) de uma Series ou das colunas numéricas de um DataFrame.

import pandas as pd

dados = {
    'Item':['Pendrive','Headset','WebCam','Teclado MK'],
    'Quantidade':[25, 12, 8, 15],
    'PrecoUnitario':[30, 150, 220, 95]
}

df = pd.DataFrame(dados)

df['Total'] = df['Quantidade'] * df['PrecoUnitario']
df.to_csv("tabela_completa.csv", index=False)
print("Tabela Completa:\n", df)

# media do spreços unitarios
print("\n Média dos preços unitarios: ")
print(df['PrecoUnitario'].mean())


print("\n Preço maior que 100 e tabela alterada: ")
print(df[df['PrecoUnitario'] > 100])
df.to_csv("filtro_maior_100.csv", index=False)
