# Crie um programa que leia uma frase e mostre quantas vezes aparece a letra A, em que posição a letra A aparece na primeira e na última vez.

frase = input('Digite uma frase: ').upper()

contagem = frase.count('A')
primeiro_a = frase.find('A')
ultimo_a = frase.rfind('A')

print(f'Quantidade de letras A: {contagem}')
print(f'Primeiro A: {primeiro_a}')
print(f'Último A: {ultimo_a}')
