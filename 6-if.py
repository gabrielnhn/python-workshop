idade = eval(input())


if (idade < 12):
    print("é jovem")
    vacinado = False

elif (idade < 60):
    print("é adulto")
    vacinado = True

else:
    print(" é idoso")
    vacinado = True

if vacinado:
    print(" foi vacinado")
