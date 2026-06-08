nome = input('Qual é o seu nome? ')
nota = float(input('Qual é a sua nota? '))

if nota >= 7:
    print(f'Parabens {nome}! Você passou de ano.')
elif nota >= 5:
    print(f'{nome}, você está de recuperação.')
else:
    print(f'Lamento {nome}. Você está reprovado.')
