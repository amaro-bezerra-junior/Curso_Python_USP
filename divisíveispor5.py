print("Programa para identificar números divisíveis por 5.")

import math

n = int(input("Digite aqui o número: "))
n1 = n

n = (n % 5)
if n == 0:
    print("Buzz")
else:
    print(n1)
