## Texto
### Lectura
Programar DAGs en Airflow implica definir `schedule_interval` con expresiones CRON, presets (`@daily`, `@hourly`) o triggers manuales. El Scheduler calcula la próxima ejecución considerando `start_date`, `catchup` y dependencias, por lo que comprender estos parámetros es crucial para evitar ejecuciones inesperadas.
Las políticas de retries, delays y SLAs determinan cómo Airflow reacciona ante fallos transitorios. Configurar `retries`, `retry_delay` y alertas evita intervenciones manuales constantes. El 20% de la resiliencia proviene de gestionar estos parámetros junto a dependencias explícitas (`set_downstream`, `>>`, `<<`).
La observabilidad nativa combina logs centralizados por tarea y métricas básicas en la UI (duración, estado, intentos). Estos logs pueden almacenarse en disco, S3 o GCS según la configuración, facilitando auditorías. Integrar con Prometheus, StatsD o herramientas equivalentes amplía el monitoreo hacia dashboards y alertas.
### Explicación con Técnica de Feynman
Programa tus DAGs como si fueran alarmas: defines cuándo deben sonar y qué hacer si nadie responde. Airflow guarda un registro de cada alarma (log) y te muestra si se apagó a tiempo, si necesitó repetir o si falló definitivamente.
### Ejemplos Simples
- Programar un DAG con `@daily` para ejecutar cada medianoche.
- Configurar `retries=2` y `retry_delay=timedelta(minutes=5)` en una tarea crítica.
- Revisar los logs de una tarea fallida desde la UI y descargar el archivo para analizarlo.
### Casos de Uso
- Automatizar pipelines de ingesta nocturna que requieren reintentos controlados ante fallos en APIs externas.
- Monitorizar duración de tareas para detectar regresiones en procesos de transformación.
- Integrar métricas de Airflow con Prometheus para correlacionar ejecuciones con uso de infraestructura.
### Ejemplo de Implementacion
Definir una política estándar de programación (nomenclatura CRON, timezone, catchup), configurar almacenamiento centralizado de logs y establecer reglas de alerta con canales de comunicación claros (correo, Slack). Documentar procedimientos para analizar fallos, incluyendo consultas a logs y métricas complementarias.
### Comandos CLI o Web UI
- `airflow dags pause <dag_id>` — detiene ejecuciones programadas.
- `airflow dags unpause <dag_id>` — reactiva el cron de un DAG.
- `airflow tasks clear <dag_id>` — limpia estados para reejecución controlada.
- `airflow tasks logs <dag_id> <task_id> <execution_date>` — descarga logs desde CLI.
- `http://localhost:8080/log` — acceso directo a logs desde la UI.
## Notas
### Cornell
<table>
  <thead>
    <tr><th>Pistas</th><th>Notas</th><th>Resumen</th></tr>
  </thead>
  <tbody>
    <tr><td>Schedule</td><td>CRON, presets, catchup y start_date.</td><td>Control de periodicidad.</td></tr>
    <tr><td>Resiliencia</td><td>Retries, delays, SLAs, dependencias.</td><td>Minimiza intervención manual.</td></tr>
    <tr><td>Logging</td><td>UI, almacenamiento configurable, integración con métricas.</td><td>Soporte para diagnóstico.</td></tr>
  </tbody>
</table>
### Outline Method
<table>
  <thead>
    <tr><th>Nivel</th><th>Punto clave</th><th>Detalle de apoyo</th></tr>
  </thead>
  <tbody>
    <tr><td>I</td><td>Programación</td><td>CRON, presets, parámetros de ejecución.</td></tr>
    <tr><td>II</td><td>Gestión de fallos</td><td>Retries, delays, SLAs.</td></tr>
    <tr><td>III</td><td>Monitoreo</td><td>Logs, UI, integraciones externas.</td></tr>
    <tr><td>IV</td><td>Buenas prácticas</td><td>Políticas comunes, documentación de incidentes.</td></tr>
  </tbody>
</table>
## Resumen
Configurar adecuadamente la programación, los reintentos y la observabilidad convierte a Airflow en un orquestador predecible. Con políticas claras y almacenamiento centralizado de logs, los equipos de datos pueden reaccionar ante incidentes con rapidez y trazabilidad.
