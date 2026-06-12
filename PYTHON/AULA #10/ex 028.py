# Escreva um programa que pense um numero entre 0 e 5. O programa deverá escrever na tela se o usuário venceu ou perdeu.
import random
resposta = random.randint(0, 5)

num = int(input('Tente adivinhar o número que estou pensando, de 0 a 5: '))


if num == resposta:
    print('Parabéns! Você acertou. ')
else:
    print(f'Que pena, você errou. O número que eu pensei era {num}')
