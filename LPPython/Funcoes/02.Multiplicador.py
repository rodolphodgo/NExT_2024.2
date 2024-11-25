valor = list(input().split(" "))
valor_inteiro = [int(x) for x in valor]
multiplicador = int(input())

def multiplicados():
    for x in valor_inteiro:
        x = x * multiplicador
        print(x)

multiplicados()