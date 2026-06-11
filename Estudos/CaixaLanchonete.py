linha1 = input('Digite o nome do produto, quantia e preço unitário: ').split()
item1 = (linha1[0])
quantia1 = int(linha1[1])
preco_unitario1 = float(linha1[2])

valor1 = quantia1 * preco_unitario1

linha2 = input('Digite o nome do produto, quantia e preço unitário:').split()
item2 = (linha2[0])
quantia2 = int(linha2[1])
preco_unitario2 = float(linha2[2])

valor2 = quantia2 * preco_unitario2

valor_total = valor1 + valor2

print(f'Conta da lanchonete: R$ {valor_total:.2f}')