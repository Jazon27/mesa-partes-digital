def validar_texto_obligatorio(texto):
    return bool(texto.strip())


def validar_dni(dni):
    return dni.isdigit() and len(dni) == 8


def validar_celular(celular):
    return celular.isdigit() and len(celular) == 9


def validar_correo(correo):
    correo = correo.strip()
    if " " in correo or correo.count("@") != 1:
        return False
    usuario, dominio = correo.split("@")
    if not usuario or "." not in dominio:
        return False
    return all(dominio.split("."))


def validar_datos(nombre, dni, celular, correo, asunto):
    if not validar_texto_obligatorio(nombre):
        return False, "El nombre no puede estar vacío."
    if not validar_dni(dni):
        return False, "El DNI debe tener exactamente 8 dígitos."
    if not validar_celular(celular):
        return False, "El celular debe tener exactamente 9 dígitos."
    if not validar_correo(correo):
        return False, "El correo electrónico no es válido."
    if not validar_texto_obligatorio(asunto):
        return False, "El asunto no puede estar vacío."
    return True, "Datos correctos."
