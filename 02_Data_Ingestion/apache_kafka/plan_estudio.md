# 🧭 Plan de Estudio Mensual

**Curso:** Data Engineering
**Módulo:** 02_Data_Ingestion
**Tema:** Apache Kafka

---

## 🎯 Objetivo del Mes

Comprender la arquitectura, fundamentos y operaciones clave de **Apache Kafka** para construir **pipelines de ingestión y streaming de datos** robustos, escalables y orientados a eventos, aplicables en ecosistemas de Data Engineering y microservicios.

---

## 🧩 Resultado Final

Al finalizar el mes, podrás **diseñar e implementar un flujo de ingestión en tiempo real** usando Apache Kafka, con productores, consumidores, topics y configuraciones básicas de persistencia y particionamiento, integrando conceptos como **producers/consumers**, **brokers**, **offsets**, **partitions**, y **Kafka Connect**.

---

## 📅 Semana 1 – Fundamentos y Arquitectura de Kafka

**Objetivo:** Entender qué es Apache Kafka, su arquitectura distribuida y el rol que cumple en la ingestión de datos modernos.

### Temas Clave

* Qué es Apache Kafka y su caso de uso principal
* Componentes esenciales: Broker, Topic, Partition, Offset
* Conceptos de *Publish–Subscribe* y *Stream Processing*
* Comparación con RabbitMQ, Kinesis y Pulsar
* Instalación local o uso de Docker

### Actividades Prácticas

* Instalar Kafka y ZooKeeper localmente o con Docker Compose
* Crear un *topic* y verificar su existencia con `kafka-topics.sh`
* Producir y consumir mensajes desde consola (`kafka-console-producer.sh` y `kafka-console-consumer.sh`)
* Visualizar flujo de datos básico entre productor y consumidor

---

## 📅 Semana 2 – Productores, Consumidores y Configuración

**Objetivo:** Aprender cómo interactúan los productores y consumidores, cómo se gestiona la durabilidad y el rendimiento del sistema.

### Temas Clave

* Productor: acknowledgments, retries, key-partitioning
* Consumidor: grupos, offsets, commits manuales/automáticos
* Concepto de *at-most-once*, *at-least-once*, *exactly-once*
* Particionamiento y replicación: claves del escalamiento horizontal

### Actividades Prácticas

* Crear un **productor** y **consumidor** simples en Python o JavaScript
* Configurar *acks* y *retries* en el productor
* Probar un *consumer group* con dos instancias y observar la repartición
* Medir la entrega garantizada de mensajes (*at-least-once*)

---

## 📅 Semana 3 – Ecosistema Kafka y Procesamiento de Datos

**Objetivo:** Conocer las extensiones y herramientas del ecosistema Kafka para ingestión y procesamiento avanzado.

### Temas Clave

* Kafka Connect: conectores *source* y *sink*
* Kafka Streams y su modelo de procesamiento
* Schema Registry (Avro/JSON) y control de compatibilidad
* Integración con Spark, Flink o KSQL (Kafka SQL Engine)
* Casos reales: pipelines en tiempo real, ETL streaming

### Actividades Prácticas

* Configurar **Kafka Connect** con un conector de archivo CSV o base de datos (ej. PostgreSQL → Kafka)
* Crear un flujo con **Kafka Streams** o **KSQL** para filtrar y transformar datos
* Visualizar el flujo con una herramienta como **Kafdrop** o **Conduktor**

---

## 📅 Semana 4 – Escalabilidad, Tuning y Proyecto Final

**Objetivo:** Consolidar los conocimientos aplicando mejores prácticas de rendimiento y diseño de arquitecturas robustas.

### Temas Clave

* Particiones, réplicas y tolerancia a fallos
* Monitoreo y métricas con Prometheus + Grafana
* Retención de datos y limpieza de logs
* Seguridad básica: autenticación, ACLs y cifrado SSL
* Buenas prácticas de diseño en entornos productivos

### Actividades Prácticas

* Configurar métricas de Kafka y visualizar en Grafana
* Probar diferentes políticas de retención (por tamaño y tiempo)
* Simular fallas de un broker y verificar tolerancia
* Optimizar throughput modificando *batch size*, *linger.ms* y *compression.type*

---

## 💡 Proyecto Opcional del Mes

**Título:** “Pipeline de Ingestión de Transacciones en Tiempo Real con Apache Kafka”

**Descripción:**
Diseña un pipeline completo que simule el flujo de transacciones bancarias o eventos de IoT en tiempo real:

1. **Productor:** genera eventos JSON (transacciones, sensores, logs).
2. **Kafka Cluster:** recibe, particiona y persiste mensajes.
3. **Kafka Streams / KSQL:** filtra y agrega estadísticas (ej. fraude, temperatura, etc.).
4. **Consumidor final:** muestra resultados en consola, base de datos o dashboard.

**Extras (si tienes más tiempo):**

* Añadir Kafka Connect para enviar los datos a PostgreSQL o S3.
* Añadir monitoreo con Prometheus y Grafana.

---

## 📚 Recursos Recomendados

### Libros y Documentación

* *Kafka: The Definitive Guide* — Neha Narkhede, Gwen Shapira, Todd Palino (O’Reilly)
* *Designing Event-Driven Systems* — Ben Stopford
* [Documentación oficial de Apache Kafka](https://kafka.apache.org/documentation/)

### Cursos y Videos

* 🎥 Confluent Developer: *Apache Kafka Fundamentals*
* 🎥 Data Engineering on YouTube (Simplilearn, Conduktor Academy)
* 🧠 Udemy: *Apache Kafka Series – Learn Apache Kafka for Beginners*

### Herramientas Útiles

* **Docker Compose:** para levantar un clúster local rápido
* **Kafdrop / Conduktor:** visualización de topics y mensajes
* **Prometheus + Grafana:** monitoreo de brokers y lag de consumidores
