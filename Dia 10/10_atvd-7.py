# Processamento de lista de números peça ao usuário para digitar uma lista de números separados por virgula.
# Calcule uma média, tratando erros de entrada e divisão por zero.

try:
    entrada = input("Digite números separados por vírgula: ")
    # separar os números
    partes = entrada.split(",")
    
    soma = 0
    quantidade = 0
    
    for p in partes:
        p = p.strip()  # tira espaços
        if p != "":
            soma += float(p)
            quantidade += 1
    
    if quantidade == 0:
        print("Você não digitou nenhum número!")
    else:
        media = soma / quantidade
        print("A média é:", media)

except ValueError:
    print("Erro! Digite apenas números separados por vírgula.")

finally:
  print("Execução do bloco try-finally foi concluída com sucesso!")