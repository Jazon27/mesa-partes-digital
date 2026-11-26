def limpiar_texto(texto):
    return " ".join(texto.split())


def validar_texto_obligatorio(texto):
    return bool(texto.strip())


def validar_nombre(nombre):
    nombre = limpiar_texto(nombre)
    if len(nombre.split()) < 2 or len(nombre) < 5 or len(nombre) > 60:
        return False
    for caracter in nombre:
        if not (caracter.isalpha() or caracter in " '-"):
            return False
    return True


def validar_dni(dni):
    return dni.isascii() and dni.isdigit() and len(dni) == 8


def validar_celular(celular):
    return celular.isascii() and celular.isdigit() and len(celular) == 9


def validar_correo(correo):
    correo = correo.strip()
    if " " in correo or ".." in correo or correo.count("@") != 1:
        return False
    usuario, dominio = correo.split("@")
    if not usuario or "." not in dominio:
        return False
    if usuario.startswith(".") or usuario.endswith("."):
        return False
    partes_dominio = dominio.split(".")
    if not all(partes_dominio):
        return False
    return partes_dominio[-1].isalpha() and len(partes_dominio[-1]) >= 2


def validar_asunto(asunto):
    asunto = limpiar_texto(asunto)
    if len(asunto) < 5 or len(asunto) > 200:
        return False
    return any(caracter.isalpha() for caracter in asunto)


def validar_codigo(codigo):
    codigo = codigo.strip().upper()
    if not codigo.startswith("EXP-"):
        return False
    numero = codigo[4:]
    return numero.isascii() and numero.isdigit() and int(numero) > 0


def obtener_errores(nombre, dni, celular, correo, asunto):
    errores = []
    if not validar_texto_obligatorio(nombre):
        errores.append("El nombre no puede estar vacío.")
    elif not validar_nombre(nombre):
        errores.append("El nombre debe tener nombres y apellidos, solo con letras.")
    if not validar_dni(dni):
        errores.append("El DNI debe tener exactamente 8 dígitos.")
    if not validar_celular(celular):
        errores.append("El celular debe tener exactamente 9 dígitos.")
    if not validar_correo(correo):
        errores.append("El correo electrónico no es válido.")
    if not validar_texto_obligatorio(asunto):
        errores.append("El asunto no puede estar vacío.")
    elif not validar_asunto(asunto):
        errores.append("El asunto debe tener entre 5 y 200 caracteres y contener letras.")
    return errores


def validar_datos(nombre, dni, celular, correo, asunto):
    errores = obtener_errores(nombre, dni, celular, correo, asunto)
    if errores:
        return False, "\n".join(errores)
    return True, "Datos correctos."
