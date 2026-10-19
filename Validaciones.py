def validar_datos(nombre, dni, celular, correo, asunto):
    if not nombre.strip() or not asunto.strip():
        return False, "El nombre y el asunto no pueden estar vacíos."
    if not dni.isdigit() or len(dni) != 8:
        return False, "El DNI debe tener exactamente 8 dígitos."
    if not celular.isdigit() or len(celular) != 9:
        return False, "El celular debe tener exactamente 9 dígitos."
    if "@" not in correo or "." not in correo:
        return False, "El correo electrónico no es válido."
    return True, "Datos correctos."
