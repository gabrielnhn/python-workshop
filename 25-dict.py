

notas = {"Gabriel": 85, "Julia": 100, "Alberto": 90}

notas["Lucas"] = 95

# print(notas)

# Convidados para uma festa
convidados = {
    "Ryu": "VIP", "Chun Li": "Convidado", "Honda": "VIP",
    "Ken": "Convidado", "Zangief": "Convidado", "Guile": "VIP"
}


for pessoa in ("Ryu", "Zangief", "Scorpion"):
    print(f"{pessoa} é {convidados.get(pessoa, 'Não convidado')}")

# for convidado in convidados:
#     print(convidado)

# for aluno, nota in notas.items():
#     print(f"{aluno} teve nota {nota}")

