# dbt (Data Build Tool)

## Texto
### Lectura

dbt (Data Build Tool) es una herramienta de transformación de datos que permite a los equipos de Data Engineering y Analytics implementar prácticas de ingeniería de software en el desarrollo de pipelines de datos. Desarrollado por Fishtown Analytics (ahora dbt Labs), dbt revoluciona el enfoque tradicional de ETL al adoptar el paradigma ELT (Extract, Load, Transform), donde las transformaciones ocurren directamente en el data warehouse utilizando SQL como lenguaje principal.

El **paradigma ELT de dbt** se fundamenta en aprovechar el poder computacional de los modernos data warehouses cloud-native como Snowflake, BigQuery, Redshift y Databricks. En lugar de extraer datos, transformarlos en herramientas externas y cargarlos (ETL tradicional), dbt permite cargar datos raw en el warehouse y ejecutar transformaciones complejas mediante SQL compilado y optimizado. Este enfoque elimina la necesidad de herramientas ETL costosas y complejas, democratizando el desarrollo de pipelines de datos para analistas que dominan SQL.

La arquitectura de dbt se basa en **modelos declarativos** definidos como archivos SQL con metadata adicional. Cada modelo representa una transformación que puede ser una tabla, vista o tabla incremental en el data warehouse. dbt construye automáticamente un **Directed Acyclic Graph (DAG)** que mapea las dependencias entre modelos, ejecutándolos en el orden correcto y paralelizando operaciones independientes. Esta aproximación garantiza consistencia, permite rollbacks seguros y facilita el debugging de pipelines complejas.

**dbt Core** proporciona funcionalidades esenciales como templating con Jinja2, macros reusables, testing automatizado y documentación auto-generada. El **templating system** permite crear SQL dinámico que se adapta a diferentes environments, mientras que las **macros** encapsulan lógica compleja reutilizable across múltiples modelos. Los **tests** integrados validan assumptions sobre datos (uniqueness, not null, relationships) ejecutándose automáticamente como parte del pipeline, mientras que la **documentación** se genera desde código y comentarios, manteniéndose siempre actualizada.

El ecosistema dbt incluye **dbt Cloud** para deployment y orquestación enterprise, **packages** para reutilización de código community-driven, y **adapters** que extienden compatibilidad a diferentes data platforms. Los **packages** permiten importar transformaciones pre-construidas para fuentes comunes como Google Analytics, Salesforce, o Stripe, acelerando significativamente el time-to-value. Los **adapters** habilitan dbt en plataformas diversas desde PostgreSQL hasta Apache Spark, manteniendo consistencia de desarrollo regardless del underlying technology.

### Explicación con Técnica de Feynman

Imagina que dbt es como un **chef muy organizado** en una cocina de restaurante que se especializa en preparar platos complejos usando ingredientes que ya están en el refrigerador.

**Los datos raw son como ingredientes básicos** ya comprados y almacenados en un refrigerador gigante (tu data warehouse). En lugar de tener que ir al mercado, procesarlos afuera y traerlos de vuelta, el chef trabaja directamente con lo que ya tienes guardado.

**Los modelos de dbt son como recetas inteligentes** escritas en un lenguaje que el chef entiende perfectamente (SQL). Cada receta no solo dice cómo hacer un plato, sino que también indica qué otros platos necesita como ingredientes. Por ejemplo, la receta de "Ensalada César Gourmet" necesita que primero hagas "Crutones Caseros" y "Aderezo César".

**El DAG es como el orden perfecto de cocina** que el chef calcula automáticamente. Sabe que debe hacer primero los crutones, luego el aderezo, y finalmente ensamblar la ensalada. Si tiene ayudantes (paralelización), puede hacer los crutones y el aderezo al mismo tiempo porque no dependen entre sí.

**Los tests son como el control de calidad** donde el chef verifica que los crutones estén crujientes, el aderezo tenga la consistencia correcta, y la ensalada tenga todos los ingredientes necesarios.

**La documentación es como un libro de cocina automático** que se actualiza solo. Cada vez que el chef modifica una receta o crea una nueva, el libro se actualiza automáticamente con fotos, ingredientes y pasos.

Lo mejor es que **otros chefs pueden usar las mismas recetas** (packages) y incluso contribuir con sus propias recetas mejoradas para que toda la comunidad las use.

### Ejemplos Simples

**E-commerce Analytics:**
- Datos raw: Orders, customers, products en tablas separadas
- Transformación: Crear tabla customer_lifetime_value uniendo orders con customers y calculando métricas
- Output: Dashboard con CLV por segmento de customer

**Marketing Attribution:**
- Datos raw: Website events, ad campaigns, conversions desde múltiples fuentes
- Transformación: Modelo de atribución first-touch y last-touch para asignar crédito a campaigns
- Output: Reportes de ROI por canal de marketing

**Financial Reporting:**
- Datos raw: Transacciones, cuentas contables, exchange rates
- Transformación: Consolidar P&L statements aplicando currency conversion y accounting rules
- Output: Estados financieros automatizados por región

**Product Analytics:**
- Datos raw: User events, feature usage, subscription data
- Transformación: Crear cohort analysis y funnel metrics para product teams
- Output: Product performance dashboards y user engagement reports

### Casos de Uso

**Modern Data Stack Implementation:**
Startups y scale-ups utilizan dbt como core de su modern data stack, combinándolo con Fivetran/Airbyte para ingestion, Snowflake/BigQuery como warehouse, y herramientas de BI como Looker o Tableau. dbt centraliza toda la business logic, permitiendo que data analysts mantengan transformaciones complejas sin depender de data engineers, acelerando significativamente el time-to-insight.

**Data Warehouse Modernization:**
Empresas tradicionales migran de ETL tools legacy (Informatica, DataStage, SSIS) hacia dbt para modernizar sus data warehouses. El approach code-first de dbt facilita version control, testing automatizado y collaboration, mientras que la ejecución nativa en cloud warehouses mejora dramatically el performance y reduce costos operacionales.

**Self-Service Analytics Platform:**
Organizaciones implementan dbt como foundation para self-service analytics, donde business users pueden crear nuevos metrics y dimensions mediante dbt models sin knowledge de infrastructure. Combined con semantic layers como LookML o Cube.js, esto democratiza data access mientras mantiene governance y consistency.

**Regulatory Compliance y Auditability:**
Industrias reguladas (finance, healthcare, pharma) leveragean dbt's built-in lineage tracking y documentation para compliance requirements. Cada transformation es versionada, testeable y auditable, facilitando regulatory audits y ensuring data quality standards required por frameworks como SOX, GDPR o FDA validation.

**Multi-tenant SaaS Analytics:**
Empresas SaaS utilizan dbt para crear analytics products para sus customers, using incremental models y partitioning strategies para efficient processing de large datasets. dbt macros permiten dynamic tenant filtering y customizable metrics per customer, enabling white-label analytics solutions.

**Real-time Analytics con Incremental Models:**
Companies processing high-volume event data (gaming, fintech, e-commerce) utilizan dbt incremental models para near real-time analytics. Combined con change data capture (CDC) y streaming ingestion, dbt processes only new/changed records, maintaining fresh analytics con minimal computational overhead.

### Ejemplo de Implementación

**Project Structure y Best Practices:**
- Establecer folder structure consistente: staging/ para raw data cleaning, marts/ para business logic, intermediate/ para complex transformations
- Implementar naming conventions claras: stg_ para staging models, int_ para intermediate, fct_ para fact tables, dim_ para dimensions
- Configurar environments separados (dev, staging, prod) con different schemas y compute resources
- Establecer code review process usando Git workflows y pull requests para quality control
- Implementar pre-commit hooks para dbt formatting, linting y basic validation

**Model Development Workflow:**
- Comenzar con staging models que clean y standardize raw data desde source systems
- Crear intermediate models para complex business logic que pueden reutilizarse across multiple marts
- Desarrollar mart models que represent final business entities consumibles por BI tools
- Implementar incremental models para large datasets usando appropriate incremental strategies
- Establecer modelo de datos dimensional (star schema) para optimal BI performance

**Testing y Quality Assurance:**
- Implementar schema tests para validate data assumptions: unique keys, not null constraints, relationships
- Crear custom tests para business rules específicas: revenue reconciliation, data freshness checks
- Configurar data quality monitoring usando packages como dbt-expectations para statistical tests
- Establecer alerting mechanisms que notifiquen cuando tests fail o data quality degrades
- Implement row-level security y column-level permissions para sensitive data protection

**Deployment y Orchestration:**
- Configurar CI/CD pipelines que ejecuten dbt tests antes de deployment a production
- Implementar blue-green deployments para zero-downtime updates de production models
- Establecer job scheduling usando dbt Cloud, Airflow, o Prefect para regular execution
- Configurar monitoring y alerting para job failures, performance degradation y resource utilization
- Implementar backup y recovery strategies para critical production models y state

### Comandos CLI o Web UI

**Project Setup y Development:**
```bash
# Inicializar nuevo proyecto dbt
dbt init my_project

# Configurar conexión a warehouse
dbt debug

# Compilar models para verificar SQL válido
dbt compile

# Ejecutar todos los models
dbt run

# Ejecutar specific model y sus dependencies
dbt run --select customer_lifetime_value+

# Ejecutar solo models modificados
dbt run --select state:modified
```

**Testing y Quality Assurance:**
```bash
# Ejecutar todos los tests
dbt test

# Test specific model
dbt test --select stg_orders

# Generar y servir documentación
dbt docs generate
dbt docs serve

# Validar freshness de source data
dbt source freshness

# Snapshot para SCD (Slowly Changing Dimensions)
dbt snapshot
```

**Production Management:**
```bash
# Full refresh de incremental models
dbt run --full-refresh

# Ejecutar con variables específicas
dbt run --vars '{"start_date": "2024-01-01"}'

# Parse project para verificar syntax
dbt parse

# List all models y sus properties
dbt list --select config.materialized:table

# Seed reference data
dbt seed
```

**Advanced Operations:**
```bash
# Ejecutar models en parallel threads
dbt run --threads 8

# Target specific environment
dbt run --target prod

# Store compilation artifacts
dbt compile --write-json

# Retry failed runs
dbt retry

# Show model lineage
dbt list --select +customer_metrics+ --output name
```

## Notas
### Cornell

<table border="1" style="width:100%">
<tr>
<th style="width:30%">Conceptos Clave</th>
<th style="width:70%">Detalles y Explicaciones</th>
</tr>
<tr>
<td><strong>ELT vs ETL Paradigm</strong></td>
<td>ELT aprovecha compute power de modern warehouses para transformaciones in-situ. Elimina necesidad de separate transformation layer. Raw data loaded first, transformed using warehouse-native SQL. Faster development, lower infrastructure costs, leverages warehouse optimizations.</td>
</tr>
<tr>
<td><strong>Materialization Strategies</strong></td>
<td>Table: Full rebuild cada run, best para small datasets. View: No storage, computed at query time. Incremental: Solo procesa new/changed records, optimal para large datasets. Ephemeral: In-memory, used como CTE in dependent models.</td>
</tr>
<tr>
<td><strong>Jinja Templating</strong></td>
<td>Permite dynamic SQL generation mediante variables, loops, conditionals. Enables environment-specific logic, date ranges, configuration-driven transformations. Macros encapsulate reusable logic. Critical para DRY principles y maintainable code.</td>
</tr>
<tr>
<td><strong>DAG Execution Order</strong></td>
<td>dbt automatically builds dependency graph desde model references. Ejecuta models en topological order. Paraleliza independent models para performance. ref() function crea dependencies, source() references raw data. Prevents circular dependencies.</td>
</tr>
<tr>
<td><strong>Testing Framework</strong></td>
<td>Schema tests: unique, not_null, accepted_values, relationships. Data tests: custom SQL assertions. Source freshness tests: validate recent data availability. Generic tests: reusable test logic. Ensures data quality y business rule compliance.</td>
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
<td rowspan="5"><strong>Core Concepts</strong></td>
<td>Models</td>
<td>SQL-based Transformations</td>
<td>Tables, views, incremental, ephemeral</td>
</tr>
<tr>
<td>Sources</td>
<td>Raw Data References</td>
<td>External tables, freshness testing</td>
</tr>
<tr>
<td>Macros</td>
<td>Reusable SQL Logic</td>
<td>Jinja templating, function-like behavior</td>
</tr>
<tr>
<td>Tests</td>
<td>Data Quality Validation</td>
<td>Schema tests, data tests, custom assertions</td>
</tr>
<tr>
<td>Documentation</td>
<td>Auto-generated Docs</td>
<td>Model descriptions, column definitions, lineage</td>
</tr>
<tr>
<td rowspan="4"><strong>Advanced Features</strong></td>
<td>Snapshots</td>
<td>SCD Implementation</td>
<td>Type 2 slowly changing dimensions</td>
</tr>
<tr>
<td>Seeds</td>
<td>Reference Data</td>
<td>CSV files, lookup tables, static data</td>
</tr>
<tr>
<td>Packages</td>
<td>Code Reusability</td>
<td>Community packages, utilities, connectors</td>
</tr>
<tr>
<td>Hooks</td>
<td>Custom Operations</td>
<td>Pre/post-hooks, operation execution</td>
</tr>
<tr>
<td rowspan="4"><strong>Operations</strong></td>
<td>Development Workflow</td>
<td>Local Development</td>
<td>dbt run, test, compile, debug</td>
</tr>
<tr>
<td>Deployment</td>
<td>Production Execution</td>
<td>CI/CD, environment management</td>
</tr>
<tr>
<td>Monitoring</td>
<td>Observability</td>
<td>Job monitoring, test results, performance</td>
</tr>
<tr>
<td>Orchestration</td>
<td>Scheduling</td>
<td>dbt Cloud, Airflow, Prefect integration</td>
</tr>
</table>

## Resumen

dbt ha transformado fundamentalmente el landscape de data transformations al democratizar el desarrollo de pipelines analíticas mediante SQL y adoptar software engineering best practices. Su paradigma **ELT-first** aprovecha el poder computacional de modern cloud warehouses, eliminando la complejidad y costos de traditional ETL tools mientras mejora significativamente developer productivity.

Las **ventajas clave** incluyen: development velocity através de SQL familiar, built-in testing y documentation, version control nativo, dependency management automático, y un ecosistema vibrante de packages y integrations. Esta combinación permite que analytics teams mantengan complex data pipelines con quality y reliability comparable a software engineering teams.

**Aplicando Pareto 80/20**: El 80% del valor de dbt se obtiene dominando el 20% esencial: model structure y materialization strategies, effective testing implementation, proper project organization, y understanding del DAG execution model. Master estos fundamentos garantiza successful dbt implementations que scale con organizational needs.

La evolución hacia **dbt Cloud**, **semantic layer** integrations, y **dbt Mesh** para large-scale organizations posiciona a dbt como la platform definitiva para modern analytics engineering, especialmente en contextos de self-service analytics y data democratization initiatives.