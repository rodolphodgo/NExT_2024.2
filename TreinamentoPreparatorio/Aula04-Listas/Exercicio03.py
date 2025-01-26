"""Considerando que as seguintes listas estão relacionadas pelo modelo e consumo de combustível (km/L), exiba:

modelos = ['Variant', 'Brasília', 'Chevette', 'Opala', 'Belina', 'Maverick']
consumos = [12.0, 9.3, 10.3, 7.3, 9.3, 9.1]

a) O modelo que consome mais combustível;
b) O modelo que consome menos combustível;
c) A média dos consumos apresentados."""

modelos = ['Variant', 'Brasília', 'Chevette', 'Opala', 'Belina', 'Maverick']
consumos = [12.0, 9.3, 10.3, 7.3, 9.3, 9.1]

maisConsome = consumos.index(max(consumos))
menosConsome = consumos.index(min(consumos))
media = sum(consumos)/4

print('O modelo que consome mais combustível', modelos[maisConsome])
print('O modelo que consome menos combustível', modelos[menosConsome])
print('A média dos consumos apresentados', media)