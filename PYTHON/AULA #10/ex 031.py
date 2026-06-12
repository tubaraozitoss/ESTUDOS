# Gere um programa que pergunte a distância de uma viagem em KM. Para precificar, considere R$0,50 por KM para viagens até 200km, e R$0,45 para viagens maiores

km = float(input('Qual a distância da viagem que você vai realizar?: '))

if km <= 200:
    print(f'Você pagará nessa viagem o valor de R$ {km * 0.50}')
else:
    print(f'Você pagará nessa viagem o valor de R$ {km * 0.45}')