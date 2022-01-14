# Descrevendo estruturas
# Duas maneiras de conseguir uma lista cujos elementos sao o dobro de outra
num = [1, 3, 5, 6]

# Lista de repetidos 6

muitos_seis = [6 for i in range(40)]
# print(muitos_seis)


# Outra maneira de fazer o ex 3!
# impares = [i for i in range(1, 100) if (i%2)==1]
# print(impares)

num = [-39, -21, 17, -36, -39, 12, 12, -4, 5, -34, -23, -18, 30, 5, -24, -23, -3, 30, 21, -29, -43, 35, -31, 0, -8, 25, 43, 4, 42, -49, -37, 24, -11, -22, -45, -33, 30, 2, -46, -35]

dobro_positivo = [x*2 if x > 0 else abs(x)*2 for x in num]

print(dobro_positivo)
