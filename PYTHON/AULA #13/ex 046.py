# Faça um programa que mostre uma contagem regressiva para o estouro de fogos de artifício indo de 0 até 10 com 1s de pausa entre eles.
import time
for c in range (11, -1, - 1):
    print(c)
    time.sleep(1)
print('🎆 FOGOS! 🎆')

