"""7. Crea una clase llamada Cuenta que tendrá los siguientes atributos: titular (que es una
persona) y cantidad (puede tener decimales). El titular será obligatorio y la cantidad es
opcional. Crear los siguientes métodos para la clase:
1.- Un constructor, donde los datos pueden estar vacíos.
2.- Los setters y getters para cada uno de los atributos. El atributo no se puede modificar
directamente, sólo ingresando o retirando dinero.
3.- mostrar(): Muestra los datos de la cuenta.
4.- ingresar(cantidad): se ingresa una cantidad a la cuenta, si la cantidad introducida es
negativa, no se hará nada.
5.- retirar(cantidad): se retira una cantidad a la cuenta. La cuenta puede estar en números
rojos."""


from ejercicio_6_POO import Persona

class Cuenta:
    def __init__(self, titular, cantidad=0):
        self.titular = titular
        self.__cantidad = cantidad

    @property
    def cantidad(self):
        return self.__cantidad

    @cantidad.setter
    def cantidad(self, monto):
        self.__cantidad = monto

    def ingresar(self, monto):
        if monto < 1:
            raise Exception("Debe ingresar un monto válido")
        self.cantidad += monto

    def retirar(self, monto):
        if self.cantidad - monto <= -100:
            raise Exception("No puedes superar una cifra negativa mayor a -100")
        self.cantidad -= monto

    def mostrar(self):
        print(f"El titular de esta cuenta es: {self.titular.nombre}, monto disponible: {self.cantidad}")


"""********** PRUEBAS ***********"""
if __name__ == "__main__":

    titular = Persona("Juan")
    cuenta= Cuenta(titular)
    cuenta.mostrar()

    cuenta.ingresar(100)

    try:
        cuenta.ingresar(-10)
    except Exception as error:
        print(error)

    cuenta.mostrar()

    cuenta.retirar(50)
    cuenta.mostrar()
    cuenta.retirar(100)
    cuenta.mostrar()

    try:
        cuenta.retirar(100)
    except Exception as error:
        print(error)

    cuenta.mostrar()