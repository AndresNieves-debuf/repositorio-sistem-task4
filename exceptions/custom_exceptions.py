class ClienteError(Exception):
    """
    Excepción para errores relacionados con clientes
    """
    pass


class ServicioError(Exception):
    """
    Excepción para errores relacionados con servicios
    """
    pass


class ReservaError(Exception):
    """
    Excepción para errores relacionados con reservas
    """
    pass


class ProcesamientoError(Exception):
    """
    Excepción para errores generales del sistema
    """
    pass