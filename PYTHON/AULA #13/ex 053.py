# Gere um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.

frase = input('Digite uma frase: ').strip().lower()
sem = frase.replace(' ', '')

if frase[::-1] == frase:
    print(f'A frase {sem.upper()} é um palíndromo.')
else:
    print(f'A frase {sem.upper()} não é um palíndromo.')