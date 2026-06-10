# Escreva um programa que leia o valor em metros e o exiba convertido em centímetros e milímetros.

metros = float(input('Quantos metros você tem? '))
cm = metros * 100
mm = metros * 1000

print(f'Além de {metros}m, você tem {cm}cm e {mm}mm. Feliz?')
