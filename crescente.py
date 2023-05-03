print("Programa para identificar números crescentes.")


crescente = True
primeiro = int(input("Digite o primeiro número da sequência: "))

valor = 0

while valor > primeiro:
    valor = int(input("Digite um número da sequência: "))
    if valor < primeiro:
        crescente = False
    primeiro = valor
if crescente:
    print("A seguência está em ordem crescente!")
else:
    print("A sequência não está em ordem crescente!")

    #corrigir o programa!


        
