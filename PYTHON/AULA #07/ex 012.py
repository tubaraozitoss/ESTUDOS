# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

inicio = float(input('Qual o valor do produto? '))
desconto = inicio * 0.05
final = inicio - desconto

print(f'Com nosso programa de fidelidade, você acaba de receber 5% de desconto no produto! Com menos R$ {desconto}, ', end=' ')
print(f'Por isso, você passa a pagar R$ {final}.')