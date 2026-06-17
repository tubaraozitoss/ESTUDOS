# Escreva um programa que leia um número inteiro e peça que o usuário escolha qual será a base de conversão:
# 1 - para binário
# 2 - para octal
# 3 - para hexadecimal

num = int(input('Digite um número: '))
print('Escolha \033[1muma\033[m opção:')
print('[1] \033[1;36mBinário\033[m')
print('[2] \033[1;36mOctal\033[m')
print('[3] \033[1;36mHexadecimal\033[m')

escolha = int(input('Digite: '))

if escolha == 1:
    print(f'O seu número em valor \033[1;36mbinário\033[m é \033[1;32m{bin(num)[2:]}\033[m.')
elif escolha == 2:
     print(f'O seu número em valor \033[1;36moctal\033[m é \033[1;32m{oct(num)[2:]}\033[m.')
elif escolha == 3:
      print(f'O seu número em valor \033[1;36mhexadecimal\033[m é \033[1;32m{hex(num)[2:]}\033[m.')
else:
     print('Digite um valor válido (as opções são 1, 2 ou 3.)')