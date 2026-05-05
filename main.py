from models.cliente import Cliente


try:
    c = Cliente(1, "Juan123", "correo_mal")
except Exception as e:
    print(e)

    