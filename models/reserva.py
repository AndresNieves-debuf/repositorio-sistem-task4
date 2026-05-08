
from exceptions.custom_exceptions import ReservaError
from utils.logger import registrar_log


class Reserva:

    def __init__(self, cliente, servicio, duracion):
         # Validaciones iniciales
        if cliente is None:
            raise ReservaError("La reserva requiere un cliente")

        if servicio is None:
            raise ReservaError("La reserva requiere un servicio")

        if duracion <= 0:
            raise ReservaError("La duración debe ser mayor que cero")

        self.cliente = cliente
        self.servicio = servicio
        self.duracion = duracion
        self.estado = "Pendiente"

        registrar_log(
            f"reserva creada | Cliente:{cliente.nombre} | servicio: {servicio.nombre}"
            )
        
    #-----------------------------------------
    # Confirmar reserva
    #-------------------------------------    

    def confirmar_reserva(self):

        try:

            if self.estado == "Cancelada":
                raise ReservaError(
                    "No se puede confirmar una reserva cancelada"
                )
            
            costo = self.servicio.calcular_costo(self.duracion)
            
            self.estado = "Confirmada"

            registrar_log(
                f"Reserva confirmada para {self.cliente.nombre} | costo: {costo}"
            )

            return costo

        except Exception as e:

            registrar_log(f"ERROR AL CONFIRMAR RESERVA: {e}")

            raise ReservaError(
                "Ocurrio un problema al confirmar la reserva"
                ) from e
        
        finally:
            registrar_log("proceso de confirmación finalizado")

    #-------------------------------------
    # Cancelar reserva
    #-------------------------------------

    def cancelar_reserva(self):

        try:

            if self.estado == "Confirmada":
                raise ReservaError(
                    "No se puede cancelar una reserva confirmada"
                )

            self.estado = "Cancelada"

            registrar_log(
                f"Reserva cancelada para {self.cliente.nombre}"
            )

            return "Reserva cancelada"

        except Exception as e:

            registrar_log(f"ERROR AL CANCELAR RESERVA: {e}")

            return f"Error: {e}"

    def procesar_reserva(self):

        try:

            if self.duracion <= 0:
              raise ReservaError(
        "La duración debe ser mayor a cero"
    )

            costo = self.servicio.calcular_costo(self.duracion)

            self.confirmar_reserva()

            registrar_log(
                f"Reserva procesada exitosamente "
                f"para {self.cliente.nombre}"
            )

            return (
                f"Reserva procesada correctamente. "
                f"Total a pagar: ${costo}"
            )

        except ReservaError as e:

            self.estado = "Cancelada"

            registrar_log(f"ERROR EN RESERVA: {e}")

            return f"Error en la reserva: {e}"

        except Exception as e:

            self.estado = "Cancelada"

            registrar_log(f"ERROR GENERAL: {e}")

            return f"Error inesperado: {e}"

        finally:

            registrar_log(
                f"Finalizó procesamiento de reserva "
                f"para {self.cliente.nombre}"
            )

    # =====================================================
    # MOSTRAR INFORMACIÓN
    # =====================================================

    def mostrar_reserva(self):

        return (
            f"\n========== RESERVA ==========\n"
            f"Cliente : {self.cliente.nombre}\n"
            f"Servicio: {self.servicio.nombre}\n"
            f"Duración: {self.duracion}\n"
            f"Estado  : {self.estado}\n"
            f"============================="
        )

