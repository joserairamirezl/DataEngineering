# Semana 3: Arquitectura Lakehouse
## Texto
### Lectura
La arquitectura Lakehouse combina la flexibilidad del Data Lake con la gobernanza y rendimiento del Data Warehouse. Se apoya en formatos de tabla con capacidades transaccionales (ACID) como Delta Lake, Apache Iceberg o Apache Hudi, que añaden metadatos ricos, índices y control de versiones sobre archivos en almacenamiento de objetos. Esto permite mantener datos en formatos abiertos (Parquet) mientras se habilitan operaciones típicas de DW como MERGE, time travel y manejo de esquemas con evoluciones controladas.  
Un Lakehouse desacopla almacenamiento y cómputo: múltiples motores (Spark, Trino, Snowflake, Databricks SQL) pueden leer las mismas tablas a través de catálogos unificados. La capa de gobernanza gestiona accesos, auditoría, linaje y calidad, lo que habilita workloads mixtos (BI, batch, streaming, ML) sin duplicar datos. Asimismo, simplifica la orquestación al permitir pipelines incrementales sobre las mismas tablas sin reexportar datasets a otros sistemas.  
El enfoque Lakehouse impulsa prácticas como medallion architecture (Bronze, Silver, Gold), manejo de transacciones en streaming (structured streaming + Delta), y adopción de estándares de metadatos abiertos (Unity Catalog, Glue, AWS Lake Formation). Facilita costos optimizados al evitar mover datos a motores especializados y reduce complejidad operativa mediante infraestructura gestionada o serverless.

### Explicación con Técnica de Feynman
Imagina que tu Data Lake es un río donde guardas todo tipo de agua, pero a veces necesitas tomar agua limpia y bien medida como en un depósito. El Lakehouse coloca compuertas inteligentes sobre ese río: cada vez que echas o sacas agua, las compuertas registran el cambio, evitan mezclas indebidas y te permiten volver atrás si algo salió mal. Así mantienes la flexibilidad de guardar de todo, pero con la precisión y control de un depósito depurado, usando las mismas tablas para reportes, ciencia de datos o streaming.

### Ejemplos Simples
*Creación y actualización de tabla Delta Lake con PySpark:*
```python
from delta import configure_spark_with_delta_pip
from pyspark.sql import SparkSession

builder = SparkSession.builder.appName("lakehouse").config(
    "spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension"
).config(
    "spark.sql.catalog.spark_catalog", "org.apache.spark.sql.delta.catalog.DeltaCatalog"
)
spark = configure_spark_with_delta_pip(builder).getOrCreate()

df = spark.read.json("s3://mi-lakehouse/bronze/ventas/2024/05/")
df.write.format("delta").mode("overwrite").save("s3://mi-lakehouse/silver/ventas/")

spark.sql("""
MERGE INTO delta.`s3://mi-lakehouse/silver/ventas/` AS target
USING delta.`s3://mi-lakehouse/bronze/ventas_incremental/` AS src
ON target.id = src.id
WHEN MATCHED THEN UPDATE SET *
WHEN NOT MATCHED THEN INSERT *
""")
```

*Time travel para auditoría:*
```sql
SELECT * FROM delta.`s3://mi-lakehouse/silver/ventas/` VERSION AS OF 12;
```

### Casos de Uso
- Reemplazar pipelines duplicados entre DW y Data Lake con tablas Delta/Iceberg únicas para BI y ML.
- Gestionar historiales de datos financieros con requisitos de auditoría y versionado.
- Aplicar machine learning iterativo sin mover datos gracias a notebooks sobre la misma capa Gold.
- Soportar analítica near real-time combinando streaming y batch en tablas ACID.

### Ejemplo de Implementacion
1. Definir zonas medallion (Bronze, Silver, Gold) dentro del Data Lake existente con estándares de nombres y particiones.  
2. Instalar y configurar motor compatible (Databricks, EMR con Delta, Snowflake Iceberg) habilitando extensiones para ACID.  
3. Migrar datasets críticos a tablas Lakehouse usando writes en formato Delta/Iceberg, validando esquema y calidad.  
4. Implementar pipelines incrementales (batch y streaming) que utilicen MERGE, OPTIMIZE y VACUUM para mantenimiento.  
5. Centralizar metadatos y permisos con Unity Catalog, AWS Glue o AWS Lake Formation para control multinivel.  
6. Exponer métricas y vistas en herramientas de BI y notebooks, aprovechando time travel para auditoría y reproducibilidad.

### Comandos CLI o Web UI
- `databricks jobs run-now --job-id <id>` para orquestar notebooks que mantienen tablas Delta.
- `spark-submit --packages io.delta:delta-spark_2.12:<version> job.py` para ejecutar transformaciones ACID on-prem o en EMR.
- `databricks fs ls dbfs:/mnt/lakehouse/silver/` para validar particiones y archivos escritos.
- `aws glue update-table --database-name gold --table-input file://table.json` para sincronizar el catálogo con tablas Lakehouse.
- `delta-table vacuum s3://mi-lakehouse/silver/ventas --retention-hours 168` (usando la CLI de Delta) para limpiar archivos obsoletos.

## Notas
### Cornell
<table>
  <tr><th>Pista / Pregunta</th><th>Notas</th></tr>
  <tr><td>¿Qué es Lakehouse?</td><td>Unifica Data Lake y DW en tablas ACID sobre almacenamiento abierto.</td></tr>
  <tr><td>Formatos clave</td><td>Delta Lake, Apache Iceberg, Apache Hudi añaden transacciones y metadatos.</td></tr>
  <tr><td>Medallion architecture</td><td>Bronze (raw), Silver (curado), Gold (consumo); habilita pipelines incrementales.</td></tr>
  <tr><td>Gobernanza</td><td>Catálogos unificados, permisos centralizados, linaje y versionado.</td></tr>
</table>

### Outline Method
<table>
  <tr><th>Nivel</th><th>Idea</th></tr>
  <tr><td>I</td><td>Lakehouse como convergencia DW + Data Lake</td></tr>
  <tr><td>II</td><td>Capacidades ACID y formatos de tabla</td></tr>
  <tr><td>III</td><td>Desacoplamiento almacenamiento-cómputo y catálogos</td></tr>
  <tr><td>III</td><td>Pipelines incrementales y medallion architecture</td></tr>
  <tr><td>II</td><td>Gobernanza, seguridad y auditoría</td></tr>
</table>

## Resumen
El Lakehouse aporta transacciones, versionado y gobernanza al Data Lake, permitiendo reutilizar datos abiertos para múltiples workloads sin duplicación. Con formatos ACID y catálogos centralizados se logra coherencia, rendimiento y trazabilidad comparables a un DW moderno, manteniendo la flexibilidad y escalabilidad inherentes al almacenamiento en la nube.
