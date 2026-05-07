from models.servicio import Servicio
from exceptions.custom_exceptions import ServicioError

#-----------------------------------------------------
#Servicio 1: Reserva de Salas
#-----------------------------------------------------

class ReservaSala(Servicio):
    def calcular_costo(self, horas, impuesto=0, descuento=0):
        
        if horas <=0:
            raise ServicioError("Las horas deben ser mayores que cero")
        costo = self.precio_base * horas

        #Aplicar impuesto
        costo += costo * impuesto

        #Aplicar descuento
        costo -= costo * descuento

        return costo
    
    def descripcion(self):
        return f"Servicio de reserva de sala:{self.nombre}"
    

# =========================================================
# SERVICIO 2: ALQUILER DE EQUIPOS
# =========================================================

class AlquilerEquipo(Servicio):

    def calcular_costo(self, dias, impuesto=0, descuento=0):

        if dias <= 0:
            raise ServicioError("Los días deben ser mayores que cero")

        costo = self.precio_base * dias

        costo += costo * impuesto
        costo -= costo * descuento

        return costo

    def descripcion(self):
        return f"Servicio de alquiler de equipos: {self.nombre}"


# =========================================================
# SERVICIO 3: ASESORÍAS ESPECIALIZADAS
# =========================================================

class Asesoria(Servicio):

    def calcular_costo(self, horas, impuesto=0, descuento=0):

        if horas <= 0:
            raise ServicioError("Las horas deben ser mayores que cero")

        # Asesoría tiene recargo especial
        costo = (self.precio_base * horas) * 1.2

        costo += costo * impuesto
        costo -= costo * descuento

        return costo

    def descripcion(self):
        return f"Servicio de asesoría especializada: {self.nombre}"