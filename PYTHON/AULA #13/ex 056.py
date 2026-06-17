# Gere um programa que leia o nome, idade e sexo de 4 pessoas. No final, mostre a média de idade do grupo e o homem mais velho.

soma_idades = 0
velho = 0
nome_velho = ''
for c in range (1, 5):

    nome = input(f'Nome do usuário {c}: ')
    idade = int(input(f'Idade do usuário {c}: '))
    sexo = input(f'Sexo do usuário {c} (digite feminino ou masculino): ').lower()
    
    soma_idades += idade
    
    if sexo == 'masculino':
        if idade > velho:
            velho = idade      
            nome_velho = nome        

media = soma_idades / 4

print(f'A média entre todas as idades inseridas é {media}.')
print(f'Além disso, o usuário {nome_velho} é o HOMEM mais velho e tem {velho} anos.')


