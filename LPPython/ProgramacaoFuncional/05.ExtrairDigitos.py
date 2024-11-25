texto = "Eu tenho 2 maçãs e 3 laranjas."

numero = list(filter(lambda n: '2' in n or '3' in n, texto))

print(numero)