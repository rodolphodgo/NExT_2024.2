'''Implemente um programa que leia o arquivo da questão anterior e gere um novo arquivo apenas com os animais terrestres.'''

terrestres = []

with open("Aula05/exercicios/animais.txt", encoding="utf-8") as arq:
    for linha in arq:
        animal, habitat = linha.strip().split(",")
        if habitat == "terrestre":
            terrestres.append(animal)

with open("Aula05/exercicios/animais_terrestres.txt", "w", encoding="utf-8") as arq:
    for animal in terrestres:
        arq.write(f"{animal}\n")

with open("Aula05/exercicios/animais_terrestres.txt", encoding="utf-8") as arq:
    print(arq.read())