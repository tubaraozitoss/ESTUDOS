# Faça um programa que leia o comprimeito do cateto oposto e adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa
import math

c1 = int(input('Digite o cateto oposto: '))
c2 = int(input('Agora, o adjascente: '))
hi = math.hypot(c1, c2)

print(f'Resultado = {(hi)}')
