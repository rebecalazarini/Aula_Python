# Crie uma lista com os nomes de 5 frutas e peça ao usuário para adicionar mais 3 frutas. Imprima a lista final. 

frutas = ['maçã', 'banana', 'laranja', 'uva', 'manga']
for i in range(3):
    nova_fruta = input("Digite o nome de uma fruta para adicionar à lista: ")
    frutas.insert(4, nova_fruta)
print(frutas)