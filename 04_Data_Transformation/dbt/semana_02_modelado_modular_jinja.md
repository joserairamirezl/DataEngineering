## Texto
### Lectura
dbt organiza las transformaciones en modelos SQL que se heredan unos de otros, lo que permite modularizar pipelines complejos. Se acostumbra dividir los modelos en capas `staging`, `intermediate` y `mart` para reflejar la madurez del dato y mantener dependencias claras. Las macros de Jinja amplían SQL con plantillas reutilizables, control de flujo ligero y variables, permitiendo parametrizar reglas de negocio y reducir duplicidad. Los métodos `ref()` y `source()` construyen dependencias explícitas entre modelos y fuentes, garantizando el orden de ejecución y la trazabilidad de linaje. Generar documentación con `dbt docs generate` y `dbt docs serve` ayuda a inspeccionar diagramas de relaciones y descripciones en contexto.
### Explicación con Técnica de Feynman
Piensa en dbt como bloques de Lego de SQL. Cada bloque (modelo) toma datos de otro bloque y los mejora. Para que no se mezclen piezas, se agrupan en niveles: primero preparas las piezas (`staging`), luego armas subcomponentes (`intermediate`) y finalmente el modelo listo para negocio (`mart`). Con Jinja puedes crear moldes reutilizables (macros) y variables, de modo que no tengas que escribir el mismo SQL cada vez. Usas `ref()` para decir “este modelo necesita a este otro bloque”, y dbt se encarga de construir todo en el orden correcto y mostrarte un mapa actualizado.
### Ejemplos Simples
- Crear un modelo `stg_orders` que limpia campos básicos y alimenta a un modelo `int_orders_enriched`.
- Definir una macro para formatear fechas y usarla en dos modelos distintos.
- Documentar un modelo con una descripción breve y verlo reflejado en `dbt docs`.
### Casos de Uso
- Empresas que necesitan homogenizar múltiples fuentes de ventas aplicando reglas comunes mediante macros reutilizables.
- Equipos que quieren implementar data marts compartiendo columnas derivadas (por ejemplo, métricas de retención) sin duplicar lógica.
- Analistas que deben exponer linaje de datos para auditorías internas usando la documentación automática de dbt.
### Ejemplo de Implementacion
Diseñar una convención de carpetas para capas `staging`, `intermediate` y `mart`, definiendo archivos `schema.yml` con descripciones y tests. Escribir macros base para operaciones repetitivas (normalización de identificadores, filtros de fechas) y usarlas a través de `ref()` en modelos dependientes. Publicar la documentación en un servidor interno para que stakeholders entiendan transformaciones y linaje.
### Comandos CLI o Web UI
- `dbt run --select tag:staging` para ejecutar únicamente la capa de preparación y detectar fallas tempranas.
- `dbt run --select modelo_a modelo_b+` para construir un subconjunto crítico a partir de modelos dependientes de alto impacto.
- `dbt ls --resource-type model --output path` para revisar rápidamente la estructura modular del proyecto.
- `dbt docs generate` seguido de `dbt docs serve` para exponer documentación interactiva con linaje.
- En dbt Cloud, crear un Job con pasos segmentados por capas (`staging`, `intermediate`, `mart`) para priorizar transformaciones clave.
## Notas
### Cornell
<table>
  <tr><th>Preguntas Clave</th><th>Notas</th></tr>
  <tr><td>¿Por qué usar capas de modelos?</td><td>Separan la preparación de datos crudos, transformaciones intermedias y métricas finales para simplificar el mantenimiento.</td></tr>
  <tr><td>¿Cómo ayuda Jinja?</td><td>Introduce macros y variables que permiten aplicar lógica reutilizable y controlada en múltiples modelos.</td></tr>
  <tr><td>¿Qué aporta `ref()`?</td><td>Asegura dependencias declarativas que mantienen el orden de ejecución y facilitan el linaje.</td></tr>
  <tr><td>¿Qué valor da la documentación?</td><td>Genera diagramas navegables que aceleran el entendimiento del pipeline por parte de analistas y auditores.</td></tr>
</table>
### Outline Method
<table>
  <tr><th>Nivel</th><th>Contenido</th></tr>
  <tr><td>I</td><td>Capas de modelos y organización modular.</td></tr>
  <tr><td>II</td><td>Uso de Jinja para macros, variables y plantillas.</td></tr>
  <tr><td>III</td><td>Dependencias declaradas con `ref()` y `source()`.</td></tr>
  <tr><td>IV</td><td>Generación y publicación de documentación interactiva.</td></tr>
</table>
## Resumen
La modularidad de dbt combinada con Jinja y referencias declarativas facilita construir pipelines escalables, reutilizables y bien documentados que mantienen alineados a los equipos de datos y negocio.
