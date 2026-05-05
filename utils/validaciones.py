import re

def validar_nombre(nombre):
    if not nombre or not nombre.strip():
        raise ValueError("El nombre no puede estar vacío")
    if any(char.isdigit() for char in nombre):
        raise ValueError("El nombre no debe contener números")
    return nombre.strip()

def validar_email(email):
    if not email or not email.strip():
        raise ValueError("El email no puede estar vacío")
    
    patron = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    if not re.match(patron, email):
        raise ValueError("Formato de email inválido")
    
    return email.strip().lower()



