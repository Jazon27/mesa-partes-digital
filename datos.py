import csv
import os


def cargar_csv(nombre_archivo):
    codigos = []
    nombres = []
    dnis = []
    celulares = []
    correos = []
    asuntos = []

    if not os.path.exists(nombre_archivo):
        return codigos, nombres, dnis, celulares, correos, asuntos

    with open(nombre_archivo, mode="r", newline="", encoding="utf-8") as archivo:
        lector = csv.reader(archivo)
        next(lector, None)  # Salta la fila de encabezados
        for fila in lector:
            if len(fila) == 6:
                codigos.append(fila[0])
                nombres.append(fila[1])
                dnis.append(fila[2])
                celulares.append(fila[3])
                correos.append(fila[4])
                asuntos.append(fila[5])

    return codigos, nombres, dnis, celulares, correos, asuntos


def guardar_csv(nombre_archivo, codigos, nombres, dnis, celulares, correos, asuntos):
    with open(nombre_archivo, mode="w", newline="", encoding="utf-8") as archivo:
        escritor = csv.writer(archivo)
        escritor.writerow(["codigo", "nombre", "dni", "celular", "correo", "asunto"])
        for i in range(len(codigos)):
            escritor.writerow([
                codigos[i],
                nombres[i],
                dnis[i],
                celulares[i],
                correos[i],
                asuntos[i]
            ])