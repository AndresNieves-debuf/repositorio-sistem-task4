from models.entidad import Entidad
from exceptions.custom_exceptions import ClienteError
from utils.validaciones import validar_nombre, validar_email

class Cliente(Entidad):

    def __init__(self, id, nombre, email):
        super().__init__(id)
        self.nombre = nombre
        self.email = email


#Encapsulación del nombre
@property
def nombre(self):
    return self._nombre


@nombre.setter
def nombre(self, valor):
    try:
        self._nombre = validar_nombre(valor)
    except Exception as e:
        raise ClienteError(f"Error en nombre:{e}") from e
    

#Encapsulación del email
@property
def email(self):
    return self._email


@email.setter
def email(self, valor):
    try:
        self._email = validar_email(valor)

    except Exception as e:
        raise ClienteError(f"Error en email:{e}") from e
    

#Metodo obligatorio heredado
def mostrar_info(self):
    return f"Cliente ID:{self._id}| Nombre: {self._nombre}| Email: {self._email}"


#Metodo adicional útil
def actualizar_email(self, nuevo_email):
    self.email = nuevo_email
    return "Email actualizado correctamente"

