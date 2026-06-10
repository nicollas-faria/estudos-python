# if = execute o codigo IF(se) alguma condição for verdadeira.
# else = else(se não) faça tal funcão

age = int(input('digite sua idade: '))

if age >= 100:
    print('Você é muito velho para criar uma conta.')
elif age >= 18:
    print('Você pode criar uma conta!')
elif age < 0:
    print('Você ainda nem nasceu!')
else:
    print('Você precisar ter +18 para criar uma conta.')