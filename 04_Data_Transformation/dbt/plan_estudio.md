# 🗓️ Plan de Estudio — Data Transformation con dbt (1 mes)

## Semana 1 — Fundamentos y Entorno de dbt

**Tema especificado:**
Introducción a dbt y su arquitectura.
Conceptos de ELT vs ETL, estructura de proyecto dbt, instalación y primeros pasos (`dbt init`, `dbt run`).

**Subtemas clave:**

* ¿Qué es dbt y su rol en el flujo de datos moderno?
* Estructura de carpetas y archivos (`models/`, `seeds/`, `tests/`, `snapshots/`).
* Configuración del entorno y conexión al data warehouse.
* Ejecución de tu primer modelo SQL con dbt.
* Diferencia entre dbt Core y dbt Cloud.

---

## Semana 2 — Modelado Modular y Jinja

**Tema especificado:**
Modelos en dbt y uso de Jinja para crear transformaciones modulares, dinámicas y reutilizables.

**Subtemas clave:**

* Tipos de modelos (`staging`, `intermediate`, `mart`).
* Dependencias y referencias con `ref()` y `source()`.
* Uso de macros, variables y templates con Jinja.
* Buenas prácticas de organización de modelos.
* Generación de documentación (`dbt docs generate`, `dbt docs serve`).

---

## Semana 3 — Testing, Versionado y Optimización

**Tema especificado:**
Pruebas de calidad de datos, versionado con Git y optimización mediante materializations.

**Subtemas clave:**

* Tests nativos (`unique`, `not_null`, `relationships`).
* Tests personalizados y configuración en `schema.yml`.
* Materializations (`view`, `table`, `incremental`).
* Snapshots y Seeds.
* Versionado y control de cambios con Git.

---

## Semana 4 — Despliegue, Orquestación y CI/CD

**Tema especificado:**
Automatización y despliegue de pipelines de dbt en entornos productivos.

**Subtemas clave:**

* Ciclo de vida de desarrollo: dev → staging → prod.
* Integración con Airflow, Dagster o dbt Cloud.
* Ejecución automatizada (`dbt build`, `dbt run`, `dbt test`).
* Configuración de `profiles.yml` y gestión de entornos.
* CI/CD con GitHub Actions o herramientas similares.

---
