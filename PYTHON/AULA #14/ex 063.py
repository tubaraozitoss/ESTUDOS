# Leia um número n inteiro e mostre na tela os n primeiros elementos de uma Sequência de Fibonacci

termos = int(input('Digite a quantidade de termos desejada: '))

primeiro = 0
segundo = 1

contador = 0

while contador != termos:
    print(primeiro)
    proximo = primeiro + segundo
    primeiro = segundo
    segundo = proximo
    contador += 1

    