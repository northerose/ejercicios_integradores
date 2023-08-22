"""5. Sabiendo que ValueError es la excepción que se lanza cuando no podemos convertir una
cadena de texto en su valor numérico, escriba una función get_int() que lea un valor entero
del usuario y lo devuelva, iterando mientras el valor no sea correcto. Intente resolver el
ejercicio tanto de manera iterativa como recursiva."""




def get_int():
    valor = input("ingrese un número: ")
    try:
        int(valor)
        print(f"El valor ingresado fue {valor}")
    except ValueError:
        print("valor incorrecto")
        get_int()




get_int()
