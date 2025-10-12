# 🧭 Plan de Estudio Mensual

**Curso:** Data Engineering
**Módulo:** 01_Architecture_and_Concepts
**Tema:** Datawarehouse – Datalake – Lakehouse

---

## 🎯 Objetivo del Mes

Comprender las diferencias, arquitectura y casos de uso de Data Warehouse, Data Lake y Lakehouse, para diseñar soluciones híbridas de análisis y almacenamiento eficientes, modernas y alineadas con la arquitectura de datos en la nube (AWS, Azure o GCP).

---

## 🧩 Resultado Final

Al finalizar el mes, podrás **diseñar y justificar una arquitectura de datos moderna (Lakehouse)** combinando almacenamiento estructurado y no estructurado, integrando componentes como S3, Glue, Athena, Redshift o BigQuery, y definir su flujo de ingestión–procesamiento–consulta.

---

## 📅 Semana 1 – Fundamentos del Data Warehouse

**Objetivo:** Comprender la arquitectura clásica del Data Warehouse y su rol histórico en el análisis de datos.

### Temas Clave

* Concepto de *Data Warehouse* (Kimball vs Inmon)
* ETL vs ELT y su impacto en la arquitectura moderna
* Modelos: estrella, copo de nieve y Data Mart
* OLTP vs OLAP

### Actividades Prácticas

* Diseñar un modelo estrella básico para ventas (hechos y dimensiones)
* Crear un pequeño flujo ETL con Python o SQL que cargue datos a una tabla analítica
* Visualizar métricas en una hoja de cálculo o dashboard simple

---

## 📅 Semana 2 – Data Lake y su Evolución

**Objetivo:** Entender la motivación y componentes de los Data Lakes en entornos distribuidos y en la nube.

### Temas Clave

* Limitaciones del Data Warehouse tradicional
* Concepto y capas del Data Lake (Raw, Curated, Consumer)
* Formatos de almacenamiento: Parquet, Avro, ORC
* Catálogo de metadatos y *schema-on-read*
* Introducción a AWS S3 + Glue + Athena

### Actividades Prácticas

* Subir datasets CSV a S3 y consultarlos con Athena (schema-on-read)
* Convertir los mismos datos a formato Parquet y comparar rendimiento
* Crear un diccionario de datos en Glue Data Catalog

---

## 📅 Semana 3 – Lakehouse Architecture

**Objetivo:** Integrar lo mejor del Data Warehouse y Data Lake, comprendiendo la arquitectura Lakehouse.

### Temas Clave

* Concepto y motivación del Lakehouse
* Delta Lake, Apache Iceberg y Apache Hudi
* Separación de almacenamiento y cómputo
* Transacciones ACID en entornos de lago
* Data governance y control de versiones

### Actividades Prácticas

* Configurar un entorno local con Delta Lake o usar Databricks Community Edition
* Ejecutar consultas ACID y ver control de versiones
* Crear un flujo incremental (append + merge)

---

## 📅 Semana 4 – Comparativa, Diseño y Proyecto Final

**Objetivo:** Consolidar conocimientos, comparar arquitecturas y diseñar una solución completa.

### Temas Clave

* Comparativa práctica: DW vs DL vs LH
* Patrones de ingestión y consumo (batch, streaming)
* Costos, escalabilidad y mantenibilidad
* Principios de arquitectura moderna de datos

### Actividades Prácticas

* Elaborar un **diagrama arquitectónico** con las tres capas del Lakehouse
* Evaluar ventajas y desventajas en un caso de negocio (ej. e-commerce o IoT)
* Documentar el flujo de datos: fuente → almacenamiento → analítica

---

## 🧠 Proyecto Opcional del Mes

**Título:** “Diseño de una Arquitectura Lakehouse Moderna para una Empresa de Retail”

**Descripción:**
Diseña una arquitectura de datos completa en AWS o GCP que combine:

* S3 (Raw Layer)
* Glue o Dataflow (Transformación)
* Athena/Redshift/BigQuery (Consulta analítica)
* Power BI o Looker (Consumo)

**Entregables:**

* Diagrama arquitectónico
* Justificación técnica
* Comparativa de rendimiento y costo
* Consulta de ejemplo (Athena o SQL analítico)

---

## 📚 Recursos Recomendados

* 📘 *The Data Warehouse Toolkit* – Ralph Kimball
* 🧠 *Data Engineering on AWS* – Packt Publishing
* 🎥 Cursos oficiales:

  * AWS Skill Builder: *Modern Data Strategy on AWS*
  * Databricks Academy: *Introduction to Lakehouse Architecture*
* 🧰 Herramientas prácticas:

  * AWS Free Tier (S3, Glue, Athena, Redshift)
  * Databricks Community Edition
  * Google Colab + PySpark