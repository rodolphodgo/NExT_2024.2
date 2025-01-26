'''Converter temperaturas

Dada a lista de temperaturas em Celsius temperaturas_c = [0, 20, 35, 100], use map para convertê-las em Fahrenheit.

 Fórmula: F = C * 9/5 + 32'''

temperaturas_c = [0, 20, 35, 100]

temperaturas_f = list(map(lambda f: f * 9/5 + 32, temperaturas_c))

print(temperaturas_f)