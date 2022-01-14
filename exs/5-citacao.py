nomes =  ["Guido van Rossum", "Linus Benedict Torvalds", "Arthur Dent", "Ford Prefect",  "Tricia McMillan", "Prostetnic Vogon Jeltz"] 

# Imprima, para cada pessoa, seu nome em formato de citação acadêmica.
# Por exemplo:
#  "Gabriel Nascarella Hishida" vira "HISHIDA, G. N."


for nome in nomes:
    print(nome.split()[-1].upper(), end=', ')    

    for subnome in nome.split()[:-1]:
        print(subnome[0], end=". ")
    
    print("")

