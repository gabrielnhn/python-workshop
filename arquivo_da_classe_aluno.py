class Aluno:
    instituicao = "UFPR"

    def __init__(self, nome, grr, periodo, curso):
        self.nome = nome
        self.grr = grr
        self.periodo = periodo
        self.curso = curso
        self.notas = []

    def recebe_nota(self, x):
        self.notas.append(x)

    def IRA(self):
        if self.notas == []:
            return 0
        else:
            return (sum(self.notas) / len(self.notas))
    
    def __str__(self):
        return f"{self.nome}, grr{self.grr}, ira: {self.IRA()}"



aluno = Aluno("Alexandre", "20181962", 8, "Engenharia Mecânica")

outro_aluno = Aluno("Gabriel", "20190261", 6, "BCC")

outro_aluno.recebe_nota(100)

# aluno.recebe_nota(7)
# aluno.recebe_nota(0)
# aluno.recebe_nota(10)

# print(f"IRA: {aluno.IRA()}")
# print(f"IRA: {outro_aluno.IRA()}")


# print(aluno)