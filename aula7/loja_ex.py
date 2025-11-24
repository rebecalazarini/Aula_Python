import pandas as pd
dados = {
    'Produto':['Mouse', 'Teclado', 'Monitor', 'Cabo HDMI'],
    'Preco':[50, 150, 800, 30],
    'Estoque':[200, 150, 75, 500]
}
df = pd.DataFrame(dados)
df['Total'] = df['Preco'] * df['Estoque']

df.to_csv("tabela_completa.csv", index=False)
print ("tabela Conpleta: \n", df)

# Criar arquivo CSV
print("\n arquivo 'tabela_completa.csv' criado com sucesso!")

# Filtro pra mostrar os preços maior que 100
print("\n Preço maior que 100 e tabela alterada: ")
print(df[df['Preco'] > 100])
df.to_csv("filtro_maior_100.csv", index=False)

