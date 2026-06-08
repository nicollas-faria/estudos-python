nome = input('Qual é o seu nome? ')
peso = float(input('Quantos você pesa(kg)? '))
altura = float(input('Qual a sua altura(m)? '))

calc = peso / (altura ** 2)
calcr = round(calc, 2)

if calc < 18.5:
    print(f'{nome}, seu IMC é {calcr} - Abaixo do peso')
elif calc <= 24.9:
    print(f'{nome}, seu IMC é {calcr} - Peso normal.')  
elif calc < 29.9:
    print(f'{nome}, seu IMC é {calcr} - Sobrepeso.')
else:
    print(f'{nome}, seu IMC é {calcr} - Obesidade.')