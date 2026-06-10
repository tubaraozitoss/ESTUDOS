# Gere um programa que calcule o valor a ser pago por um aluguel de carros.

vd = 80
vkm = 0.75
dias = int(input('Por quantos dias o carro foi alugado?: '))
km = float(input('Por quantos qulômetros foi rodado?: '))
valor = (dias * vd) + (km * vkm)

print(f'O valor final a ser pago é R${valor:.2f}.')
