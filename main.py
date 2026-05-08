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
            "Consultoría",
            200
        )

        print(
            servicio3.descripcion()
        )

        print(
            servicio3.calcular_costo(
                2,
                impuesto=0.19,
                descuento=0.10
            )
        )

    except Exception as e:

        print(e)
        registrar_log(f"Error operación 9: {e}")

    # =====================================================
    # OPERACIÓN 10
    # Reserva inválida
    # =====================================================

    try:

        reserva2 = Reserva(
            cliente1,
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

 