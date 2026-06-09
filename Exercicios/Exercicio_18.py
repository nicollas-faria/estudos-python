reais = float(input('Converta reais para dolar: '))

dolar = reais / 5.20
dolar_arredondado = round(dolar, 2)

print(f'com R$:{reais:.2f} Você pode comprar U$:{dolar_arredondado:.2f} dólares, que tristeza :(')