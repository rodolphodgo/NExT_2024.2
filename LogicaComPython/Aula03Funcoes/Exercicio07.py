"""Faça um programa para imprimir:

1
2   2
3   3   3
.....
n   n   n   n   n   n  ... n"""

def piramide(n):
    for x in range(1, n + 1):
        for y in range(x):
            print(x, end=" ")
        print()

piramide(5)