'''Extrair os dígitos de uma string

Dada a string texto = "Eu tenho 2 maçãs e 3 laranjas.", use filter para extrair os dígitos e formar uma lista ['2', '3'].'''

texto = "Eu tenho 2 maçãs e 3 laranjas."

numero = list(filter(lambda n: '2' in n or '3' in n, texto))

print(numero)