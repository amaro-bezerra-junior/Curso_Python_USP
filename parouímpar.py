print("Programa para identificação de números pares e ímpares")

import math

n = int(input("Digite aqui um número: "))

n = (n % 2 == 0)
if n:
    print("par")
else:
    print("ímpar")
