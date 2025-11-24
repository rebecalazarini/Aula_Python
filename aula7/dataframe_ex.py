import pandas as pd

# dados = {
#     'Nome':['Alice', 'Bob', 'Carlos],
#     'Idade':[25, 20, 25],
#     'Salario':[5000, 6000, 7000]
# }
# df = pd.DataFrame(dados)
# print(df)
#  print (df[df['Idaded'] > 28])

# Criar coluna 
# df['Bonus'] = df ['Salario'] * 0.1
# print (df)

# Excluir coluna
# df= df.drop(columns=['Bonus'])

dados = [['Alice', 25, 5000], ['Bob', 30 , 6000], ['Carlos', 35 , 7000]]
df = pd.DataFrame(dados, columns=['Nome', 'Idade', 'Salario'])
print(df)