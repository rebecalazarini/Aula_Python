# Instalar: pip install openpyxl

import pandas as pd
import os

arquivo = 'c:/Users/Instrutor/Desktop/produtos_cadastrados.xlsx'

if os.path.exists(arquivo):
    produtos = pd.read_excel(arquivo)
    print("Arquivo existente")
else:
    produtos = pd.DataFrame(columns=['ID', 'Nome','Preco', 'Estoque'])
    print(" Nenhum arquivo encontrado. Um novo foi criado.")

# define o próximo id automaticamente
if not produtos.empty:
    id_atual = produtos['ID'].max() + 1
else:
    id_atual = 1

while True:
    print("\nCadastro de Produtos")
    print(f"ID do Produto: {id_atual}")

    nome = input("Nome do Produto: ")
    preco = float(input("Preço do Produto: "))
    estoque = int(input("Qtd em estoque: "))

    produtos.loc[len(produtos)] = [id_atual, nome, preco, estoque]
    id_atual += 1
    print("Produtos ja cadstrados: ")
    print(produtos)

    continuar = input("Deseja cadastrar outro produto? (s/n): ").lower()
    if continuar == 'n':
        break

produtos.to_excel(arquivo, index=False)
print(f"\nDados salvos {arquivo}")