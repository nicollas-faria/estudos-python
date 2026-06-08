# desafio 1

#nome = input('Qual é o seu nome? ')
#print ('Seja bem vindo(a)!', nome + ',', 'Prazer em te conhecer!')

# desafio 2 

#dia = input('Dia ')
#mes = input('Mês ')
#ano = input('Ano ')
#print('Você nasceu no dia', dia, 'de', mes, 'de', ano + '.', 'Está correto?')

# desafio 3 

#numero1 = int(input('Digite seu primeiro numero '))
#numero2 = int(input('Digite seu segundo numero '))
#print ('A soma é', numero1 + numero2)

# Desafio 4
#idade = (10)
#if idade >= 18:
#    print ('você é maior de idade')
#else:
#    print ('você é menor de idade')

# Desafio 5

#idade = int(input('Quantos anos voce tem? '))
#if idade < 18:
#    print ('você é menor de idade')
#elif idade <= 22:
#    print ('Você tem entre 18 e 22 Anos')
#else:
#    print ('você tem mais de 22 Anos')

# Desafio 6

#x = 10
#y = 20

#if x != y:
#    print ('x é diferente de y')
#else:
#    print ('x é igual a y')

# Desafio 7 

dia = int(input('Digite o numero do dia de 1-7: '))

match dia:

    case 1:
        print('Domingo')
    case 2: 
        print('Segunda')
    case 3:
        print('Terça')
    case 4:
        print('Quarta')
    case 5:
        print('Quinta')
    case 6:
        print('Sexta')
    case 7: 
        print('Sabado')
    case _:
        print('Dia invalido')