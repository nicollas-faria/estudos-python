NUMBER = int(input('Digite a quantia de funcionarios: '))
horas_trabalhadas = int(input('Digite as horas trabalhadas: '))
valor_phora = float(input('Digite o valor que recebe por horas trabalhadas: '))

SALARY = round(horas_trabalhadas * valor_phora, 2)

print(f'NUMBER = {NUMBER}')
print(f'SALARY = U$ {SALARY:.2f}')
