# Leia 3 palavras ou frases e indique quantos são palíndromos

contador = 0

for c in range (1,4):
    entrada = input('Digite uma palavra ou frase: ').lower()
    entrada = entrada.replace(' ', '')

    if entrada == entrada[::-1]:
        contador += 1

print(f'Das 3 entradas, {contador} são palíndromos.')  
