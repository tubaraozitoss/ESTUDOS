# Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lido.

for c in range (1, 6):
    peso = float(input(f'Peso {c}: '))
    
    if c == 1:
        maior = peso
        menor = peso
    if peso > maior:
        maior = peso
    if peso < menor:
        menor = peso

print(f'Maior peso: {maior}.')
print(f'Menor peso: {menor}.')
