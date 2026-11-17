
# TC-03: Cambio de idioma de artículos en Wikipedia

## 1. Información general

| Campo | Descripción |
|---|---|
| Identificador | TC-03 |
| Elemento de prueba | EP-03 – Enlaces de idioma |
| Condición de prueba | CP-03 – Cambio de idioma de un artículo |
| Riesgo asociado | RSK-05 |
| Prioridad | Alta |
| Tipo | Funcional – Manual |
| Responsable | Jhon Herney Anacona - Miguel Ángel Pardo |

## 2. Objetivo

Verificar que los enlaces de idioma de Wikipedia permitan acceder al artículo equivalente en otro idioma y regresar correctamente al artículo original, tanto en artículos con muchos idiomas disponibles como en artículos con pocos.

## 3. Precondiciones

- Tener conexión a Internet y un navegador actualizado.
- Acceder a https://es.wikipedia.org/.
- No tener iniciada una sesión de usuario.
- Identificar un artículo con muchos idiomas disponibles y otro con pocos.
- Verificar que ambos artículos tengan enlaces de idioma disponibles.

## 4. Datos de prueba y resultados esperados

| Escenario | Dato de entrada | Resultado esperado |
|---|---|---|
| Artículo con muchos idiomas | Colombia | Mostrar los idiomas disponibles y permitir acceder al artículo equivalente en otro idioma, por ejemplo, inglés. |
| Cambio al idioma inglés | Artículo de Colombia en inglés | Mostrar correctamente el artículo equivalente en inglés. |
| Regreso al idioma original | Artículo de Colombia en inglés | Permitir regresar correctamente al artículo de Colombia en español. |
| Artículo con pocos idiomas | Artículo seleccionado con pocos idiomas disponibles | Mostrar los idiomas disponibles y permitir seleccionar otro idioma existente. |
| Regreso desde artículo con pocos idiomas | Artículo seleccionado en otro idioma | Permitir regresar correctamente al artículo original en español. |

**Nota:** Para el segundo artículo, se debe seleccionar uno que realmente tenga pocos idiomas disponibles. Se debe registrar su nombre y los idiomas encontrados.

## 5. Pasos de ejecución

**Escenario 1: Artículo con muchos idiomas**

1. Abrir Wikipedia en español.
2. Buscar el artículo "Colombia".
3. Identificar la sección de idiomas disponibles.
4. Seleccionar el idioma inglés.
5. Verificar que se abra el artículo equivalente en inglés.
6. Seleccionar nuevamente el idioma español.
7. Verificar que se regrese al artículo original.
8. Guardar capturas de pantalla como evidencia.

**Escenario 2: Artículo con pocos idiomas**

1. Abrir Wikipedia en español.
2. Buscar un artículo que tenga pocos idiomas disponibles.
3. Identificar los idiomas disponibles.
4. Seleccionar uno de los idiomas existentes.
5. Verificar que se abra el artículo equivalente.
6. Seleccionar nuevamente el idioma español.
7. Verificar que se regrese al artículo original.
8. Guardar capturas de pantalla como evidencia.

## 6. Criterios de aceptación

El caso se aprobará si:

- El artículo con muchos idiomas muestra correctamente sus opciones de idioma.
- El enlace seleccionado dirige al artículo equivalente en el idioma elegido.
- Es posible regresar al artículo original en español.
- El artículo con pocos idiomas permite realizar correctamente el cambio de idioma.
- No se presentan errores de navegación ni enlaces rotos.

Cada escenario se calificará individualmente como Aprobado o Fallido.

## 7. Registro de resultados

| Escenario | Resultado obtenido | Estado |
|---|---|---|
| Artículo con muchos idiomas | El artículo de Colombia mostró correctamente las opciones de idiomas disponibles. | Aprobado |
| Cambio al idioma inglés | El articulo de colombia mostro correctamente el cambio de idiomas | Aprobado |
| Regreso al idioma español | El articulo de colombia mostro correctamente el cambio de idioma | Aprobado |
| Artículo con pocos idiomas | El articulo selecionado "El dorado" mostro una disminucion  | Aprobado |
| Regreso desde el artículo con pocos idiomas | Wikipedia permitió regresar correctamente al artículo original en español. | Aprobado |

**Trazabilidad:** RSK-05 → CP-03 → TC-03.


