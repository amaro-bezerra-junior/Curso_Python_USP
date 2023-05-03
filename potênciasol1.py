print("Calculo de potências\n")
x = int(input("Digite a base: "))
n = int(input("Digite o expoente (inteiro >= 0): "))
i = 0
x_i = 1
while i < n:
    i = i + 1
    x_i = x_i * x
    print("O valor de", x, "elevado a", n, "é", x_i)
