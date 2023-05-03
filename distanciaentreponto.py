print("Distância entre dois pontos")

import math

xa = float(input("Digite o valor da variável XA: "))
xb = float(input("Digite o valor da variável XB: "))
ya = float(input("Digite o valor da variável YA: "))
yb = float(input("Digite o valor da variável YB: "))

if xa < 0 and yb < 0:
    print("perto")
else:
    d1 = math.sqrt(((xb) - (xa)) ** 2) + math.sqrt(((yb) - (ya)) ** 2)
    if d1 >= 10:
        print("longe")
    else:
        if d1 < 10:
            print("perto")
