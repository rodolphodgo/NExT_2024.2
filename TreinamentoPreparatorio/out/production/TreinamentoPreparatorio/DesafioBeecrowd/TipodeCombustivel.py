opcao = []
entrada = 1

while entrada != 4:
 entrada = int(input())
 if entrada == 1:
  opcao.append(entrada)
 elif entrada == 2:
  opcao.append(entrada)
 elif entrada == 3:
  opcao.append(entrada)

print('MUITO OBRIGADO')
print('Alcool:', opcao.count(1))
print('Gasolina:', opcao.count(2))
print('Diesel:', opcao.count(3))