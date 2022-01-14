retangulos = [(20, 40), (300, 50), (90, 100), (50, 50), (80, 5), (40, 1000)]

# Com base na lista de retangulos representados
# como duplas (largura, comprimento),
# imprima, para cada retangulo, a sua area.

for largura, comprimento in retangulos: 
    area = largura * comprimento

    print(f"A área do retângulo é {area}")