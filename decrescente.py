print("Programa para identificar números decrescentes.")

primeiro = int(input("Digite o primeiro número da sequência: "))
decrescente = True
valor = 1

while valor != 0 and decrescente:
    valor = int(input("Digite o próximo número da sequência: "))
    if valor > primeiro:
        decrescente = False
    primeiro = valor
if decrescente:
    print("A seguência está em ordem decrescente!")
else:
    print("A sequência não está em ordem decrescente!")
