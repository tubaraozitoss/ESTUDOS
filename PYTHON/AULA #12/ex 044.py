# Elabore um programa que calcule o valor a ser pago por um produto, considerando as condições:
# À vista no dinheiro/cheque - 10% de desconto
# À vista no cartão - 5% de desconto
# Em até 2x no cartão - preço normal
# 3x ou mais no cartão - 20% de juros

valor = float(input('Valor a ser pago: '))

print('Qual método de pagamento você deseja utilizar?')
print('[ 1 ] À vista no dinheiro/cheque \033[1;32m(10% de desconto)\033[m.')
print('[ 2 ] À vista no cartão \033[1;32m(5% de desconto)\033[m.')
print('[ 3 ] Em até 2x no cartão \033[1;34m(Preço normal)\033[m.')
print('[ 4 ] 3x ou mais no cartão \033[1;31m(20% de juros)\033[m.')

resposta = int(input('Digite o número da opção desejada: '))
juros = valor + (valor * 0.2)

if resposta == 4:
    parcelas = int(input('Quantas parcelas? '))

if resposta == 1:
    print(f'O valor final é de R$ {valor - (valor * 0.1):.2f}.')
elif resposta == 2:
    print(f'O valor final é de R$ {valor - (valor * 0.05):.2f}.')
elif resposta == 3:
    print(f'O valor final é de R$ {valor:.2f}.')
elif resposta == 4:
    if parcelas >= 3:
        print(f'O valor final é de R$ {juros:.2f}.')
        print(f'As parcelas ficam em {parcelas} vezes de {juros / parcelas}')
    else:
        print(f'O valor final é de R$ {valor:.2f}.')  
else:
    print('Digite um valor válido (1, 2, 3 ou 4).')
