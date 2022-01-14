texto_n = input("Insira n: ")
# a partir de um número N lido do terminal,
# imprima na saída padrão todos os naturais>0 pares menores
# ou iguais à N!
n = eval(texto_n)

i = 1
while i <= n:

    if (i % 2) == 0:
        print(i) 

    i += 1
