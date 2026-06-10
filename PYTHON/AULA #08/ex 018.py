# Faça um programa que leia um angulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
import math

angulo = int(input('Qual o ângulo?: '))

rad = math.radians(angulo)

seno = math.sin(rad) # Cateto oposto / Hipotenusa
cosseno = math.cos(rad) # Cateto adjacente / Hipotenusa
tangente = math.tan(rad) # Cateto oposto / Cateto adjacente
print(f' O seno, cosseno e tangente de seu ângulo são, respectivamente {seno:.2f}, {cosseno:.2f}, {tangente:.2f}.')