"""Faça um programa para imprimir:

1
1   2
1   2   3
.....
1   2   3   ...  n"""

def piramide(n):
    for x in range(1, n + 1):
        for y in range(1, x + 1):
            print(y, end=" ")
        print()

piramide(5)