from models import cliente
from models.cliente import Cliente
from models.servicio_especificos import (
   ReservaSala,
    AlquilerEquipo,
     Asesoria
 )

from models.reserva import Reserva

from utils.logger import registrar_log

def ejecutar_pruebas():
    
    registrar_log("---INICIO DEL SISTEMA DE RESERVAS---")

    # =========================================
    # LISTAS INTERNAS DEL SISTEMA
    # =========================================
   
    clientes = []
    servicios = []
    reservas = []

    #-------------------------
    # Operación 1:
    # Cliente valido
    #-------------------------

    try:
        
        cliente1 = Cliente(
    1,
    "Juan Perez",
    "juan@email.com"
)

        clientes.append(cliente1)

        print(cliente1.mostrar_info())

    except Exception as e:
        
        print(e)
        registrar_log(f"Error operación 1: {e}")
      
      
    # =====================================================
    # OPERACIÓN 2
    # Cliente inválido
    # =====================================================

    try:

        cliente2 = Cliente(
            2,
            "Pedro123",
            "correo_mal"
        )

        print(cliente2.mostrar_info())

    except Exception as e:

        print(e)
        registrar_log(f"Error operación 2: {e}")

    # =====================================================
    # OPERACIÓN 3
    # Servicio válido
    # =====================================================

    try:

        servicio1 = ReservaSala(
            "Sala VIP",
            100
        )

        servicios.append(servicio1)

        print(servicio1.descripcion())

    except Exception as e:

        print(e)
        registrar_log(f"Error operación 3: {e}")

    # =====================================================
    # OPERACIÓN 4
    # Servicio inválido
    # =====================================================

    try:

        servicio2 = AlquilerEquipo(
            "",
            -50
        )

        print(servicio2.descripcion())

    except Exception as e:

        print(e)
        registrar_log(f"Error operación 4: {e}")

    # =====================================================
    # OPERACIÓN 5
    # Reserva válida
    # =====================================================

    try:

        reserva1 = Reserva(
            cliente1,
            servicio1,
            3
        )

        reservas.append(reserva1)

        print(
            reserva1.mostrar_reserva()
        )

    except Exception as e:

        print(e)
        registrar_log(f"Error operación 5: {e}")

    # =====================================================
    # OPERACIÓN 6
    # Confirmar reserva
    # =====================================================

    try:

        print(
            reserva1.confirmar_reserva()
        )

    except Exception as e:

        print(e)
        registrar_log(f"Error operación 6: {e}")

    # =====================================================
    # OPERACIÓN 7
    # Cancelar reserva
    # =====================================================

    try:

        print(
            reserva1.cancelar_reserva()
        )

    except Exception as e:

        print(e)
        registrar_log(f"Error operación 7: {e}")

    # =====================================================
    # OPERACIÓN 8
    # Procesar reserva cancelada
    # =====================================================

    try:

        print(
            reserva1.procesar_reserva()
        )

    except Exception as e:

        print(e)
        registrar_log(f"Error operación 8: {e}")

    # =====================================================
    # OPERACIÓN 9
    # Asesoría válida
    # =====================================================

    try:
        
        servicio3 = Asesoria(
            "Consultoria",
            200
            )
        
        servicios.append(servicio3)

        print(
            servicio3.descripcion()
            )
        
        costo = servicio3.calcular_costo(
            2,
            impuesto=0.19,
            descuento=0.1
            )

    except Exception as e:

        print(e)
        registrar_log(f"Error operación 9: {e}")

    else:

        print(
            f"Costo calculado correctamente: ${costo}"
            )

        registrar_log(
            "Operación 9 ejecutada exitosamente"
            )

    # =====================================================
    # OPERACIÓN 10
    # Reserva inválida
    # =====================================================

    try:

        reserva2 = Reserva(
            cliente,
            servicio3,
            -5
        )

        print(
            reserva2.mostrar_reserva()
        )

    except Exception as e:

        print(e)
        registrar_log(f"Error operación 10: {e}")

    registrar_log("===== FIN DEL SISTEMA =====")


# =========================================================
# EJECUCIÓN PRINCIPAL
# =========================================================

if __name__ == "__main__":

    ejecutar_pruebas()

 