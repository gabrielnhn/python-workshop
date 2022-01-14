
from arquivo_da_classe_aluno import Aluno
from aluno_mecanica import Aluno_mecanica as A_mec

g = Aluno("Gabriel", 2361, 5, "BCC")
a = A_mec("Alexandre", 1435, 7)

g.recebe_nota(90)
a.recebe_nota(95)

g.recebe_nota(80)
a.recebe_nota(100)

print(g)
print(a)
a.jogar_sinuca_no_caem()
g.jogar_sinuca_no_caem() # ?