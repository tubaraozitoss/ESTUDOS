# Leia o nome e idade de 5 peessoas, mostrando ao fim a pessoa mais velha e a mais nova

mais_velho = ''
mais_novo = ''
velho = 0
novo = 0

for c in range (1,6):
    nome = input(f'Nome da pessoa {c}: ')
    idade = int(input(f'Idade da pessoa {c}: '))

    if c == 1:
        velho = idade
        novo = idade
        mais_velho = nome
        mais_novo = nome
    if idade > velho:
        velho = idade
        mais_velho = nome
    if idade < novo:
        novo = idade
        mais_novo = nome

print(f'{mais_novo} é a pessoa mais nova, com {novo} ano(s).')
print(f'{mais_velho} é a pessoa mais velha, com {velho} anos.')