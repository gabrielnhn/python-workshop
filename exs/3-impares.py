# Leia um numeiro inteiro positivo n do terminal,
# e imprima todos os inteiros ímpares positivos ate n
texto_n = input()
n = eval(texto_n)

print(list(range(1, n+1, 2)))