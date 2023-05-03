print("Calculador de consumo por quilometro rodado")

litros = input("Informe a quantidade de litros abastecido: ")
km = input("Informe os quilometros rodados: ")

consumo = float(km) / float(litros)

print("O veículo fez", consumo, "por litro de combustível.")

