import pandas as pd

dados = [10, 20, 30, 40]
serie = pd.Series(dados, index=['a','b', 'c', 'd'])
print(serie[serie > 15])

# import pandas as pd
# dados = [10, 20, 30 , 40]
# serie = pd.Series(dados)
# print(serie)

# import pandas as pd
# dados = [10, 20, 30 , 40]
# serie = pd.Series(dados, index=['a','b','c','d'])
# print(serie)

# import pandas as pd
# dados = [10, 20, 30 , 40]
# serie = pd.Series(dados, index=['a','b','c','d'])
# print(serie * 2)