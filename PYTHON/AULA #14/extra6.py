# Pergunte o valor da compra e o dinheiro entregue. Enquanto o valor entregue for menor que o da compra, peça outro valor.

compra = float(input('Valor total da sua compra: '))
entregue = float(input('Insira as cédulas para pagar: '))

while entregue < compra:
    
    adicional = float(input('Valor insuficiente, insira mais dinheiro: '))

    entregue += adicional

print(f'Compra concluída! Troco {entregue - compra:.2f}')