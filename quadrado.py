print("Cálculo dos quadrados de uma sequência de números.")
print("A sequência termina com um 0 (zero).\n")

num = int(input("Digite um número: "))
while num != 0:
    quadrado = num * num
    print(num, "ao quadrado é", quadrado)
    num = int(input("Digite um número: "))
    
