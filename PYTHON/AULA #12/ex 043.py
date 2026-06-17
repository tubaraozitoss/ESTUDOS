# Desenvolva um programa que calcule o IMC do usuário e mostre seu status
# Abaixo de 18.5 - abaixo do peso
# Entre 18.5 e 25 - peso ideal
# 25 até 30 - sobrepeso
# 30 até 40 - obesidade
# acima de 40 - obesidade mórbida

peso = float(input('Digite o seu peso: '))
altura = float(input('Digite sua altura: '))
imc = peso / (altura ** 2)

if imc < 18.5:
    print(f'Seu IMC é {imc}. Você está abaixo do peso.')
elif imc <= 25:
    print(f'Seu IMC é {imc}. Você está em um peso ideal.')
elif imc <= 30:
    print(f'Seu IMC é {imc}. Você está acima do peso.')
elif imc <= 40:
    print(f'Seu IMC é {imc}. Você está em estado de obesidade.')
else:
    print(f'Seu IMC é {imc}. Você está em obesidade mórbida.')


