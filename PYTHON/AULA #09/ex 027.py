# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

nome = input('Qual o seu nome?: ').upper().strip()

nome_separado = nome.split()
primeiro = nome_separado[0]
último = nome_separado[-1]

print(f'Primeiro nome: {primeiro}, último nome: {último}')