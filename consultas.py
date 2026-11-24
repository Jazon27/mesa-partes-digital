def extraer_numero_codigo(codigo):
    
    try:
        parte_numerica = codigo.strip().upper().replace("EXP-", "")
        return int(parte_numerica)
    except ValueError:
        return 0


def buscar_expediente(codigos, codigo_buscado):
    
    codigo_objetivo = codigo_buscado.strip().upper()
    
    for i in range(len(codigos)):
        if codigos[i].strip().upper() == codigo_objetivo:
            return i
            
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
    
    total = len(codigos)
    
    if total == 0:
        print("\n[Aviso] No hay expedientes registrados para mostrar.\n")
        return

    # Se crea una lista de índices [0, 1, 2, ...] para ordenar sin alterar
    # el orden de inserción original ni desincronizar las listas paralelas
    indices = list(range(total))

    # Ordenamiento Burbuja descendente basado en el número de expediente
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
