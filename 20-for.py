alunos = ["João", "Guilherme", "Tiago", "Vinicius", "Ian"]
notas = [0, 100, 90, 80, 70,]

for aluno in alunos:
    print(aluno + " é aluno", end=" ")
    if aluno in aprovados:
        print("aprovado")
    else:
        print("reprovado")
