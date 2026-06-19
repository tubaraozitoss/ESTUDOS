# Melhore o ex 028 onde o computador vai pensar entre 0 e 10. Só que agora o usuário tenta até adivinhar, e mostra no fim quantos palpites.

from random import randint
from time import sleep

num = int(input('Tente adivinhar o número: '))
palpite = 1
pc = randint(1, 10)

while num != pc:
    print(f'Você errou! Eu pensei no número {pc}. Deixa eu pensar em outro...')
    sleep(1)

    pc = randint(1, 10)
    num = int(input('Tente adivinhar o número novamente: '))
    palpite += 1

print(f'Você acertou! Levaram {palpite} chutes.')