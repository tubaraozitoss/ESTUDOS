# Gere um programa que demonstre diversas informações sobre uma variável.

algo = input('Digite algo: ')
print(f'O tipo primitivo é {type(algo)}')
print(f'É um número? {algo.isnumeric()}')
print(f'É letra? {algo.isalpha()}')
print(f'Está em maiúsculo? {algo.isupper()}')
print(f'Está em minúsculo? {algo.islower()}')