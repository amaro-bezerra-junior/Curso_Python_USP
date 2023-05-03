print("Programa para identificar números divisíveis por 3 e 5.")

import math

n = int(input("Digite aqui o número: "))

n1 = n

n = (n % 3) or (n % 5)
if n == 0:
    print("FizzBuzz")
else:
    print(n1)
