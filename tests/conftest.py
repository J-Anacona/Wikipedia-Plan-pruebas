"""Fixtures compartidas: sesión con User-Agent y pausa entre peticiones."""
import time

import pytest
import requests

from comun import USER_AGENT

PAUSA_SEGUNDOS = 1.0  # pocas peticiones: como máximo una por segundo


@pytest.fixture(scope="session")
def sesion():
    if "[correo]" in USER_AGENT:
        pytest.exit("Completa tu correo en USER_AGENT (tests/comun.py) antes de ejecutar.")
    s = requests.Session()
    s.headers.update({"User-Agent": USER_AGENT, "Accept": "application/json"})
    return s


@pytest.fixture(autouse=True)
def pausa():
    yield
    time.sleep(PAUSA_SEGUNDOS)
