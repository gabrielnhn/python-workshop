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
    
aluno = Aluno_mecanica("Alexandre", "20181962", 8)
aluno.recebe_nota(70)
aluno.IRA()
aluno.jogar_sinuca_no_caem()


outro_aluno = Aluno("Gabriel", "20190261", 6, "BRUHH")
outro_aluno.jogar_sinuca_no_caem()

print(aluno.instituicao)