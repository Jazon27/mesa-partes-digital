from consultas import buscar_expediente
nombres_lista = []
dni_lista = []
celular_lista = []
correo_lista = []
asunto_lista = []
codigos_lista = []

print("MESA DE PARTES DIGITAL")

while True:
    print("\n[MENU PRINCIPAL]")
    print("1. Registrar expediente")
    print("2. Buscar expediente")
    print("3. Ver expedientes guardados")
    print("4. Salir")

    opcion = input("Elige una opción (1-4): ")

    if opcion == "1":
        print("\n--- REGISTRO ---")
        nombre = input("Nombres y apellidos: ")

        dni = input("DNI (8 dígitos): ")
        while len(dni) != 8 or not dni.isdigit():
            print("Error: El DNI debe tener exactamente 8 números.")
            dni = input("Ingrese un DNI valido (8 dígitos): ")

        celular = input("Celular (9 dígitos): ")
        while len(celular) != 9 or not celular.isdigit():
            print("Error: El celular debe tener exactamente 9 números.")
            celular = input("Ingrese un celular valido (9 dígitos): ")

        correo = input("Correo electronico: ")
        asunto = input("Asunto del trámite: ")

        codigo = "EXP-" + str(len(codigos_lista) + 1)

        nombres_lista.append(nombre)
        dni_lista.append(dni)
        celular_lista.append(celular)
        correo_lista.append(correo)
        asunto_lista.append(asunto)
        codigos_lista.append(codigo)

        print(f"¡Registrado con éxito! Tu código es: {codigo}")

    
    elif opcion == "2":
        print("\n------- Búsqueda de Expediente -------")
        print("Ingrese el código del expediente o DNI:")
        print("Código (EXP-1)")
        print("DNI (71234567)")

        buscar = input("Buscar: ").strip()
        encontrados = []
        encontrados = buscar_expediente(
            buscar,
            codigos_lista,
            nombres_lista,
            dni_lista,
            celular_lista,
            correo_lista,
            asunto_lista
            )

        if len(encontrados) == 0:
            print("\nNo se encontro ningun expediente.")
        else:
            print(f"\nSe encontraron {len(encontrados)} expediente(s):")
            print("-" * 30)

            for i in encontrados:
                print(f"Código:  {codigos_lista[i]}")
                print(f"Nombre:  {nombres_lista[i]}")
                print(f"DNI:     {dni_lista[i]}")
                print(f"Celular: {celular_lista[i]}")
                print(f"Correo:  {correo_lista[i]}")
                print(f"Asunto:  {asunto_lista[i]}")

                if i != encontrados[-1]:
                    print("-" * 30)

            print("-" * 30)
        input("\nPresione enter para ir al menu principal...")

    elif opcion == "3":
        print("\n--- LISTA DE EXPEDIENTES ---")
        if len(codigos_lista) == 0:
            print("No hay expedientes registrados.")
        else:
            for i in range(len(codigos_lista) - 1, -1, -1):
                print(f"[{codigos_lista[i]}] - {nombres_lista[i]} | Asunto: {asunto_lista[i]}")
            
    elif opcion == "4":
        print("Saliendo del programa...")
        break

    else:
        print("Opción inválida. Intenta del 1 al 4.")
