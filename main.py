from models.cliente import Cliente


try:
    c = Cliente(1, "Juan123", "correo_mal")
except Exception as e:
    print(e)

    


from models.servicio_especificos import ReservaSala

sala = ReservaSala("Sala VIP", 100)

print(sala.descripcion())

print("Costo normal:",
      sala.calcular_costo(2))

print("Costo con impuesto:",
      sala.calcular_costo(2, impuesto=0.19))

print("Costo con descuento:",
      sala.calcular_costo(2, descuento=0.10))