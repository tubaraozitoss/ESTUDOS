# Faça um programa que leia o ano de nascimento de um jovem e informe: se ele ainda vai se alistar, se é hora de se alistar ou se já passou o tempo do alistamento.
from datetime import date
hoje = date.today()
ano = int(input('Em que ano você nasceu? '))
idade = hoje.year - ano

if idade > 18:
    print(f'O seu tempo de alistamento já está ultrapassado há {idade - 18} anos. Regularize a situação com urgência.')
elif idade < 18:
    print(f'Falta(m) {18 - idade} ano(s) para que você possa se alistar.')
else:
    print('Você deve se alistar \033[1mjá!')
    print('\033[1;32mBoa sorte!\033[m')