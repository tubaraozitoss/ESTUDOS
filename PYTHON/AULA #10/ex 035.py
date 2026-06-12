# Gere um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo

n1 = int(input('Valor da primeira reta: '))
n2 = int(input('Valor da segunda reta: '))
n3 = int(input('Valor da terceira reta: '))

if n1 + n2 > n3 and n1 + n3 > n2 and n2 + n3 > n1:
    print('As retas podem formar um triângulo!')
else:
    print('As retas não podem formar um triângulo.')