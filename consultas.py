from dataclasses import dataclass
from difflib import SequenceMatcher
import re
from typing import Iterable, Sequence


@dataclass(frozen=True)
class ResultadoExpediente:
    indice: int
    codigo: str
    nombre: str
    dni: str
    celular: str
    correo: str
    asunto: str
    puntaje: float
    criterio: str


_PATRON_CODIGO = re.compile(r"^EXP-[A-Z0-9]{2,}(?:-[A-Z0-9]+)*$")
_PATRON_DNI = re.compile(r"^\d{8}$")


def _validar_integridad_paralela(*listas: Sequence[object]) -> int:
    longitudes = {len(lst) for lst in listas}
    if len(longitudes) != 1:
        raise ValueError(
            f"Las listas paralelas tienen longitudes inconsistentes: {sorted(longitudes)}"
        )
    return longitudes.pop()


def _similitud_normalizada(consulta: str, objetivo: str) -> float:
    consulta_norm = " ".join(consulta.lower().split())
    objetivo_norm = " ".join(objetivo.lower().split())
    if not consulta_norm or not objetivo_norm:
        return 0.0
    if consulta_norm in objetivo_norm:
        return 0.85 + (len(consulta_norm) / max(len(objetivo_norm), 1)) * 0.14
    return SequenceMatcher(None, consulta_norm, objetivo_norm).ratio() * 0.8


def buscar_expediente_avanzado(
    buscar: str,
    codigos_lista: Sequence[str],
    nombres_lista: Sequence[str],
    dni_lista: Sequence[str],
    celular_lista: Sequence[str],
    correo_lista: Sequence[str],
    asunto_lista: Sequence[str],
    *,
    umbral_difuso: float = 0.65,
    permitir_busqueda_texto: bool = True,
) -> list[ResultadoExpediente]:
    """
    Busca expedientes por código ('EXP-...'), DNI (8 dígitos) o coincidencia
    aproximada en nombre/asunto, devolviendo resultados ordenados por relevancia.
    """
    total = _validar_integridad_paralela(
        codigos_lista,
        nombres_lista,
        dni_lista,
        celular_lista,
        correo_lista,
        asunto_lista,
    )

    termino = buscar.strip()
    if not termino:
        return []

    termino_upper = termino.upper()
    es_codigo = bool(_PATRON_CODIGO.match(termino_upper))
    es_dni = bool(_PATRON_DNI.match(termino))

    if termino.isdigit() and not es_dni:
        raise ValueError("El DNI debe tener exactamente 8 dígitos numéricos.")

    if termino_upper.startswith("EXP-") and not es_codigo:
        raise ValueError(
            "Formato de código inválido. Use un formato como 'EXP-2026-001' o 'EXP-A1B2'."
        )

    coincidencias: list[ResultadoExpediente] = []

    for i in range(total):
        codigo_actual = str(codigos_lista[i]).strip().upper()
        dni_actual = str(dni_lista[i]).strip()
        nombre_actual = str(nombres_lista[i]).strip()
        asunto_actual = str(asunto_lista[i]).strip()

        puntaje = 0.0
        criterio = ""

        if es_codigo and codigo_actual == termino_upper:
            puntaje = 1.0
            criterio = "codigo_exacto"
        elif es_dni and dni_actual == termino:
            puntaje = 0.99
            criterio = "dni_exacto"
        elif permitir_busqueda_texto and not (es_codigo or es_dni):
            sim_nombre = _similitud_normalizada(termino, nombre_actual)
            sim_asunto = _similitud_normalizada(termino, asunto_actual)
            if sim_nombre >= sim_asunto and sim_nombre >= umbral_difuso:
                puntaje = round(sim_nombre, 4)
                criterio = "nombre_aproximado"
            elif sim_asunto > sim_nombre and sim_asunto >= umbral_difuso:
                puntaje = round(sim_asunto, 4)
                criterio = "asunto_aproximado"

        if criterio:
            coincidencias.append(
                ResultadoExpediente(
                    indice=i,
                    codigo=codigos_lista[i],
                    nombre=nombres_lista[i],
                    dni=dni_lista[i],
                    celular=celular_lista[i],
                    correo=correo_lista[i],
                    asunto=asunto_lista[i],
                    puntaje=puntaje,
                    criterio=criterio,
                )
            )

    coincidencias.sort(key=lambda item: (-item.puntaje, item.indice))
    return coincidencias
