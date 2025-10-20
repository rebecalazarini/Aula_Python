# Estrutura de decisão em Phython

- O for loop em Python é usado para iterar sobre uma sequência (como uma lista, string ou range de números). Ele percorre cada item da sequência e executa o bloco de código dentro do loop.
- Exemplo, esse código imprime números de 0 a 4
```bash
for i in range(5):
print(i)
```
- While loop: O while loop repete um bloco de código enquanto uma condição for verdadeira. É útil quando não sabemos exatamente quantas vezes o loop precisará ser executado.
-Exemplo, esse código também imprime os números de 0 a 4, como o for, mas aqui usamos uma variável para controlar o loop.
```bash
i = 0
while i < 5:
print(i)
i +=1
```
- Do-While (Simulação em Python): Python não tem uma estrutura do-while nativa, mas podemos simular seu comportamento. Em um do-while, o bloco de código é executado pelo menos uma vez, independentemente da condição, e depois a condição é verificada.
- Exemplo, Esse código imprime de 0 a 4, simulando o comportamento de um do-while.
```bash
i = 0
while True:
print(i)
i += 1
if i >= 5:
break
```