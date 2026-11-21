CURSO: Fundamento de programación

DOCENTE: DANNY MANUEL HERRERA NAJAR

INTEGRANTES: JEISON JAIR CHANTA SOLANO, DAVID SEBASTIAN LOPE LEGUIA, ERICK YOSHIMAR LOPEZ VELAZCO, JUAN DANIEL TUCTO VARGAS

Resumen:

Tras la visita de campo del 7 de octubre de 2026 y la respuesta oficial de la Oficina de Trámite Documentario y Archivo Central (Carta N.º 00071-2026-OTDAC/MDEA), se determinó que la municipalidad cuenta con un Sistema de Gestión Documental, pero enfrenta errores materiales de digitación en ventanilla (en nombres, DNI, celular, dirección y correo electrónico) y demoras por solicitudes incompletas o ilegibles.

Para solucionar el problema se escogió la alternativa dos, "Sistema modular en Python con ordenamiento y búsqueda binaria" que valide formatos antes de guardar, mantenga los registros ordenados numéricamente por código (EXP-n), permita realizar consultas rápidas mediante búsqueda binaria, liste los expedientes de mayor a menor y garantice la persistencia de datos en el expediente.csv 

El sistema aplica teoría de conjuntos y cardinalidad (DNI de 8 dígitos y celular de 9), lógica proposicional para bloquear registros inválidos, descomposición Entrada, Proceso, Salida : IPO y eficiencia algorítmica logarítmica Olog2n en búsqueda binaria reduciendo drásticamente las comparaciones frente a una búsqueda secuencial lineal

Partes del Git hub

app.py — Chanta Solano Jeison Jair (Menú, registro e integración)

validacion.py — Lopez Velazco Erick (Filtros de campos obligatorios, DNI, celular y correo)

datos.py — Lope Leguía David (Carga y guardado en expedientes.csv)

consultas.py — Tucto Vargas Juan Daniel (Ordenamiento sincronizado, búsqueda binaria y listado descendente)

expedientes.csv — Archivo de datos (Se crea automático o lo suben con los 3 registros de prueba)
README.md — Documentación del repositorio
