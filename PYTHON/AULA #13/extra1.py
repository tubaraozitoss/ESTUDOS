# Leia 8 números e no final mostre a quantidade de pares e ímpares.

par = 0
impar = 0

for c in range (1,9):
    num = int(input(f'{c} - Digite um número: '))
    if num % 2 == 0:
        par += 1
    else:
        impar += 1

print(f'Quantidade de números \033[1mímpares\033[m digitados: {impar}')
print(f'Quantidade de números \033[1mpares\033[m digitados: {par}')
