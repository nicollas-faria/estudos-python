import math

A = float(input('Digite o lado A de seu triangulo: '))
B = float(input('Digite o lado B de seu triangulo: '))

hypotenuse = math.sqrt(pow(A , 2) + pow(B, 2))

print(f'A hypotenusa de seu triangulo é: {round(hypotenuse, 2)}')