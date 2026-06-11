total_geral = 0

while True:
    linha = input('Digite o produto (ou "fim 0 0" para encerrar): ').split()
    
    if linha[0] == 'fim':
        break
    
    produto = (linha[0])
    quantia = int(linha[1])
    preco = float(linha[2])

    total_geral += preco * quantia

print('Compra encerrada!')
print(f'Total da compra: R$ {total_geral:.2f}')