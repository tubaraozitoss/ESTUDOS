# Gere um programa que leia a velocidade de um carro. Se ultrapassar 80km/h, multado. A multa vai custar R$7 por cada KM acima do limite

kmh = float(input("Scanner, qual a velocidade do carro que acabou de passar aqui? "))

if kmh <= 80:
    print('Você escapou da multa.')
else:
    multa = (kmh - 80) * 7
    print(f'Você está sendo multado. O valor de sua multa é R$ {multa:.2f}.')