# Leia 5 números e para cada um diga se é primo ou não.
divisores = 0

for c in range (1, 6):
    num = int(input('Digite um número: '))
    divisores = 0
    
    for i in range (1, num + 1):
        if num % i == 0:
            divisores += 1

    if divisores == 2:
            print(f'{num} -> Primo')
    else:
            print(f'{num} -> Não primo')