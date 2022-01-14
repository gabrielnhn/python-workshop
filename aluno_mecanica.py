from arquivo_da_classe_aluno import Aluno

class Aluno_mecanica(Aluno):
    curso = "Mecânica"

    def __init__(self, nome, grr, periodo):
        self.nome = nome
        self.grr = grr
        self.periodo = periodo
        self.notas = []
    
    def jogar_sinuca_no_caem(self):
        print(f"{self.nome} se sente revitalizado após jogar aquela sinuca no CAEM")
    

pi = 3.14159265358979323846
