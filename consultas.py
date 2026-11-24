def buscar_expediente(
    buscar,
    codigos_lista,
    nombres_lista,
    dni_lista,
    celular_lista,
    correo_lista,
    asunto_lista,
):
    buscar_upper = buscar.upper()
    es_codigo_valido = buscar_upper.startswith("EXP-") and len(buscar) > 4
    es_dni_valido = len(buscar) == 8 and buscar.isdigit()

    if not (es_codigo_valido or es_dni_valido):
        if buscar.isdigit():
            print("\nEl DNI debe tener 8 dígitos.")
        return []

    return [
        i
        for i, codigo in enumerate(codigos_lista)
        if buscar_upper == codigo.upper() or buscar == dni_lista[i]
    ]
