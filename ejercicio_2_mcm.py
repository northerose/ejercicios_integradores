from ejercicio_1_mcd import mcd

"""2. Escribir una función que calcule el mínimo común múltiplo entre dos números."""

#Mínimo común múltiplo de 85 y 32

def mcm(number_1, number_2):
    result = (number_1 * number_2) / mcd(number_1, number_2)
    return result

print(mcm(85, 32))
