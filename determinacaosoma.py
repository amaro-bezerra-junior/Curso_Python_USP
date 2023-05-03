print("Programa para realizar a soma de valores e encerra ao digitar zero.")

soma = 0
valor = 1

while valor != 0:
    valor = int(input("Digite os valores a ser somados: "))
    soma = soma + valor
print("A soma dos valores digitados é:",soma)


