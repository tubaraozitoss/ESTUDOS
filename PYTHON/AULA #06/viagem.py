# Gere um programa que auxilie o usuário a saber qual será o gasto de combustível e o valor gasto durante uma viagem.

nome = input('Qual o seu nome? ')
km = float(input('Qual a distância da viagem? '))
kml = float(input('Qual o consumo do seu carro (km/l)? '))
gas = float(input('QUal o valor do litro da gasolina na sua regiâo? '))
litros = km / kml
reais = litros * gas


print('=== RESUMO DA VIAGEM ===')
print()
print(f'Motorista: {nome}')
print()
print(f'Distância: {km} km')
print(f'Consumo do carro: {kml} km/L')
print()
print(f'Combustível necessário: {litros:.1f}  L')
print(f'Gasto estimado: R${reais:.2f}.')
print()
print('=' * 25)
print('BOA VIAGEM!')
print('=' * 25)

# Este código foi criado separadamente, sem orientação do professor, para que aprimore meus conhecimentos.
