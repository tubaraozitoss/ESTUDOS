# Faça um programa que leia um número inteiro e diga se ele é ou não um primo.

n1 = int(input('Digite um valor: '))

contador = 0

for c in range (1, n1 + 1):
    if n1 % c == 0:
        contador += 1

if contador == 2:
    print(f'O número {n1} é primo.')
else:
    print(f'O número {n1} não é primo.')
