# Refaça o ex 035.py, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# Equilátero - todos os lados iguais
# Isósceles - dois lados iguais
# Escaleno - todos os lados diferentes

lado1 = float(input('Lado 1: '))
lado2 = float(input('Lado 2: '))
lado3 = float(input('Lado 3: '))

if lado1 + lado2 > lado3 and lado1 + lado3 > lado2 and lado2 + lado3 > lado1:
    print('As retas podem formar um triângulo!')

    if lado1 == lado2 == lado3:
        print('Os seus lados formam um triângulo EQUILÁTERO, pois todos os lados são iguais.')
    elif lado1 == lado2 != lado3 or lado1 == lado3 != lado2 or lado2 == lado3 != lado1:
        print('Os seus lados formam um triângulo ISÓSCELES, pois possui dois lados iguais e um diferente.')
    else:
        print('Os seus lados formam um triângulo ESCALENO, pois todos os lados são diferentes.')

else:
    print('As retas não podem formar um triângulo.')
    
