# Crie um programa que indique se o nome da pessoa possui SILVA em algum lugar.

print('Seu nome tem Silva? ')
nome = input('Qual o seu nome? ')
resposta = nome.upper()
resposta = 'SILVA' in resposta
print(resposta)
