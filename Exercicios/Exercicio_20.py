valor = float(input('Digite o valor do produto: '))
desconto = int(input('Digite o desconto(%) do produto: '))

valor_do_desconto = valor * (desconto / 100)
preco_final = round(valor - valor_do_desconto, 2)

print(f'O produto que era R$:{valor:.2f} está saindo por R$:{preco_final:.2f} com {desconto}% de desconto.')