def entrada():
    valor = list(input().split(" "))
    valor_inteiro = [int(x) for x in valor]
    valor_inteiro.reverse()
    print(valor_inteiro)

entrada()