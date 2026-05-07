from abc import ABC, abstractmethod
from exceptions.custom_exceptions import ServicioError

class Servicio(ABC):

    def __init__(self, nombre, precio_base):
        self.nombre = nombre
        self.precio_base = precio_base

    #Encapsulación del nombre
    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
        if not valor or not valor.strip():
            raise ServicioError("El nombre del servicio no puede estar vacío")
        self._nombre = valor.strip()

    #Encapsulación del precio
    @property
    def precio_base(self):
        return self._precio_base

    @precio_base.setter
    def precio_base(self, valor):
        if valor <= 0:
            raise ServicioError("El precio base debe ser mayor que cero")
        self._precio_base = valor

    #Método abstracto obligatorio
    @abstractmethod
    def calcular_costo(self, tiempo, impuesto=0, descuento=0):
        pass

    #Método abstracto obligatorio
    @abstractmethod
    def descripcion(self):
        pass


