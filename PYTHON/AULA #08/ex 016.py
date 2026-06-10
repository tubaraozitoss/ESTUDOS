# Crie um programa que leia um número real e mostre na tela a porção inteira.

from math import trunc, ceil, floor

n1 = float(input('Digite um número: '))

print(f'Arrendondando para cima, o seu número fica {ceil(n1)}. Para baixo, {floor(n1)}.')
print(f'Porção inteira: {trunc(n1)}')
