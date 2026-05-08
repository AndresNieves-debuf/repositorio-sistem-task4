from datetime import datetime
import os

# Ruta del archivo de logs
LOG_PATH = "data/logs.txt"


def registrar_log(mensaje):

    try:

        # Crear carpeta data si no existe
        os.makedirs("data", exist_ok=True)

        # Abrir archivo y guardar log
        with open(LOG_PATH, "a", encoding="utf-8") as archivo:

            archivo.write(
                f"{datetime.now()} - {mensaje}"
                )
            
    except Exception as e:

        print(
            f"Error al escribir log:{e}"
            )

