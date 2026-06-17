# Escreva um programa para aprovar um emprestimo bancário para compra de uma casa. O programa deve perguntar: valor da casa, salario e em quantos anos o usuário vai pagar. Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.

valor = float(input('Valor da casa desejada: R$ '))
salario = float(input('Salário atual: R$ '))
anos = int(input('Durante quantos anos serão pagas as prestações?: ')) * 12
prestacao = valor / anos
print(f'Valor total de cada prestação: R$ {prestacao:.2f}.')

if prestacao > salario * 0.3:
    print('Infelizmente, o valor da prestação excede 30% de seu salário, impossibilitando a compra da casa.')
else:
    print('Parabéns! Você está apto para comprar uma de nossas moradias.')
