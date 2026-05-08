def registrar_log(mensaje):

    with open("data/logs.txt", "a", encoding="utf-8") as archivo:
        archivo.write(f"{mensaje}\n")