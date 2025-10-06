# Estrutura de decisão em Phython

- A declaração if executa um bloco de código se uma condição for verdadeira. Em portugol seria o “SE”

EX: 
x = 10
if x > 5:
    print("x é maoir que 5")

- A declaração else fornece um caminho alternativo caso acondição no if seja falsa.Em portugol “Senao”

EX:
x = 10
if x > 5:
    print("x é maoir que 5")
else:
    print("x é menor ou igual a 5)

- Declaração elif (else if)
Permite testar várias condições. Se a primeira condição for falsa, ela testa a próxima.Em portugol (senao se)

EX:
x = 7
if x > 10:
    print("x é maoir que 5")
elif x > 5:
    print("x esta entre 6 e 10)
else:
    print("x é 5 ou menor)

## Expressão condicional (ternária)
- Permite a escrita de decisões simples em uma única linha.

resultado = valor1 if condição else valor2

EX:
x = 10
mensagem = "x é grande" if x > 5 else "x é pequeno"
print (mensagem)

# Operadores lógicos
- Comparadores: ==, !=, >, <, >=, <=

- Operadores lógicos: and, or, not