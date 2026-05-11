# Software FJ - Sistema Integral de Gestión de Clientes, Servicios y Reservas

## Descripción del Proyecto

Software FJ es un sistema integral desarrollado en Python utilizando Programación Orientada a Objetos (POO), diseñado para gestionar clientes, servicios y reservas sin utilizar bases de datos.

El sistema permite administrar diferentes tipos de servicios ofrecidos por la empresa Software FJ, incluyendo:

* Reservas de salas
* Alquiler de equipos
* Asesorías especializadas

Toda la información se gestiona mediante objetos, listas internas y archivos de logs, implementando una arquitectura modular, extensible y estable.

---

# Objetivo del Proyecto

Desarrollar una aplicación orientada a objetos que implemente de manera rigurosa:

* Abstracción
* Herencia
* Polimorfismo
* Encapsulación
* Manejo avanzado de excepciones

Garantizando que el sistema continúe funcionando aun cuando ocurran errores durante la ejecución.

---

# Tecnologías Utilizadas

* Python 3
* Programación Orientada a Objetos (POO)
* Manejo de excepciones
* Manejo de archivos
* Visual Studio Code
* GitHub

---

# Estructura del Proyecto

```plaintext
SOFTWARE-FJ/
│
├── data/
│   └── logs.txt
│
├── exceptions/
│   ├── __init__.py
│   └── custom_exceptions.py
│
├── models/
│   ├── __init__.py
│   ├── entidad.py
│   ├── cliente.py
│   ├── servicio.py
│   ├── servicio_especificos.py
│   └── reserva.py
│
├── tests/
│   └── test_operaciones.py
│
├── utils/
│   ├── __init__.py
│   ├── logger.py
│   └── validaciones.py
│
├── main.py
└── README.md
```

---

# Explicación de la Arquitectura

## models/

Contiene las clases principales del sistema.

### entidad.py

Clase abstracta base del sistema.

### cliente.py

Clase encargada de gestionar clientes y validar información personal.

### servicio.py

Clase abstracta que define la estructura general de los servicios.

### servicio_especificos.py

Contiene los servicios derivados:

* ReservaSala
* AlquilerEquipo
* Asesoria

### reserva.py

Gestiona reservas, estados y procesamiento.

---

## exceptions/

Contiene las excepciones personalizadas utilizadas por el sistema.

### custom_exceptions.py

Incluye:

* ClienteError
* ServicioError
* ReservaError
* ProcesamientoError

---

## utils/

Contiene herramientas auxiliares.

### validaciones.py

Validaciones estrictas para:

* nombres
* correos electrónicos
* datos inválidos

### logger.py

Registra errores y eventos importantes en:

```plaintext
data/logs.txt
```

---

## tests/

Contiene pruebas del sistema.

---

# Principios de Programación Orientada a Objetos Implementados

## Abstracción

Se implementaron clases abstractas:

* Entidad
* Servicio

Utilizando:

```python
from abc import ABC, abstractmethod
```

---

## Herencia

Las clases:

* ReservaSala
* AlquilerEquipo
* Asesoria

heredan de la clase abstracta Servicio.

---

## Polimorfismo

Cada servicio redefine métodos como:

```python
descripcion()
calcular_costo()
```

permitiendo comportamientos diferentes según el tipo de servicio.

---

## Encapsulación

La clase Cliente utiliza atributos privados:

```python
self.__nombre
self.__email
```

además de propiedades getter y setter.

---

# Manejo Avanzado de Excepciones

El sistema implementa:

* try/except
* try/except/else
* try/finally
* excepciones personalizadas
* encadenamiento de excepciones

Ejemplo:

```python
try:
    costo = servicio.calcular_costo(2)

except Exception as e:
    print(e)

else:
    print("Costo calculado correctamente")
```

---

# Registro de Logs

Todos los errores y eventos importantes se almacenan en:

```plaintext
data/logs.txt
```

Ejemplos:

* creación de clientes
* reservas exitosas
* errores de validación
* fallos de procesamiento

---

# Manejo de Listas Internas

El sistema utiliza listas para almacenar información temporalmente:

```python
lista_clientes = []
lista_servicios = []
lista_reservas = []
```

Esto permite gestionar información sin necesidad de utilizar bases de datos.

---

# Servicios Implementados

## ReservaSala

Gestiona reservas de salas empresariales.

### Funciones

* descripción de salas
* cálculo de costos por horas
* impuestos y descuentos

---

## AlquilerEquipo

Gestiona alquiler de equipos tecnológicos.

### Funciones

* alquiler por días
* cálculo de costos
* validación de precios

---

## Asesoria

Gestiona asesorías especializadas.

### Funciones

* asesorías por horas
* cálculo de tarifas
* procesamiento de costos

---

# Clase Reserva

La clase Reserva integra:

* cliente
* servicio
* duración
* estado

### Estados disponibles

* Pendiente
* Confirmada
* Cancelada

### Funciones principales

* confirmar_reserva()
* cancelar_reserva()
* procesar_reserva()
* mostrar_reserva()

---

# Validaciones Implementadas

El sistema valida:

* nombres vacíos
* nombres con números
* correos inválidos
* precios negativos
* duración negativa
* parámetros faltantes

---

# Operaciones Simuladas

El sistema ejecuta al menos 10 operaciones completas incluyendo:

## Operaciones válidas

* registro de clientes
* creación de servicios
* reservas exitosas
* procesamiento de reservas

## Operaciones inválidas

* clientes con nombres incorrectos
* servicios inválidos
* reservas con duración negativa
* errores de procesamiento

El sistema continúa funcionando aun cuando ocurren errores.

---

# Cómo Ejecutar el Proyecto

## 1. Clonar el repositorio

```bash
git clone URL_DEL_REPOSITORIO
```

---

## 2. Abrir el proyecto en Visual Studio Code

```bash
cd software-fj
```

---

## 3. Ejecutar el sistema

```bash
python main.py
```

---

# Resultados Esperados

El sistema mostrará:

* clientes registrados
* servicios creados
* reservas procesadas
* errores controlados
* registros en logs

---

# Características del Sistema

* Arquitectura modular
* Sistema extensible
* Manejo robusto de errores
* Sin uso de bases de datos
* Programación orientada a objetos
* Registro automático de logs
* Validaciones estrictas
* Continuidad del sistema ante errores

---

# Conclusiones

El proyecto Software FJ demuestra la correcta aplicación de los principios de Programación Orientada a Objetos mediante una arquitectura modular y estable.

El sistema implementa correctamente abstracción, herencia, polimorfismo, encapsulación y manejo avanzado de excepciones, permitiendo gestionar clientes, servicios y reservas de manera eficiente.

Además, el uso de listas internas y archivos de logs permite mantener la aplicación funcional sin utilizar motores de bases de datos.

---

# Integrantes del Equipo

* Integrante 1: Jhon Alexander Martinez Silva
* Integrante 2: Andrés David Nieves Pedrozo 

---

# Estado del Proyecto

Proyecto funcional y listo para ejecución.
