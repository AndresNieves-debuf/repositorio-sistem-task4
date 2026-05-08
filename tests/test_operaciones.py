from models.cliente import Cliente
from models.servicio_especificos import ReservaSala

def test_cliente_valido():
    cliente = Cliente(
        1,
        "Juan Perez",
        "juan@email.com"
    )
    assert cliente.id == 1
    assert cliente.nombre == "Juan Perez"
    assert cliente.email == "juan@email.com"

    def test_servicio_valido():
        servicio = ReservaSala(
            "Sala VIP",
            100
            )
        assert servicio.nombre == "Sala VIP"
        assert servicio.costo == 100