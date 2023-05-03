print("Programa para contagem de números pares e ímpares")

import math

soma = 0
cont = 0

for c in range(1, 8):
    n = int(input("Digite o {} valor: ".format(c)))
    soma += n
    cont += 1
print("Você digitou", cont, "números e a soma é:", soma)

