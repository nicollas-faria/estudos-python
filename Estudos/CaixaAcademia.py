faturamento_total = 0
musculacao = 90.00
treino_funcional = 120.00
jiu_jitsu = 150.00

print('Planos disponíveis:\nmusculacao\ntreino_funcional\njiu_jitsu')
    # Aplicamos o .lower() aqui para evitar problemas com maiúsculas
while True:
    resposta = input('Digite o plano escolhido(ex:musculacao, treino-funcional ou jiu_jitsu) e Quantia de meses assinado: ').lower().split()

    if resposta[0] == 'sair':
        break
    # Aplicamos o len() aqui para garantir que a lista tem o plano e o mês
    if len(resposta) < 2:
        print('Erro! Você precisa digitar o plano E a quantia de meses (ex: musculacao 3)')
        continue # Volta para o início do while sem quebrar o programa

    plano = (resposta[0])
    mes = int(resposta[1])

    if plano == 'musculacao':
        faturamento_total += mes * musculacao
    elif plano == 'treino_funcional':
        faturamento_total += mes * treino_funcional
    elif plano == 'jiu_jitsu':
        faturamento_total += mes * jiu_jitsu
    else:
        print("Plano invalido! Use 'musculacao', 'treino_funcional' ou 'jiu_jitsu'!")

    
print(f'Vendas encerradas\nValor total faturado: R$ {faturamento_total}')

