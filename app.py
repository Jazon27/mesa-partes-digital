from validaciones import (validar_texto_obligatorio, 
validar_dni, 
validar_celular, 
validar_correo)
from datos import cargar_csv, guardar_csv
from consultas import (
    ordenar_listas_por_codigo,
    busqueda_binaria,
    mostrar_expediente,
    ordenar_expedientes,
    extraer_numero_codigo
)

archivo_datos = "expedientes.csv"


def siguiente_codigo(codigos):
    if len(codigos) == 0:
        return "EXP-1"
    mayor = extraer_numero_codigo(codigos[-1])
    return f"EXP-{mayor + 1}"


def registrar_expediente(codigos, nombres, dnis, celulares, correos, asuntos):
    print("Registro de nuevo expediente")
while True:
        nombre = input("Nombres y apellidos: ").strip()
        if validar_texto_obligatorio(nombre):
            break
        print("Error: El nombre no puede estar vacío.")
        
    while True:
        dni = input("DNI (8 dígitos): ").strip()
        if validar_dni(dni):
            break
        print("Error: El DNI debe tener exactamente 8 dígitos.")

    while True:
        celular = input("Celular (9 dígitos): ").strip()
        if validar_celular(celular):
            break
        print("Error: El celular debe tener exactamente 9 dígitos.")

    while True:
        correo = input("Correo electrónico: ").strip()
        if validar_correo(correo):
            break
        print("Error: El correo electrónico no es válido.")

    while True:
        asunto = input("Asunto del trámite: ").strip()
        if validar_texto_obligatorio(asunto):
            break
        print("Error: El asunto no puede estar vacío.")

    codigo = siguiente_codigo(codigos)
    codigos.append(codigo)
    nombres.append(nombre)
    dnis.append(dni)
    celulares.append(celular)
    correos.append(correo)
    asuntos.append(asunto)

    ordenar_listas_por_codigo(codigos, nombres, dnis, celulares, correos, asuntos)
    guardar_csv(archivo_datos, codigos, nombres, dnis, celulares, correos, asuntos)
    print(f"Expediente registrado con éxito. Código asignado: {codigo}")


def mostrar_menu():
    print("\n   MESA DE PARTES DIGITAL - EL AGUSTINO")
    print("1. Registro de nuevo expediente")
    print("2. Buscar expediente")
    print("3. Ver expedientes ordenados (mayor a menor)")
    print("4. Salir y guardar cambios")


def main():
    codigos, nombres, dnis, celulares, correos, asuntos = cargar_csv(archivo_datos)
    ordenar_listas_por_codigo(codigos, nombres, dnis, celulares, correos, asuntos)

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            registrar_expediente(codigos, nombres, dnis, celulares, correos, asuntos)
        elif opcion == "2":
            buscado = input("Ingrese el código del expediente: ").strip()
            pos = busqueda_binaria(codigos, buscado)
            if pos != -1:
                mostrar_expediente(pos, codigos, nombres, dnis, celulares, correos, asuntos)
            else:
                print("Expediente no encontrado.")
        elif opcion == "3":
            ordenar_expedientes(codigos, nombres, dnis, celulares, correos, asuntos)
        elif opcion == "4":
            guardar_csv(archivo_datos, codigos, nombres, dnis, celulares, correos, asuntos)
            print("Cambios guardados. Muchas gracias.")
            break
        else:
            print("Opción inválida. Intente nuevamente.")


if __name__ == "__main__":
    main()