from Validaciones import validar_datos
from datos import cargar_csv, guardar_csv
from consultas import (
    ordenar_lista_por_codigo,
    busqueda_binaria,
    mostrar_expedientes,
    listar_descendente,
    extraer_numero_codigo
)

archivo_datos = "expedientes.csv"

def siguiente_codigo(codigos):
    if len(codigos)== 0 :
        return "EXP-1"
    mayor = extraer_numero_codigo(codigos[-1])
    return f"EXP-{mayor + 1}"

def registrar_expediente(codigos, nombres, dnis, celulares, correos, asuntos):
    print("Registro de nuevo expediente")
    while True :
        nombre = input("Nombres y apellidos: ").strip()
        dni = input("DNI (8 digitos):").strip()
        celular = input("Celular (9 dígitos): ").strip()
        correo = input("Correo electrónico: ").strip()
        asunto = input("Asunto del trámite: ").strip()
        if validar_datos(nombre, dni, celular, correo, asunto):
            break
        print("Por favor, ingrese datos validos")

        codigo =siguiente_codigo(codigos)
        codigos.append(codigo)
        nombres.append(nombre)
        dnis.append(dni)
        celulares.append(celular)
        correos.append(correo)
        asuntos.append(asunto)
        ordenar_lista_por_codigo(codigos, nombres, dnis, celulares, correos, asuntos)
        guardar_csv(archivo_datos, codigos, nombres, dnis, celulares, correos, asuntos)
        print(f"Expediente Registrado con Exito. Código asignado : {codigo}")


def mostrar_menu():
    print("   MESA DE PARTES DIGITAL - EL AGUSTINO")
    print("1. Registro de nuevo expediente")
    print("2. Mostrar expediente")
    print("3. Ver expedientes ordenados (mayor a menor)")
    print("4. salir y guardar cambios")

def main():
    codigos, nombres, dnis, celulares, correos, asuntos = cargar_csv(archivo_datos)
    ordenar_lista_por_codigo(codigos, nombres, dnis, celulares, correos, asuntos)
    while True:
        mostrar_menu()
        opcion = input("seleccione una opción: ").strip()
        if opcion == "1":
            registrar_expediente(codigos, nombres, dnis, celulares, correos, asuntos)
        elif opcion == "2":
            buscado = input("Ingrese el código del expediente").strip()
            pos = busqueda_binaria(codigos, buscado)
            if pos != -1:
                mostrar_expedientes(pos,codigos, nombres, dnis, celulares, correos, asuntos, pos)
            else:
                print("Expediente no encontrado.")
        elif opcion == "3":
            listar_descendente(codigos, nombres, dnis, celulares, correos, asuntos)
        elif opcion =="4":
            guardar_csv(archivo_datos, codigos, nombres, dnis, celulares, correos, asuntos)
            print("Cambios guardados. Muchas gracias.")
            break
        else:
            print("Opción inválida. Intente nuevamente.")
            
    if __name__ == "__main__":
    main()