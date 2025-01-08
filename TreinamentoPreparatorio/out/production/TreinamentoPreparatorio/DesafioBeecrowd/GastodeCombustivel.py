tempo = float(input())
velocidade = float(input())

kml = 12
distancia = tempo * velocidade
litros = distancia / kml

print(f'{litros:.3f}')