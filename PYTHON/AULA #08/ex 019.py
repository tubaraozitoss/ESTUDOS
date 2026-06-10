# Um professor quer sortear um dos seus quatro alunos para pagar o quadro. Faça um programa que ajude ele, lendo o nome deles e sorteando.
import random

a1 = input('Primeiro aluno: ')
a2 = input('Segundo aluno: ')
a3 = input('Terceiro aluno: ')
a4 = input('Quarto aluno: ')
lista = [a1, a2, a3, a4]

print(f'O aluno sorteado foi {random.choice(lista)}')

