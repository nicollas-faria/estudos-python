item = input('Qual produto você quer comprar? ')
price = float(input('Qual é o valor do produto: '))
quantity = int(input('Qual é a quantia de produtos que você deseja? '))

total = price * quantity

print(f'Você comprou {quantity}x {item}/s')
print(f'O total é: R$:{total:.2f}')
