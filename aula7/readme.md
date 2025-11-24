# Biblioteca Pandas
## criada para trabalhar com grandes volumes de dados de forma eficiente e flexível. Ela fornece estruturas de dados e ferramentas para análise de dados, sendo amplamente usada em ciência de dados e aprendizado de máquina, devido à sua capacidade de manipulação de dados de forma tabular (similar ao Excel).

# Quando utilizar o panda
- Utilize Pandas quando precisar:
- Manipular grandes volumes de dados tabulares.
- Fazer operações de leitura, limpeza, transformação e análise de dados.
- Manipular arquivos de dados (como .csv, .excel, .json, .txt).
- Trabalhar com dados numéricos e alfanuméricos.

# Para instalar Pandas, você pode usar o seguinte comando no terminal:
- PIP INSTALL PANDAS

## Estruturas de Dados em Pandas
- Series: Uma estrutura unidimensional, similar a uma coluna de dados, com índices.
- DataFrame: Estrutura bidimensional (linhas e colunas), similar a uma tabela, onde cada coluna é uma Series.

## SERIE
- Uma Series em Pandas é uma estrutura de dados unidimensional, similar a uma lista ou um array, mas com o diferencial de possuir um índice associado a cada elemento. É como se fosse uma coluna de dados com rótulos para cada linha.
  - Características principais 
    - Unidimensional: Uma Series contém apenas uma coluna de dados.
    - Índices: Cada valor em uma Series é indexado, e você pode acessar 
    - valores específicos através desses índices.
    - Flexível com Tipos de Dados: Pode armazenar qualquer tipo de dado, como números, strings, datas, etc.

# Exemplo:
```bash
import pandas as pd
dados = [10, 20, 30 , 40]
serie = pd.Series(dados)
print(serie)
```
# Definindo índices
```bash
serie = pd.Series(dados, index=['a','b','c',d'])
print(serie)
```
# Operações com series
```bash
print(serie[serie > 15])
```
```bash
print(serie * 2)
```
# Dataframe
- Um DataFrame é uma estrutura de dados bidimensional, como uma tabela, onde cada coluna é uma Series. Ele é o principal objeto de dados em Pandas, pois organiza dados em linhas e colunas, permitindo a manipulação tabular com facilidade.

## Características principais 
- Bidimensional: Um DataFrame possui linhas e colunas.
- Colunas com Índices: Cada coluna tem seu próprio índice e nome, facilitando a organização.
- Tipos de Dados Diversos: Pode conter dados de diferentes tipos, por exemplo, números em uma coluna e strings em outra.

# Exemplo
```bash
dados = {
    'Nome':['Alice', 'Bob', 'Carlos],
    'Idade':[25, 20, 25],
    'Salario':[5000, 6000, 7000]
}
df = pd.DataFrame(dados)
print(df)
```
# A partir de uma lista de listas
```bash
dados = [['Alice', 25, 5000], ['Bob', 30 , 6000], ['Carlos', 35 , 7000]]
df = pd.DataFrame(dados, columns=['Nome', 'Idade', 'Salario'])
print(df)
```

# Operações com DataFrame 
- Selecionar colunas: print(df['Nome’])
- Selecionar múltiplas colunas: print(df[['Nome', 'Salario’]])
- Filtrar Dados (linhas): print(df[df['Idade'] > 28])
- Adicionar Nova Coluna: df['Bonus'] = df['Salario'] * 0.1
- Remover Coluna: df = df.drop(columns=['Bonus’])
- Estatísticas Rápidas: print(df.describe())
