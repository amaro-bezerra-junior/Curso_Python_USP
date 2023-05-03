print("Programa realiza a soma dos números digitado e termina quando digitar o número zero")

soma = 0

valor = 1

while valor != 0:
    valor = int(input("Digite o valor a ser somado: "))
    soma = soma + valor
    
print("O valor da soma é:", soma)
