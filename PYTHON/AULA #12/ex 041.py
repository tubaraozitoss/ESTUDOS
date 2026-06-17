# Gere um programa que leia o ano de nascimento de um atleta e mostre sua categoria:
# Até 9 anos: mirim
# Até 14 anos: infantil
# Até 19 anos: junior
# Até 20 anos: sênior
# Acima: master

idade = int(input('Qual a idade do atleta? '))

if idade <= 9:
    print(f'O atleta tem \033[1m{idade}\033[m anos, classificando-se como \033[1;33mMIRIM\033[m.')
elif idade <= 14:
    print(f'O atleta tem \033[1m{idade}\033[m anos, classificando-se como \033[1;33mINFANTIL\033[m.')
elif idade <= 19:
    print(f'O atleta tem \033[1m{idade}\033[m anos, classificando-se como \033[1;33mJUNIOR\033[m.')
elif idade == 20:
    print(f'O atleta tem \033[1m{idade}\033[m anos, classificando-se como \033[1;33mSENIOR\033[m.')
else:
    print(f'O atleta tem \033[1m{idade}\033[m anos, classificando-se como \033[1;33mMASTER\033[m.')
