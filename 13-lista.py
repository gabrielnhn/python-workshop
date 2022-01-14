nomes = ["Joao", "Lucas", "Juliana"]

numeros = [42, 420, 13, 27, 69, 81]

coisas = [3.1415926535, 'oi', -20, [1,2,3]]

l = []

l.append(5)
l.append(6)

print(l[1])

l.insert(1, 42)
a = l.pop(1)

l.remove(5)

try:
    l.remove(69)
except:
    print("ERRO!")

l.clear()
print(l)

print(numeros != nomes)

print(numeros + nomes)