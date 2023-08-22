
"""8. Vamos a definir ahora una “Cuenta Joven”, para ello vamos a crear una nueva clase
CuantaJoven que deriva de la clase creada en el punto 7. Cuando se crea esta nueva clase,
además del titular y la cantidad se debe guardar una bonificación que estará expresada en
tanto por ciento. Crear los siguientes métodos para la clase:
1.- Un constructor.
2.- Los setters y getters para el nuevo atributo.
3.- En esta ocasión los titulares de este tipo de cuenta tienen que ser mayor de edad, por lo
tanto hay que crear un método es_titular_valido() que devuelve verdadero si el titular es
mayor de edad pero menor de 25 años y falso en caso contrario.
4.- Además, la retirada de dinero sólo se podrá hacer si el titular es válido.
5.- El método mostrar() debe devolver el mensaje de “Cuenta Joven” y la bonificación de la
cuenta"""


from ejercicio_6_POO import Persona
from ejercicio_7_cuenta import Cuenta

class CuentaJoven(Cuenta):
    def __init__ (self, titular, cantidad=0, bonificacion=0):
        super().__init__(titular, cantidad)
        self.__bonificacion = bonificacion

    def es_titular_valido(self):
        return 18 <= self.titular.edad <= 25
    
    def retirar(self, monto):
        if not self.es_titular_valido():
            raise Exception("Titular no válido")
        self.cantidad -= monto

    def ingresar(self, monto):
        if self.es_titular_valido():
            bonificacion = (monto * self.bonificacion) / 100
        else:
            bonificacion = 0
        self.cantidad += bonificacion

    def mostrar(self):  
        print(f"Cuenta Joven:")
        print(f"Bonificación {self.bonificacion}%")
        print(f"Saldo Total Cuenta Joven {self.cantidad}")
        super().mostrar()

    @property
    def bonificacion(self):
        return self.__bonificacion
    
    @bonificacion.setter
    def bonificacion(self, porcentaje):
        self.__bonificacion = porcentaje
       

"""********** PRUEBAS ***********"""
if __name__ == "__main__":
    titular = Persona("Juan", 64)
    cuenta= CuentaJoven(titular)
    cuenta.cantidad = 200
    cuenta.bonificacion = 10
    cuenta.mostrar()

    try:
        cuenta.retirar(50)
    except Exception as error:
        print(error)
    
    cuenta.mostrar()
    cuenta.ingresar(50)
    cuenta.mostrar()