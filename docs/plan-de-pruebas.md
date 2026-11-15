## 3. Contexto de las pruebas

### 3.1 Elementos de prueba

El sistema bajo prueba es la edición en español de Wikipedia (es.wikipedia.org),
tratada como caja negra. Los elementos probados son:

| ID | Elemento de prueba | Qué es | Caso |
| -- | ------------------ | ------ | ---- |
| EP-01 | Búsqueda | Cuadro de búsqueda de la interfaz | TC-01 |
| EP-02 | Menú de apariencia | Opciones de texto, ancho y color | TC-02 |
| EP-03 | Enlaces de idioma | Cambio de idioma de un artículo | TC-03 |
| EP-04 | API de resumen de página | Endpoint /api/rest_v1/page/summary/{título} | TC-04 |
| EP-05 | Navegación | Página aleatoria, enlaces internos e índice | TC-05 |
| EP-06 | Formulario de inicio de sesión | Solo validación de errores, sin crear cuentas | TC-06 |
| EP-07 | Tiempo de carga de artículos | Medición ligera con las herramientas del navegador | TC-07 |
| EP-08 | API de búsqueda | Búsqueda mediante la API de acciones (format=json) | TC-08 |

### 3.2 Alcance y exclusiones

Dentro del alcance: los ocho elementos anteriores.

Fuera del alcance:

| Exclusión | Justificación |
| --------- | ------------- |
| Edición y guardado de artículos | Modificaría un sitio real y público |
| Pruebas de carga y estrés | Saturarían infraestructura ajena |
| Seguridad profunda | No hay autorización para pruebas de intrusión |
| Creación de cuentas y sesiones reales | No se usan credenciales reales |
| Límites de búsqueda y tipos de página en la interfaz | Cubiertos por TC-08 y TC-04 a nivel de API |

### 3.3 Suposiciones y restricciones

- Se prueba sin acceso al código ni a la infraestructura (caja negra).
- Wikipedia cambia a diario: se registran fecha, idioma y enlace permanente (oldid) de cada artículo usado.
- Todas las pruebas son de solo lectura; las automatizadas hacen pocas peticiones y usan un User-Agent identificable.
- Las APIs públicas pueden cambiar; se verificó su vigencia en la fecha de elaboración.
- El equipo es de dos personas.

### 3.4 Partes interesadas

- Docente(ROBERTO JOSE CALDERON BERMEJO): auditor y destinatario del plan.
- Autores del plan (A y B): diseñan y ejecutan las pruebas.
- Wikimedia / comunidad de Wikipedia: titulares del sistema probado, no destinatarios de los resultados.



## 5. Estrategia de pruebas o derivacion de casos

### 5.1 Derivación de condiciones de prueba

| ID | Condición | Regla verificable | Riesgo |
| --- | --- | --- | --- |
| CP-01 | Búsqueda por tipo de término | La búsqueda lleva al artículo esperado cuando el término es exacto, parcial, con redirección, con error o sin resultados | RSK-01 |
| CP-02 | Persistencia de la apariencia | Los ajustes de texto, ancho y color se aplican y se conservan al navegar a otras páginas | RSK-03 |
| CP-03 | Cambio de idioma de un artículo | El enlace de idioma lleva al artículo equivalente y permite volver al original, tanto en un artículo con muchos idiomas como en uno con pocos | RSK-05 |
| CP-04 | Respuesta de la API de resumen | La API responde con el código de estado y la estructura correctos para un título existente, con redirección, de desambiguación e inexistente | RSK-06 |
| CP-05 | Destino de la navegación | La página aleatoria, los enlaces internos y las anclas del índice llevan al destino correcto | RSK-07 |
| CP-06 | Validación del inicio de sesión | El inicio de sesión rechaza campos vacíos, usuario inexistente y clave incorrecta con mensajes claros | RSK-09 |
| CP-07 | Tiempo de carga por tamaño de artículo | Un artículo corto, uno mediano y uno muy largo cargan dentro de un tiempo aceptable | RSK-10 |
| CP-08 | Parámetros de la API de búsqueda | La API de búsqueda respeta el parámetro de cantidad y maneja bien la consulta vacía y los caracteres especiales | RSK-11 |

### 5.2 Técnicas de diseño de pruebas

| Condición | Técnica | Justificación | Datos o situaciones que genera |
| --- | --- | --- | --- |
| CP-01 | Partición de clases de equivalencia | Los términos de búsqueda se agrupan en clases que el sistema trata igual | Un término de cada clase: exacto, parcial, con redirección, con error y sin resultados |
| CP-02 | Transición de estados | La apariencia cambia de estado según la opción elegida | Cambios entre las opciones de texto, ancho y color, y verificación del estado al navegar a otra página |
| CP-03 | Transición de estados | El artículo pasa de un idioma a otro y vuelve | Ir y volver entre idiomas en un artículo con muchos idiomas y en otro con pocos |
| CP-04 | Partición de clases de equivalencia | Los tipos de título forman clases con respuestas distintas | Un título de cada clase: existente, con redirección, de desambiguación e inexistente |
| CP-05 | Partición de clases de equivalencia | Los tipos de destino forman clases con comportamiento propio | Un caso de página aleatoria, enlace interno y ancla del índice |
| CP-06 | Partición de clases de equivalencia y análisis de valores límite | Las entradas inválidas forman clases, y los campos vacíos están en el límite | Campos vacíos, usuario inexistente y clave incorrecta (credenciales ficticias) |
| CP-07 | Partición de clases de equivalencia | Los artículos se agrupan por tamaño | Un artículo corto, uno mediano y uno muy largo |
| CP-08 | Partición de clases de equivalencia y análisis de valores límite | Las consultas forman clases y el parámetro de cantidad tiene límites | Consulta con resultados, vacía y con caracteres especiales; valores en los límites de la cantidad |


### 5.3 Generación de casos de prueba y trazabilidad

| Caso | Descripción | Condición | Riesgo | Técnica | Prioridad | Ejecución |
| --- | --- | --- | --- | --- | --- | --- |
| TC-01 | Búsqueda con un término exacto, parcial, con redirección, con error y sin resultados | CP-01 | RSK-01 | Partición de clases de equivalencia | 1 | Manual |
| TC-02 | Cambio del tamaño de texto, ancho y color del menú de apariencia, y verificación al navegar a otra página | CP-02 | RSK-03 | Transición de estados | 1 | Manual |
| TC-03 | Cambio de idioma de un artículo con muchos idiomas y de otro con pocos, ir y volver | CP-03 | RSK-05 | Transición de estados | 1 | Manual |
| TC-04 | Consulta a la API de resumen con un título existente, con redirección, de desambiguación e inexistente | CP-04 | RSK-06 | Partición de clases de equivalencia | 1 | Automatizada (enlace al script en `/tests`) |
| TC-05 | Uso de la página aleatoria, un enlace interno y un ancla del índice | CP-05 | RSK-07 | Partición de clases de equivalencia | 1 | Manual |
| TC-06 | Inicio de sesión con campos vacíos, usuario inexistente y clave incorrecta (credenciales ficticias) | CP-06 | RSK-09 | Partición de clases de equivalencia y análisis de valores límite | 1 | Manual |
| TC-07 | Medición del tiempo de carga de un artículo corto, uno mediano y uno muy largo | CP-07 | RSK-10 | Partición de clases de equivalencia | 1 | Manual |
| TC-08 | Consulta a la API de búsqueda con resultados, vacía, con caracteres especiales y con valores límite de cantidad | CP-08 | RSK-11 | Partición de clases de equivalencia y análisis de valores límite | 1 | Automatizada (enlace al script en `/tests`) |

### 5.4 Requisitos de entorno y datos de prueba

| Elemento | Requisito |
| --- | --- |
| Sitio bajo prueba | es.wikipedia.org (real, público, solo lectura) |
| Navegador | [Chrome o Edge, versión], sin extensiones y sin sesión iniciada (salvo TC-06); pestaña Network para TC-07 |
| Scripts (TC-04 y TC-08) | Python 3 + `requests` + `pytest`, en `/tests`, con User-Agent identificable y pocas peticiones |
| Equipo y conexión | [sistema operativo] y [tipo de conexión], anotados en cada medición |

**Datos DAT-01**

| Caso | Datos |
| --- | --- |
| TC-01 | Un término por clase: exacto, parcial, con redirección, con error y sin resultados |
| TC-02 | Opciones del menú: texto (3), ancho (2) y color (3) |
| TC-03 | Un artículo con muchos idiomas y otro con pocos |
| TC-04 | Títulos: existente, con redirección, de desambiguación e inexistente |
| TC-05 | Página aleatoria, un enlace interno y un ancla del índice |
| TC-06 | Credenciales ficticias: campos vacíos, usuario inexistente y clave incorrecta |
| TC-07 | Artículo corto, mediano y muy largo, 3 mediciones cada uno |
| TC-08 | Consulta con resultados, vacía y con caracteres especiales; límites de cantidad según la documentación de la API |

De cada artículo usado se registran fecha, idioma y enlace permanente (oldid), porque Wikipedia cambia a diario. No se edita nada ni se crean cuentas.

### 5.5 Criterios de suspensión y finalización

**Criterios de suspensión**

| Situación | Acción |
| --- | --- |
| es.wikipedia.org no está disponible o responde con errores generalizados | Suspender la ejecución y reintentar después |
| Una API cambia su ruta o su formato de respuesta, o se retira (TC-04 y TC-08) | Suspender ese caso, revisar la documentación vigente y ajustar el script |
| El sitio limita o bloquea las peticiones de los scripts | Suspender los scripts y reducir las peticiones antes de reanudar |
| Un defecto bloqueante impide continuar con un caso | Registrar el defecto y pasar al siguiente caso |
| Un artículo usado cambia de forma que invalida los datos del caso | Elegir otro artículo, registrar su enlace permanente (oldid) y repetir el caso |

Se reanuda cuando la causa se resuelve, y se anota en la bitácora cuándo se suspendió y por qué.

**Criterios de finalización**

- Los 8 casos (TC-01 a TC-08) fueron ejecutados.
- Los 8 riesgos Altos del producto tienen su caso ejecutado (cobertura del 100%).
- Cada defecto encontrado está registrado en `docs/defectos.md` con su ID (`[DEF-01]`, etc.) y su evidencia.
- La matriz de trazabilidad bidireccional está completa, sin casos huérfanos ni riesgos graves sin caso.
- Los resultados de cada caso quedan guardados en `/evidencias` o en `/tests`.
- Se redactó el informe de cierre.