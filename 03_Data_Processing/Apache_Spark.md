# Apache Spark

## Texto
### Lectura

Apache Spark es un motor de procesamiento de datos distribuido y de código abierto diseñado para manejar big data analytics de manera rápida y eficiente. Desarrollado en UC Berkeley y posteriormente donado a la Apache Software Foundation, Spark revolucionó el procesamiento de grandes volúmenes de datos al introducir el concepto de **Resilient Distributed Datasets (RDDs)** y posteriormente los **DataFrames** y **Datasets**, que permiten operaciones en memoria hasta 100 veces más rápidas que los sistemas tradicionales basados en MapReduce.

La arquitectura de Spark se fundamenta en un modelo **master-worker** donde el **Driver Program** coordina la ejecución de tareas distribuidas a través de múltiples **Executors** que corren en diferentes nodos del cluster. El **Spark Context** actúa como el punto de entrada principal que gestiona la conexión con el cluster manager (YARN, Kubernetes, Mesos o Standalone), mientras que el **Cluster Manager** se encarga de la asignación de recursos. Esta arquitectura permite que Spark ejecute aplicaciones de manera resiliente, recuperándose automáticamente de fallos de nodos mediante el lineage de transformaciones almacenado en los RDDs.

Una característica distintiva de Spark es su **modelo de programación unificado** que integra múltiples paradigmas de procesamiento bajo una sola plataforma. **Spark Core** proporciona las funcionalidades básicas de computación distribuida, mientras que **Spark SQL** permite consultas SQL sobre datos estructurados y semi-estructurados. **Spark Streaming** (y su sucesor **Structured Streaming**) habilita el procesamiento de streams en tiempo real, **MLlib** ofrece algoritmos de machine learning escalables, y **GraphX** facilita el procesamiento de grafos. Esta convergencia elimina la necesidad de múltiples herramientas especializadas y simplifica significativamente las pipelines de datos.

El **Catalyst Optimizer** es el cerebro detrás del rendimiento superior de Spark SQL y DataFrames. Este optimizador basado en reglas analiza las consultas y genera planes de ejecución optimizados mediante técnicas como predicate pushdown, column pruning, y join reordering. Combined con **Tungsten**, el motor de ejecución vectorizada que opera directamente sobre memoria binaria, Spark logra performance comparable a sistemas nativos escritos en C++, mientras mantiene la expresividad y facilidad de uso de lenguajes de alto nivel como Scala, Python y Java.

La **gestión de memoria** en Spark utiliza un modelo híbrido que combina heap memory con off-heap storage para optimizar tanto performance como garbage collection. El **Unified Memory Manager** administra dinámicamente la memoria entre execution y storage, adaptándose automáticamente a los patrones de uso de cada aplicación. Las **particiones inteligentes** distribuyen datos basándose en características como tamaño, localidad y patterns de acceso, mientras que técnicas como **columnar storage** y **compression** minimizan el footprint de memoria y maximizan el throughput de I/O.

### Explicación con Técnica de Feynman

Imagina que Apache Spark es como una **fábrica súper inteligente** que puede procesar enormes cantidades de materiales (datos) de manera muy eficiente.

**El Driver es como el gerente de la fábrica** que coordina todo el trabajo. Este gerente recibe un proyecto grande (tu programa) y lo divide en tareas más pequeñas que pueden hacerse al mismo tiempo.

**Los Executors son como equipos de trabajadores especializados** distribuidos en diferentes pisos de la fábrica. Cada equipo puede trabajar independientemente en su parte del proyecto, pero todos siguen las instrucciones del gerente.

**Los RDDs son como contenedores inteligentes** que guardan los materiales de manera que si un contenedor se rompe o se pierde, la fábrica puede recrearlo automáticamente porque recuerda cómo se hizo.

La parte más genial es que **toda la fábrica puede trabajar en la memoria** (como tener todo en mesas de trabajo) en lugar de tener que guardar y buscar cosas en el almacén constantemente. Esto hace que todo sea muchísimo más rápido.

**Spark tiene diferentes departamentos especializados**: 
- Un departamento de consultas (Spark SQL) que entiende preguntas en lenguaje normal
- Un departamento de transmisión en vivo (Streaming) que procesa materiales que llegan continuamente
- Un departamento de inteligencia artificial (MLlib) que encuentra patrones en los materiales
- Un departamento de redes (GraphX) que entiende cómo las cosas están conectadas

Lo mejor es que **todos estos departamentos comparten la misma infraestructura** y pueden trabajar juntos sin problemas, como si fueran parte de la misma fábrica súper eficiente.

### Ejemplos Simples

**Análisis de Logs Web:**
- Datos: Archivos de logs de servidor web con millones de registros diarios
- Procesamiento: Filtrar errores 404, contar visitas por página, identificar IPs más activas
- Output: Dashboard con métricas de tráfico y errores en tiempo real

**Procesamiento de Ventas:**
- Datos: Transacciones de e-commerce desde múltiples tiendas y canales
- Procesamiento: Agregar ventas por región, calcular productos más vendidos, detectar patrones estacionales
- Output: Reportes ejecutivos y predicciones de demanda

**Análisis de Redes Sociales:**
- Datos: Posts, likes, comentarios y shares de plataforma social
- Procesamiento: Calcular engagement rates, identificar trending topics, analizar sentiment
- Output: Métricas de contenido y recomendaciones de audiencia

**Limpieza de Datos de IoT:**
- Datos: Lecturas de sensores con ruido y valores faltantes
- Procesamiento: Filtrar outliers, interpolar valores perdidos, normalizar escalas
- Output: Dataset limpio listo para machine learning

### Casos de Uso

**Real-time Fraud Detection en Fintech:**
Bancos utilizan Spark Streaming para analizar transacciones en tiempo real, aplicando modelos ML que detectan patrones fraudulentos basándose en ubicación geográfica, patrones de gasto y comportamiento histórico. El sistema procesa millones de transacciones por segundo, generando alerts instantáneos y bloqueando transacciones sospechosas automáticamente.

**Recommendation Systems a Gran Escala:**
Plataformas como Netflix y Spotify emplean Spark MLlib para procesar terabytes de datos de comportamiento de usuarios, generando recomendaciones personalizadas mediante collaborative filtering y matrix factorization. El sistema actualiza modelos continuamente basándose en interacciones recientes, mejorando la precisión de recomendaciones en tiempo real.

**ETL Pipelines para Data Lakes:**
Organizaciones empresariales utilizan Spark para procesar datos batch desde múltiples fuentes (databases, APIs, files), aplicando transformaciones complejas como joins entre datasets masivos, agregaciones temporales y data quality checks. Los resultados se almacenan en formatos optimizados como Parquet en data lakes para análisis posteriores.

**Genomics y Bioinformática:**
Institutos de investigación médica procesan secuencias de ADN utilizando Spark para identificar variaciones genéticas asociadas con enfermedades. El sistema maneja datasets de petabytes, ejecutando algoritmos de alignment y variant calling distribuidos a través de clusters de cientos de nodos.

**Supply Chain Optimization:**
Empresas manufactureras emplean Spark para optimizar cadenas de suministro analizando datos de inventario, demanda histórica, patrones climáticos y eventos geopolíticos. El sistema genera predicciones de demanda y optimiza rutas de distribución mediante algoritmos de graph processing en GraphX.

**Ad-Tech y Real-time Bidding:**
Plataformas de publicidad digital utilizan Spark Streaming para procesar bid requests en tiempo real, aplicando modelos ML que predicen probabilidad de click y optimizan pujas automáticamente. El sistema maneja millones de requests por segundo con latencias sub-100ms.

### Ejemplo de Implementación

**Cluster Configuration y Resource Management:**
- Configurar cluster Spark con YARN o Kubernetes como resource manager
- Establecer dynamic allocation para scaling automático basado en workload
- Configurar appropriate executor memory, cores y número de executors por aplicación
- Implementar fair scheduler para compartir recursos entre múltiples users y aplicaciones
- Establecer monitoring con Spark UI, Ganglia y custom metrics para observability

**Data Source Integration y Optimization:**
- Configurar conectores para múltiples fuentes: HDFS, S3, databases, Kafka streams
- Implementar partitioning strategies que minimicen data shuffling y maximicen locality
- Utilizar appropriate file formats (Parquet, Delta Lake) con compression para optimal I/O
- Configurar predicate pushdown y column pruning para minimizar data scanning
- Establecer caching strategies para datasets accessed múltiples veces

**Application Development Best Practices:**
- Diseñar transformaciones que minimicen expensive operations como joins y groupBy
- Implementar appropriate partitioning keys para evitar data skew
- Utilizar broadcast variables para lookup tables pequeñas shared across executors
- Configurar appropriate parallelism levels basados en cluster capacity y data characteristics
- Implementar checkpointing para long-running streaming applications

**Performance Tuning y Memory Management:**
- Configurar Tungsten para off-heap memory management y vectorized execution
- Ajustar garbage collection settings para minimizar pause times
- Implementar appropriate serialization (Kryo vs Java) para network efficiency
- Configurar adaptive query execution para runtime optimization
- Establecer appropriate storage levels para persistent RDDs y DataFrames

### Comandos CLI o Web UI

**Spark Application Submission:**
```bash
# Enviar aplicación Spark al cluster
spark-submit \
  --class com.company.DataProcessor \
  --master yarn \
  --deploy-mode cluster \
  --executor-memory 4g \
  --executor-cores 2 \
  --num-executors 10 \
  --conf spark.sql.adaptive.enabled=true \
  application.jar input-path output-path

# Spark Shell interactivo con configuración
spark-shell \
  --master yarn \
  --executor-memory 2g \
  --executor-cores 2 \
  --conf spark.sql.warehouse.dir=/user/warehouse
```

**Monitoring y Debugging:**
```bash
# Acceder a Spark History Server
spark-class org.apache.spark.deploy.history.HistoryServer

# Verificar aplicaciones running
yarn application -list -appStates RUNNING

# Logs de aplicación específica
yarn logs -applicationId application_1234567890123_0001

# Monitoring de recursos del cluster
yarn top
```

**Spark SQL Interactive:**
```sql
-- Crear tabla temporal desde archivo
CREATE TEMPORARY VIEW sales 
USING PARQUET 
OPTIONS (path "/data/sales/2024/");

-- Query optimizada con pushdown
SELECT region, product_category, 
       SUM(sales_amount) as total_sales
FROM sales 
WHERE date >= '2024-01-01' 
  AND region IN ('US', 'EU')
GROUP BY region, product_category
ORDER BY total_sales DESC;

-- Análisis de performance de query
EXPLAIN COST 
SELECT * FROM large_table a 
JOIN small_table b ON a.key = b.key;
```

**Streaming Applications:**
```bash
# Structured Streaming desde Kafka
spark-submit \
  --packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.4.0 \
  --class StreamProcessor \
  streaming-app.jar

# Checkpointing para fault tolerance
spark-submit \
  --conf spark.sql.streaming.checkpointLocation=/checkpoints/app1 \
  streaming-app.jar
```

**Cluster Management:**
```bash
# Iniciar Spark Master
start-master.sh

# Agregar Worker al cluster
start-worker.sh spark://master-host:7077

# Verificar status del cluster
spark-class org.apache.spark.deploy.Client \
  -c spark://master-host:7077 status driver-id

# Dynamic scaling de executors
spark-submit \
  --conf spark.dynamicAllocation.enabled=true \
  --conf spark.dynamicAllocation.minExecutors=1 \
  --conf spark.dynamicAllocation.maxExecutors=20 \
  application.jar
```

## Notas
### Cornell

<table border="1" style="width:100%">
<tr>
<th style="width:30%">Conceptos Clave</th>
<th style="width:70%">Detalles y Explicaciones</th>
</tr>
<tr>
<td><strong>RDD vs DataFrame vs Dataset</strong></td>
<td>RDD: Low-level API con control total pero sin optimizaciones. DataFrame: High-level API con Catalyst optimizer, schema-aware. Dataset: Type-safe version de DataFrame con compile-time checking. DataFrames preferidos para mayoría de casos por balance performance/usabilidad.</td>
</tr>
<tr>
<td><strong>Lazy Evaluation</strong></td>
<td>Transformaciones son lazy (no ejecutan inmediatamente), Actions trigger execution. Permite Catalyst optimizar entire query plan antes de execution. Transformations: map, filter, join. Actions: collect, count, save. Estrategia clave para performance optimization.</td>
</tr>
<tr>
<td><strong>Partitioning y Data Locality</strong></td>
<td>Data distributed across partitions para paralelismo. Hash partitioning, range partitioning, custom partitioners. Data locality minimiza network I/O. Repartition vs coalesce para partition management. Partition size optimal: 100MB-1GB por partition.</td>
</tr>
<tr>
<td><strong>Catalyst Optimizer</strong></td>
<td>Rule-based optimizer para Spark SQL y DataFrames. Predicate pushdown, column pruning, join reordering, constant folding. Genera efficient physical plans desde logical plans. Extensible mediante custom optimization rules. Core del superior performance de Spark SQL.</td>
</tr>
<tr>
<td><strong>Shuffle Operations</strong></td>
<td>Expensive operations que redistribuyen data across partitions: groupBy, join, distinct. Involve disk I/O y network transfer. Minimizar mediante proper partitioning y broadcast joins. Tungsten shuffle manager optimiza performance mediante off-heap operations.</td>
</tr>
</table>

### Outline Method

<table border="1" style="width:100%">
<tr>
<th style="width:20%">Nivel 1</th>
<th style="width:25%">Nivel 2</th>
<th style="width:30%">Nivel 3</th>
<th style="width:25%">Detalles</th>
</tr>
<tr>
<td rowspan="5"><strong>Core Architecture</strong></td>
<td>Driver Program</td>
<td>Application Coordinator</td>
<td>SparkContext, job scheduling</td>
</tr>
<tr>
<td>Executors</td>
<td>Worker Processes</td>
<td>Task execution, data storage</td>
</tr>
<tr>
<td>Cluster Manager</td>
<td>Resource Management</td>
<td>YARN, Kubernetes, Mesos, Standalone</td>
</tr>
<tr>
<td>RDD Abstraction</td>
<td>Distributed Collections</td>
<td>Fault tolerance, lazy evaluation</td>
</tr>
<tr>
<td>Memory Management</td>
<td>Unified Memory Manager</td>
<td>Execution vs storage memory</td>
</tr>
<tr>
<td rowspan="5"><strong>Programming APIs</strong></td>
<td>Spark Core</td>
<td>RDD Operations</td>
<td>Transformations, actions, persistence</td>
</tr>
<tr>
<td>Spark SQL</td>
<td>Structured Data</td>
<td>DataFrames, Datasets, Catalyst</td>
</tr>
<tr>
<td>Streaming</td>
<td>Real-time Processing</td>
<td>DStreams, Structured Streaming</td>
</tr>
<tr>
<td>MLlib</td>
<td>Machine Learning</td>
<td>Algorithms, pipelines, model selection</td>
</tr>
<tr>
<td>GraphX</td>
<td>Graph Processing</td>
<td>Graph algorithms, property graphs</td>
</tr>
<tr>
<td rowspan="4"><strong>Performance Optimization</strong></td>
<td>Catalyst Optimizer</td>
<td>Query Optimization</td>
<td>Rule-based optimization, code generation</td>
</tr>
<tr>
<td>Tungsten Engine</td>
<td>Execution Engine</td>
<td>Off-heap memory, vectorization</td>
</tr>
<tr>
<td>Adaptive Query Execution</td>
<td>Runtime Optimization</td>
<td>Dynamic partition pruning, join selection</td>
</tr>
<tr>
<td>Caching Strategies</td>
<td>Memory Management</td>
<td>Storage levels, LRU eviction</td>
</tr>
</table>

## Resumen

Apache Spark ha revolucionado el procesamiento de big data al unificar múltiples paradigmas de computación bajo una plataforma coherente y de alto rendimiento. Su arquitectura basada en **RDDs inmutables** y **lazy evaluation** permite fault tolerance automático y optimizaciones inteligentes, mientras que el **Catalyst Optimizer** y **Tungsten engine** proporcionan performance comparable a sistemas nativos.

Las **ventajas clave** incluyen: processing en memoria hasta 100x más rápido que MapReduce, API unificada para batch y streaming, ecosistema integrado con SQL/ML/Graph processing, y compatibilidad con múltiples cluster managers y storage systems. Esta convergencia elimina la complejidad de mantener múltiples herramientas especializadas.

**Aplicando Pareto 80/20**: El 80% del valor de Spark se obtiene dominando el 20% crítico: entender RDD/DataFrame abstractions, optimizar partitioning strategies, configurar appropriate resource allocation, y implementar efficient caching. Master estos fundamentos garantiza aplicaciones Spark exitosas y escalables.

La evolución hacia **Spark 3.x** con Adaptive Query Execution, GPU acceleration y mejor integración con Kubernetes posiciona a Spark como la plataforma definitiva para unified analytics, especialmente en contextos de lakehouse architectures y cloud-native data processing.
