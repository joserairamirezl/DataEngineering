# Semana 1: Fundamentos y Arquitectura de Apache Spark
## Texto
### Lectura
Apache Spark es un motor de procesamiento distribuido diseñado para ejecutar cargas de trabajo de Big Data con alta velocidad y tolerancia a fallos. Basado en memoria y optimizaciones de planificación, Spark supera las limitaciones de Hadoop MapReduce al minimizar escrituras a disco intermedias. Su arquitectura consta de un driver program que coordina tareas y un conjunto de ejecutores distribuidos en un clúster. La abstracción fundamental son los Resilient Distributed Datasets (RDD), colecciones inmutables particionadas que se procesan en paralelo.  
Spark soporta múltiples APIs (Scala, Python, SQL) y módulos especializados: Spark SQL para datos estructurados, MLlib para machine learning, GraphX para grafos y Structured Streaming para flujos en tiempo real. El clúster puede ejecutarse en modo standalone o sobre gestores como YARN, Kubernetes o Mesos. El planificador de Spark combina DAG Scheduler y Task Scheduler para optimizar transformaciones y acciones, aplicando tolerancia a fallos mediante lineage que reconstruye particiones perdidas.  
Para Data Engineering, comprender la arquitectura de clúster, el ciclo de DAGs y los conceptos de transformación perezosa es crucial. Permite diseñar pipelines eficientes, seleccionar el modo de despliegue adecuado y aprovechar caché en memoria para acelerar análisis repetitivos o ETL.

### Explicación con Técnica de Feynman
Imagina Spark como un equipo de cocina industrial. El chef principal (driver) decide la receta y divide las tareas. Cada cocinero (ejecutor) trabaja en su estación, preparando una porción del platillo (partición) siguiendo las instrucciones. Si un cocinero se retrasa o se va, el chef asigna su tarea a otro gracias a la lista de pasos (lineage). Nada se sirve hasta que el chef dice “acción”, así que los ingredientes (transformaciones) se preparan mentalmente hasta que se necesita el plato final.

### Ejemplos Simples
*Inicializar SparkSession en PySpark:*
```python
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("fundamentos").getOrCreate()
datos = [("A", 10), ("B", 20), ("C", 30)]
df = spark.createDataFrame(datos, ["categoria", "valor"])
df.show()
```

*Transformaciones y acción con RDD:*
```python
rdd = spark.sparkContext.parallelize([1, 2, 3, 4])
dobles = rdd.map(lambda x: x * 2)  # transformación perezosa
resultado = dobles.collect()       # acción que dispara el trabajo
print(resultado)
```

### Casos de Uso
- Consolidar logs masivos de aplicaciones web en pipelines batch diarios.
- Procesar grandes volúmenes de datos financieros para reportes regulatorios.
- Limpiar y transformar datos crudos en data lakes para consumo analítico.
- Ejecutar notebooks exploratorios sobre datasets de terabytes sin replicar a bases tradicionales.

### Ejemplo de Implementacion
1. Instalar Apache Spark localmente o aprovisionar un clúster en AWS EMR, Databricks o Kubernetes.  
2. Configurar variables de entorno (`SPARK_HOME`, `PATH`) y dependencias (Java, Python).  
3. Crear un proyecto PySpark o Scala, inicializando `SparkSession` y validando lectura de archivos locales o S3.  
4. Definir transformaciones sobre RDD o DataFrames y observar el DAG generado en la UI para entender dependencias.  
5. Experimentar con `cache()` y `persist()` para datos reutilizados y comparar tiempos.  
6. Documentar lecciones aprendidas sobre configuración de driver, ejecutores y memoria para próximos ejercicios.

### Comandos CLI o Web UI
- `spark-shell` para iniciar una sesión interactiva en Scala y explorar RDD/DataFrames.
- `pyspark` para lanzar una consola Python respaldada por SparkSession.
- `spark-submit --master local[2] app.py` para ejecutar scripts PySpark controlando número de threads locales.
- `spark-submit --master yarn --deploy-mode cluster app.py` para enviar trabajos a YARN desde la terminal.
- `tail -f $SPARK_HOME/logs/*driver*.log` para monitorear logs del driver durante la ejecución.

## Notas
### Cornell
<table>
  <tr><th>Pista / Pregunta</th><th>Notas</th></tr>
  <tr><td>Arquitectura</td><td>Driver coordina, ejecutores procesan; clúster standalone, YARN, Kubernetes.</td></tr>
  <tr><td>RDD</td><td>Colecciones distribuidas inmutables; tolerancia a fallos por lineage.</td></tr>
  <tr><td>Transformaciones vs acciones</td><td>Transformaciones perezosas construyen DAG; acciones disparan ejecución.</td></tr>
  <tr><td>Módulos</td><td>Spark SQL, Structured Streaming, MLlib, GraphX amplían capacidades del motor base.</td></tr>
</table>

### Outline Method
<table>
  <tr><th>Nivel</th><th>Idea</th></tr>
  <tr><td>I</td><td>Visión general de Apache Spark</td></tr>
  <tr><td>II</td><td>Componentes del clúster: driver, ejecutores, clúster manager</td></tr>
  <tr><td>III</td><td>RDD y transformaciones perezosas</td></tr>
  <tr><td>III</td><td>APIs y módulos especializados</td></tr>
  <tr><td>II</td><td>Primeros pasos prácticos y mejores prácticas básicas</td></tr>
</table>

## Resumen
Spark habilita procesamiento distribuido eficiente gracias a su arquitectura basada en memoria, DAGs y RDDs. Comprender el papel del driver, los ejecutores y las transformaciones perezosas permite construir pipelines ETL escalables y sentar las bases para módulos avanzados de Spark en las siguientes semanas.
