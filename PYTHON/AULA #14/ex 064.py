# Leia vários vários números inteiros (só pare de ler quando 999 for indicado) e no fim mostre quantos valores foram ditos e a soma deles.

num = int(input('Digite um valor (digitar 999 encerra o programa): '))


soma = 0
contador = 0

while num != 999:
    soma += num
    contador += 1
    num = int(input('Próximo valor: '))

print(f'Soma: {soma}')
print(f'Total de números informados: {contador}')