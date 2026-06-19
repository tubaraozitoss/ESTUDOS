# Melhore o desafio anterior, perguntando se o usuário quer mostrar mais alguns termos ou não.

termo = int(input('Qual o primeiro termo da PA?: '))
razao = int(input('Razão da PA: '))

contador = 0
limite = 10

while limite != contador:

    while contador < limite:
        print(termo)
        termo = termo + razao
        contador += 1
    mais = int(input('Quantos termos você deseja continuar recebendo?: '))
    limite = limite + mais
