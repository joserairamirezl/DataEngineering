# Datawarehouse, Datalake y Lakehouse

## Texto
### Lectura

En el ecosistema de Data Engineering, la evolución de las arquitecturas de almacenamiento de datos ha sido fundamental para gestionar el creciente volumen, velocidad y variedad de información empresarial. Tres conceptos centrales dominan este panorama: **Data Warehouse**, **Data Lake** y **Lakehouse**, cada uno representando una respuesta específica a diferentes necesidades y desafíos tecnológicos.

Un **Data Warehouse** es una solución de almacenamiento estructurada y optimizada para análisis y reportes empresariales. Se caracteriza por implementar un esquema definido antes de la carga de datos (schema-on-write), lo que garantiza alta calidad y consistencia de la información. Los data warehouses utilizan arquitecturas como el modelo estrella o copo de nieve, donde los datos se organizan en tablas de hechos y dimensiones. Esta estructura permite consultas rápidas y eficientes mediante tecnologías como columnar storage y índices especializados. Sin embargo, su rigidez estructural limita la capacidad de adaptarse rápidamente a nuevos tipos de datos o cambios en los requisitos de negocio.

Por otro lado, un **Data Lake** surge como respuesta a la necesidad de almacenar datos diversos y no estructurados a gran escala. Opera bajo el principio de schema-on-read, permitiendo almacenar datos en su formato nativo sin transformaciones previas. Esta flexibilidad facilita la ingesta de datos desde múltiples fuentes: logs de aplicaciones, IoT, redes sociales, documentos, imágenes y videos. Los data lakes aprovechan sistemas de almacenamiento distribuido como HDFS o Amazon S3, ofreciendo escalabilidad horizontal y costos reducidos. No obstante, esta flexibilidad puede derivar en "data swamps" si no se implementan adecuadas prácticas de gobierno y catalogación de datos.

El concepto de **Lakehouse** emerge como una arquitectura híbrida que combina la flexibilidad del data lake con las garantías transaccionales y de rendimiento del data warehouse. Utiliza formatos de almacenamiento abiertos como Delta Lake, Apache Iceberg o Apache Hudi, que proporcionan características ACID, versionado de datos y optimizaciones de rendimiento sobre sistemas de archivos distribuidos. Esta convergencia permite ejecutar tanto cargas de trabajo de machine learning como análisis tradicional de BI sobre la misma plataforma, eliminando la necesidad de múltiples copias de datos y reduciendo la complejidad operacional.

### Explicación con Técnica de Feynman

Imagina que tienes una biblioteca gigante donde necesitas organizar diferentes tipos de información. Hay tres formas principales de hacerlo:

**Data Warehouse** es como una biblioteca tradicional muy organizada. Todos los libros están perfectamente catalogados, ordenados por categorías específicas y colocados en estantes numerados. Encontrar información es súper rápido porque sabes exactamente dónde buscar. Pero si quieres agregar un tipo nuevo de material (como revistas digitales), necesitas reorganizar toda la biblioteca y crear nuevas secciones, lo cual toma mucho tiempo.

**Data Lake** es como un almacén gigante donde puedes guardar cualquier cosa: libros, revistas, videos, fotos, documentos sueltos. No hay un orden específico al principio, simplemente lo guardas todo. Es genial porque puedes almacenar cualquier tipo de información sin preocuparte por organizarla primero. Pero cuando necesitas encontrar algo específico, puede tomar mucho tiempo buscarlo entre todo lo que tienes.

**Lakehouse** es como tener lo mejor de ambos mundos: un almacén gigante donde puedes guardar cualquier cosa, pero con un sistema inteligente que automáticamente organiza y cataloga todo lo que entra. Puedes guardar información de cualquier tipo y, cuando la necesites, el sistema te ayuda a encontrarla rápidamente, incluso te permite organizarla de diferentes maneras según lo que necesites en ese momento.

### Ejemplos Simples

**Data Warehouse:**
- Una cadena de tiendas que consolida todas sus ventas diarias en tablas organizadas por: fecha, producto, tienda y cliente
- Un banco que almacena transacciones en estructuras predefinidas para generar reportes regulatorios
- Una universidad que organiza calificaciones de estudiantes en dimensiones de tiempo, curso y departamento

**Data Lake:**
- Netflix guardando todos los logs de visualización, metadatos de videos, comentarios de usuarios y datos de sensores de sus servidores
- Una empresa de IoT almacenando millones de lecturas de sensores en tiempo real sin procesar
- Un hospital guardando historiales médicos, imágenes de rayos X, audio de consultas y datos de dispositivos médicos

**Lakehouse:**
- Spotify combinando datos de streaming, preferencias musicales, datos sociales y análisis de audio en una plataforma única
- Una empresa automotriz integrando datos de telemetría de vehículos, feedback de usuarios y datos de mantenimiento
- Un retailer unificando datos de ventas online, comportamiento web, inventario y redes sociales

### Casos de Uso

**Data Warehouse - Casos Típicos:**
1. **Reportes Financieros Regulatorios**: Bancos necesitan generar reportes consistentes mensualmente con datos históricos auditables
2. **Dashboard Ejecutivo**: CEOs requieren métricas consolidadas de rendimiento empresarial con tiempos de respuesta garantizados
3. **Análisis de Ventas**: Equipos comerciales necesitan comparar rendimiento por regiones, productos y períodos específicos

**Data Lake - Casos Típicos:**
1. **Data Science y ML**: Científicos de datos exploran patrones en datos no estructurados para desarrollar modelos predictivos
2. **Archivo Histórico**: Organizaciones necesitan preservar datos brutos para futuros análisis no definidos actualmente
3. **Ingesta de IoT**: Dispositivos generan millones de eventos por segundo que requieren almacenamiento flexible y económico

**Lakehouse - Casos Emergentes:**
1. **Real-time Analytics**: Empresas de delivery necesitan análisis inmediato de demanda y optimización de rutas sobre datos streaming
2. **Customer 360**: Retailers unifican datos transaccionales, comportamentales y de interacción para personalización en tiempo real
3. **Compliance y Auditabilidad**: Organizaciones financieras requieren flexibilidad de data lake con garantías transaccionales de data warehouse

### Ejemplo de Implementación

**Data Warehouse Implementation:**
- Definir esquema dimensional basado en procesos de negocio identificados
- Implementar procesos ETL para extraer, limpiar y transformar datos desde sistemas fuente
- Configurar particionado por fecha y indexación en columnas de filtro frecuente
- Establecer SLAs de carga nocturna y ventanas de mantenimiento
- Crear vistas materializadas para consultas complejas recurrentes
- Implementar estrategias de backup y recuperación para datos críticos

**Data Lake Implementation:**
- Diseñar estructura de directorios jerárquica considerando patterns de acceso futuro
- Configurar políticas de lifecycle management para optimizar costos de almacenamiento
- Implementar data cataloging con herramientas como Apache Atlas o AWS Glue
- Establecer controles de acceso granulares y cifrado de datos en reposo
- Crear pipelines de calidad de datos para detectar y notificar anomalías
- Implementar estrategias de compresión y formato de archivos (Parquet, Avro)

**Lakehouse Implementation:**
- Seleccionar formato transaccional (Delta Lake, Iceberg, Hudi) según requisitos específicos
- Diseñar arquitectura de metadatos distribuida para manejo de esquemas evolutivos
- Configurar optimizaciones automáticas como compaction y Z-ordering
- Implementar time travel y branching para desarrollo y testing seguro
- Establecer governance framework que balancee flexibilidad con control
- Crear estrategias de caching inteligente para workloads mixtos OLAP/OLTP

### Comandos CLI o Web UI

**Data Warehouse (SQL-based):**
```sql
-- Crear tabla particionada por fecha
CREATE TABLE sales_fact (
    date_key DATE,
    product_key INT,
    customer_key INT,
    sales_amount DECIMAL(10,2)
) PARTITION BY RANGE (date_key);

-- Consulta optimizada con índices
SELECT p.product_name, SUM(s.sales_amount)
FROM sales_fact s
JOIN product_dim p ON s.product_key = p.product_key
WHERE s.date_key >= '2024-01-01'
GROUP BY p.product_name;
```

**Data Lake (AWS S3/Hadoop):**
```bash
# Subir datos al data lake
aws s3 cp local_data/ s3://my-datalake/raw/sales/year=2024/month=10/ --recursive

# Listar particiones
hdfs dfs -ls /datalake/raw/customer_events/

# Crear tabla externa en Hive
CREATE EXTERNAL TABLE customer_events (
    event_id STRING,
    timestamp BIGINT,
    user_id STRING
) PARTITIONED BY (year INT, month INT)
STORED AS PARQUET
LOCATION 's3://my-datalake/processed/events/';
```

**Lakehouse (Delta Lake):**
```python
# Crear tabla Delta
df.write.format("delta").saveAsTable("sales_bronze")

# Operación MERGE (UPSERT)
deltaTable = DeltaTable.forName(spark, "sales_silver")
deltaTable.alias("target").merge(
    source_df.alias("source"),
    "target.id = source.id"
).whenMatchedUpdate(set = {
    "amount": "source.amount",
    "updated_date": "current_timestamp()"
}).whenNotMatchedInsert(values = {
    "id": "source.id",
    "amount": "source.amount"
}).execute()

# Time travel
spark.read.format("delta").option("versionAsOf", 5).table("sales_silver")
```

## Notas
### Cornell

<table border="1" style="width:100%">
<tr>
<th style="width:30%">Conceptos Clave</th>
<th style="width:70%">Detalles y Explicaciones</th>
</tr>
<tr>
<td><strong>Schema-on-Write vs Schema-on-Read</strong></td>
<td>Schema-on-Write (Data Warehouse): Estructura definida antes de cargar datos, garantiza calidad pero reduce flexibilidad. Schema-on-Read (Data Lake): Estructura aplicada al consultar, máxima flexibilidad pero requiere más procesamiento en query time.</td>
</tr>
<tr>
<td><strong>ACID Properties</strong></td>
<td>Atomicidad, Consistencia, Aislamiento y Durabilidad. Críticas en Data Warehouses tradicionales, ausentes en Data Lakes básicos, recuperadas en arquitecturas Lakehouse mediante formatos como Delta Lake.</td>
</tr>
<tr>
<td><strong>Partitioning Strategies</strong></td>
<td>Data Warehouse: Particionado por fechas para optimizar queries temporales. Data Lake: Particionado por múltiples dimensiones para mejorar pruning. Lakehouse: Particionado dinámico con optimizaciones automáticas.</td>
</tr>
<tr>
<td><strong>Data Governance</strong></td>
<td>Data Warehouse: Governance implícito por estructura rígida. Data Lake: Requiere governance explícito para evitar data swamps. Lakehouse: Balance entre flexibilidad y control mediante políticas automatizadas.</td>
</tr>
<tr>
<td><strong>Cost Optimization</strong></td>
<td>Data Warehouse: Costos altos por hardware especializado y licencias. Data Lake: Costos reducidos usando commodity hardware y storage. Lakehouse: Costos optimizados mediante tiering inteligente y compute elástico.</td>
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
<td rowspan="4"><strong>Data Warehouse</strong></td>
<td>Características</td>
<td>Schema-on-Write</td>
<td>Estructura predefinida, alta calidad</td>
</tr>
<tr>
<td>Arquitectura</td>
<td>Modelo Dimensional</td>
<td>Tablas de hechos y dimensiones</td>
</tr>
<tr>
<td>Casos de Uso</td>
<td>BI y Reporting</td>
<td>Dashboards ejecutivos, reportes regulatorios</td>
</tr>
<tr>
<td>Tecnologías</td>
<td>Columnar Storage</td>
<td>Redshift, Snowflake, BigQuery</td>
</tr>
<tr>
<td rowspan="4"><strong>Data Lake</strong></td>
<td>Características</td>
<td>Schema-on-Read</td>
<td>Flexibilidad máxima, datos crudos</td>
</tr>
<tr>
<td>Arquitectura</td>
<td>Almacenamiento Distribuido</td>
<td>HDFS, S3, Azure Data Lake</td>
</tr>
<tr>
<td>Casos de Uso</td>
<td>ML y Data Science</td>
<td>Exploración, análisis predictivo</td>
</tr>
<tr>
<td>Desafíos</td>
<td>Data Swamps</td>
<td>Falta de catalogación y governance</td>
</tr>
<tr>
<td rowspan="4"><strong>Lakehouse</strong></td>
<td>Características</td>
<td>Híbrido</td>
<td>Flexibilidad + Transaccionalidad</td>
</tr>
<tr>
<td>Arquitectura</td>
<td>Formatos Transaccionales</td>
<td>Delta Lake, Iceberg, Hudi</td>
</tr>
<tr>
<td>Casos de Uso</td>
<td>Workloads Mixtos</td>
<td>BI + ML + Real-time analytics</td>
</tr>
<tr>
<td>Ventajas</td>
<td>Convergencia</td>
<td>Eliminación de silos de datos</td>
</tr>
</table>

## Resumen

Las arquitecturas de datos han evolucionado para abordar diferentes necesidades empresariales. Los **Data Warehouses** ofrecen estructura y rendimiento óptimo para análisis tradicional de BI, pero carecen de flexibilidad para datos no estructurados. Los **Data Lakes** proporcionan flexibilidad máxima y costos reducidos, pero pueden volverse inmanejables sin governance adecuado. 

La arquitectura **Lakehouse** emerge como la solución convergente, combinando la flexibilidad del data lake con las garantías transaccionales del data warehouse. Esta evolución permite a las organizaciones ejecutar workloads diversos sobre una plataforma unificada, eliminando la complejidad de mantener múltiples sistemas y copias de datos.

**Principio de Pareto aplicado**: El 80% del valor en estas arquitecturas proviene del 20% de características críticas: calidad de datos, governance, performance de queries y flexibilidad de esquemas. La elección entre estas arquitecturas debe basarse en los requisitos específicos de latencia, consistencia y variedad de datos de cada organización.