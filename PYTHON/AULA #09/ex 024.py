# Crie um programa que indique se o nome da cidade se inicia com SANTO.

print('A sua cidade começa com SANTO?')
cidade = input('Qual o nome da sua cidade? ')
resposta = cidade.upper().startswith('SANTO')


print(resposta)