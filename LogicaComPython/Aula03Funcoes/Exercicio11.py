"""Um palíndromo é uma palavra que se soletra da mesma forma nos dois sentidos, como “osso” e “reviver”. Escreva um função que dado uma plavra verifique se ela é palindro.

"""

def palidromo(palavra):
    if palavra == palavra[::-1]:
        print("É um palidromo")
    else:
        print("Não é um palidromo")

palidromo("osso")
palidromo("reviver")
palidromo("palavra")