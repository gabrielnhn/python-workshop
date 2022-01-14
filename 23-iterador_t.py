l = [('a', 1), ('c', 3), ("K", 42)]

for t in l:
    letra, numero = t
    print(letra, numero)

for letra, numero in l:
    print(letra, numero)