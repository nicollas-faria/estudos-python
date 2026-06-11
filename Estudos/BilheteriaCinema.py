total_arrecadado = 0
meia = 5.00
inteira = 10.00

while True:
    resposta = input('Digite o filme, tipo de entrada e a quantia de ingressos para o tipo de ingresso (ou "fim" para encerrar): ').split()

    if resposta[0] == 'fim':
        break

    filme = (resposta[0])
    tipo_ingresso = (resposta[1])
    quantia = int(resposta[2])
    
    if tipo_ingresso == 'meia':
        total_arrecadado += quantia * meia
    elif tipo_ingresso == 'inteira':
        total_arrecadado += quantia * inteira
    else:
        print("Tipo de ingresso Invalido! Use 'meia' ou 'inteira'.")

print(f'Vendas Encerradas!\nTotal arrecadado pelo cinema: R$ {total_arrecadado:.2f}')