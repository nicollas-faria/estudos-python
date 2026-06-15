def maior_numero(*numeros):
    maior_numero = numeros[0]

    for numero in numeros:
        if numero > maior_numero:
            maior_numero = numero
    return maior_numero

def menor_numero(*numeros):
    menor_numero = numeros[0]

    for numero in numeros:
        if numero < menor_numero:
            menor_numero = numero
    return menor_numero

print(menor_numero(5, 3, 8, 1, 9))
print(menor_numero(-10, -5, -20))
print(menor_numero(7))
print(menor_numero(4, 4, 4, 4))
