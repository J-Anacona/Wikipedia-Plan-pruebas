# Plan de Pruebas de Wikipedia en español

Plan y ejecución de pruebas de software sobre **Wikipedia en español** (es.wikipedia.org), basado en la norma **ISO/IEC/IEEE 29119-3** con enfoque de **pruebas basadas en riesgos (RBT)**. Trabajo de la asignatura Pruebas de Software.


## Resumen

- **Objeto de prueba:** ocho funciones sencillas pero importantes de Wikipedia en español, probadas como caja negra y en modo de solo lectura.
- **Enfoque:** cada prueba nace de un riesgo evaluado. La cadena es riesgo → condición de prueba → técnica formal → caso de prueba, con trazabilidad en ambos sentidos.
- **Casos:** 8 casos (4 por integrante): 6 manuales y 2 automatizados.
- **Documentación:** todo en Markdown dentro de `docs/`, con control de versiones en Git.

## Equipo
| Autor | Rol |
| --- | --- |
| Jhon Herney Anacona | Analista y ejecutor de pruebas (TC-01 a TC-04). Líder de documentación: tailoring, matriz de riesgos, trazabilidad e informe de cierre |
| Miguel Ángel Pardo | Analista y ejecutor de pruebas (TC-05 a TC-08). Líder técnico: entorno, datos de prueba, scripts compartidos y PDF final |

- **Docente y auditor:** ROBERTO JOSE CALDERON BERMEJO.

## Sistema bajo prueba y reglas de uso

El sistema probado es la edición en español de Wikipedia, un sitio público de terceros. Por eso:

- Se prueba como **caja negra**, sin acceso al código ni a la infraestructura.
- Todas las pruebas son de **solo lectura**: no se edita ni se guarda nada, y no se crean cuentas ni se usan credenciales reales.
- Los scripts hacen **pocas peticiones** (una por segundo como máximo) y se identifican con un User-Agent.
- No se hacen pruebas de carga, estrés ni seguridad profunda.
- Wikipedia cambia a diario: de cada artículo usado se anotan la fecha, el idioma y el enlace permanente (oldid).

Este proyecto es un trabajo académico y no tiene relación con la Fundación Wikimedia.

## Casos de prueba

| ID | Elemento de prueba | Técnica | Tipo | Riesgo |
| --- | --- | --- | --- | --- |
| TC-01 | Búsqueda: tipos de término | Partición de equivalencia | Manual | RSK-01 |
| TC-02 | Menú de apariencia (texto, ancho y color) | Transición de estados | Manual | RSK-03 |
| TC-03 | Cambio de idioma de un artículo | Transición de estados | Manual | RSK-05 |
| TC-04 | API de resumen de página | Partición de equivalencia | **Automatizado** | RSK-06 |
| TC-05 | Navegación: aleatorio, enlaces internos e índice | Partición de equivalencia | Manual | RSK-07 |
| TC-06 | Validación del inicio de sesión (sin cuentas reales) | Equivalencia y valores límite | Manual | RSK-09 |
| TC-07 | Rendimiento ligero: tiempo de carga de artículos | Partición de equivalencia | Manual | RSK-10 |
| TC-08 | API de búsqueda | Equivalencia y valores límite | **Automatizado** | RSK-11 |

El detalle de cada caso está en [`docs/casos/`](docs/casos/) y la trazabilidad completa en la sección 5.3 del plan.

## Estructura del repositorio

```
Wikipedia-Plan-pruebas/
├── README.md
├── docs/
│   ├── plan-de-pruebas.md     Documento principal (secciones 1 a 8)
│   ├── casos/                 Un archivo por caso: TC-01.md ... TC-08.md
│   ├── decisiones.md          Bitácora de decisiones y su justificación
│   └── defectos.md            Registro de defectos encontrados
├── tests/                     Scripts automatizados (TC-04 y TC-08)
├── evidencias/                Capturas y resultados, una carpeta por caso
└── entrega/                   PDF final y script que lo genera
```

## Cómo leer la documentación

1. [`docs/plan-de-pruebas.md`](docs/plan-de-pruebas.md): el plan completo. Sigue la estructura de la guía de la asignatura.

   | Sección | Contenido |
   | --- | --- |
   | 1 y 2 | Información del documento, introducción y declaración de adaptación (tailoring) |
   | 3 | Contexto: elementos de prueba, alcance, exclusiones y supuestos |
   | 4 | Riesgos, matriz de exposición y tratamiento |
   | 5 | Condiciones, técnicas, casos, trazabilidad, entorno y criterios de suspensión y finalización |
   | 6, 7 y 8 | Tareas y esfuerzo, roles y cronograma |

2. [`docs/casos/`](docs/casos/): precondiciones, datos, pasos y resultados de cada caso.
3. [`docs/decisiones.md`](docs/decisiones.md): por qué se decidió cada cosa.
4. [`docs/defectos.md`](docs/defectos.md): fallos encontrados, con su evidencia.

## Ejecutar las pruebas automatizadas

Los casos TC-04 y TC-08 se ejecutan con Python y pytest. Los comandos son para Windows (PowerShell) y se corren desde la raíz del repositorio.

**1. Requisitos:** Python 3 e internet.

**2. Instalar las librerías:**

```
python -m pip install -r tests/requirements.txt
```

**3. Configurar el User-Agent.** En `tests/comun.py`, reemplaza `[correo]` por tu correo. Sin eso, los scripts se detienen a propósito.

**4. TC-04 (API de resumen).** En `tests/test_tc04_api_resumen.py` completa los títulos de las clases de redirección y desambiguación, verificados antes a mano en el navegador. Luego:

```
python -m pytest tests/test_tc04_api_resumen.py -v --junitxml=evidencias/TC-04/junit.xml
```

**5. TC-08 (API de búsqueda):**

```
python -m pytest tests/test_tc08_api_busqueda.py -v --junitxml=evidencias/TC-08/junit.xml
```

Cada petición guarda un `.json` en `evidencias/TC-04/` o `evidencias/TC-08/`, con la fecha, la URL, el estado y el cuerpo recortado. Una prueba fallida no siempre es un defecto de Wikipedia: primero hay que comprobar que el dato de entrada sea válido.

## Evidencias y defectos

- Las capturas de los casos manuales y los resultados de los automatizados se guardan en `evidencias/`, en una carpeta por caso.
- Cada defecto se registra como un issue con la etiqueta `defecto` y un ID en el título (por ejemplo, `[DEF-01]`), y se resume en `docs/defectos.md`.

## Flujo de trabajo

- **Issues y tablero:** cada tarea es un issue y se sigue en el tablero kanban de GitHub Projects (Todo, In Progress y Done). Etiquetas: `tarea`, `caso-manual`, `caso-automatizado` y `defecto`.
- **Ramas:** cada autor trabaja en su propia rama y la une a `main` mediante un Pull Request que revisa el otro autor.
- **Edición:** para evitar conflictos, cada autor edita secciones y archivos distintos, y se unen los cambios con frecuencia.
- **Versiones:** el historial de commits y Pull Requests es el control de versiones del documento. La versión final del plan se publica como release.

## Generar el PDF

El PDF de entrega se arma a partir de los archivos Markdown con el script de `entrega/`. Los `.md` son la fuente y el PDF no se actualiza solo: hay que regenerarlo al final y subirlo.

```
python -m pip install markdown==3.7
python entrega/generar_pdf.py
```

Requiere Chrome o Edge instalado. El resultado queda en `entrega/`. Todos los archivos deben guardarse en UTF-8.



## Referencias

- ISO/IEC/IEEE 29119-3:2021, Software testing: Test documentation.
- ISO/IEC/IEEE 29119-4, Software testing: Test techniques.
- Guía de la asignatura: "Plan de Pruebas de Software: Guía de Estructura y Gestión".
- [Wikimedia APIs, registro de cambios](https://www.mediawiki.org/wiki/Wikimedia_APIs/Changelog).
- [Vector 2022, documentación del tema](https://www.mediawiki.org/wiki/Vector_2022).