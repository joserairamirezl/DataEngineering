# Semana 2: Data Lake y su Evolución
## Texto
### Lectura
El Data Lake redefine la forma de almacenar datos al permitir la ingestión masiva de información estructurada, semiestructurada y no estructurada sin imponer un esquema rígido al inicio. Se apoya en almacenamiento distribuido y económico (como Amazon S3, Azure Data Lake Storage o Google Cloud Storage) y en formatos optimizados para análisis como Parquet, Avro u ORC. Esta flexibilidad resuelve las limitaciones del Data Warehouse tradicional frente a volúmenes y diversidad crecientes, pero exige prácticas rigurosas de gobierno, particionamiento y metadatos para evitar el síndrome del “data swamp”.  
Los Data Lakes modernos se organizan por capas: Raw (datos tal cual llegan), Curated (datos limpios y enriquecidos) y Consumer (datasets listos para analítica). El esquema se aplica en lectura (schema-on-read) gracias a catálogos como AWS Glue o Hive Metastore, permitiendo que distintos motores (Athena, Spark, Presto) interpreten los mismos archivos. La elasticidad de cómputo desacoplado posibilita correr transformaciones serverless, notebooks o clusters temporales según la carga.  
La evolución del Data Lake incluye gobierno centralizado, versionado, políticas de seguridad fino, orquestadores de flujos y pipelines automatizados. También integra datos en tiempo real mediante ingestion streaming (Kinesis, Kafka) y machine learning con frameworks como Spark ML o SageMaker, manteniendo un repositorio flexible para exploración avanzada.

### Explicación con Técnica de Feynman
Piensa en un Data Lake como un gran depósito de contenedores donde guardamos datos tal como llegan: archivos CSV, logs JSON, imágenes o tablas. No clasificamos todo al inicio, pero sí etiquetamos cada contenedor con metadatos para encontrarlos luego. Cuando alguien necesita analizar, abre el contenedor, decide cómo interpretar los datos y los transforma. Para que el almacén no se vuelva un caos, necesitamos zonas organizadas (raw, curated, consumer), reglas de acceso y herramientas que cataloguen automáticamente lo que entra.

### Ejemplos Simples
*Estructura de carpetas en S3:*
```
s3://mi-datalake/
 ├── raw/
 │   └── ventas/2024/05/archivo.csv
 ├── curated/
 │   └── ventas/2024/05/ventas_curated.parquet
 └── consumer/
     └── bi/ventas_mensuales.parquet
```

*Conversión básica de CSV a Parquet con PySpark:*
```python
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("csv2parquet").getOrCreate()
df = spark.read.option("header", True).csv("s3://mi-datalake/raw/ventas/*.csv")
df_clean = df.dropDuplicates().fillna({"ingresos": 0})
df_clean.write.mode("overwrite").parquet("s3://mi-datalake/curated/ventas/")
```

### Casos de Uso
- Centralizar logs de aplicaciones y métricas IoT para analítica near real-time.
- Crear repositorios de datasets para ciencia de datos y entrenamiento de modelos.
- Almacenar registros históricos de transacciones bancarias sin límites de granularidad.
- Habilitar exploración self-service para equipos de BI y analistas avanzados.

### Ejemplo de Implementacion
1. Crear un bucket versionado en S3 y definir políticas IAM, cifrado y lifecycle.  
2. Establecer naming conventions y particionamiento por fecha, región u otra clave de negocio.  
3. Configurar pipelines de ingesta (batch y streaming) que validen formatos y coloquen archivos en la capa Raw.  
4. Automatizar transformaciones hacia la capa Curated mediante Spark/Glue, controlando calidad y metadatos.  
5. Registrar datasets en Glue Data Catalog y exponerlos a motores como Athena o Redshift Spectrum.  
6. Implementar monitoreo (CloudWatch, Lake Formation) y alertas para detectar retrasos, duplicados o accesos indebidos.

### Comandos CLI o Web UI
- `aws s3 cp ./ventas.csv s3://mi-datalake/raw/ventas/2024/05/` para ingestar archivos rápidamente.
- `aws s3api put-bucket-versioning --bucket mi-datalake --versioning-configuration Status=Enabled` para activar versionado.
- `aws glue create-crawler --name crawler-ventas --role GlueCrawlerRole --targets S3Targets=[{Path="s3://mi-datalake/curated/ventas/"}]` para catalogar metadatos.
- `aws athena start-query-execution --query-string "<SELECT ...>" --query-execution-context Database=analytics` para consultar sin servidores.
- `aws lakeformation grant-permissions --principal DataLakePrincipalIdentifier=<arn> --resource Table={CatalogId=<id>,DatabaseName=analytics,Name=ventas_curated}` para gobernar el acceso.

## Notas
### Cornell
<table>
  <tr><th>Pista / Pregunta</th><th>Notas</th></tr>
  <tr><td>¿Por qué un Data Lake?</td><td>Flexibilidad para almacenar datos variados a gran escala con bajo costo.</td></tr>
  <tr><td>Estructura por capas</td><td>Raw preserva origen, Curated limpia y enriquece, Consumer entrega datasets listos.</td></tr>
  <tr><td>Schema-on-read</td><td>Definimos esquema al consumir datos; depende de catálogos como Glue o Hive.</td></tr>
  <tr><td>Riesgo de data swamp</td><td>Sin gobernanza y metadatos, el repositorio pierde valor y trazabilidad.</td></tr>
</table>

### Outline Method
<table>
  <tr><th>Nivel</th><th>Idea</th></tr>
  <tr><td>I</td><td>Concepto y motivación del Data Lake</td></tr>
  <tr><td>II</td><td>Arquitectura por capas y formatos columnares</td></tr>
  <tr><td>III</td><td>Ingesta (batch/streaming) y almacenamiento en S3</td></tr>
  <tr><td>III</td><td>Catálogo de metadatos y motores de consulta</td></tr>
  <tr><td>II</td><td>Gobernanza, seguridad y monitoreo</td></tr>
</table>

## Resumen
El Data Lake proporciona un repositorio flexible y escalable para datos de todo tipo, desacoplando almacenamiento y cómputo. Su éxito depende de estructurar capas claras, catalogar metadatos y aplicar políticas de gobierno que eviten el desorden. Esta base soporta analítica avanzada, machine learning y escenarios tiempo real en la nube.
