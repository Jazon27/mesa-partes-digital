def buscar_expediente(buscar, codigos_lista, nombres_lista, dni_lista, celular_lista, correo_lista, asunto_lista):
    encontrados = []
    
    es_codigo_valido = buscar.upper().startswith("EXP-") and len(buscar) != 4 and len(buscar) > 4
    es_dni_valido = len(buscar) == 8 and buscar.isdigit()

    if not es_codigo_valido and not es_dni_valido:
        if buscar.isdigit() and len(buscar) != 8:
            print("\nEl DNI debe tener 8 dígitos.")
        return encontrados
    
    for i in range(len(codigos_lista)):
        codigo_igual = buscar.upper() == codigos_lista[i].upper()
        dni_igual = buscar == dni_lista[i]
        if codigo_igual or dni_igual:
            encontrados.append(i)
    return encontrados