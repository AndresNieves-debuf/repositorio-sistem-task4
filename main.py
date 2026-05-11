from models.cliente import Cliente
from models.servicio_especificos import (
    ReservaSala,
    AlquilerEquipo,
    Asesoria
)
from models.reserva import Reserva
from utils.logger import registrar_log

def ejecutar_pruebas():
    registrar_log("--- INICIO DEL SISTEMA DE RESERVAS ---")
    print("Iniciando simulación de 10 operaciones...\n")

    # =========================================
    # 1. LISTAS INTERNAS (CONTENEDORES)
    # =========================================
    lista_clientes = []
    lista_servicios = []
    lista_reservas = []

    # =====================================================
    # OPERACIÓN 1: Registro de Clientes Válidos (Bucle)
    # =====================================================
    datos_clientes = [
        (1, "Juan Perez", "juan@email.com"),
        (2, "Maria Lopez", "maria@email.com")
    ]

    for datos in datos_clientes:
        try:
            nuevo_cliente = Cliente(datos[0], datos[1], datos[2])
            lista_clientes.append(nuevo_cliente) # CORREGIDO: Se agrega a la lista
            print(f"Operación 1: {nuevo_cliente.mostrar_info()}")
        except Exception as e:
            registrar_log(f"Error registrando cliente: {e}")

    # =====================================================
    # OPERACIÓN 2: Cliente Inválido (Nombre con números)
    # =====================================================
    try:
        cliente_error = Cliente(3, "Carlos123", "carlos@email.com")
        lista_clientes.append(cliente_error)
    except Exception as e:
        print(f"Operación 2 (Esperada): {e}")
        registrar_log(f"Error operación 2: {e}")

    # =====================================================
    # OPERACIÓN 3: Servicio de Sala Válido
    # =====================================================
    try:
        sala_vip = ReservaSala("Sala VIP", 150.0)
        lista_servicios.append(sala_vip) # CORREGIDO
        print(f"Operación 3: {sala_vip.descripcion()}")
    except Exception as e:
        registrar_log(f"Error operación 3: {e}")

    # =====================================================
    # OPERACIÓN 4: Servicio Inválido (Nombre vacío)
    # =====================================================
    try:
        servicio_nulo = ReservaSala("", 100)
    except Exception as e:
        print(f"Operación 4 (Esperada): {e}")
        registrar_log(f"Error operación 4: {e}")

    # =====================================================
    # OPERACIÓN 5: Reserva Válida (Juan Perez reserva Sala VIP)
    # =====================================================
    try:
        if lista_clientes and lista_servicios:
            reserva1 = Reserva(lista_clientes[0], lista_servicios[0], 3)
            lista_reservas.append(reserva1) # CORREGIDO
            print(f"Operación 5: Reserva creada para {lista_clientes[0].nombre}")
    except Exception as e:
        registrar_log(f"Error operación 5: {e}")

    # =====================================================
    # OPERACIÓN 6: Procesar Reserva (Cálculo con Polimorfismo)
    # =====================================================
    try:
        if lista_reservas:
            resultado = lista_reservas[0].procesar_reserva()
            print(f"Operación 6: {resultado}")
    except Exception as e:
        registrar_log(f"Error operación 6: {e}")

    # =====================================================
    # OPERACIÓN 7: Alquiler de Equipo Válido
    # =====================================================
    try:
        laptop = AlquilerEquipo("Laptop Gamer", 50.0)
        lista_servicios.append(laptop)
        print(f"Operación 7: {laptop.descripcion()}")
    except Exception as e:
        registrar_log(f"Error operación 7: {e}")

    # =====================================================
    # OPERACIÓN 8: Reserva de Equipo con Impuesto/Descuento
    # =====================================================
    try:
        costo_equipo = laptop.calcular_costo(
            dias=2,
            impuesto=0.15,
            descuento=0.05
        )
    except Exception as e:
        registrar_log(f"Error operación 8: {e}")
    else:
        print(
            f"Operación 8 exitosa: ${costo_equipo}"
        )

        registrar_log(
        "Operación 8 ejecutada correctamente"
    )

    # =====================================================
    # OPERACIÓN 9: Asesoría Válida
    # =====================================================
    try:
        asesoria_legal = Asesoria("Consultoría TI", 200.0)
        lista_servicios.append(asesoria_legal)
        print(f"Operación 9: {asesoria_legal.descripcion()}")
    except Exception as e:
        registrar_log(f"Error operación 9: {e}")

    # =====================================================
    # OPERACIÓN 10: Reserva Inválida (Duración negativa)
    # =====================================================
    try:
        reserva_fallida = Reserva(lista_clientes[0], lista_servicios[-1], -10)
    except Exception as e:
        print(f"Operación 10 (Esperada): {e}")
        registrar_log(f"Error operación 10: {e}")

    print("\n--- Simulación finalizada. Revisa data/logs.txt para más detalles. ---")
    registrar_log("--- FIN DEL SISTEMA ---")

if __name__ == "__main__":
    ejecutar_pruebas()

 