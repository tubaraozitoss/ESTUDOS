# Digite um programa que compare valores (mostre se o primeiro valor é maior, ou se o segundo é maior, ou se são iguais).
n1 = float(input('Digite um valor: '))
n2 = float(input('Digite outro valor: '))

if n1 > n2:
    print(f'O \033[1mprimeiro\033[m valor digitado \033[1m({n1})\033[m é maior que o segundo \033[1m({n2})\033[m.')
elif n2 > n1:
    print(f'O \033[1msegundo\033[m valor digitado \033[1m({n2})\033[m é maior que o primeiro \033[1m({n1})\033[m.')
else:
    print(f'Os valores \033[1m{n1} e {n2}\033[m são iguais.')