## Texto
### Lectura
dbt actúa como la capa de transformación en arquitecturas ELT modernas, permitiendo que los equipos de datos conviertan datos crudos almacenados en el data warehouse en modelos analíticos confiables. Sus proyectos se estructuran en carpetas como `models/`, `seeds/`, `tests/` y `snapshots/`, cada una con responsabilidades claras que favorecen la mantenibilidad. La instalación de dbt Core requiere un entorno Python administrado (por ejemplo, virtualenv) y la conexión a un warehouse compatible como Snowflake, BigQuery o Redshift. Una vez configurado el perfil, comandos básicos como `dbt init` generan la estructura del proyecto y `dbt run` ejecuta los modelos SQL declarativos. Comprender la diferencia entre dbt Core (open source, ejecutado vía CLI) y dbt Cloud (servicio gestionado con orquestación y UI) ayuda a elegir la plataforma adecuada según el tamaño del equipo y los requisitos operativos.
### Explicación con Técnica de Feynman
Imagina que tienes todos tus datos en una gran hoja de cálculo en la nube y quieres que estén limpios, documentados y listos para usarse. dbt es como un organizador inteligente que te ayuda a escribir instrucciones en SQL para transformar esos datos paso a paso, guardando cada transformación en carpetas específicas. Lo instalas en tu computadora, le dices cómo conectarse a tu almacén de datos y con un par de comandos (`dbt init`, `dbt run`) él ejecuta tus instrucciones y deja los resultados listos para análisis. Si prefieres no preocuparte por servidores, dbt Cloud es la misma idea pero con una página web que automatiza las ejecuciones.
### Ejemplos Simples
- Crear un proyecto local de práctica conectando dbt Core a un warehouse de prueba como DuckDB.
- Generar un primer modelo que calcula ventas totales por día a partir de una tabla de transacciones brutas.
- Ejecutar `dbt run` para compilar modelos en vistas y verificar que aparezcan en el esquema destino.
### Casos de Uso
- Equipos de analítica que necesitan un framework reproducible para curar métricas de negocio a partir de datos brutos.
- Startups que centralizan datos en BigQuery y requieren transformar registros operativos en tablas analíticas sin construir pipelines complejos.
- Consultoras que estandarizan implementaciones de data warehouses usando un modelo base de proyecto dbt reutilizable.
### Ejemplo de Implementacion
Definir un entorno virtual de Python controlado, instalar `dbt-core` y el adaptador del warehouse, y crear el archivo `profiles.yml` con credenciales seguras. Documentar el objetivo de cada carpeta del proyecto, generar modelos iniciales siguiendo convenciones de nomenclatura y ejecutar `dbt run` para validar la conexión. Complementar con procesos de onboarding que expliquen la diferencia entre entornos locales y gestionados como dbt Cloud.
### Comandos CLI o Web UI
- `dbt init proyecto_nombre` para generar la estructura base priorizando el 20 % de tareas iniciales.
- `dbt debug` para validar la conectividad y variables críticas antes de correr transformaciones extensas.
- `dbt run --select modelo` para ejecutar únicamente el modelo con mayor impacto inmediato.
- `dbt test` para lanzar pruebas predefinidas y asegurar calidad mínima sin revisar todo el catálogo.
- En dbt Cloud, programar un Job principal con los pasos `run` y `test` que cubren la mayoría de ejecuciones.
## Notas
### Cornell
<table>
  <tr><th>Preguntas Clave</th><th>Notas</th></tr>
  <tr><td>¿Qué problema resuelve dbt en ELT?</td><td>Estandariza transformaciones SQL directamente en el warehouse, evitando pipelines ETL complejos.</td></tr>
  <tr><td>¿Cómo se estructura un proyecto?</td><td>Carpetas `models/`, `tests/`, `snapshots/`, `seeds/` separan responsabilidades de desarrollo.</td></tr>
  <tr><td>¿Qué pasos iniciales son críticos?</td><td>Configurar entorno Python, adaptador del warehouse y ejecutar `dbt init`, `dbt run`, `dbt test`.</td></tr>
  <tr><td>¿Cuándo usar dbt Core vs Cloud?</td><td>Core para control local; Cloud para equipos que necesitan orquestación y UI gestionada.</td></tr>
</table>

### Outline Method
<table>
  <tr><th>Nivel</th><th>Contenido</th></tr>
  <tr><td>I</td><td>Rol de dbt en ELT moderno y arquitectura básica.</td></tr>
  <tr><td>II</td><td>Instalación, perfiles y conexión al warehouse.</td></tr>
  <tr><td>III</td><td>Estructura de carpetas y convenciones del proyecto.</td></tr>
  <tr><td>IV</td><td>Diferencias operativas entre dbt Core y dbt Cloud.</td></tr>
</table>

## Resumen
dbt introduce una capa de transformación modular que se integra directamente en el warehouse, exigiendo configuraciones iniciales sencillas y ofreciendo la opción entre ejecución local o en la nube para adaptarse a distintos equipos de datos.
