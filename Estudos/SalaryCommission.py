
nome = input('Digite seu nome: ')
salario_fixo = float(input('Informe seu salario: '))
vendas_totais = float(input('Quantos produtos voce vendeu no mes?(R$) '))

comissao = vendas_totais * (15 / 100)
salario = salario_fixo + comissao

print(f'TOTAL = R$ {salario:.2f}')
