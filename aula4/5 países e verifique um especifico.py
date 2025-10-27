 # Crie uma lista com os nomes de 5 países e verifique se um país específico está na lista. 
paises = ['Brasil', 'Argentina', 'Chile', 'Colombia', 'Italia']
pais_especifico = input("Digit eo nome do país pra ver se esta na lista: ")
if pais_especifico in paises:
    print(f"{pais_especifico} está na lista.")
else:
    print(f"{pais_especifico} não está na lista.")
