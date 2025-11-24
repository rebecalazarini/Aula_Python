import pandas as pd
dados = {
    'Produto':['Caderno', 'Lapis', 'Mochila', 'Borracha'],
    'Preco':[12, 2, 85, 3],
    'Vendidos':[40, 150, 10, 80]
}
df = pd.DataFrame(dados)
df['Faturamento'] = df['Preco'] * df['Vendidos']

print("\nFaturamento acima de 100 reais: ")

print(df[df['Faturamento'] > 500])
df.to_csv("faturamento_acima_100.csv", index=False)

# Ordem alfabetica
df = df.sort_values('Produto')
print("\nArquivo em ordem alfabetica")
print(df)
df.to_csv("ordem.csv", index=False)