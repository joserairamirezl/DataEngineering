## Texto
### Lectura
La calidad de datos en dbt se asegura con tests nativos (`unique`, `not_null`, `relationships`) declarados en archivos `schema.yml`, así como tests personalizados escritos en SQL para reglas específicas. Estos tests se integran con la ejecución habitual y fallan el pipeline cuando se detectan inconsistencias. Las materializations (`view`, `table`, `incremental`) permiten optimizar el rendimiento y el costo al decidir cómo persisten los modelos en el warehouse según frecuencia de consulta y volumen de datos. Snapshots y seeds amplían el control histórico y la ingesta de datos estáticos. Versionar los proyectos con Git proporciona trazabilidad sobre cambios en modelos, macros y configuraciones, habilitando revisiones y despliegues confiables.
### Explicación con Técnica de Feynman
Piensa que cada modelo de dbt es una receta. Antes de servirla, verificas si cumple reglas básicas: no hay ingredientes repetidos (`unique`), no faltan datos esenciales (`not_null`) y las relaciones con otras tablas tienen sentido (`relationships`). Si una regla falla, detienes la cocina para revisar. Luego decides cómo guardar el resultado: como una vista rápida (`view`), una tabla materializada (`table`) o una tabla que solo agrega nuevas filas (`incremental`). Guardas fotos de versiones anteriores (snapshots) y archivos estáticos (seeds) para comparar cambios con el tiempo. Todo se maneja con Git, que lleva un diario de cada modificación.
### Ejemplos Simples
- Declarar un test `not_null` sobre la columna `customer_id` de un modelo de ventas.
- Cambiar un modelo de `view` a `table` para mejorar el tiempo de respuesta en dashboards semanales.
- Crear un snapshot que registre precios de productos y permita detectar cambios históricos.
### Casos de Uso
- Equipos financieros que necesitan validar integridad de claves y montos antes de publicar reportes regulatorios.
- Startups que optimizan costos en warehouses pagos seleccionando materializations livianas para modelos poco consultados.
- Empresas retail que requieren historial de atributos de producto mediante snapshots para análisis de pricing.
### Ejemplo de Implementacion
Configurar archivos `schema.yml` con tests nativos priorizando las columnas críticas y añadir consultas personalizadas cuando se detecten reglas específicas del negocio. Analizar patrones de uso para definir materializations apropiadas y documentarlas en cada modelo. Incorporar snapshots para entidades que necesitan trazabilidad histórica y seeds para catálogos controlados. Integrar el repositorio dbt con una política de ramas y revisiones de código que exijan aprobación antes de fusionar cambios.
### Comandos CLI o Web UI
- `dbt test --select modelo_critico` para validar campos clave antes de autorizar un despliegue.
- `dbt run --full-refresh --select incremental_model` para reconstruir tablas incrementales cuando cambian sus reglas.
- `dbt snapshot` para ejecutar snapshots y mantener el historial de entidades sensibles.
- `dbt seed --show` para cargar archivos estáticos y validar su contenido principal.
- En Git, usar `git diff` y `git tag` para revisar cambios de modelos y marcar versiones relevantes del proyecto.
## Notas
### Cornell
<table>
  <tr><th>Preguntas Clave</th><th>Notas</th></tr>
  <tr><td>¿Cómo se asegura calidad de datos?</td><td>Tests declarativos en `schema.yml` más pruebas personalizadas que detienen el pipeline ante anomalías.</td></tr>
  <tr><td>¿Qué materialization elegir?</td><td>Depende de uso y costo: `view` para consultas livianas, `table` para performance, `incremental` para grandes volúmenes.</td></tr>
  <tr><td>¿Para qué sirven snapshots y seeds?</td><td>Snapshots capturan históricos controlados; seeds cargan catálogos estáticos versionados.</td></tr>
  <tr><td>¿Cómo ayuda Git?</td><td>Garantiza trazabilidad de cambios, revisiones en equipo y despliegues ordenados.</td></tr>
</table>
### Outline Method
<table>
  <tr><th>Nivel</th><th>Contenido</th></tr>
  <tr><td>I</td><td>Testing nativo y personalizado en `schema.yml`.</td></tr>
  <tr><td>II</td><td>Materializations y decisiones de performance.</td></tr>
  <tr><td>III</td><td>Snapshots y seeds para control histórico y datos estáticos.</td></tr>
  <tr><td>IV</td><td>Versionado con Git y flujos de revisión.</td></tr>
</table>
## Resumen
dbt combina pruebas declarativas, materializations flexibles y versionado con Git para sostener pipelines consistentes, optimizados y auditables en entornos de datos dinámicos.
