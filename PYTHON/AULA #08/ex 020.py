# Agora, o professor do ex 019 quer randomizar a ordem de apresentação dos alunos.
import random

a1 = input('Primeiro aluno: ')
a2 = input('Segundo aluno: ')
a3 = input('Terceiro aluno: ')
a4 = input('Quarto aluno: ')
lista = [a1, a2, a3, a4]
random.shuffle(lista) # Ao colocar a função no print direto, não dá certo.

print(f'A ordem da apresentação será: {lista}')
