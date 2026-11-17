
import pytest

from comun import BASE, guardar_evidencia

CASO = "TC-08"
API = BASE + "/w/api.php"
LIMITE_MAXIMO = 500
ESPECIALES = {
    "tildes-enie": "áéíóú ñ",
    "simbolos": "&=?#%",
    "html": "<b>negrita</b>",
    "comillas": "\"dobles\" y 'simples'",
    "unicode": "日本語",
    "emoji": "😀",
}


def buscar(sesion, texto, **extra):
    params = {"action": "opensearch", "search": texto, "format": "json", **extra}
    return sesion.get(API, params=params, timeout=15)


def json_sin_fallo_de_servidor(r):
    assert r.status_code < 500, f"Error de servidor: {r.status_code}"
    return r.json()  # lanza error si el cuerpo no es JSON válido


def test_consulta_con_resultados(sesion):
    r = buscar(sesion, "Colombia")
    guardar_evidencia(CASO, "con-resultados", r)
    assert r.status_code == 200
    datos = r.json()
    assert isinstance(datos, list) and len(datos) == 4
    assert datos[0] == "Colombia"
    assert 1 <= len(datos[1]) <= 10  # 10 es el valor por defecto de limit


def test_consulta_vacia(sesion):
    r = buscar(sesion, "")
    guardar_evidencia(CASO, "vacia", r)
    datos = json_sin_fallo_de_servidor(r)
    assert isinstance(datos, (list, dict))


@pytest.mark.parametrize("texto", ESPECIALES.values(), ids=ESPECIALES.keys())
def test_caracteres_especiales(sesion, texto):
    r = buscar(sesion, texto)
    nombre = "especial-" + next(k for k, v in ESPECIALES.items() if v == texto)
    guardar_evidencia(CASO, nombre, r)
    datos = json_sin_fallo_de_servidor(r)
    if isinstance(datos, list):
        assert len(datos) == 4
        assert datos[0] == texto


@pytest.mark.parametrize("limite", [0, 1, 2, 500, 501], ids=lambda n: f"limit-{n}")
def test_valores_limite_de_cantidad(sesion, limite):
    r = buscar(sesion, "Co", limit=limite)
    guardar_evidencia(CASO, f"limit-{limite}", r)
    datos = json_sin_fallo_de_servidor(r)
    if isinstance(datos, list):
        titulos = datos[1]
        assert len(titulos) <= LIMITE_MAXIMO
        if limite in (1, 2, 500):
            assert len(titulos) <= limite
        if limite == 1:
            assert len(titulos) == 1
