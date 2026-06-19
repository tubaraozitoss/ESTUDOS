# Leia varios numeros inteiros. Mostre a média, e o maior e o menor valores digitados. O programa pergunta ao usuário se deseja continuar ou não.

num = int(input('Digite um valor: '))

soma = num
contador = 1
maior = num
menor = num

continuar = input('Deseja continuar? S/N: ').upper()

while continuar == 'S':
    
    num = int(input('Digite um valor: '))

    soma += num
    contador += 1

    if num > maior:
        maior = num
    if num < menor:
        menor = num

    continuar = input('Deseja continuar? S/N: ').upper()

media = soma / contador

print(f'A média entre os {contador} valores digitados é {media:.2f}.')
print(f'Maior valor: {maior}')
print(f'Menor valor: {menor}')
