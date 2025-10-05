# Apache Airflow

## Texto
### Lectura

Apache Airflow es una plataforma de código abierto para desarrollar, programar y monitorear flujos de trabajo de datos mediante código. Desarrollado originalmente por Airbnb y posteriormente donado a la Apache Software Foundation, Airflow se ha consolidado como el estándar de facto para orquestación de pipelines de datos en entornos de Data Engineering. Su filosofía "Configuration as Code" permite definir flujos de trabajo complejos mediante Python, proporcionando flexibilidad, versionado y mantenibilidad superiores a herramientas tradicionales de ETL basadas en interfaces gráficas.

La arquitectura de Airflow se fundamenta en **Directed Acyclic Graphs (DAGs)** que representan workflows compuestos por **tasks** interconectadas con dependencies explícitas. Cada **task** encapsula una unidad de trabajo específica (ejecutar queries SQL, procesar archivos, llamar APIs, etc.) mediante **operators** especializados. El **Scheduler** es el componente central que parsea DAGs, determina qué tasks están listas para ejecutar basándose en dependencies y triggers, y las envía a **Executors** que manejan la ejecución real en workers distribuidos.

El **Airflow Webserver** proporciona una interfaz web rica que permite visualizar DAGs, monitorear executions en tiempo real, debugging de failures, y gestión de configurations. La **metadata database** (PostgreSQL, MySQL) almacena state de DAG runs, task instances, connections, variables y logs, enabling audit trails y historical analysis. Esta arquitectura distribuida permite scaling horizontal mediante múltiples workers y soporta diferentes execution environments desde local development hasta large-scale production clusters.

Los **Operators** son building blocks reutilizables que abstraen diferentes tipos de operaciones. **BashOperator** ejecuta comandos shell, **PythonOperator** runs Python functions, **SQLOperator** ejecuta queries en databases, mientras que **custom operators** encapsulan business logic específica. Los **Sensors** son operators especializados que esperan external conditions (file arrival, API availability, database records) antes de proceder, enabling event-driven workflows y integration con external systems.

El **XCom (Cross-Communication)** mechanism permite que tasks compartan data mediante key-value store en metadata database. Combined con **templating** usando Jinja2, los DAGs pueden ser dynamic y data-driven, adaptándose a runtime conditions. Las **connections** centralizan credentials y configuration para external systems, mientras que **variables** almacenan global configuration accessible across DAGs, promoting reusability y security best practices.

### Explicación con Técnica de Feynman

Imagina que Airflow es como un **director de orquesta muy inteligente** que coordina una sinfonía compleja donde cada músico (task) debe tocar en el momento exacto y en el orden correcto.

**Los DAGs son como partituras musicales** que muestran exactamente qué músico debe tocar cuándo, qué instrumento usar, y qué otros músicos deben terminar antes de que ellos empiecen. La partitura está escrita en un lenguaje que el director entiende perfectamente (Python).

**El Scheduler es como el director** que lee la partitura, ve qué músicos están listos para tocar, y les da la señal para comenzar. Nunca se confunde sobre el orden porque sigue las reglas escritas en la partitura.

**Los Operators son como diferentes tipos de instrumentos**. Tienes el "BashOperator" que es como un tambor (ejecuta comandos simples), el "PythonOperator" que es como un piano (puede hacer cosas más complejas), y el "SQLOperator" que es como un violín (se especializa en hablar con bases de datos).

**Los Workers son como los músicos individuales** que realmente tocan los instrumentos cuando el director les da la señal. Pueden estar en diferentes lugares (servidores) pero todos siguen las instrucciones del director.

**La Web UI es como un tablero gigante** donde puedes ver toda la orquesta en acción: qué músico está tocando ahora, quién terminó bien, quién se equivocó, y cuánto tiempo lleva cada pieza musical.

**Los Sensors son como músicos especiales** que esperan señales externas antes de tocar. Por ejemplo, esperan que llegue un mensaje específico o que otro evento ocurra antes de comenzar su parte.

Lo mejor es que **si un músico se equivoca**, el director puede hacer que solo ese músico repita su parte sin tener que empezar toda la sinfonía desde el principio.

### Ejemplos Simples

**ETL Pipeline Diario:**
- Task 1: Extraer datos de base de datos de ventas (SQLOperator)
- Task 2: Procesar y limpiar datos (PythonOperator)  
- Task 3: Cargar datos a data warehouse (SQLOperator)
- Task 4: Enviar reporte por email (EmailOperator)

**Data Quality Pipeline:**
- Task 1: Esperar archivo CSV (FileSensor)
- Task 2: Validar formato y contenido (PythonOperator)
- Task 3: Si válido → cargar datos, Si inválido → enviar alerta
- Task 4: Actualizar dashboard de calidad de datos

**ML Model Training Pipeline:**
- Task 1: Extraer datos de training (SQLOperator)
- Task 2: Preprocessing y feature engineering (PythonOperator)
- Task 3: Entrenar modelo (PythonOperator)
- Task 4: Evaluar performance (PythonOperator)
- Task 5: Si performance > threshold → deploy modelo

**API Integration Pipeline:**
- Task 1: Verificar disponibilidad de API (HttpSensor)
- Task 2: Extraer datos desde API (PythonOperator)
- Task 3: Transformar formato (PythonOperator)
- Task 4: Almacenar en database (SQLOperator)

### Casos de Uso

**Enterprise Data Warehouse Orchestration:**
Corporaciones financieras utilizan Airflow para orquestar complex ETL pipelines que procesan terabytes de transactional data diariamente. Los DAGs coordinan extraction desde múltiples source systems (core banking, trading platforms, CRM), apply business rules y regulatory transformations, y populate dimensional models en enterprise data warehouses. Task failures trigger automatic retries y alerting, while audit logs satisfy compliance requirements.

**Real-time Data Pipeline Coordination:**
Empresas de e-commerce emplean Airflow para coordinar near real-time pipelines que process clickstream data, inventory updates y order events. Aunque Airflow no es streaming tool, orquesta micro-batch processing tasks que run frecuentemente (cada 5-15 minutes), triggering Spark jobs, updating ML model features, y refreshing recommendation engines para maintain fresh personalization.

**Multi-Cloud Data Integration:**
Organizations con hybrid/multi-cloud architectures utilizan Airflow para orchestrate data movement between different cloud providers y on-premises systems. DAGs coordinate data replication from AWS S3 to Google BigQuery, sync customer data between Salesforce y internal databases, y manage backup/disaster recovery workflows across multiple regions y availability zones.

**ML Pipeline Automation:**
Data Science teams implementan MLOps workflows usando Airflow para automate complete ML lifecycle. DAGs orchestrate data preprocessing, feature engineering, model training con hyperparameter tuning, model evaluation, A/B testing deployment, y performance monitoring. Integration con MLflow, Kubeflow y model registries enables automated model deployment pipelines.

**Regulatory Compliance Reporting:**
Industrias reguladas (banking, healthcare, telecommunications) utilizan Airflow para generate complex regulatory reports que require data from múltiples systems y precise timing. DAGs ensure data lineage tracking, implement approval workflows, generate audit trails, y coordinate report submission to regulatory bodies with built-in retry mechanisms y failure notifications.

**IoT Data Processing Orchestration:**
Manufacturing companies emplean Airflow para orchestrate IoT data processing pipelines que handle sensor data desde factory floors. DAGs coordinate data ingestion desde industrial systems, apply predictive maintenance algorithms, trigger alerts para equipment anomalies, y generate operational dashboards while ensuring data quality y system availability.

### Ejemplo de Implementación

**Airflow Architecture Setup:**
- Deployar Airflow using Kubernetes Helm charts para high availability y auto-scaling
- Configurar external PostgreSQL database para metadata store con read replicas para performance
- Implementar Redis como message broker para CeleryExecutor distributed task execution  
- Establecer separate webserver, scheduler, y worker pools basados en workload requirements
- Configurar persistent volumes para DAG storage, logs, y temporary processing files

**DAG Development Best Practices:**
- Establecer consistent naming conventions para DAGs, tasks, y connections siguiendo organizational standards
- Implementar modular DAG design mediante task groups y SubDAGs para reusability y maintainability
- Configurar appropriate retry policies, SLA monitoring, y alerting para critical business processes
- Utilizar Airflow Variables y Connections para environment-specific configuration management
- Implementar custom operators para frecuently used business logic patterns

**Security y Access Control:**
- Integrar con enterprise authentication systems (LDAP, OAuth, SAML) para centralized user management
- Implementar role-based access control (RBAC) para different user personas: developers, operators, viewers
- Configurar encrypted connections para databases, APIs, y external systems usando Airflow Connections
- Establecer secrets management integration con HashiCorp Vault o cloud-native secret stores
- Implementar network security mediante VPN, firewalls, y encrypted communication channels

**Monitoring y Observability:**
- Configurar comprehensive logging usando structured logs forwarded to centralized logging systems
- Implementar metrics collection mediante Prometheus/StatsD para performance monitoring y alerting
- Establecer SLA monitoring con automatic escalation para business-critical workflows
- Configurar custom health checks y readiness probes para Kubernetes deployments
- Implementar distributed tracing para complex workflows spanning multiple systems y services

### Comandos CLI o Web UI

**DAG Management:**
```bash
# Listar todos los DAGs
airflow dags list

# Triggear DAG manualmente
airflow dags trigger my_etl_dag

# Pausar/despausar DAG
airflow dags pause my_etl_dag
airflow dags unpause my_etl_dag

# Ver estado de DAG runs
airflow dags state my_etl_dag 2024-10-04

# Backfill DAG para rango de fechas
airflow dags backfill my_etl_dag \
  --start-date 2024-10-01 \
  --end-date 2024-10-04
```

**Task Operations:**
```bash
# Ejecutar task específica
airflow tasks run my_etl_dag extract_data 2024-10-04

# Ver logs de task
airflow tasks log my_etl_dag extract_data 2024-10-04

# Listar tasks de DAG
airflow tasks list my_etl_dag

# Test task sin dependencies
airflow tasks test my_etl_dag extract_data 2024-10-04

# Clear task state para re-execution
airflow tasks clear my_etl_dag \
  --task-regex ".*transform.*" \
  --start-date 2024-10-04
```

**Connections y Variables:**
```bash
# Crear connection a database
airflow connections add postgres_default \
  --conn-type postgres \
  --conn-host localhost \
  --conn-login airflow \
  --conn-password secret \
  --conn-port 5432

# Listar connections
airflow connections list

# Set variable global
airflow variables set DATA_PATH "/opt/data"

# Get variable value
airflow variables get DATA_PATH

# Import variables desde JSON
airflow variables import variables.json
```

**Maintenance y Debugging:**
```bash
# Verificar configuración
airflow config list

# Test DAG parsing
airflow dags test my_etl_dag

# Database upgrade
airflow db upgrade

# Create admin user
airflow users create \
  --username admin \
  --password admin \
  --firstname Admin \
  --lastname User \
  --role Admin \
  --email admin@example.com

# Scheduler daemon
airflow scheduler

# Webserver daemon
airflow webserver --port 8080
```

## Notas
### Cornell

<table border="1" style="width:100%">
<tr>
<th style="width:30%">Conceptos Clave</th>
<th style="width:70%">Detalles y Explicaciones</th>
</tr>
<tr>
<td><strong>DAG Structure</strong></td>
<td>Directed Acyclic Graph define workflow mediante tasks y dependencies. No cycles permitidos para evitar infinite loops. Tasks ejecutan en topological order respecting dependencies. Schedule interval determina cuándo DAG runs (cron expression, timedelta, @daily, @hourly).</td>
</tr>
<tr>
<td><strong>Executors</strong></td>
<td>SequentialExecutor: Single-threaded, development only. LocalExecutor: Multi-threaded, single machine. CeleryExecutor: Distributed, multiple workers. KubernetesExecutor: Container-based, dynamic scaling. CeleryKubernetesExecutor: Hybrid approach.</td>
</tr>
<tr>
<td><strong>Task Dependencies</strong></td>
<td>Upstream/Downstream relationships usando >> operator o set_upstream/downstream methods. Task groups para logical grouping. Branching con BranchPythonOperator para conditional workflows. Trigger rules: all_success (default), all_failed, one_success, none_failed.</td>
</tr>
<tr>
<td><strong>XCom Mechanism</strong></td>
<td>Cross-communication entre tasks mediante key-value store. Limited size (48KB by default). JSON serializable data only. Alternative: external storage (S3, shared filesystem) para large datasets. Custom XCom backends para different storage systems.</td>
</tr>
<tr>
<td><strong>Sensors y Scheduling</strong></td>
<td>FileSensor: Wait for file existence. HttpSensor: API availability check. SqlSensor: Database condition monitoring. Custom sensors para specific conditions. Poke vs reschedule mode para resource optimization. Timeout y exponential backoff configuration.</td>
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
<td rowspan="5"><strong>Core Architecture</strong></td>
<td>Scheduler</td>
<td>DAG Parsing y Execution</td>
<td>Task queuing, dependency resolution</td>
</tr>
<tr>
<td>Webserver</td>
<td>UI Interface</td>
<td>DAG visualization, monitoring, debugging</td>
</tr>
<tr>
<td>Executor</td>
<td>Task Execution Engine</td>
<td>Local, Celery, Kubernetes options</td>
</tr>
<tr>
<td>Metadata Database</td>
<td>State Management</td>
<td>DAG runs, task instances, connections</td>
</tr>
<tr>
<td>Workers</td>
<td>Task Processing</td>
<td>Distributed execution, scaling</td>
</tr>
<tr>
<td rowspan="4"><strong>DAG Components</strong></td>
<td>Operators</td>
<td>Task Implementation</td>
<td>Bash, Python, SQL, HTTP, custom</td>
</tr>
<tr>
<td>Sensors</td>
<td>Condition Waiting</td>
<td>File, HTTP, SQL, time-based</td>
</tr>
<tr>
<td>Hooks</td>
<td>External Connections</td>
<td>Database, API, cloud service integration</td>
</tr>
<tr>
<td>Task Groups</td>
<td>Logical Organization</td>
<td>UI grouping, dependency management</td>
</tr>
<tr>
<td rowspan="4"><strong>Operations</strong></td>
<td>Scheduling</td>
<td>Automated Execution</td>
<td>Cron expressions, intervals, catchup</td>
</tr>
<tr>
<td>Monitoring</td>
<td>Observability</td>
<td>Logs, metrics, alerting, SLA tracking</td>
</tr>
<tr>
<td>Security</td>
<td>Access Control</td>
<td>Authentication, authorization, encryption</td>
</tr>
<tr>
<td>Maintenance</td>
<td>System Health</td>
<td>Database cleanup, log rotation, upgrades</td>
</tr>
</table>

## Resumen

Apache Airflow se ha establecido como la plataforma líder para workflow orchestration en Data Engineering, proporcionando una solución robusta y flexible para coordinar pipelines de datos complejas. Su paradigma **"Configuration as Code"** mediante Python DAGs ofrece unprecedented flexibility, version control, y maintainability comparado con traditional ETL tools basadas en GUI.

Las **ventajas fundamentales** incluyen: rich ecosystem de operators y hooks, distributed execution capabilities, comprehensive monitoring y alerting, extensive integration options, y active community support. La **Web UI intuitiva** combined con programmatic access via CLI permite tanto operational monitoring como automated management, satisfying needs de diferentes user personas.

**Aplicando Pareto 80/20**: El 80% del valor de Airflow se obtiene dominando el 20% esencial: DAG structure y dependency management, appropriate executor selection para scaling needs, effective monitoring y alerting setup, y security best practices implementation. Master estos fundamentals garantiza successful Airflow deployments que pueden scale desde simple automation hasta enterprise-grade orchestration.

La evolución hacia **Airflow 2.x** con improved UI, better Kubernetes integration, y enhanced security features, combined con growing ecosystem de providers y integrations, consolida a Airflow como la orchestration platform of choice para modern data architectures, especialmente en cloud-native y hybrid environments.