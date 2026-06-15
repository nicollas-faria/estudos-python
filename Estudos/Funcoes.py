idade = 25

def minha_funcao():
    nome='nicollas'
    print(f'Olá, {nome}! Essa é a minha função. Sua idade é {idade} anos.')

def somar(n1, n2):
    resultado = n1 + n2 
    return resultado

def saudacao(nome):
    print(f'Olá, {nome}! muito prazer em te conhecer.')

def verificar_par(numero):
    if numero % 2 == 0:
        return True 
    else:
        return False

def somar_lista(*numeros):
    resultado = 0
    for numero in numeros:
        resultado += numero
    return resultado

def calcular_media(*numeros):
    qtd = len(numeros)
    soma = 0
    for numero in numeros:
        soma += numero
    media = soma / qtd
    return media

def informacoes_pessoais(**info):
    for chave, valor in info.items():
        print(f'{chave}: {valor}')

# exercicios:
   
def numero_regressivo(numero):
    for numero in range(numero, -1, -1):
        print(numero)

def lista_numero_maior(*numeros):
    numero = []
    for i in range(len(numeros)):
        numero.append(numeros[i])
    return max(numero)

# correção exercicios:

# contagem regressiva:

def contagem_regressiva(numero):
    while True:
        print(numero)
        numero -= 1
        if numero <= 0:
            break

# segunda opção para contagem regressiva:

def contagem_regressiva(numero):
    for i in range(numero, -1, -1):
        print(i)


# maior numero da lista:

def maior_numero(lista_de_numeros):
    maior_numero = lista_de_numeros[0]
    for numero in lista_de_numeros:
        if numero > maior_numero:
            maior_numero = numero
    return maior_numero

# ou utilizar a função max() diretamente:

def maior_numero(lista_de_numeros):
    maior_numero = max(lista_de_numeros)
    return maior_numero


lista = [3, 7, 2, 9, 5]
maior_numero_da_lista = maior_numero(lista)
print(f'O maior número da lista é: {maior_numero_da_lista}')
