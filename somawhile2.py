print("Determine a quantidade de números a ser somado.")

tamanho = int(input("Informe a quantidade de números a ser somado: "))

soma = 0
i = 1

while i < tamanho:
    valor = int(input("Digite o número a ser somado: "))
    soma = soma + valor
    
print("A soma dos números é:", soma)
