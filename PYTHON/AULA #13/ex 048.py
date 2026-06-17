# Faça um programa que calque a soma entre todos os números ímpares que são múltiplos de 3 e que se encontram no intervalo de 1 até 500.
soma = 0
for c in range (0, 500, 3):
    if c % 2 == 1:
        soma = soma + c
print(soma)
   
