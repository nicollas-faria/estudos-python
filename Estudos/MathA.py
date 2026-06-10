import math

radius = float(input('Digite o raio para o circulo: '))

area = math.pi * radius ** 2 # or pow(radius, 2) that's right

print(f'A area de seu circulo é: {round(area, 2)}cm²')