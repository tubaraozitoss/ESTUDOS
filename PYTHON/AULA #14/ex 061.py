# Refaça o ex 051 usando while.

termo = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Agora, a razão: '))
contador = 1

while contador <= 10:
    print(f'{termo}')
    termo = termo + razao
    contador += 1