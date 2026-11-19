# Registro de defectos

## DEF-01: Artículo corto (Colombia) supera el umbral de tiempo de carga

| Campo | Detalle |
|---|---|
| ID | DEF-01 |
| Fecha de detección | 2026-11-18 |
| Detectado por | Persona B |
| Caso de prueba | TC-07 |
| Riesgo asociado | RSK-10 |
| Entorno | es.wikipedia.org, navegador actualizado sin extensiones, caché desactivada, Wi-Fi (por confirmar), sin sesión iniciada |
| Severidad | Baja |
| Prioridad | Media |
| Estado | Confirmado |

**Descripción:**
El artículo "Colombia" (escenario de artículo corto) tardó en promedio 5.05 s en cargar, por encima del umbral de aceptación de 5 s. La diferencia es mínima (0.05 s) y una de las tres mediciones (4.82 s) sí estuvo dentro del umbral.

**Pasos para reproducir:**
1. Abrir las herramientas de desarrollo en la pestaña Network con la caché desactivada.
2. Cargar el artículo "Colombia".
3. Anotar el tiempo de carga.
4. Repetir la medición 3 veces.

**Resultado esperado:**
Promedio de carga menor o igual a 5 s.

**Resultado obtenido:**
Mediciones de 5.39 s, 4.82 s y 4.95 s, con promedio de 5.05 s.

**Evidencia:**
`evidencias/TC-07/` (captura de la pestaña Network).

**Observaciones:**
Medido el 18/11/2026 a las 20:17 aprox. Al ser un incumplimiento marginal y con variación entre mediciones, conviene repetir la prueba en otro horario para descartar que sea ruido de la red.

---

## DEF-02: Artículo muy largo (Historia de Colombia) supera el umbral de tiempo de carga

| Campo | Detalle |
|---|---|
| ID | DEF-02 |
| Fecha de detección | 2026-11-18 |
| Detectado por | Persona B |
| Caso de prueba | TC-07 |
| Riesgo asociado | RSK-10 |
| Entorno | es.wikipedia.org, navegador actualizado sin extensiones, caché desactivada, Wi-Fi (por confirmar), sin sesión iniciada |
| Severidad | Media |
| Prioridad | Media |
| Estado | Confirmado |

**Descripción:**
El artículo "Historia de Colombia" (escenario de artículo muy largo) tardó en promedio 5.97 s en cargar, casi 1 s por encima del umbral de 5 s. Las tres mediciones superaron el umbral.

**Pasos para reproducir:**
1. Abrir las herramientas de desarrollo en la pestaña Network con la caché desactivada.
2. Cargar el artículo "Historia de Colombia".
3. Anotar el tiempo de carga.
4. Repetir la medición 3 veces.

**Resultado esperado:**
Promedio de carga menor o igual a 5 s.

**Resultado obtenido:**
Mediciones de 5.82 s, 6.14 s y 5.96 s, con promedio de 5.97 s.

**Evidencia:**
`evidencias/TC-07/` (captura de la pestaña Network).

**Observaciones:**
Medido el 18/11/2026 a las 20:17 aprox. El resultado es consistente en las tres mediciones y coincide con lo esperado para el riesgo RSK-10 (carga de artículos extensos).