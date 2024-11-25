lista = ["Bruna", "Jurandir", "Ivete", "Cláudia", "Rafael"]

busca = input()

def buscador():
    if busca in lista:
        return True
    else:
        return False

print(buscador())