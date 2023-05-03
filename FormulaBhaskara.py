print("Programa para calular a formula de Bhaskara.")

import math

variavelA = int(input("Informe o valor da variável A: "))
variavelB = int(input("Informe o valor da variável B: "))
variavelC = int(input("Informe o valor da variável C: "))

delta = (variavelB ** 2) - 4 * (variavelA * variavelC)

if delta == 0:
    raiz1 = (- variavelB + math.sqrt(delta)) / (2 * variavelA)
    print("a raiz desta equação é", raiz1)
else:
    if delta < 0:
        print("esta equação não possui raízes reais")
    else:
        raiz1 = (- variavelB + math.sqrt(delta)) / (2 * variavelA)
        raiz2 = (- variavelB - math.sqrt(delta)) / (2 * variavelA)
        if raiz1 < raiz2:
            print("as raízes da equação são", raiz1, "e", raiz2)
        if raiz1 > raiz2:
            print("as raízes da equação são", raiz2, "e", raiz1)
