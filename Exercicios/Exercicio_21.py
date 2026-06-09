salario = float(input('Digite o seu salario mensal: '))
aumento = int(input('Digite o aumento de seu salario em %: '))

aumento_no_salario = salario * (aumento / 100)
salario_final = round(salario + aumento_no_salario, 2)

print(f'Seu salario atual de R$:{salario:.2f} teve um aumento de {aumento}%. Resultando um novo salário de R$:{salario_final:.2f}')