
from exceptions.custom_exceptions import ReservaError
from utils.logger import registrar_log


class Reserva:

    def __init__(self, cliente, servicio, duracion):

        self.cliente = cliente
        self.servicio = servicio
        self.duracion = duracion
        self.estado = "Pendiente"

    def confirmar_reserva(self):

        try:

            if self.estado == "Cancelada":
                raise ReservaError(
                    "No se puede confirmar una reserva cancelada"
                )

            self.estado = "Confirmada"

            registrar_log(
                f"Reserva confirmada para {self.cliente.nombre}"
            )

            return "Reserva confirmada correctamente"

        except Exception as e:

            registrar_log(f"ERROR AL CONFIRMAR RESERVA: {e}")

            return f"Error: {e}"

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
                    "La duración de la reserva debe ser mayor a cero"
                )

            costo = self.servicio.calcular_costo()

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

    def mostrar_info(self):

        return (
            f"Cliente: {self.cliente.nombre}\n"
            f"Servicio: {self.servicio.nombre}\n"
            f"Duración: {self.duracion}\n"
            f"Estado: {self.estado}"
        )

