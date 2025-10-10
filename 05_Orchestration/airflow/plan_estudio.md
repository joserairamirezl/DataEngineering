# 🧭 Plan de Estudio — Data Engineering

## Módulo: 05_Orchestration

### Tema: Apache Airflow

---

## 🎯 Objetivo del mes

Dominar los fundamentos de **Apache Airflow** como orquestador de *workflows* de datos, entendiendo su arquitectura, componentes principales y las buenas prácticas para desplegar, programar y monitorear DAGs de forma profesional.
Al finalizar el mes deberías ser capaz de:

* Crear, ejecutar y depurar DAGs en Airflow.
* Entender la arquitectura y los componentes principales (Scheduler, Executor, Webserver, Metadata DB).
* Integrar Airflow con herramientas comunes del ecosistema de datos (dbt, Spark, AWS, GCP).
* Automatizar pipelines reproducibles y observables.

---

## 📅 Semana 1 — Fundamentos y Arquitectura de Airflow

**Objetivo:** Comprender qué resuelve Airflow, su arquitectura interna y su flujo de ejecución.

**Temas clave (80/20):**

* ¿Qué es Apache Airflow y por qué se usa en Data Engineering?
* Conceptos fundamentales: DAGs, Tasks, Operators, Schedulers, Executors.
* Arquitectura general: Webserver, Scheduler, Metadata DB, Worker.
* Instalación local y estructura de un proyecto Airflow.
* Creación de tu primer DAG y ejecución manual.

**Actividades prácticas:**

* Instalar Airflow en entorno local o Docker Compose.
* Crear un DAG simple (por ejemplo, ETL con tareas dummy).
* Navegar por la UI y observar el flujo de tareas.

---

## 📅 Semana 2 — Operators, Hooks y XComs

**Objetivo:** Aprender a conectar Airflow con otros sistemas y crear DAGs dinámicos y reutilizables.

**Temas clave (80/20):**

* Tipos de Operators: *BashOperator*, *PythonOperator*, *EmailOperator*, *BranchOperator*.
* Uso de Hooks y conexiones (AWS, GCP, Databases).
* Variables y parámetros en tareas.
* Comunicación entre tareas con *XComs*.
* Plantillas Jinja y macros.

**Actividades prácticas:**

* Crear un DAG con PythonOperator que procese datos.
* Implementar conexión a una base de datos o API con Hook.
* Pasar datos entre tareas usando XComs.
* Configurar variables y templates dinámicos.

---

## 📅 Semana 3 — Programación, Monitoreo y Logging

**Objetivo:** Dominar la ejecución automatizada, monitoreo y manejo de logs y errores.

**Temas clave (80/20):**

* Configuración de *schedules* (CRON, presets, triggers).
* Retries, SLA, dependencias y *task context*.
* Logging: estructura de logs, almacenamiento y depuración.
* Monitoreo desde la UI y métricas básicas.
* Integración con Prometheus/Grafana para observabilidad avanzada.

**Actividades prácticas:**

* Configurar un DAG con retries y alertas de fallo.
* Analizar logs y estados de ejecución.
* Probar una integración simple con Prometheus o un email de alerta.

---

## 📅 Semana 4 — Integraciones Avanzadas y Despliegue

**Objetivo:** Llevar Airflow a un entorno productivo, integrándolo con pipelines reales y aplicando buenas prácticas.

**Temas clave (80/20):**

* Integración con dbt, Spark o BigQuery.
* Despliegue con Docker Compose, Helm o MWAA (Managed Workflows on AWS).
* Versionado de DAGs con Git.
* Modularización y testing de DAGs.
* Buenas prácticas de arquitectura y seguridad (RBAC, Connections, Secrets).

**Actividades prácticas:**

* Desplegar Airflow con Docker Compose.
* Versionar DAGs con Git y configurar CI/CD (GitHub Actions).
* Integrar Airflow con un pipeline dbt o Spark simple.

---

## 🧠 Resultado al final del mes

Deberías poder:
✅ Comprender y explicar la arquitectura de Airflow.
✅ Crear y ejecutar DAGs funcionales con dependencias, retries y XComs.
✅ Monitorear y depurar pipelines de datos.
✅ Integrar Airflow con sistemas externos y aplicar buenas prácticas de despliegue.

---

## 📚 Recursos recomendados

**Documentación oficial:**

* [Apache Airflow Docs](https://airflow.apache.org/docs/)
* [Airflow Concepts Overview](https://airflow.apache.org/docs/apache-airflow/stable/concepts.html)

**Videos / Playlists:**

* *“Airflow Tutorial for Beginners” – TechWorld with Nana*
* *“Airflow in Production – Astronomer Academy (Free)*

**Repositorios útiles:**

* [`apache/airflow`](https://github.com/apache/airflow) – proyecto oficial
* [`puckel/docker-airflow`](https://github.com/puckel/docker-airflow) – despliegue Docker clásico
* [`astronomer/airflow-demo`](https://github.com/astronomer/airflow-demo) – ejemplos modernos
