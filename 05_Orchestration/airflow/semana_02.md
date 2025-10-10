## Texto
### Lectura
En Airflow, los Operators encapsulan lógica reutilizable para ejecutar acciones específicas: BashOperator para comandos, PythonOperator para funciones personalizadas, EmailOperator para notificaciones y BranchOperator para rutas condicionales. Elegir correctamente el Operator cubre gran parte de la orquestación sin reinventar código.
Hooks actúan como conectores hacia sistemas externos (bases de datos, nubes, APIs), gestionando credenciales desde la Metadata DB. Este diseño permite que un DAG replique pipelines en distintos ambientes modificando solo la conexión. Las Variables complementan la parametrización guardando configuraciones contextualizadas.
XComs (cross-communications) permiten pasar pequeños volúmenes de datos entre tareas. Si se abusa de XComs para mover grandes datasets, se saturará la base de metadatos; por eso, un uso disciplinado es parte del 20% de prácticas que determina el 80% de la estabilidad.
Las plantillas Jinja habilitan dinamismo en parámetros de Operators (por ejemplo, fechas de ejecución), permitiendo DAGs más expresivos sin código complejo. Entender cómo se combinan macros de Airflow con estas plantillas es clave para pipelines dependientes de ventanas de datos.
### Explicación con Técnica de Feynman
Imagina que un DAG es una fábrica modular: los Operators son máquinas especializadas; los Hooks son puertos que conectan la fábrica con el exterior; las Variables son perillas que cambian configuraciones; y los XComs son notas pequeñas que un operario deja a otro para continuar el trabajo.
### Ejemplos Simples
- Usar BashOperator para ejecutar un comando muy corto en una tarea.
- Definir una Variable desde la UI y leerla en un PythonOperator.
- Enviar un valor pequeño entre dos tareas usando XComs para decidir la siguiente acción.
### Casos de Uso
- Automatizar extracción de datos desde una API REST con HttpHook y procesarlos con PythonOperator.
- Ejecutar cargas hacia warehouses utilizando PostgresHook o BigQueryHook con credenciales centralizadas.
- Enviar notificaciones automáticas por email cuando una rama de procesamiento detecta condiciones especiales.
### Ejemplo de Implementacion
Mapear qué sistemas externos participan en el pipeline, registrar conexiones con roles y permisos adecuados, estandarizar el uso de Variables para rutas y credenciales no sensibles, y establecer guías sobre cuándo usar XComs versus almacenamiento externo. Documentar Operators personalizados en un repositorio común para fomentar reutilización.
### Comandos CLI o Web UI
- `airflow connections add` — administra Hooks y credenciales.
- `airflow variables set` — define variables para parametrización.
- `airflow dags trigger <dag_id>` — ejecuta DAGs bajo demanda para pruebas.
- `http://localhost:8080/variable/list/` — gestiona Variables desde la UI.
- `http://localhost:8080/connection/list/` — revisa conexiones disponibles.
## Notas
### Cornell
<table>
  <thead>
    <tr><th>Pistas</th><th>Notas</th><th>Resumen</th></tr>
  </thead>
  <tbody>
    <tr><td>Operators</td><td>Bash, Python, Email, Branch cubren escenarios comunes.</td><td>Bloques reutilizables del DAG.</td></tr>
    <tr><td>Hooks y Variables</td><td>Conexiones externas y parametrización centralizada.</td><td>Separan código de configuración.</td></tr>
    <tr><td>XComs</td><td>Intercambio ligero de datos; evitar uso intensivo.</td><td>Comunicación controlada entre tareas.</td></tr>
  </tbody>
</table>
### Outline Method
<table>
  <thead>
    <tr><th>Nivel</th><th>Punto clave</th><th>Detalle de apoyo</th></tr>
  </thead>
  <tbody>
    <tr><td>I</td><td>Tipos de Operators</td><td>Encapsulan acciones, fomentan reutilización.</td></tr>
    <tr><td>II</td><td>Hooks y conexiones</td><td>Gestión de credenciales y endpoints.</td></tr>
    <tr><td>III</td><td>Variables y templating</td><td>Parametrización dinámica con Jinja.</td></tr>
    <tr><td>IV</td><td>XComs</td><td>Comunicación controlada entre tareas.</td></tr>
  </tbody>
</table>
## Resumen
Dominar Operators, Hooks, Variables y XComs convierte a los DAGs en piezas flexibles y mantenibles. Aplicar buenas prácticas en estos componentes evita sobrecargas en la metadata y facilita conectar Airflow con el ecosistema de datos.
