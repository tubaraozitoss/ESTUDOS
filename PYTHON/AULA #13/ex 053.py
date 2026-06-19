# Gere um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.

frase = input('Digite uma frase: ').strip().lower()
sem = frase.replace(' ', '')

if sem[::-1] == sem:
    print(f'A frase {frase.upper()} é um palíndromo.')
else:
    print(f'A frase {frase.upper()} não é um palíndromo.')