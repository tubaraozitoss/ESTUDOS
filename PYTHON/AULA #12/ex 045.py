# Gerue um programa que faça o computador jogar jokenpô com você.
import random

print(('=-' * 10) + (' Vamos jogar \033[1;30mJOKENPÔ!\033[m ') + ('=-' * 10))

jogadas = ['pedra', 'papel', 'tesoura']
jogador = input('Qual a sua escolha? Pedra, papel ou tesoura? ').lower()
pc = random.choice(jogadas)

if jogador == pc:
    print('Deu \033[1;36mempate!\033[m Melhor do que perder né, rs.')
elif jogador == 'pedra' and pc == 'papel':
    print('Você: PEDRA')
    print('PC: PAPEL')
    print('Você \033[31mperdeu!\033[m')
elif jogador == 'papel' and pc == 'pedra':
    print('Você: PAPEL')
    print('PC: PEDRA')
    print('Você \033[32mganhou!\033[m')    
elif jogador == 'tesoura' and pc == 'pedra':
    print('Você: TESOURA')
    print('PC: PEDRA')
    print('Você \033[31mperdeu!\033[m')   
elif jogador == 'pedra' and pc == 'tesoura':
    print('Você: PEDRA')
    print('PC: TESOURA')
    print('Você \033[32mganhou!\033[m')
elif jogador == 'papel' and pc == 'tesoura':
    print('Você: PAPEL')
    print('PC: TESOURA')
    print('Você \033[31mperdeu!\033[m')
elif jogador == 'tesoura' and pc == 'papel':
    print('Você: TESOURA')
    print('PC: PAPEL')
    print('Você \033[32mganhou!\033[m')
else:
    print('Jogada inválida. Escolha pedra, papel ou tesoura.')