nomes =  ["Guido van Rossum", "Linus Benedict Torvalds", "Arthur Dent", "Ford Prefect",  "Tricia McMillan", "Prostetnic Vogon Jeltz"] 

# Imprima, para cada pessoa, seu nome em formato de citação acadêmica.
# Por exemplo:
#  "Gabriel Nascarella Hishida" vira "HISHIDA, G. N."

for nome in nomes:

    resultado = nome.split()[-1].upper()
    subnomes = nome.split()
    for subnome in subnomes[:-1]:
        resultado += " " + subnome[0]

    print(resultado)