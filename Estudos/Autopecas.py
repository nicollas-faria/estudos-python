linha1 = input().split()
peca1 = int(linha1[0])
numero_pecas1 = int(linha1[1])
valor_unitario1 = float(linha1[2])

valor_peca1 = numero_pecas1 * valor_unitario1

linha2 = input().split()
peca2 = int(linha2[0])
numero_pecas2 = int(linha2[1])
valor_unitario2 = float(linha2[2])

valor_peca2 = numero_pecas2 * valor_unitario2

VALOR_TOTAL = valor_peca1 + valor_peca2

print(f'VALOR A PAGAR: R$ {VALOR_TOTAL:.2f}')
