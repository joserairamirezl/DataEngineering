# Semana 4: Optimización, Operación y Proyecto Final
## Texto
### Lectura
El cierre del módulo se centra en llevar Spark a producción mediante optimización de rendimiento, administración del clúster y diseño de proyectos integrales. El rendimiento depende de parámetros como número de particiones, tamaño de shuffle, broadcast de dimensiones pequeñas y uso correcto de `cache/persist`. Ajustar `spark.sql.shuffle.partitions`, `spark.executor.memory` y `spark.executor.instances` equilibra recursos frente a la carga. Técnicas como Adaptive Query Execution (AQE), repartition/coalesce y broadcast joins minimizan costos de shuffle.  
Desde la operación, se requieren estrategias de monitoreo con Spark UI, History Server, métricas JMX y herramientas como Ganglia, Prometheus o Datadog. El manejo de logs, retries y políticas de tolerancia a fallos es esencial para jobs críticos. La seguridad se implementa con autenticación Kerberos o TLS, aislamiento de usuarios y control de acceso a datos (Ranger, Lake Formation).  
El proyecto final integra lectura de datos masivos, transformaciones batch y streaming, almacenamiento en formatos eficientes y automatización mediante orquestadores (Airflow, Oozie) o plataformas (Databricks Jobs, EMR Step Functions). Documentar arquitectura, costos estimados y runbooks operativos asegura que la solución sea sostenible y escalable.

### Explicación con Técnica de Feynman
Piensa que Spark es una flota de camiones que transporta datos. Si los camiones son demasiado grandes o pequeños, el viaje se vuelve ineficiente. Ajustar particiones es elegir el tamaño justo de los camiones; usar broadcast es enviar una camioneta ligera con datos pequeños para que todos los camiones grandes no tengan que cargarlos. Monitorear la flota es mirar el tablero que muestra rutas, consumo y retrasos. El proyecto final es planificar toda la operación: qué rutas seguir, cuántos camiones usar y qué hacer si uno se detiene.

### Ejemplos Simples
*Configuración de parámetros en `spark-submit`:*
```bash
spark-submit \
  --master yarn \
  --deploy-mode cluster \
  --conf spark.sql.shuffle.partitions=200 \
  --conf spark.executor.instances=10 \
  --conf spark.executor.memory=4g \
  --conf spark.executor.cores=2 \
  job.py
```

*Uso de broadcast join en PySpark:*
```python
from pyspark.sql import functions as F
from pyspark.sql import SparkSession

spark = SparkSession.builder.getOrCreate()
fact = spark.read.parquet("s3://lake/silver/fact_ventas")
dim = spark.read.parquet("s3://lake/silver/dim_tiempo")

joined = fact.join(F.broadcast(dim), "fecha_id")
joined.write.mode("overwrite").parquet("s3://lake/gold/ventas_by_fecha")
```

### Casos de Uso
- Pipeline de facturación que debe procesar 5 TB diarios con SLA de 90 minutos.
- Plataforma de marketing que combina batch nocturno con streaming para segmentación en tiempo real.
- Proyecto regulatorio que exige auditoría, control de acceso y versionado de datasets.
- Programa de migración a la nube que necesita automatizar Spark en Airflow/Databricks con monitoreo robusto.

### Ejemplo de Implementacion
1. Definir el alcance del proyecto final (datasets, SLA, métricas de negocio) y seleccionar entorno (EMR, Databricks, Synapse).  
2. Diseñar arquitectura: ingestión (batch/streaming), capas de almacenamiento (bronze/silver/gold), orquestación y herramientas de consumo.  
3. Implementar jobs Spark SQL y Structured Streaming optimizados (broadcast joins, AQE, particionamiento) y validar con `explain`.  
4. Configurar despliegue automatizado (`spark-submit`, jobs programados, notebooks) y versionar código con repositorios Git.  
5. Habilitar monitoreo y alertas: Spark History Server, métricas JMX a Prometheus y dashboards en Grafana o Datadog.  
6. Documentar runbooks de operación, estrategias de escalado, estimaciones de costo y plan de pruebas de resiliencia (reprocesos, errores de red).

### Comandos CLI o Web UI
- `spark-submit --conf spark.sql.adaptive.enabled=true job.py` para activar Adaptive Query Execution.
- `yarn application -list` y `yarn logs -applicationId <id>` para monitorear jobs en YARN.
- `spark-history-server` para revisar ejecuciones históricas y comparar DAGs.
- `airflow dags trigger spark_pipeline` para orquestar ejecuciones desde Airflow.
- `databricks jobs run-now --job-id <id>` para ejecutar pipelines administrados en Databricks (si aplica).

## Notas
### Cornell
<table>
  <tr><th>Pista / Pregunta</th><th>Notas</th></tr>
  <tr><td>Optimización</td><td>Ajustar particiones, usar broadcast, habilitar AQE, cache selectivo.</td></tr>
  <tr><td>Recursos</td><td>Configurar memoria, núcleos y número de ejecutores según carga.</td></tr>
  <tr><td>Monitoreo</td><td>Spark UI, History Server, métricas JMX, integración con Prometheus/Grafana.</td></tr>
  <tr><td>Proyecto final</td><td>Diseño end-to-end, automatización, documentación y pruebas de resiliencia.</td></tr>
</table>

### Outline Method
<table>
  <tr><th>Nivel</th><th>Idea</th></tr>
  <tr><td>I</td><td>Optimización de trabajos Spark</td></tr>
  <tr><td>II</td><td>Gestión de recursos y configuración del clúster</td></tr>
  <tr><td>III</td><td>Monitoreo, seguridad y operación continua</td></tr>
  <tr><td>III</td><td>Automatización y orquestación de pipelines</td></tr>
  <tr><td>II</td><td>Proyecto final con entregables operativos</td></tr>
</table>

## Resumen
La cuarta semana consolida el uso de Spark en producción: optimizar jobs, administrar recursos y asegurar observabilidad. Con estas prácticas, el proyecto final puede desplegarse con confianza, integrando batch y streaming, automatización y monitoreo alineados a objetivos de negocio.
