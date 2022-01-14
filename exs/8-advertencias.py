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

        informacoes = line.split(maxsplit=1)

        data = informacoes[0]
        dia, mes, ano = data[1:-1].split("/")
        data_advertencia = datetime.date(int(ano), int(mes), int(dia))

        hoje = datetime.date.today()
        ano_passado = datetime.date(hoje.year - 1, hoje.month, hoje.day)

        if ano_passado < data_advertencia:
            advertencia_valida = True
        else:
            advertencia_valida = False


        resto = informacoes[1]


        if advertencia_valida:
            nome, razao_advertencia = resto.split(": ")
            # print(f"nome: {nome}, razao: {razao_advertencia}")

            advertecias[nome] = advertecias.get(nome, 0) + 1

    print(advertecias)

for membro in advertecias:
    if advertecias[membro] > 2:
        print(f"{membro} foi cancelado.")
        pass
