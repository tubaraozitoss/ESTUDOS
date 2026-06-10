#  Crie um programa que leia o nome completo de alguém e mostre: O nome com letras maiúsculas, minúsculas, quantas letras tem ao todo e no primeiro nome.

nome = input('Qual é o seu nome COMPLETO?: ')

print(nome.upper())
print(nome.lower())

nome2 = nome.replace(' ', '')
print(len(nome2))
print(len(nome.split()[0]))
