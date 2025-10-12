# 🧭 Plan de Estudio Mensual

**Curso:** Data Engineering
**Módulo:** 03_Data_Processing
**Tema:** Apache Spark

---

## 🎯 Objetivo del Mes

Comprender los fundamentos, arquitectura y ecosistema de Apache Spark para construir y optimizar procesos de **procesamiento distribuido** (batch y streaming) en grandes volúmenes de datos, integrando conceptos de **RDDs**, **DataFrames**, y **Spark SQL** con un enfoque orientado al rendimiento y buenas prácticas.

---

## 🧩 Resultado Final

Al finalizar el mes, serás capaz de **diseñar y ejecutar un pipeline de procesamiento distribuido** con Apache Spark, realizando transformaciones, agregaciones y análisis sobre grandes datasets, tanto en modo batch como en streaming, con despliegue local o en la nube (AWS EMR, Databricks o Glue).

---

## 📅 Semana 1 – Fundamentos y Arquitectura de Spark

**Objetivo:** Comprender la arquitectura distribuida de Spark y su ecosistema base para procesamiento paralelo.

### Temas Claves

* Qué es Apache Spark y su historia (MapReduce → Spark)
* Arquitectura: Driver, Executor, Cluster Manager
* Conceptos base: RDD, DAG, Transformations vs Actions
* SparkContext, Jobs, Stages, Tasks
* Instalación local o entorno en Databricks Community Edition

### Actividades Prácticas

* Instalar PySpark localmente o usar Databricks CE
* Leer un dataset CSV y aplicar transformaciones (`map`, `filter`, `reduceByKey`)
* Visualizar el plan de ejecución (DAG) desde la UI de Spark
* Calcular métricas simples (promedios, conteos) con RDDs

---

## 📅 Semana 2 – DataFrames y Spark SQL

**Objetivo:** Usar el modelo estructurado de Spark SQL y DataFrames para análisis declarativos y eficientes.

### Temas Claves

* Limitaciones de RDD → evolución hacia DataFrame y Dataset
* Creación de DataFrames desde CSV, Parquet, JSON
* Operaciones comunes: `select`, `filter`, `groupBy`, `agg`
* *Lazy Evaluation* y optimizador Catalyst
* Consultas SQL sobre DataFrames
* Formatos columnar (Parquet/ORC) y particionamiento

### Actividades Prácticas

* Cargar datasets (ventas, logs o sensores) en Parquet y ejecutar queries SQL
* Comparar tiempos entre RDD y DataFrame
* Usar `explain()` para ver el plan lógico y físico
* Crear una tabla temporal y consultar con Spark SQL

---

## 📅 Semana 3 – Spark Streaming y Procesamiento en Tiempo Real

**Objetivo:** Aprender a procesar flujos de datos en tiempo real con Spark Structured Streaming.

### Temas Claves

* Conceptos: micro-batch vs stream continuo
* Fuentes: Kafka, Socket, Files streaming
* *Watermarking*, *windowing* y *checkpointing*
* Operaciones stateful y agregaciones temporales
* Integración con Kafka → Spark Streaming → sink Parquet/console

### Actividades Prácticas

* Crear un streaming job que lea de Kafka o socket (local)
* Aplicar transformaciones (`groupBy`, `count`, `window`)
* Escribir resultados en Parquet o consola
* Visualizar procesamiento en Spark UI en tiempo real

---

## 📅 Semana 4 – Optimización, Tuning y Proyecto Final

**Objetivo:** Consolidar el conocimiento optimizando jobs y diseñando un pipeline completo de procesamiento.

### Temas Claves

* *Shuffle*, particiones y *wide transformations*
* Configuración de memoria y ejecutores
* *Broadcast joins*, *caching* y *checkpointing*
* *Adaptive Query Execution (AQE)*
* Arquitectura de referencia: Spark en AWS EMR o Databricks

### Actividades Prácticas

* Medir rendimiento con y sin cache en DataFrames
* Aplicar *repartition* y *coalesce* para optimizar procesos
* Configurar variables (`spark.sql.shuffle.partitions`, `executor.memory`)
* Ejecutar una pipeline de inicio a fin (ingestión → procesamiento → output)

---

## 💡 Proyecto Opcional del Mes

**Título:** “Pipeline de Procesamiento Analítico de Ventas con Apache Spark”

**Descripción:**
Diseña un pipeline de procesamiento batch + streaming usando Spark para simular una empresa de retail:

1. **Ingesta:** Leer archivos CSV/JSON desde S3 o local.
2. **Procesamiento Batch:** Limpieza y agregación de ventas por día, país y producto.
3. **Procesamiento Streaming:** Simular ventas en tiempo real (vía Kafka o socket).
4. **Output:** Escribir resultados en Parquet y consultar con Spark SQL o Athena.

**Extras (para nivel avanzado):**

* Añadir alertas de fraude en tiempo real usando *window aggregations*.
* Integrar monitoreo con Prometheus + Grafana para Spark metrics.

---

## 📚 Recursos Recomendados

### 📘 Libros y Documentación

* *Learning Spark (2nd Edition)* – Jules Damji (O’Reilly)
* *High Performance Spark* – Holden Karau & Rachel Warren
* [Documentación oficial de Apache Spark](https://spark.apache.org/docs/latest/)

### 🎥 Cursos y Tutoriales

* Databricks Academy – *Introduction to Apache Spark*
* Udemy – *Apache Spark for Data Engineers (PySpark)*
* YouTube – Krish Naik / Data Engineer One / Conduktor Academy

### 🧰 Herramientas Recomendadas

* **Databricks Community Edition** (ideal para entornos gratuitos)
* **AWS Glue / EMR** para ejecutar Spark en la nube
* **Jupyter + PySpark** para entornos locales de aprendizaje
* **Spark UI + Prometheus/Grafana** para monitoreo y tuning

---

¿Quieres que te genere también una **versión diaria (lunes a viernes)** para este mismo plan — ideal si estudiarás 1 hora por día con teoría + práctica guiada?
