'''Crie um arquivo que contenha, em cada linha, o nome de um animal e seu habitat, separado por vírgula, como no exemplo:
baleira,aquático
tucano,aéreo
tubarão,aquático
coelho,terrestre
leão,terrestre
golfinho,aquático
camaleão,arbóreo
cobra,terrestre
urso-polar,gelado
coruja,aéreo
canguru,terrestre
tartaruga,aquático'''

with open("Aula05/exercicios/animais.txt", "w", encoding="utf-8") as arq:
    for _ in range(3):
        animal = input("Informe o animal: ")
        habitat = input("Informa seu habitat: ")
        arq.write(f"{animal},{habitat}\n")

with open("Aula05/exercicios/animais.txt", encoding="utf-8") as arq:
    print(arq.read())