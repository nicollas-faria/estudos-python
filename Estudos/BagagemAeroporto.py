total_excesso_peso = 0
valor_total = 0

# Configurações da Econômica
valor_economica = 80
economica = 23
taxa_economica = 130

# Configurações da Executiva
valor_executiva = 120
executiva = 32
taxa_executiva = 160

# Configurações da Primeira Classe
valor_primeira = 180
primeira = 40
taxa_primeira = 200

print('Seja bem-vindo(a) à companhia aerea planout!')
print(f'Planos disponíveis para bagagens:\nEconomica({economica}kg): R$ {valor_economica:.2f}\nExecutiva({executiva}kg): R$ {valor_executiva:.2f}\nPrimeira({primeira}kg): R$ {valor_primeira:.2f}')

while True:
    resposta = input('\nDigite seu plano desejado e o peso de sua mala (ou "fim" para encerrar a compra.): ').lower().split()

    if resposta[0] == 'fim':
        break
    
    if len(resposta) < 2:
        print('Erro! você precisa digitar seu plano e o peso de sua mala')
        continue
    
    plano = (resposta[0])
    peso = float(resposta[1])

    if plano == 'economica':
        valor_total += valor_economica
        if peso > 23:
            print('Plano não compativel com o peso da carga! Escolha um plano compativel ou sera sujeito a uma taxa de excesso de peso.')
            total_excesso_peso += abs(peso - economica)
            valor_total += taxa_economica
    elif plano == 'executiva':
        valor_total += valor_executiva
        if peso > 32:
            print('Plano não compativel com o peso da carga! Escolha um plano compativel ou sera sujeito a uma taxa de excesso de peso.')
            total_excesso_peso += abs(peso - executiva)
            valor_total += taxa_executiva
    elif plano == 'primeira':
        valor_total += valor_primeira
        if peso > 40:
            print('Plano não compativel com o peso da carga! Você sera sujeito a uma taxa de excesso de peso.')
            total_excesso_peso += abs(peso - primeira)
            valor_total += taxa_primeira
    else:
        print('Plano invalido! Escolha um plano entre "economica", "executiva" ou "primeira"!')
    
print('\nVoo finalizado!')
print(f'Peso total excedido: {total_excesso_peso:.2f}kg')
print(f'Valor total de compra: R$ {valor_total:.2f}')
