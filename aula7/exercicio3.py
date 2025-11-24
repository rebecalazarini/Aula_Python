import pandas as pd

dados = {
    'Nome':['Ana Souza', 'João Lima', 'Carla Mendes', 'Pedro Rocha'],
    'Idade':[28, 32, 41, 22],
    'Salario':[3500, 4200, 5100, 2800]
}
df = pd.DataFrame(dados)

# Salario acima da media
media_salario = df['Salario'].mean()
print("Média dos salários: ", media_salario)
print("\nFuncionários com salário acima da média:")
print(df[df['Salario'] > media_salario])
df.to_csv("acima_media.csv", index= False)

# salario em ordem descrescente
print("\nSalario em ordem descrecente:")
df_desc = df.sort_values('Salario', ascending=False)
print(df_desc)

print("\nFuncionários com idade menor que 30:")
print(df[df['Idade'] < 30 ])
df.to_csv("idade_menor_30.csv", index= False)
