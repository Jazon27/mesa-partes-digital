def extraer_numero_codigo(codigo):
    try:
        parte_numerica = codigo.strip().upper().replace("EXP-", "")
        return int(parte_numerica)
    except ValueError:
        return 0


def ordenar_listas_por_codigo(codigos, nombres, dnis, celulares, correos, asuntos):
    """Ordena las 6 listas paralelas de forma ascendente (necesario para búsqueda binaria)."""
    total = len(codigos)
    for i in range(total - 1):
        for j in range(total - 1 - i):
            num_actual = extraer_numero_codigo(codigos[j])
            num_siguiente = extraer_numero_codigo(codigos[j + 1])
            if num_actual > num_siguiente:
                codigos[j], codigos[j + 1] = codigos[j + 1], codigos[j]
                nombres[j], nombres[j + 1] = nombres[j + 1], nombres[j]
                dnis[j], dnis[j + 1] = dnis[j + 1], dnis[j]
                celulares[j], celulares[j + 1] = celulares[j + 1], celulares[j]
                correos[j], correos[j + 1] = correos[j + 1], correos[j]
                asuntos[j], asuntos[j + 1] = asuntos[j + 1], asuntos[j]


def busqueda_binaria(codigos, codigo_buscado):
    """Busca un expediente por código usando búsqueda binaria. Devuelve el índice o -1."""
    objetivo = extraer_numero_codigo(codigo_buscado)
    if objetivo == 0:
        return -1

    izquierda = 0
    derecha = len(codigos) - 1

    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        valor_medio = extraer_numero_codigo(codigos[medio])

        if valor_medio == objetivo:
            return medio
        elif valor_medio < objetivo:
            izquierda = medio + 1
        else:
            derecha = medio - 1

    return -1


def mostrar_expediente(indice, codigos, nombres, dnis, celulares, correos, asuntos):
    print("\n" + "=" * 45)
    print(f" DETALLE DEL EXPEDIENTE: {codigos[indice]}")
    print("=" * 45)
    print(f"  Código  : {codigos[indice]}")
    print(f"  Nombre  : {nombres[indice]}")
    print(f"  DNI     : {dnis[indice]}")
    print(f"  Celular : {celulares[indice]}")
    print(f"  Correo  : {correos[indice]}")
    print(f"  Asunto  : {asuntos[indice]}")
    print("=" * 45 + "\n")


def ordenar_expedientes(codigos, nombres, dnis, celulares, correos, asuntos):
    """Lista los expedientes en orden descendente (del más reciente al más antiguo)."""
    total = len(codigos)
    if total == 0:
        print("\n[Aviso] No hay expedientes registrados para mostrar.\n")
        return

    indices = list(range(total))
    for i in range(total - 1):
        for j in range(total - 1 - i):
            num_actual = extraer_numero_codigo(codigos[indices[j]])
            num_siguiente = extraer_numero_codigo(codigos[indices[j + 1]])
            if num_actual < num_siguiente:
                indices[j], indices[j + 1] = indices[j + 1], indices[j]

    print("\n" + "=" * 75)
    print(" LISTADO DE EXPEDIENTES (ORDEN DESCENDENTE POR CÓDIGO)")
    print("=" * 75)
    print(f"{'CÓDIGO':<10} | {'DNI':<10} | {'SOLICITANTE':<25} | {'ASUNTO'}")
    print("-" * 75)

    for idx in indices:
        print(f"{codigos[idx]:<10} | {dnis[idx]:<10} | {nombres[idx][:25]:<25} | {asuntos[idx]}")

    print("=" * 75 + "\n")
