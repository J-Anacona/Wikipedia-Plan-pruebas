Plan de Pruebas de Software - Wikipedia en español

## 1. Información específica del documento

### 1.1 Identificador único del documento

WIKI-PP-2026-01 (Plan de Pruebas, versión 0.1)

### 1.2 Organización emisora y autores

Organización - curso Pruebas de Software, 2026-2.
Autores: Jhon Herney Anacona, Miguel Ángel Pardo.

### 1.3 Autoridad de aprobación

ROBERTO JOSE CALDERON BERMEJO, docente del curso de Pruebas de Software.

### 1.4 Historial de cambios y control de versiones

| Versión | Fecha | Autor | Cambio |
| --- | --- | --- | --- |
| 0.1 | 15/11/2026 | Jhon Herney Anacona y Miguel Ángel Pardo | Primer borrador: contexto de las pruebas, riesgos y estrategia de pruebas (secciones 3, 4 y 5). |
| 0.2 | 15/11/2026 | Jhon Herney Anacona y Miguel Ángel Pardo | Información del documento e introducción con la declaración de adaptación (secciones 1 y 2). |


## 2. Introducción y declaración de adaptación (Tailoring)

### 2.1 Alcance del documento

Este documento establece el qué, el porqué, el cómo y los recursos de las pruebas aplicadas a Wikipedia en español. Abarca verificaciones de funcionalidad, navegación, validación y rendimiento básico sobre ocho elementos (sección 3.1), y orienta tanto la ejecución como el registro de los resultados.

**Sistema bajo prueba.** Wikipedia en español (es.wikipedia.org) es una enciclopedia en línea, pública y colaborativa, desarrollada sobre MediaWiki y operada por la Fundación Wikimedia. Se prueba como caja negra, en modo de solo lectura y sin acceso a su código.

### 2.2 Referencias documentales

| ID | Documento |
| --- | --- |
| REF-01 | ISO/IEC/IEEE 29119-3:2021 - Software testing: Test documentation. |
| REF-02 | ISO/IEC/IEEE 29119-4 - Software testing: Test techniques. |
| REF-03 | Guía de la asignatura: "Plan de Pruebas de Software: Guía de Estructura y Gestión" y "Estructura Actualizada del Plan de Pruebas". |
| REF-04 | Wikimedia APIs, registro de cambios: https://www.mediawiki.org/wiki/Wikimedia_APIs/Changelog . |
| REF-05 | Vector 2022, documentación del tema de Wikipedia: https://www.mediawiki.org/wiki/Vector_2022 . |
| REF-06 | Repositorio del proyecto: [URL del repositorio]. |

### 2.3 Conformidad y adaptación (Tailoring)

**Declaración.** El proyecto aplica la norma ISO/IEC/IEEE 29119-3 con conformidad adaptada.

**Justificación.** Wikipedia es un sitio informativo público de criticidad baja a moderada para este plan: una falla en las funciones probadas afecta la consulta de información, pero no pone en riesgo vidas ni dinero. Además, el proyecto tiene restricciones fuertes: un equipo de 2 personas, pruebas de caja negra sobre un sitio de terceros, sin acceso al código, sin entorno propio y sin autorización para pruebas intrusivas, y con la obligación de respetar las normas de uso de Wikimedia (solo lectura y pocas peticiones).

**Qué se conserva.** Se mantiene completo lo que da trazabilidad: el plan, el análisis de riesgos, la estrategia, las condiciones, los casos con su trazabilidad, los datos, el entorno, los reportes de defectos y el informe de cierre.

**Qué se excluye o se simplifica, y qué riesgo se asume:**

| Elemento de la norma | Decisión | Justificación | Riesgo asumido |
| --- | --- | --- | --- |
| Documentación organizacional (política y estrategia organizacional de pruebas) | Excluido | No existe una organización de pruebas; el plan es de un solo proyecto. | Bajo. No hay otros proyectos que deban alinearse. |
| Volumen de casos: 8 (4 por integrante) | Reducido | Equipo de 2 personas. | Medio. Los riesgos Medios y Bajos quedan sin prueba directa; los 8 casos cubren el 100% de los riesgos Altos del producto (5.3). |
| Informes de estado periódicos e informe de incidentes formal | Simplificados | Se reemplazan por la bitácora `decisiones.md`, el tablero del repositorio y una plantilla de issue de GitHub con los campos esenciales. | Bajo. Hay menos formalidad documental, pero se conservan los datos esenciales. |
| Pruebas de carga y estrés | Excluidas | Saturarían infraestructura ajena y no están autorizadas. | Medio. No se conoce el comportamiento bajo alta demanda; TC-07 mide el tiempo de carga con pocas peticiones. |
| Seguridad profunda, edición y guardado de artículos, creación de cuentas y sesiones reales | Excluidos | Son intrusivos o modificarían un sitio real y público. | Medio. Pueden existir vulnerabilidades y fallos en la edición o en las cuentas sin detectar; TC-06 solo revisa la validación con credenciales ficticias. |
| Límites de búsqueda y tipos de página en la interfaz | Excluidos | Se cubren a nivel de API (TC-08 y TC-04). | Bajo. Pueden existir defectos que solo aparezcan en la interfaz; TC-01 cubre la búsqueda desde la interfaz. |

Las conclusiones del plan se limitan a los ocho elementos de la sección 3.1 y no pueden generalizarse a toda Wikipedia.

### 2.4 Glosario

| Término | Definición sencilla |
| --- | --- |
| Caja negra | Prueba que evalúa lo que el sistema hace sin conocer su código interno. |
| Caso de prueba (TC) | Prueba concreta con precondiciones, pasos y resultado esperado. |
| Condición de prueba (CP) | Regla del sistema que se puede verificar y que se deriva de un riesgo. |
| Elemento de prueba (EP) | Parte del sistema que se somete a prueba. |
| Riesgo (RSK) | Posible fallo del producto o del proyecto, evaluado por su probabilidad y su impacto. |
| Exposición al riesgo | Probabilidad × impacto, en escala de 1 a 4: 1-3 Bajo, 4-6 Medio, 8-9 Alto y 12-16 Crítico. |
| Técnicas de diseño | Partición de clases de equivalencia (agrupar entradas que el sistema trata igual), valores límite (probar los bordes de cada clase) y transición de estados (probar los cambios entre estados). |
| Trazabilidad | Relación entre riesgos, condiciones y casos que permite verificar la cobertura en ambos sentidos. |
| Defecto | Diferencia entre el resultado obtenido y el esperado. |
| API | Interfaz que permite consultar un servicio mediante peticiones, sin usar su pantalla. |
| Enlace permanente (oldid) | Dirección que apunta a una versión concreta de un artículo de Wikipedia. |
| Tailoring | Adaptación justificada de la norma a las condiciones del proyecto. |


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

## 4. Gestión de riesgos y matriz de exposición (RBT - Risk-Based Testing)

### 4.1 Identificación de riesgos

#### Riesgos del producto

| ID | Riesgo | Causa | Funcionalidad |
| --- | --- | --- | --- |
| RSK-01 | La búsqueda no devuelve el artículo esperado para un término válido (exacto, parcial o con redirección) | Manejo deficiente de coincidencias, redirecciones o caracteres como tildes y ñ | EP-01 Búsqueda |
| RSK-02 | La búsqueda falla o muestra una página rota con una consulta sin resultados o con caracteres especiales | Validación insuficiente de la entrada | EP-01 Búsqueda |
| RSK-03 | El ajuste de texto, ancho o color no se aplica o no se conserva al navegar | La preferencia no se guarda o no se propaga a otras páginas | EP-02 Apariencia |
| RSK-04 | Un texto ampliado o un ancho distinto deforma la página y oculta contenido | Diseño que no se adapta a todos los tamaños | EP-02 Apariencia |
| RSK-05 | El enlace de idioma no lleva al artículo equivalente, lleva a uno inexistente o no permite volver | Enlaces entre idiomas desactualizados o mal asociados | EP-03 Idioma |
| RSK-06 | La API de resumen devuelve un código de estado o una estructura incorrectos (éxito para un título inexistente, campos faltantes) | Manejo deficiente de redirecciones, desambiguación o títulos inexistentes; cambios en el endpoint | EP-04 API de resumen |
| RSK-07 | La página aleatoria, un enlace interno o un ancla del índice lleva a un destino incorrecto | Anclas con caracteres especiales, redirecciones o enlaces mal formados | EP-05 Navegación |
| RSK-08 | La página aleatoria devuelve contenido que no es un artículo (redirección, desambiguación) | La selección aleatoria no filtra tipos de página | EP-05 Navegación |
| RSK-09 | El formulario de inicio de sesión no valida bien (campos vacíos, usuario o clave incorrectos) o da mensajes que confunden o revelan información | Validación incompleta o mensajes de error poco cuidados | EP-06 Inicio de sesión |
| RSK-10 | Un artículo largo carga con una lentitud que deteriora el uso | Muchas imágenes, tablas o plantillas, y conexión limitada | EP-07 Rendimiento |
| RSK-11 | La API de búsqueda no respeta los parámetros (cantidad de resultados) o falla con consulta vacía o caracteres especiales | Validación de parámetros deficiente; cambios en la API | EP-08 API de búsqueda |
| RSK-12 | Un aviso temporal (por ejemplo, un banner de campaña) tapa o desplaza el contenido | Elementos promocionales sobre la página | General |

#### Riesgos del proyecto

| ID | Riesgo | Causa | Funcionalidad |
| --- | --- | --- | --- |
| RSK-13 | Los resultados no se pueden reproducir porque el contenido de Wikipedia cambia | Edición continua de artículos y de la interfaz | Todas |
| RSK-14 | Una API pública cambia, se retira o limita las peticiones durante el trabajo | Políticas de deprecación de Wikimedia | EP-04 y EP-08 |
| RSK-15 | No se puede analizar la causa de un fallo | Prueba de caja negra, sin acceso al código | Todas |
| RSK-16 | Las mediciones de rendimiento varían y no son comparables | Conexión inestable, o equipos distintos | EP-07 Rendimiento |
| RSK-17 | Conflictos al unir el trabajo de las dos ramas | Edición simultánea de los mismos archivos | Repositorio |

### 4.2 Matriz de análisis de riesgos

Se usa una escala de 1 a 4 para la probabilidad (P) y para el impacto (I). La exposición se calcula como **P × I**: de 1 a 3 es Bajo, de 4 a 6 es Medio, de 8 a 9 es Alto y de 12 a 16 es Crítico.

| Valor | P (probabilidad) | I (impacto) |
| --- | --- | --- |
| 1 | Rara | Leve: molestia menor |
| 2 | Poco probable | Moderado: afecta pero hay alternativa |
| 3 | Probable | Grave: bloquea o afecta mucho una función |
| 4 | Casi segura | Crítico: el usuario no puede usar el servicio |

### 4.3 Tratamiento y mitigación

Cada riesgo recibe un tratamiento según su nivel de exposición:

- **Crítico y Alto:** mitigación obligatoria mediante casos de prueba.
- **Medio:** la prueba es opcional; en cada caso se justifica técnicamente si se prueba o se omite.
- **Bajo:** aceptación formal, sin prueba.

#### Riesgos del producto

| ID | Exposición | Tratamiento | Caso de prueba | Justificación |
| --- | --- | --- | --- | --- |
| RSK-01 | 8 Alto | Mitigar con prueba | TC-01 | Riesgo Alto: cobertura obligatoria |
| RSK-02 | 4 Medio | Aceptar sin prueba directa | Ninguno | Se omite por las exclusiones de la sección 3.2; los límites de búsqueda se cubren a nivel de API en TC-08 |
| RSK-03 | 9 Alto | Mitigar con prueba | TC-02 | Riesgo Alto: cobertura obligatoria |
| RSK-04 | 4 Medio | Aceptar sin prueba directa | Ninguno | Se omite por las exclusiones de la sección 3.2; TC-02 ya recorre las opciones de apariencia |
| RSK-05 | 9 Alto | Mitigar con prueba | TC-03 | Riesgo Alto: cobertura obligatoria |
| RSK-06 | 9 Alto | Mitigar con prueba | TC-04 | Riesgo Alto: cobertura obligatoria |
| RSK-07 | 9 Alto | Mitigar con prueba | TC-05 | Riesgo Alto: cobertura obligatoria |
| RSK-08 | 4 Medio | Aceptar sin prueba directa | Ninguno | Se omite por las exclusiones de la sección 3.2; los tipos de página se cubren a nivel de API en TC-04 |
| RSK-09 | 8 Alto | Mitigar con prueba | TC-06 | Riesgo Alto: cobertura obligatoria |
| RSK-10 | 9 Alto | Mitigar con prueba | TC-07 | Riesgo Alto: cobertura obligatoria |
| RSK-11 | 9 Alto | Mitigar con prueba | TC-08 | Riesgo Alto: cobertura obligatoria |
| RSK-12 | 3 Bajo | Aceptar formalmente | Ninguno | Exposición Baja: se acepta sin prueba para optimizar el esfuerzo |

#### Riesgos del proyecto

| ID | Exposición | Tratamiento | Acción | Justificación |
| --- | --- | --- | --- | --- |
| RSK-13 | 8 Alto | Mitigar con acción de gestión | Anotar fecha, idioma y enlace permanente (oldid) de cada artículo usado | Es un riesgo del proyecto, no del producto: no se resuelve con un caso de prueba |
| RSK-14 | 6 Medio | Mitigar con acción de gestión | Verificar la documentación vigente de las APIs antes de programar TC-04 y TC-08 | Prevenir el cambio es más eficiente que probarlo |
| RSK-15 | 4 Medio | Aceptar | Registrar evidencia (capturas y datos) de cada fallo | Es una limitación inherente a la prueba de caja negra |
| RSK-16 | 6 Medio | Mitigar con acción de gestión | Repetir cada medición de TC-07 unas 3 veces y anotar fecha, hora y conexión | La repetición reduce la variación entre mediciones |
| RSK-17 | 6 Medio | Mitigar con acción de gestión | Una rama por persona, archivos distintos y Pull Request revisado por la otra persona | El flujo de trabajo en GitHub ya previene los conflictos |

#### Verificación de cobertura

Los 8 riesgos Altos del producto (RSK-01, 03, 05, 06, 07, 09, 10 y 11) quedan cubiertos por los 8 casos de prueba (TC-01 a TC-08), con cobertura del 100% y sin casos huérfanos. El riesgo Alto del proyecto (RSK-13) se trata con una acción de gestión.


## 5. Estrategia de pruebas y derivacion de casos

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
| TC-04 | Consulta a la API de resumen con un título existente, con redirección, de desambiguación e inexistente | CP-04 | RSK-06 | Partición de clases de equivalencia | 1 | Automatizada  |
| TC-05 | Uso de la página aleatoria, un enlace interno y un ancla del índice | CP-05 | RSK-07 | Partición de clases de equivalencia | 1 | Manual |
| TC-06 | Inicio de sesión con campos vacíos, usuario inexistente y clave incorrecta (credenciales ficticias) | CP-06 | RSK-09 | Partición de clases de equivalencia y análisis de valores límite | 1 | Manual |
| TC-07 | Medición del tiempo de carga de un artículo corto, uno mediano y uno muy largo | CP-07 | RSK-10 | Partición de clases de equivalencia | 1 | Manual |
| TC-08 | Consulta a la API de búsqueda con resultados, vacía, con caracteres especiales y con valores límite de cantidad | CP-08 | RSK-11 | Partición de clases de equivalencia y análisis de valores límite | 1 | Automatizada  |

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


## 6. Actividades de prueba y estimaciones

### 6.1 Desglose de tareas y 6.2 Estimación de esfuerzo

| # | Actividad | Responsable | Horas | Depende de |
| --- | --- | --- | --- | --- |
| 1 | Cerrar el plan (secciones 1 a 8), revisarlo entre ambos y validarlo con el docente | A y B | 7 | - |
| 2 | Preparar el entorno de pruebas (navegador, Python y datos DAT-01) | B | 3 | 1 |
| 3 | Diseñar en detalle los 8 casos en `docs/casos/` (resultados esperados y criterios medibles) | A y B | 10 | 1 |
| 4 | Programar los scripts de TC-04 y TC-08 en `/tests` | A y B | 8 | 2 y 3 |
| 5 | Ejecutar los 6 casos manuales y guardar la evidencia | A y B | 9 | 3 |
| 6 | Ejecutar los 2 casos automatizados y registrar los defectos encontrados | A y B | 5 | 4 y 5 |
| 7 | Revisión cruzada de resultados y de la trazabilidad | A y B | 3 | 5 y 6 |
| 8 | Informe de cierre y PDF final | A y B | 5 | 7 |
| **Total** | | | **50** | (≈ 25 h por integrante) |

## 7. Personal

### 7.1 Roles y responsabilidades de prueba

Cada integrante se encarga de sus propios casos: los diseña, los ejecuta y los documenta, conserva la evidencia y registra los defectos que encuentre. A su vez, revisa el trabajo de su compañero/a cuando este llega por Pull Request.

| Integrante | Rol adicional | Riesgos y casos a cargo |
| --- | --- | --- |
| Jhon Herney Anacona (A) | Líder de pruebas: tailoring, matriz de riesgos, trazabilidad e informe de cierre | RSK-01, 03, 05 y 06: TC-01, TC-02, TC-03 y TC-04 |
| Miguel Ángel Pardo (B) | Automatización y entorno: configuración, datos de prueba y PDF final | RSK-07, 09, 10 y 11: TC-05, TC-06, TC-07 y TC-08 |


## 8. Cronograma

### 8.1 Hitos y fechas de ejecución

| Fase | Actividades | Hito | Fechas |
| --- | --- | --- | --- |
| 1. Planificación y diseño | Tareas 1 a 3: cerrar y validar el plan, preparar el entorno y diseñar los 8 casos | H1: plan v1.0 y casos diseñados | 19/11/2026 |
| 2. Ejecución | Tareas 4 a 6: programar los scripts, ejecutar los casos y registrar defectos | H2: 8 casos ejecutados | 19/11/2026 |
| 3. Cierre | Tareas 7 y 8: revisión cruzada, informe de cierre y PDF final | H3: informe y release final listos |19/11/2026 |
| - | Entrega al docente | H4: entrega | 19/11/2026 |