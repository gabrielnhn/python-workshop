# Parte 1:
    # Escreva um programa que, com base no arquivo 'advertencias.txt',
    # imprima para cada membro todas as advertencias que o mesmo tomou,
    # e se recebeu mais que 2 advertencias, imprima que o mesmo está CANCELADO.

# Parte 2:
    # Cada advertência, na prática, tem validade de apenas 1 ano.
    # Ignore todas as advertências feitas a mais de 1 ano. 

import datetime

advertecias = {}

with open("./advertencias.txt", "r") as file:
    for line in file:

        line = line.rstrip()
        razao = line.split(': ')[1]
        line = line.split(':')[0]
        nome = line.split(') ')[1]

        # print(nome)
        if nome in advertecias:
            advertecias[nome].append(razao)
        else:
            advertecias[nome] = [razao]

        # advertecias[nome] = advertecias.get(nome, 0) + 1

for nome, razoes in advertecias.items():
    # print(nome, razoes)
    print(nome, len(razoes))
    if len(razoes) >= 3:
        print("BANIDO")

        