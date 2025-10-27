# Listas

- Listas são estruturas de dados em Python utilizadas para armazenar coleções de itens, podendo ser de diferentes tipos (números, strings, outras listas, etc.). Elas são mutáveis, ou seja, você pode adicionar, remover ou modificar elementos após a criação da lista.

- Criando uma lista
```bash
minha_lista = [1,2,3,"oi",True]
```

- Acessando elementos
```bash
minha_lista = ['manga', 'banana', 'maçã', 'laranja', 'coco']
primeiro_elemento = minha_lista[0] # Acessa o indice 0 (manga)
ultimo_elemento = minha_lista[-1] # Acessa o último indice (coco)

print(primeiro_elemento)
print(ultimo_elemento)
```
- Adicionando elementos
```bash
minha_lista.append(4) # Adiciona ao final da lista, indice 4
minha_lista.insert(2, "novo") # Adiciona na posição 2
```
- Removendo elementos
```bash
minha_lista.remove("Ola") # Remove o primeiro elemento com o valor "Ola"
del minha_lista[0] # Remove o elemento na posição 0
```
## Método POP 
- O método pop() é uma ferramenta poderosa em Python quando se trata de manipular listas. Ele serve para remover e retornar um elemento de uma lista, o que significa que você pode tanto excluir o elemento quanto armazenar seu valor em uma variável para uso posterior.
- Como funciona o pop?
  - Remoção: O método pop() remove o elemento da lista na posição especificada.
  - Retorno: Ele retorna o valor do elemento que foi removido.
  - Sem índice: Se você não passar nenhum índice para o pop(), ele remove e retorna o último elemento da lista por padrão.
```bash
lista.pop(indice)
```
exemplo:
```bash
minha_lista = [10,20,30,40]

ultimo_elemento = minha_lista.pop()
print(ultimo_elemento) # Imprime só o 40
print(minha_lista) # Imprime [10,20,30]

# Removendo o elemento na posição 1
elemento_removido = minha_lista.pop(1)
print(elemento_removido) # Imprime 20
print(minha_lista) # Imprime [10,30]
```
- Usos comuns para o POP
  - Remoção de elementos: Quando você precisa remover um elemento específico de uma lista.
  - Implementação de pilhas (LIFO): O pop() é ideal para remover o último elemento adicionado a uma lista, simulando o comportamento de uma pilha.
  - Implementação de filas (FIFO): Embora não seja a forma mais eficiente, o pop(0) pode ser usado para remover o primeiro elemento adicionado a uma lista, simulando o comportamento de uma fila.
- Cuidados com o pop 
  - Índice inválido: Se você passar um índice que não existe na lista, ocorrerá um IndexError.
  - Lista vazia: Tentar remover um elemento de uma lista vazia também resultará em um IndexError.
- Quando usar o POP VS DEL
  - pop(): Quando você precisa tanto remover o elemento quanto obter seu valor.
  - del: Quando você apenas precisa remover o elemento e não se importa com seu valor.
## INSERT: Inserindo Elementos em Listas
- O método insert() é outra ferramenta útil para manipular listas em Python. Diferentemente do pop(), que remove elementos, o insert() adiciona um elemento a uma lista em uma posição específica.

- Como funciona o Insert?
  - Inserção: O método insert() insere um elemento na posição indicada, deslocando os demais elementos para a direita.
  - Argumentos: O insert() recebe dois argumentos:
  - O índice onde o elemento será inserido.
  - O valor a ser inserido.
```bash
minha_lista = [10,20,30]
minha_lista.insert(1, 15) # Insere o 15 no indice 1
print(minha_lista) # Imprima [10, 15, 20,30]
```
## Comparando insert() com append():
 - append(): Adiciona um elemento ao final da lista.
 - insert(): Adiciona um elemento em uma posição específica.

## Cuidados para utilizar o insert
- Índice inválido: Se você passar um índice maior que o comprimento da lista, o elemento será inserido no final.
- Índice negativo: Índices negativos contam a partir do final da lista.
```bash
nomes = []
for i in range(3):
nome = input("Digite um nome: ")
nomes.insert(0, nome) # Insere no inicio e mantem a ordem de digitação
print(nomes)
```
 