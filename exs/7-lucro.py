# A tabela 'compras.csv' mostra quanto que certa loja
# pagou na compra de produtos que revendeu, a cada mes;
# E a tabela 'vendas.csv' mostra o quanto que a loja
# recebeu vendendo os mesmos produtos.

# Escreva um programa que leia o conteudo destes 2 arquivos
# e escreve em um nova tabela 'lucro.csv' o lucro da loja em cada mes.

import csv
with open("./vendas.csv", "r") as vendas_file:
    vendas = {}
    vendas_reader = csv.reader(vendas_file)

    for linha in vendas_reader:
        if linha[0] != "DATA":
            vendas[linha[0]] = eval(linha[1])
    
    # print(vendas)

with open("./compras.csv", "r") as compras_file:
    compras = {}
    compras_reader = csv.reader(compras_file)

    for linha in compras_reader:
        if linha[0] != "DATA":
            compras[linha[0]] = eval(linha[1])
    
    # print(compras)

lucros = {}

for data in compras:
    venda = vendas[data]
    compra = compras[data]

    lucro = venda - compra
    lucros[data] = lucro

print(lucros)



with open("./lucro.csv", "w", newline='') as file:
    writer = csv.writer(file)

    writer.writerow(("DATA", "LUCRO"))

    for data, valor in lucros.items():
        writer.writerow((data, valor))

