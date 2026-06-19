# Leia 5 notas e mostre a média das notas, a maior e a menor.

maior = 0
menor = 0
soma = 0

for c in range (1,6):
    notas = float(input(f'Nota {c}: '))
    soma += notas

    if c == 1:
        maior = notas
        menor = notas
    if notas > maior:
        maior = notas
    if notas < menor:
        menor = notas

media = soma / 5

if media < 4:
    print(f'Média entre as notas: {media}. \033[1;31mREPROVADO\033[m.')
elif media < 7:
    print(f'Média entre as notas: {media}. \033[1;35mRECUPERAÇÃO\033[m.')
else:
    print(f'Média entre as notas: {media}. \033[1;32mAPROVADO\033[m.')

print(f'Maior nota: \033[1m{maior}\033[m')
print(f'Menor nota: \033[1m{menor}\033[m')

