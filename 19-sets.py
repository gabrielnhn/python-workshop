# Conjuntos
# Mutável

# Conjuntos matemáticos. Não tem ordem, não tem elementos repetidos.

s = set() ### NÃO FAÇA s = {}.
s = {2, 3, 3.1, 4} 

s.add(42)
s.remove(42)

print(42 in s)

l = [0, 1, 0, 13]
s = set(l)
l = list(s)
