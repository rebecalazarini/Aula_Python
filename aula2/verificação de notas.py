# Verificação de Notas: Peça ao usuário para inserir uma nota entre 0 e 100 e informe se ele foi aprovado (nota >= 60) ou reprovado.

nota = int(input("Digite sua nota (0-100): "))
resultado = "Aprovado" if nota >= 60 else "Reprovado"
print("Você foi", resultado)