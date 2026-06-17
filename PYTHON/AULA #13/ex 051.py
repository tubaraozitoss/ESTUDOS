# Gere um programa que leia o termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa PA.

termo = int(input('Digite o termo da PA: '))
razao = int(input('Agora, a razão: '))

for c in range (1, 11):
        print(f'O {c}º termo é: {termo}')
        termo = termo + razao
        

