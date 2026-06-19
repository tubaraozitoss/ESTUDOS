# Faça um programa que leia o sexo de uma pessoa que só aceite M ou F. Caso esteja errado, peça a digitação novamente até ter um valor correto.

sexo = input('Qual o seu sexo? Responda com M ou F: ').upper()

while sexo != 'M' and sexo != 'F':
    print('Digite um valor válido (M ou F)')
    sexo = input('Qual o seu sexo? Responda com M ou F: ').upper()
    
print('Valor aceito.')