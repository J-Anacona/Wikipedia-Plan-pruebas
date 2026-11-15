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