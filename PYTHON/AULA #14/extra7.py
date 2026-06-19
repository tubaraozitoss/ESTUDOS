# Programa de votação.
from time import sleep

print('=-' * 5)
print('URNA')
print('=-' * 5)

escolha = 5
contador_a = 0
contador_b = 0
contador_branco = 0

while escolha != 0:

    print('Opções')
    print('[ 1 ] Candidato A')
    print('[ 2 ] Candidato B')
    print('[ 3 ] Branco')
    print('[ 0 ] Encerrar votação')

    escolha = int(input('Tecle uma das opções: '))

    if escolha == 1:
        contador_a += 1
        
    elif escolha == 2:
        contador_b += 1  
    elif escolha == 3:
        contador_branco += 1
    elif escolha == 0:
        print('Contabilizando votos...')
        sleep(1.5)
    else:
        print('Opção inválida!')

print(f'Candidato A: {contador_a} votos')
print(f'Candidato B: {contador_b} votos')
print(f'Votos em branco: {contador_branco} votos')
print('Fim.')