"""1.- Escribir una función que calcule el máximo común divisor entre dos números."""

# Máximo común divisor de 50 y 60

def mcd(number_1, number_2):
    count = 0
    while number_2 != 0:
        count = number_2
        number_2 = number_1 % number_2
        number_1 = count
    return number_1

print(mcd(50, 60))