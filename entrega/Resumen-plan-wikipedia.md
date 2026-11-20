# Plan de Pruebas de Wikipedia

**Resumen de avances | Pruebas de Software**

## 1. Qué se hizo

- Se diseñó el plan de pruebas bajo la norma **ISO/IEC/IEEE 29119-3:2013**, con enfoque **RBT** (pruebas basadas en riesgos).
- Aplicativo elegido: **Wikipedia** (es.wikipedia.org), solo lectura y caja negra; la edición de artículos se descartó.
- Trabajo dividido entre 2 personas (**Jhon Herney Anacona** y **Miguel Angel Pardo**), con 8 casos de prueba (TC-01 a TC-08), 4 por persona.
- Se redactaron las secciones 4 a 8 del plan (borrador) y se identificó la matriz de riesgos.
- Todo el trabajo se gestiona en GitHub con Markdown: ramas por persona y Pull Request revisado por la otra persona.

## 2. Riesgos identificados

| Total | Del producto | Del proyecto | Críticos | Altos |
|:-----:|:------------:|:------------:|:--------:|:-----:|
| 17 (RSK-01 a RSK-17) | 12 | 5 | 0 | 9 (RSK-01, 03, 05, 06, 07, 09, 10, 11, 13) |

## 3. Casos de prueba

| Tipo | Cantidad | Detalle |
|------|:--------:|---------|
| Manuales | 6 | TC-01, TC-02, TC-03, TC-05, TC-06, TC-07 |
| Automatizados (API) | 2 | TC-04 y TC-08, en Python con `pytest` y `requests` |

## 4. Resultados obtenidos

### TC-04 (API, automatizado)

Pasa **4 de 4** escenarios:

- Artículo existente (Colombia)
- Redirección (Colombia (república))
- Desambiguación (Mercurio)
- Artículo inexistente

### TC-07 (tiempo de carga, manual)

Técnica de partición de clases de equivalencia por tamaño; umbral de aceptación de **5 s**; 3 mediciones por artículo.

| Artículo | Med. 1 | Med. 2 | Med. 3 | Promedio | Estado |
|----------|:------:|:------:|:------:|:--------:|:------:|
| Corto (Colombia) | 5.39 s | 4.82 s | 4.95 s | 5.05 s | Fallido |
| Mediano (Medellín) | 4.15 s | 4.38 s | 4.27 s | 4.27 s | Aprobado |
| Muy largo (Historia de Colombia) | 5.82 s | 6.14 s | 5.96 s | 5.97 s | Fallido |

## 5. Defectos registrados

| ID | Descripción | Severidad | Riesgo | Estado |
|----|-------------|:---------:|:------:|:------:|
| DEF-01 | Artículo corto (Colombia) supera el umbral: 5.05 s frente a 5 s. Incumplimiento marginal con variación entre mediciones. | Baja | RSK-10 | Confirmado |
| DEF-02 | Artículo muy largo (Historia de Colombia) supera el umbral: 5.97 s en promedio, las 3 mediciones fuera del límite. | Media | RSK-10 | Confirmado |

## 6. Conclusiones preliminares

- El comportamiento funcional de la API de resúmenes es correcto en los escenarios probados.
- El rendimiento se degrada con el tamaño del artículo, lo que confirma el riesgo **RSK-10** (carga de artículos extensos).
- El incumplimiento del artículo corto es marginal; conviene repetir la medición en otro horario para descartar ruido de red.