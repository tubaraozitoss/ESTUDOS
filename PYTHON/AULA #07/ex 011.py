# Escreva um programa que leia a altura e largura de uma parede em metros, calcule sua área e a quantidade de tinta necessária, considerando
# que 1 litro de tinta pinta 2m²

altura = float(input('Indique a altura da sua parede: '))
largura = float(input('Indique a largura da sua parede: '))
area = altura * largura
tinta = area / 2
galao = tinta / 10
valor = 56.5
print(f'Considerando a altura de {altura}m, e a largura de {largura}m, temos a área de {area}m²')
print(f'Com isso, sabe-se que são necessários {tinta} litros de tinta, que equivalem a {galao} galões, que custam {valor * galao}.')
