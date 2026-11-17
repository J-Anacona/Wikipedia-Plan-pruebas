# Pruebas automatizadas (TC-04 y TC-08)

Scripts de los dos casos automatizados del plan de pruebas de Wikipedia en español.

| Caso | Archivo | Responsable |
| --- | --- | --- |
| TC-04 API de resumen de página | `test_tc04_api_resumen.py` | A |
| TC-08 API de búsqueda | `test_tc08_api_busqueda.py` | B |

`comun.py` y `conftest.py` son compartidos (entorno y User-Agent).

## Antes de ejecutar

1. Instala Python 3 y las librerías: `pip install -r tests/requirements.txt`
2. En `tests/comun.py` reemplaza `[correo]` por tu correo en `USER_AGENT`.
3. En `test_tc04_api_resumen.py` completa los títulos `redireccion` y `desambiguacion`.
   Verifícalos a mano en el navegador (es.wikipedia.org). Mientras sean `None`, esos
   dos casos se omiten.
4. Verifica la documentación vigente de las APIs (ver el plan, sección 5.4).

## Ejecutar (desde la raíz del repositorio)

```
pytest tests/test_tc04_api_resumen.py -v --junitxml=evidencias/TC-04/junit.xml
pytest tests/test_tc08_api_busqueda.py -v --junitxml=evidencias/TC-08/junit.xml
```

Cada petición guarda un `.json` en `evidencias/TC-04/` o `evidencias/TC-08/` con la
fecha, la URL, el estado y el cuerpo (recortado). Se hace una petición por segundo
como máximo. Una prueba fallida no siempre es un defecto de Wikipedia: revisa primero
que el dato de entrada sea válido.
