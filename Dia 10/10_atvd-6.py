# Peça ao usuário uma tempreem Celsius e converta para Fahrenheit.
# Caputre erros de entrada e imprima a temperatura convertida

try: 
  Celsius = float(input("Digite uma temperatura em Celsius: "))

  fahrenheit = (Celsius * 9/5) + 32

except ValueError:
  print("Error: Você deve digitar apenas um número!")

else: 
  print(f"{Celsius} são {fahrenheit}")

finally:
  print("Execução do bloco try-finally foi concluída com sucesso!")