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


pi = 3.14