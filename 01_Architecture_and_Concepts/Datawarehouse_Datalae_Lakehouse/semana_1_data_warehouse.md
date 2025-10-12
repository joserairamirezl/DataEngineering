# Semana 1: Fundamentos del Data Warehouse
## Texto
### Lectura
El Data Warehouse (DW) surgió para responder preguntas estratégicas con datos históricos limpios y consistentes. Se construye sobre un modelo relacional diseñado para análisis, donde la normalización extrema se sacrifica para privilegiar consultas rápidas y agregaciones. Los enfoques de Kimball (bus dimensional y marts) e Inmon (integración corporativa centralizada) siguen vigentes, aunque hoy conviven con arquitecturas híbridas. Comprender sus diferencias ayuda a elegir cómo organizar hechos y dimensiones, cómo gobernar los metadatos y qué procesos de integración se necesitan.  
La separación entre sistemas transaccionales (OLTP) y analíticos (OLAP) es clave: OLTP optimiza escrituras cortas y consistencia inmediata; OLAP optimiza lecturas masivas con latencia aceptable. Las cargas históricas se procesan mediante ETL clásica (extraer–transformar–cargar) o ELT (extraer–cargar–transformar), según la capacidad del motor analítico moderno. El objetivo sigue siendo disponer de una “única fuente de verdad” sobre indicadores críticos como ventas, inventario o riesgo.  
El modelado dimensional (estrella o copo de nieve) facilita la exploración guiada por métricas y dimensiones. Habilita herramientas de BI, cubos OLAP y consultas SQL que los analistas pueden mantener. En la nube, servicios como Amazon Redshift, Snowflake o Google BigQuery automatizan escalado y administración, pero los principios fundamentales permanecen: calidad de datos, rendimiento de consulta y gobernanza.

### Explicación con Técnica de Feynman
Imagina que una empresa quiere responder preguntas como “¿cuánto vendimos por región el mes pasado?”. El Data Warehouse es como una gran biblioteca organizada donde cada libro (tabla de hechos) cuenta una parte cuantitativa de la historia y cada índice (tabla de dimensiones) describe atributos que dan contexto. Las operaciones diarias se copian, limpian y ordenan en esta biblioteca para que, cuando alguien pregunte, la respuesta esté lista sin volver a revisar todos los sistemas originales. Por eso necesitamos procesos que limpien y transformen datos antes de guardarlos, y modelos que permitan buscar rápido sin perder significados.

### Ejemplos Simples
*Modelo estrella de ventas (SQL simplificado):*
```sql
CREATE TABLE dim_tiempo (
    id_tiempo INT PRIMARY KEY,
    fecha DATE,
    mes INT,
    anio INT
);

CREATE TABLE dim_tienda (
    id_tienda INT PRIMARY KEY,
    nombre VARCHAR(100),
    region VARCHAR(50)
);

CREATE TABLE fact_ventas (
    id_tiempo INT,
    id_tienda INT,
    sku VARCHAR(50),
    unidades INT,
    ingresos NUMERIC(12,2)
);
```
*Consulta OLAP básica:*
```sql
SELECT t.region, ti.mes, SUM(f.ingresos) AS ingresos_totales
FROM fact_ventas f
JOIN dim_tienda t ON f.id_tienda = t.id_tienda
JOIN dim_tiempo ti ON f.id_tiempo = ti.id_tiempo
GROUP BY t.region, ti.mes;
```

### Casos de Uso
- Consolidar ventas omnicanal para marketing y forecasting.
- Monitorear métricas de manufactura (rendimiento, scrap, OEE) con datos históricos.
- Evaluar rentabilidad de portafolios financieros conforme a regulaciones (Basel, IFRS).
- Analizar indicadores de experiencia de cliente con históricos de CRM y soporte.

### Ejemplo de Implementacion
1. Identificar fuentes OLTP (ERP, CRM, POS) y definir alcance del modelo estrella inicial.  
2. Configurar un pipeline ETL/ELT: extracción incremental, validaciones de calidad, normalización de claves y codificaciones.  
3. Diseñar el modelo dimensional en el DW destino (por ejemplo Redshift o BigQuery) y crear tablas persistentes.  
4. Implementar cargas iniciales (full load) y luego cargas incrementales con ventanas de tiempo o marcas de agua.  
5. Publicar métricas en dashboards de BI y monitorear rendimiento, calidad y latencia de datos.  
6. Documentar glosario, reglas de negocio y políticas de acceso para asegurar gobernanza continua.

### Comandos CLI o Web UI
- `psql -h <host> -U <usuario> -d <dw> -c "<consulta>"` para validar modelos y ejecutar consultas en Redshift/PostgreSQL.
- `aws glue start-job-run --job-name cargar_dim_tiempo` para orquestar cargas ETL en Glue (principal pipeline crítico).
- `bq query --use_legacy_sql=false "<consulta>"` para ejecutar transformaciones ELT en BigQuery.
- `snowsql -q "<consulta>"` para revisar cargas en Snowflake sin ingresar a la consola.
- `aws redshift-data execute-statement --cluster-identifier <id> --database <db> --sql "<stmt>"` para automatizar scripts de mantenimiento.

## Notas
### Cornell
<table>
  <tr><th>Pista / Pregunta</th><th>Notas</th></tr>
  <tr><td>¿Por qué separar OLTP y OLAP?</td><td>Optimizar consultas analíticas sin afectar operaciones; diferentes patrones de acceso.</td></tr>
  <tr><td>ETL vs ELT</td><td>ETL transforma antes de cargar; ELT aprovecha potencia del DW para transformar.</td></tr>
  <tr><td>Modelo estrella</td><td>Centraliza hechos numéricos; dimensiones describen contexto y habilitan agregaciones rápidas.</td></tr>
  <tr><td>Gobernanza</td><td>Glosario, control de accesos y linaje aseguran confianza en la “única versión de la verdad”.</td></tr>
</table>

### Outline Method
<table>
  <tr><th>Nivel</th><th>Idea</th></tr>
  <tr><td>I</td><td>Arquitectura DW: almacenamiento histórico integrado</td></tr>
  <tr><td>II</td><td>Procesos ETL/ELT y separación OLTP/OLAP</td></tr>
  <tr><td>III</td><td>Modelado dimensional (estrella, copo de nieve)</td></tr>
  <tr><td>III</td><td>Herramientas en la nube (Redshift, Snowflake, BigQuery)</td></tr>
  <tr><td>II</td><td>Gobernanza y métricas de calidad</td></tr>
</table>

## Resumen
El Data Warehouse ofrece un repositorio analítico consolidado que convierte datos operacionales dispersos en información confiable. Se apoya en modelos dimensionales, procesos ETL/ELT y plataformas OLAP que habilitan análisis histórico consistente. Dominar estos fundamentos permite escalar hacia arquitecturas modernas sin perder disciplina en calidad y gobierno de datos.
