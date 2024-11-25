numero = int(input())

def positivo_negativo():
    if numero > 0:
        return True
    elif numero < 0:
        return False
    else:
        return "Nulo"

print(positivo_negativo())