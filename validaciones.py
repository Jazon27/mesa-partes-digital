def validar_texto_obligatorio(texto):
    return bool(texto.strip())

def validar_dni(dni):
    return dni.isdigit() and len(dni) == 8

def validar_celular(celular):
    return celular.isdigit() and len(celular) == 9

def validar_correo(correo):
    return correo.count("@") == 1 and "." in correo.split("@")[1]

def validar_datos(nombre, dni, celular, correo, asunto):
    if not validar_texto_obligatorio(nombre) or not validar_texto_obligatorio(asunto):
        return False, "El nombre y el asunto no pueden estar vacíos."
    if not validar_dni(dni):
        return False, "El DNI debe tener exactamente 8 dígitos."
    if not validar_celular(celular):
        return False, "El celular debe tener exactamente 9 dígitos."
    if not validar_correo(correo):
        return False, "El correo electrónico no es válido."
    return True, "Datos correctos."
