# Gere um programa que leia duas notas de um aluno: 
# Se abaixo de 5: reprovado.
# Se entre 5.0 e 6.9: recuperação.
# Se acima de 7: aprovado.

titulo = ' SISTEMA ENSINO - MÉDIA '

print('=-' * 15)
print(f'\033[1m{titulo.center(30)}\033[m')
print('=-' * 15)

n1 = float(input('Nota 1: '))
n2 = float(input('Nota 2: '))
n3 = float(input('Nota 3: '))
media = (n1 + n2 + n3) / 3

if media < 5:
    print(f'Sua média é {media}.\nVocê está \033[1;31mREPROVADO\033[m.')
elif media >= 7:
    print(f'Sua média é {media}.\nVocê está \033[1;32mAPROVADO\033[m!')
else:
    print(f'Sua média é {media}.\nVocê está em \033[1;30mRECUPERAÇÃO\033[m.')

