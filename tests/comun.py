"""Constantes y utilidades comunes de los scripts automatizados (TC-04 y TC-08)."""
import json
from datetime import datetime, timezone
from pathlib import Path

import requests

RAIZ = Path(__file__).resolve().parent.parent
BASE = "https://es.wikipedia.org"  # sitio de prueba (sección 5.4 del plan)

# Wikimedia pide identificar a quien consulta sus APIs: completa tu correo.
USER_AGENT = (
    "PlanPruebasWikipedia/1.0 "
    "(trabajo universitario de Pruebas de Software; contacto:jhon.anacona083@pascualbravo.edu.co) "
    f"python-requests/{requests.__version__}"
)


def guardar_evidencia(caso: str, nombre: str, respuesta: requests.Response) -> None:
    """Guarda en evidencias/<caso>/<nombre>.json lo esencial de una respuesta."""
    carpeta = RAIZ / "evidencias" / caso
    carpeta.mkdir(parents=True, exist_ok=True)
    registro = {
        "fecha_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "url": respuesta.url,
        "estado": respuesta.status_code,
        "content_type": respuesta.headers.get("Content-Type"),
        "redirecciones_seguidas": len(respuesta.history),
        "cuerpo": respuesta.text[:3000],
    }
    (carpeta / f"{nombre}.json").write_text(
        json.dumps(registro, ensure_ascii=False, indent=2), encoding="utf-8"
    )
