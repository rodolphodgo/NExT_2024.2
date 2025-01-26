'''Use o módulo datetime para implementar uma função que retorne quanto tempo falta para o final deste módulo:

Exiba o tempo seguindo o formato: Tempo restante para o fim do módulo: XX dias e YY horas;'''

from datetime import datetime

agora = datetime.now()

fim = datetime(2024, 12, 2, 22, 0, 0)

restante = fim - agora

print(restante)