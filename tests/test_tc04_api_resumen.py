
from urllib.parse import quote

import pytest

from comun import BASE, guardar_evidencia

CASO = "TC-04"
ENDPOINT = BASE + "/api/rest_v1/page/summary/{titulo}"
CAMPOS = ("type", "title", "lang", "extract", "content_urls")

# Un título por clase. Verifica cada uno en el navegador antes de usarlo.
TITULOS = {
    "existente": "Colombia",
    "redireccion": "Estados Unidos de América",     
    "desambiguacion": "Mercurio",   
    "inexistente": "Zzxqv_titulo_que_no_existe_2026",
}


def pedir(sesion, titulo, **params):
    url = ENDPOINT.format(titulo=quote(titulo, safe=""))
    return sesion.get(url, params=params, timeout=15)


def titulo_o_omitir(clase):
    titulo = TITULOS[clase]
    if titulo is None:
        pytest.skip(f"Falta elegir y verificar a mano el título de la clase '{clase}'.")
    return titulo


def test_titulo_existente(sesion):
    r = pedir(sesion, TITULOS["existente"])
    guardar_evidencia(CASO, "existente", r)
    assert r.status_code == 200
    assert "json" in r.headers["Content-Type"]
    datos = r.json()
    for campo in CAMPOS:
        assert campo in datos, f"Falta el campo '{campo}' en la respuesta"
    assert datos["type"] == "standard"
    assert datos["lang"] == "es"
    assert datos["extract"].strip() != ""


def test_titulo_con_redireccion(sesion):
    titulo = titulo_o_omitir("redireccion")
    # La API resuelve la redirección por dentro y responde 200 con el artículo destino.
    r = pedir(sesion, titulo)
    guardar_evidencia(CASO, "redireccion", r)
    assert r.status_code == 200
    datos = r.json()
    if datos["titles"]["canonical"] == titulo.replace(" ", "_"):
        pytest.skip("El título elegido no es una redirección: elige otro.")
    assert datos["titles"]["canonical"] != titulo.replace(" ", "_")
    # Con redirect=false la documentación indica que responde 200 sin redirigir.
    r2 = pedir(sesion, titulo, redirect="false")
    guardar_evidencia(CASO, "redireccion-sin-seguir", r2)
    assert r2.status_code == 200
    assert not r2.history


def test_titulo_de_desambiguacion(sesion):
    titulo = titulo_o_omitir("desambiguacion")
    r = pedir(sesion, titulo)
    guardar_evidencia(CASO, "desambiguacion", r)
    assert r.status_code == 200
    assert r.json()["type"] == "disambiguation"


def test_titulo_inexistente(sesion):
    r = pedir(sesion, TITULOS["inexistente"])
    guardar_evidencia(CASO, "inexistente", r)
    assert r.status_code == 404
    assert "json" in r.headers["Content-Type"]
    assert "extract" not in r.json()
