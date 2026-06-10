#  Crie um programa que leia o nome completo de alguém e mostre: O nome com letras maiúsculas, minúsculas, quantas letras tem ao todo e no primeiro nome.

nome = str(input('Qual é o seu nome COMPLETO?: ')).strip()

print(f'Seu nome em letras maiúsculas é {nome.upper()}.')
print(f'Seu nome em letras minúsculas é {nome.lower()}.')

print(f' Além disso, o seu nome possui {len(nome) - nome.count(' ')} letras.')
print(f'Seu primeiro nome é {nome.split()[0]} e possui {len (nome.split()[0])} letras.') 
