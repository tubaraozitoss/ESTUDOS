# Faça um programa que leia um número qualquer e mostre o seu fatorial.

n1 = int(input('Digite um valor: '))
resultado = 1

while n1 > 1:
    resultado = resultado * n1
    n1 -= 1

print(resultado)
