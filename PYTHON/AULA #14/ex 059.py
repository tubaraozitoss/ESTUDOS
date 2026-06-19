# Crie um programa que leia 2 valores e mostre um menu: 1, somar. 2, multiplicar. 3, maior. 4, novos numeros. 5, sair do programa.

n1 = int(input('Digite um valor: '))
n2 = int(input('Agora outro: '))
escolha = 0

while escolha != 5:

    print('Escolha uma das opções do menu:')
    print('')
    print('[ 1 ] - Soma')
    print('[ 2 ] - Multiplicação')
    print('[ 3 ] - Mostre o maior valor')
    print('[ 4 ] - Escolher outros valores')
    print('[ 5 ] - Finalizar')
    print('')
    escolha = int(input('Qual opção deseja escolher?: '))
    print('')

    if escolha == 1:
        print(f'A soma entre {n1} e {n2} é {n1 + n2}.')
    elif escolha == 2:
        print(f'A multiplicação entre {n1} e {n2} é {n1 * n2}.')
    elif escolha == 3:
        if n1 > n2:
            print(f'O valor {n1} é o maior valor.')
        elif n1 < n2:
            print(f'O valor {n2} é o maior valor.')
        else:
            print(f'Os valores {n1} e {n2} são iguais.')
    elif escolha == 4:
        print('Claro!')
        n1 = int(input('Digite um valor: '))
        n2 = int(input('Agora outro: '))
    else:
        print('Opção inválida, reiniciando programa.')
print('Fim.')