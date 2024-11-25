idades = []
entrada = 0

while entrada >= 0:
  entrada = float(input())
  if entrada >= 0 :
    idades.append(entrada)

print(f'{sum(idades)/len(idades):.2f}')