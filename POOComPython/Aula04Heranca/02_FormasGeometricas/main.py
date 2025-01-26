from retangulo import Retangulo
from circulo import Circulo

forma1 = Retangulo(10, 20)
print(forma1.largura)
print(forma1.altura)
print(forma1.calcular_area())
print(forma1.calcular_perimetro())

forma2 = Circulo(10)
print(forma2.raio)
print(forma2.calcular_area())
print(forma2.calcular_perimetro())