numeros = input().split(' ')

n1 = int(numeros[0])
n2 = int(numeros[1])

if n1 % n2 == 0:
  print('Sao Multiplos')
elif n2 % n1 == 0:
  print('Sao Multiplos')
else:
  print('Nao sao Multiplos')