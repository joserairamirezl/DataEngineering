## Texto
### Lectura
Apache Airflow nació para orquestar flujos de trabajo de datos declarativos, permitiendo definir DAGs (Directed Acyclic Graphs) donde cada nodo representa una tarea y cada arista describe dependencias. Esta separación entre definición y ejecución ofrece transparencia operativa: la UI refleja el estado del pipeline y facilita reintentos o backfills controlados.
La arquitectura base se compone de Webserver para visualizar y gestionar DAGs, Scheduler que interpreta dependencias y agenda tareas, Worker o Executor encargado de ejecutar las tareas y la base de metadatos que registra historiales. El 20% más relevante para obtener el 80% de valor consiste en entender cómo interactúan Scheduler, Executor y Metadata DB; dominar esta relación evita cuellos de botella comunes al iniciar proyectos.
Airflow adopta un enfoque "configuration as code": los DAGs se codifican en Python, pero las tareas pueden ejecutar procesos externos, lo que se alinea con necesidades de Data Engineering que abarcan ETL, validaciones y cargas hacia almacenes analíticos. El modelo orientado a dependencias temporales facilita orquestar pipelines complejos con ventanas de cron reducidas.
Instalar Airflow localmente o con Docker Compose permite experimentar con la UI, identificar cómo se registran DAGs y validar que las tareas cambian de estado (queued, running, success, failed). Familiarizarse con estos estados y con los logs web es esencial para diagnosticar problemas desde el primer día.
### Explicación con Técnica de Feynman
Piensa en Airflow como un director de orquesta: el partitura es el DAG, cada músico es una tarea y el director decide cuándo entra cada uno para que la música suene sin errores. Si algo falla, el director identifica al músico y le pide repetir su parte sin reiniciar toda la sinfonía.
### Ejemplos Simples
- Crear un DAG minimalista con dos tareas dummy para ver el flujo visual.
- Ejecutar manualmente un DAG desde la UI para observar cómo cambian los estados.
- Pausar y reactivar un DAG para entender cómo controla el Scheduler la ejecución.
### Casos de Uso
- Orquestar una cadena diaria de ingesta de datos desde APIs hacia un data lake.
- Controlar la ejecución de ETL sobre warehouses como Snowflake o BigQuery con dependencias temporales.
- Programar tareas de preparación de modelos analíticos que requieren extracción, limpieza y carga escalonada.
### Ejemplo de Implementacion
Iniciar un entorno local, definir convenciones de nomenclatura para DAGs y tareas, registrar conexiones básicas (por ejemplo, bases de datos y data lakes) y documentar el proceso de despliegue de nuevos DAGs en un repositorio compartido. Establecer ciclos de revisión para validar dependencias y cron antes de activar cada pipeline.
### Comandos CLI o Web UI
- `airflow db init` — inicializa la base de metadatos.
- `airflow webserver --port 8080` — levanta la interfaz web.
- `airflow scheduler` — inicia el planificador de tareas.
- `airflow dags list` — muestra los DAGs disponibles.
- `http://localhost:8080/home` — panel principal para monitorear ejecuciones.
## Notas
### Cornell
<table>
  <thead>
    <tr><th>Pistas</th><th>Notas</th><th>Resumen</th></tr>
  </thead>
  <tbody>
    <tr><td>¿Qué es?</td><td>Orquestador basado en DAGs con dependencias declarativas.</td><td>Coordina pipelines de datos.</td></tr>
    <tr><td>Arquitectura</td><td>Webserver, Scheduler, Executor/Workers, Metadata DB.</td><td>Piezas críticas del flujo.</td></tr>
    <tr><td>Primeros pasos</td><td>Instalación, prueba de estados, uso de UI.</td><td>Base para operativizar.</td></tr>
  </tbody>
</table>
### Outline Method
<table>
  <thead>
    <tr><th>Nivel</th><th>Punto clave</th><th>Detalle de apoyo</th></tr>
  </thead>
  <tbody>
    <tr><td>I</td><td>Definición de Airflow</td><td>DAGs como código, orquestación flexible.</td></tr>
    <tr><td>II</td><td>Componentes principales</td><td>Scheduler, Executor, Metadata DB, Webserver.</td></tr>
    <tr><td>III</td><td>Flujo de trabajo</td><td>Estados de tareas, logs, UI interactiva.</td></tr>
    <tr><td>IV</td><td>Prácticas iniciales</td><td>Entorno local, convenciones, revisión de cron.</td></tr>
  </tbody>
</table>
## Resumen
Comprender la arquitectura fundamental y experimentar con un DAG simple permiten aprovechar Airflow como orquestador confiable. El dominio temprano del Scheduler, la UI y la base de metadatos reduce la fricción al crear pipelines más complejos.
