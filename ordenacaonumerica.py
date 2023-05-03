print("Programa com ordenação númerica. Por favor informe os números.")

import math

a = int(input("Informe um número para a variável A: "))
b = int(input("Informe um número para a variável B: "))
c = int(input("Informe um número para a variável C: "))

crescente = a < b < c

if a < b < c:
    print("crescente")
else:
    print("não está em ordem crescente")
    
