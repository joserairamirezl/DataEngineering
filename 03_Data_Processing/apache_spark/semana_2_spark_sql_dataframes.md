# Semana 2: Spark SQL y DataFrames
## Texto
### Lectura
Spark SQL introduce una capa estructurada sobre Spark que permite trabajar con datos tabulares mediante DataFrames y consultas SQL unificadas. Un DataFrame es una colección distribuida organizada en columnas, respaldada por el motor Catalyst que optimiza consultas y aplica reglas de planificación lógica y física. Gracias al formato columnar y al almacenamiento en memoria, Spark SQL ofrece un rendimiento superior en comparaciones, filtrados y agregaciones frente a RDDs puros.  
El motor soporta múltiples fuentes: CSV, JSON, Parquet, ORC, JDBC y catálogos como Hive Metastore o Glue. Las vistas temporales y las tablas permanentes habilitan consultas interactivas desde SQL, mientras que el DataFrame API en Python, Scala o Java integra funcionalidad declarativa con funciones de ventana, UDF/UDAF y operaciones complejas. El Tungsten Engine optimiza ejecución a nivel de bytecode y administración de memoria off-heap, reduciendo overhead de la JVM.  
Para Data Engineering, dominar Spark SQL permite construir pipelines ETL que leen, limpian, agregan y almacenan datasets en formatos eficientes. Además, facilita interoperar con herramientas BI que se conectan mediante JDBC/ODBC, manteniendo un único motor de procesamiento. La capacidad de definir esquemas explícitos y aplicar validaciones de calidad ayuda a garantizar consistencia en el data lake.

### Explicación con Técnica de Feynman
Imagina que un DataFrame es como una hoja de cálculo gigante repartida en varias mesas. Spark SQL actúa como un supervisor que entiende instrucciones en lenguaje natural (SQL) y decide cómo dividir el trabajo entre las mesas para que todos calculen resultados rápidamente. El supervisor conoce trucos (optimizaciones) para evitar repetir operaciones y reacomoda los cálculos en un orden más eficiente antes de que alguien empiece a trabajar.

### Ejemplos Simples
*Lectura de CSV y consulta SQL:*
```python
df = spark.read.option("header", True).csv("s3://datos/ventas.csv")
df.createOrReplaceTempView("ventas")

resultado = spark.sql("""
  SELECT region, SUM(cantidad) AS total
  FROM ventas
  GROUP BY region
""")
resultado.show()
```

*Uso de funciones de ventana:*
```python
from pyspark.sql import functions as F, Window

ventana = Window.partitionBy("region").orderBy(F.desc("ingresos"))
df_con_rank = df.withColumn("ranking", F.dense_rank().over(ventana))
df_con_rank.show()
```

### Casos de Uso
- Transformar datasets crudos en tablas limpias y particionadas (bronze → silver → gold).
- Ejecutar agregaciones masivas para reportes financieros o métricas operativas.
- Enriquecer datos combinando fuentes JDBC y archivos Parquet en una única consulta.
- Preparar datasets para machine learning generando features agregados.

### Ejemplo de Implementacion
1. Definir `SparkSession` con soporte a Hive y catálogos externos (`enableHiveSupport`).  
2. Cargar datos desde múltiples fuentes (CSV, Parquet, JDBC) especificando esquemas y opciones de lectura.  
3. Registrar vistas temporales o tablas permanentes para permitir consultas SQL reutilizables.  
4. Diseñar transformaciones con funciones integradas, expresiones SQL y ventanas, asegurando particionamiento adecuado.  
5. Escribir resultados en formatos columnares (Parquet/Delta) con particiones y compresión (`snappy`, `zstd`).  
6. Verificar planes de ejecución (`df.explain(True)`) y tunear `spark.sql.shuffle.partitions` según el tamaño de datos.

### Comandos CLI o Web UI
- `spark-sql -f consulta.sql` para ejecutar scripts SQL directamente en el clúster.
- `beeline -u "jdbc:hive2://<host>:10000/default"` para conectarse a HiveServer2 respaldado por Spark thrift server.
- `spark-submit --packages org.postgresql:postgresql:42.6.0 job.py` para incluir conectores JDBC en la ejecución.
- `aws s3 ls s3://datos/ventas/` para validar estructuras de particionamiento antes de cargar en Spark.
- `curl -X GET http://<driver-host>:4040/api/v1/applications` para inspeccionar planes de ejecución vía Spark UI REST.

## Notas
### Cornell
<table>
  <tr><th>Pista / Pregunta</th><th>Notas</th></tr>
  <tr><td>DataFrame</td><td>Abstracción columnar optimizada por Catalyst; interoperable con APIs y SQL.</td></tr>
  <tr><td>Fuentes soportadas</td><td>CSV, JSON, Parquet, ORC, JDBC, catálogos Hive/Glue.</td></tr>
  <tr><td>Optimización</td><td>Catalyst planifica lógicamente y físicamente; Tungsten gestiona memoria eficiente.</td></tr>
  <tr><td>Buenas prácticas</td><td>Definir esquemas, particionar salidas, revisar `explain`, ajustar `shuffle.partitions`.</td></tr>
</table>

### Outline Method
<table>
  <tr><th>Nivel</th><th>Idea</th></tr>
  <tr><td>I</td><td>Spark SQL como capa estructurada</td></tr>
  <tr><td>II</td><td>DataFrames y consultas SQL declarativas</td></tr>
  <tr><td>III</td><td>Fuentes de datos y formatos columnares</td></tr>
  <tr><td>III</td><td>Funciones avanzadas: ventanas, UDF, persistencia</td></tr>
  <tr><td>II</td><td>Optimización y mejores prácticas operativas</td></tr>
</table>

## Resumen
Spark SQL habilita pipelines estructurados declarativos apoyados en DataFrames optimizados por Catalyst. Dominar la lectura de múltiples fuentes, la construcción de consultas avanzadas y la escritura eficiente en formatos columnares permite entregar datasets confiables y de alto rendimiento dentro del ecosistema de datos.
