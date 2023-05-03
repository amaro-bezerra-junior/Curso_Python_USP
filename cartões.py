print("Programa para ler número de cartões")

meuCartao = int(input("Digite o número do seu cartão de crédito: "))

cartaoLido = 1
encontreiMeuCartaoNaLista = False

while cartaoLido != 0 and not encontreiMeuCartaoNaLista:
    cartaoLido = int(input("Digite o número do próximo cartão: "))
    if cartaoLido == meuCartao:
        encontreiMeuCartaoNaLista = True
if encontreiMeuCartaoNaLista:
    print("Meu cartão consta na lista")
else:
    print("Meu cartão não consta na lista")
