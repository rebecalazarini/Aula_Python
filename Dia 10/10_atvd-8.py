# Manipulação de dicionário.
# Crie uma dicionário e peça ao usuário para acessar uma chave. Captura KeyError e exiba uma mensagem apropriada.

Alunos = [
  {
    "Nome": "Ana",
    "Nota1": 8.5,
    "Nota2": 5.2,
    "Nota3": 6.4
},
  {
    "Nome": "Rebeca",
    "Nota1": 7,
    "Nota2": 10,
    "Nota3": 5
},
  {
    "Nome": "Ricardo",
    "Nota1": 9,
    "Nota2": 5.2,
    "Nota3": 7
},
  {
    "Nome": "Steffanny",
    "Nota1": 5,
    "Nota2": 10,
    "Nota3": 7
}
]

for aluno in Alunos:
    try:
        # Calcula a média do aluno
        media = (aluno["Nota1"] + aluno["Nota2"] + aluno["Nota3"]) / 3
        print(f"{aluno['Nome']} --- Média: {media:.2f}")
    except KeyError as e:
        print(f"Chave {e} não encontrada para o aluno {aluno.get('Nome', 'Desconhecido')}")