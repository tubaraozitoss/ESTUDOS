# Crie um programa que o ano de nascimento de sete pessoas. No final mostre quantas pessoas atingiram ou não a maioridade.
from datetime import date
hoje = date.today()

contador = 0

for c in range (1, 8):
    ano = int(input(f'Ano de nascimento da pessoa {c}: '))
    idade = hoje.year - ano
    if idade >= 18:
        contador += 1

print(f'Entre os participantes, temos {contador} pessoas de maior.')
print(f'Já de menor, temos {7 - contador}.')