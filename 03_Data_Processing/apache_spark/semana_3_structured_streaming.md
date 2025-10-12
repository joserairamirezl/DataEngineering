# Semana 3: Structured Streaming y Procesamiento en Tiempo Real
## Texto
### Lectura
Structured Streaming es el motor de procesamiento de flujos de Spark que extiende la API de DataFrames para manejar datos en tiempo real. Se basa en el paradigma de micro-batches (o continuous processing experimental) que procesa datos incrementales mientras mantiene semántica declarativa similar a la de Spark SQL. Cada lote incremental se trata como una tabla inmutable, lo que permite aplicar agregaciones, joins y ventanas con lógica consistente. Los checkpoints y write-ahead logs (WAL) garantizan tolerancia a fallos al guardar offsets y estado en almacenamiento confiable.  
Las fuentes soportadas incluyen Kafka, sockets, archivos, Kinesis y Delta Live Tables. Los sinks permiten escribir en memoria, consola, archivos, Kafka, JDBC o Delta. Structured Streaming gestiona el estado de agregaciones mediante `state stores`, optimiza con `watermarks` para descartar datos atrasados y soporta diferentes garantías de entrega (*at-least-once*, *exactly-once* en ciertos sinks). Integrar triggers (`processingTime`, `once`) controla la cadencia de ejecución, mientras que la API SQL permite crear vistas temporales sobre streams.  
Para Data Engineering, Structured Streaming permite construir pipelines event-driven que alimentan dashboards, detección de fraude, ETL incremental y sincronizaciones near real-time. Su integración con métodos batch facilita mantener un único código que opera en lotes y flujos, simplificando mantenimiento y pruebas.

### Explicación con Técnica de Feynman
Piensa en Structured Streaming como una cinta transportadora que entrega paquetes pequeños de datos cada pocos segundos. Puedes aplicar las mismas recetas que usas en lotes, pero ahora en mini-lotes: sumar, filtrar o agrupar mientras llegan. Cada vez que terminas un conjunto, apuntas en un cuaderno dónde te quedaste (checkpoint). Así, si ocurre un apagón, simplemente lees el cuaderno y continúas desde el último paquete procesado.

### Ejemplos Simples
*Lectura desde Kafka y agregación por ventana:*
```python
from pyspark.sql import functions as F

df = (
    spark.readStream.format("kafka")
    .option("kafka.bootstrap.servers", "localhost:9092")
    .option("subscribe", "transacciones")
    .load()
)

datos = df.selectExpr("CAST(value AS STRING)")
agregado = (
    datos.withColumn("monto", F.col("value").cast("double"))
         .withWatermark("timestamp", "5 minutes")
         .groupBy(F.window("timestamp", "10 minutes"),)
         .agg(F.sum("monto").alias("total"))
)

query = (
    agregado.writeStream.outputMode("update")
    .format("console")
    .option("checkpointLocation", "/tmp/chk/transacciones")
    .start()
)
```

*Stream-to-Delta sink:*
```python
query = (
    datos.writeStream.format("delta")
    .outputMode("append")
    .option("checkpointLocation", "s3://chk/transacciones")
    .start("s3://lake/bronze/transacciones/")
)
```

### Casos de Uso
- Generar dashboards near real-time de ventas o métricas operativas.
- Detectar patrones de fraude aplicando umbrales sobre eventos financieros en streaming.
- Construir ETL incremental que actualiza tablas Delta o Parquet continuamente.
- Sincronizar datos de IoT entre Kafka y sistemas downstream con baja latencia.

### Ejemplo de Implementacion
1. Configurar fuente de datos streaming (Kafka, Kinesis o archivos en carpeta monitorizada).  
2. Crear `SparkSession` con dependencias requeridas (`spark-sql-kafka`, conectores).  
3. Definir transformaciones declarativas (parseo, limpieza, agregaciones, ventanas) empleando funciones SQL.  
4. Establecer `checkpointLocation` en almacenamiento durable (S3, HDFS) y seleccionar modo de salida (`append`, `update`, `complete`).  
5. Ajustar triggers y `watermark` para controlar latencia y manejo de late data.  
6. Monitorear la UI de Structured Streaming y métricas (`lastProgress`) para validar latencia, throughput y estado almacenado.

### Comandos CLI o Web UI
- `spark-submit --packages org.apache.spark:spark-sql-kafka-0-10_2.12:<version> stream.py` para habilitar conectores Kafka. 
- `nc -lk 9999` para simular una fuente de streaming por socket durante pruebas locales.
- `aws s3 cp --recursive s3://chk/transacciones/ ./checkpoint_backup` para respaldar checkpoints críticos.
- `curl http://<driver-host>:4040/api/v1/applications/<appId>/streaming/statistics` para extraer métricas de streams.
- `delta-table vacuum s3://lake/bronze/transacciones --retention-hours 168` para mantener almacenamiento limpio en sinks Delta.

## Notas
### Cornell
<table>
  <tr><th>Pista / Pregunta</th><th>Notas</th></tr>
  <tr><td>Structured Streaming</td><td>Extiende DataFrames con micro-batches declarativos y tolerancia a fallos.</td></tr>
  <tr><td>Checkpoints</td><td>Persisten offsets y estado; indispensables para reinicios seguros.</td></tr>
  <tr><td>Watermarks</td><td>Gestionan datos atrasados en ventanas, liberando estado antiguo.</td></tr>
  <tr><td>Sinks</td><td>Consola, archivos, Kafka, Delta; elegir según latencia y garantías deseadas.</td></tr>
</table>

### Outline Method
<table>
  <tr><th>Nivel</th><th>Idea</th></tr>
  <tr><td>I</td><td>Introducción a Structured Streaming</td></tr>
  <tr><td>II</td><td>Arquitectura de micro-batches y checkpoints</td></tr>
  <tr><td>III</td><td>Fuentes, transformaciones y sinks principales</td></tr>
  <tr><td>III</td><td>Garantías de entrega, watermarks y triggers</td></tr>
  <tr><td>II</td><td>Monitoreo y operación de pipelines en tiempo real</td></tr>
</table>

## Resumen
Structured Streaming aporta procesamiento en tiempo real a Spark reutilizando la API declarativa de DataFrames. Al combinar checkpoints, watermarks y sinks confiables, habilita pipelines event-driven resilientes que mantienen latencia baja sin sacrificar consistencia ni simplicidad de desarrollo.
