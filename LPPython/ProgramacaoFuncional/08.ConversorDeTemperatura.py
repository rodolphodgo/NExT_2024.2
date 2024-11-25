temperaturas_c = [0, 20, 35, 100]

temperaturas_f = list(map(lambda f: f * 9/5 + 32, temperaturas_c))

print(temperaturas_f)