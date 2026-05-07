Este módulo corresponde a la gestión de clientes dentro del sistema Software FJ.
Su objetivo es garantizar el registro seguro y validado de la información de los clientes mediante la aplicación de principios de Programación Orientada a Objetos (POO) y manejo controlado de excepciones.

Además, se implementa un sistema de validaciones reutilizable para evitar datos incorrectos y mejorar la estabilidad del sistema.
Estructura utilizada:

SOFTWARE-FJ/
│
├── models/
│   ├── entidad.py
│   ├── cliente.py
│
├── utils/
│   ├── validaciones.py
│
├── exceptions/
│   ├── custom_exceptions.py

Principios POO aplicados
Abstracción

La clase Cliente hereda de la clase abstracta Entidad, reutilizando atributos y métodos comunes del sistema.

Encapsulación

Los atributos sensibles (nombre y email) están protegidos mediante:
@property
setters personalizados
Esto evita modificaciones incorrectas de los datos.

Modularidad

Las validaciones fueron separadas en el archivo:
utils/validaciones.py
Esto permite reutilizar las funciones en otras partes del sistema.

Archivo: models/entidad.py

Función

Define una clase abstracta base para las entidades del sistema.

Código implementado:

from abc import ABC, abstractmethod

class Entidad(ABC):

    def __init__(self, id):
        self._id = id

    @abstractmethod
    def mostrar_info(self):
        pass


Características

Uso de ABC

Método abstracto obligatorio

Base reutilizable para futuras entidades

Archivo: utils/validaciones.py

Función

Contiene funciones reutilizables para validar datos de entrada.

Código implementado:

import re

def validar_nombre(nombre):

    if not nombre or not nombre.strip():
        raise ValueError("El nombre no puede estar vacío")

    if any(char.isdigit() for char in nombre):
        raise ValueError("El nombre no debe contener números")

    return nombre.strip()


def validar_email(email):

    if not email or not email.strip():
        raise ValueError("El email no puede estar vacío")

    patron = r'^[\w\.-]+@[\w\.-]+\.\w+$'

    if not re.match(patron, email):
        raise ValueError("Formato de email inválido")

    return email.strip().lower()


Validaciones implementadas

Validación de nombre

Se verifica que:

No esté vacío

No contenga números

Se eliminen espacios innecesarios

Validación de email

 Se verifica que:

 No esté vacío
 Cumpla formato válido de correo electrónico
 Se normalice a minúsculas

Archivo: exceptions/custom_exceptions.py

Función

 Define excepciones personalizadas para mejorar el control de errores.

Código implementado:

class ClienteError(Exception):
    pass

class ServicioError(Exception):
    pass

class ReservaError(Exception):
    pass

Archivo: models/cliente.py

Función
 
 Representa la entidad Cliente dentro del sistema.


Código implementado:

 from models.entidad import Entidad
 from exceptions.custom_exceptions import ClienteError
 from utils.validaciones import validar_nombre, validar_email

class Cliente(Entidad):

    def __init__(self, id, nombre, email):
        super().__init__(id)
        self.nombre = nombre
        self.email = email

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
        try:
            self._nombre = validar_nombre(valor)
        except Exception as e:
            raise ClienteError(f"Error en nombre: {e}") from e

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, valor):
        try:
            self._email = validar_email(valor)
        except Exception as e:
            raise ClienteError(f"Error en email: {e}") from e

    def mostrar_info(self):
        return f"Cliente ID: {self._id} | Nombre: {self._nombre} | Email: {self._email}"

    def actualizar_email(self, nuevo_email):
        self.email = nuevo_email
        return "Email actualizado correctamente"


Manejo de excepciones
 --Excepciones personalizadas utilizadas
 ClienteError

 --Técnicas implementadas
 try / except

 Encadenamiento de excepciones:
 raise ClienteError(...) from e

Ejemplo de prueba:
 from models.cliente import Cliente

try:
    cliente = Cliente(1, "Juan123", "correo_mal")
except Exception as e:
    print(e)

Resultado esperado
 Error en nombre: El nombre no debe contener números

Estos son los resultados obtenidos hasta ahora:
 El módulo desarrollado permite:

 ✔ Registrar clientes válidos

 ✔ Detectar datos incorrectos

 ✔ Evitar que el sistema falle

 ✔ Mantener validaciones reutilizables

 ✔ Aplicar correctamente principios POO