# Gere um programa que leia 3 números e mostre o menor e o maior.

n1 = int(input('Digite um valor: '))
n2 = int(input('Outro: '))
n3 = int(input('Último: '))

maior = n1
menor = n1

if n2 > maior:
    maior = n2
if n2 < menor:
    menor = n2
if n3 > maior:
    maior = n3
if n3 < menor:
    menor = n3

print(f'O maior número é {maior}.')
print(f'O menor número é {menor}.')

