print("Promaga para realizar a multiplicação dos números.")

tamanho = int(input("Digite a quantidade a ser multiplicada: "))
produto = 1
i = 0

while i < tamanho:
    valor = int(input("Digite o valor a ser multiplicado: "))
    produto = produto * valor
    i = i + 1
print("O produto dos valores é:", produto)
