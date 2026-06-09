nota = int(input('Qual é a sua nota em português? '))
nota1 = int(input('QUal é a sua nota em matematica? '))

# da para tirar a media tudo de uma vez tambem.

soma = nota + nota1
#media = soma / 2
media = (nota + nota1) / 2


#os dois metodos funcionam, porem prefiro o primeiro..

print(f'A sua media entre português e matemática é: {media:.1f}')

#print(f'A sua media entre português e matemática é: {(nota + nota1) / 2}')