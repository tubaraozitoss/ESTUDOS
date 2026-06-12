# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.

salario = float(input('Qual o seu salário?: '))
aumento1 = salario * 0.10
aumento2 = salario * 0.15

if salario > 1250:
    print(f'O seu salário está recebendo um aumento de 10%, indo de {salario} para {salario + aumento1}.')
else:
    print(f'O seu salário está recebendo um aumento de 15%, indo de {salario} para {salario + aumento2}.')
