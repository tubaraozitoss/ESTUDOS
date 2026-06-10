# Faça um algoritmo que conceda 15% de aumento para um funcionário.

salario_base = float(input('Qual o seu salário atual? '))
aumento = salario_base * 0.15
salario_final = salario_base + aumento

print(f'Por merecimento (parabéns!!!), Você acaba de receber R$ {aumento:.2f} de aumento! Com isso, passa a receber R$ {salario_final:.2f}.')
