"""6. Crear una clase llamada Persona. Sus atributos son: nombre, edad y DNI. Construya los
siguientes métodos para la clase:
* Un constructor, donde los datos pueden estar vacíos.
* Los setters y getters para cada uno de los atributos. Hay que validar las entradas de
datos.
* mostrar(): Muestra los datos de la persona.
* Es_mayor_de_edad(): Devuelve un valor lógico indicando si es mayor de edad."""

class  Persona (object):
    def __init__(self, nombre=None, edad=None, dni=None):
        self.__nombre = nombre
        self.__edad = edad
        self.__dni = dni

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, value):
        if value.isalpha():
            self.__nombre = value
        else:
            raise Exception("Debe ser un valor alfabético")

    @property
    def edad(self):
        return self.__edad
    
    @edad.setter
    def edad(self, value):
        if type(value) == int:
            self.__edad = value
        else:
            raise Exception("Debe ser un valor numérico entero")

    @property
    def dni(self):
        return self.__dni

    @dni.setter
    def dni(self, value):
        if type(value) == int and len(str(value)) == 8:
            self.__dni = value
        else:
            raise Exception("El DNI debe estar compuesto de 8 dígitos enteros")

    def mostrar(self):
        print(f"{self.nombre}, {self.edad}, {self.dni}")
    

    def es_mayor_edad(self):
        if self.edad >= 18:
            print("Es mayor de edad")
        else:
            print("Es menor de edad")

    
"""********** PRUEBAS ***********"""
if __name__ == "__main__":
    persona = Persona(nombre="Gustavo", edad=33, dni=1234578)

    try:
        persona.nombre = "1213desf"
    except Exception as error:
        print(error)

    persona.mostrar()

    persona.es_mayor_edad()

    persona.edad = 17

    persona.mostrar()

    persona.es_mayor_edad()

    try:
        persona.dni = 12345
    except Exception as error:
        print(error)

    try:
        persona.edad = "u9hu"
    except Exception as error:
        print(error)

