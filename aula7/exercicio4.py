import pandas as pd

dados = ({
    'produto':['Impressora', 'Tablet', 'SSD', 'Mouse'],
    'Avaliacoes':[
        [5,4,4,3],
        [4,5,5,5],
        [5,5,5,4],
        [3,4,3,4]
    ]
})

# media das avaliacoes
df = pd.DataFrame(dados)
df['Media_Avaliacoes'] = df['Avaliacoes'].apply(lambda x: sum(x)/len(x))
print("\nMedia: ")
print(df)

# media >=4.5
print("\nMedia >= 4.5:")
print (df[df['Media_Avaliacoes'] >= 4.5])
df.to_csv("Media_Avaliacoes.csv", index= False)

# ordem decrescente
print("\nOrdem decrescente das medias: ")
df_desc = df.sort_values('Media_Avaliacoes', ascending=False)
print(df_desc)