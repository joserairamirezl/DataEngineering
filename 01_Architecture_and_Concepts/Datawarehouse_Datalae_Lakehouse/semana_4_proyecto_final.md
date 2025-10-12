# Semana 4: Comparativa y Proyecto Final Lakehouse
## Texto
### Lectura
La última semana integra los aprendizajes previos para evaluar cuándo usar Data Warehouse, Data Lake o Lakehouse, y cómo diseñar una solución híbrida alineada al negocio. La comparativa debe considerar rendimiento, latencia, diversidad de datos, gobierno, costos y habilidades del equipo. Un enfoque pragmático reconoce que muchas organizaciones mantienen más de un patrón: un DW para reporting regulatorio, un Lake para ciencia de datos y un Lakehouse como capa unificadora.  
El diseño de arquitectura moderna requiere mapear fuentes (batch, streaming), capas de almacenamiento, procesamiento (ETL/ELT, streaming), catálogos y herramientas de consumo (BI, ML). Además, se deben establecer mecanismos de seguridad (IAM, encriptación, tokenización), monitoreo (observabilidad de pipelines, auditorías) y optimización de costos (particionamiento, auto-suspend). El objetivo es justificar técnicamente la elección de servicios como S3, Glue, Redshift, Athena, Databricks, BigQuery, Lake Formation o Power BI según los requerimientos de negocio.  
Un entregable típico incluye un diagrama de arquitectura, un documento de decisiones (ADR), estimaciones de costo y un flujo de datos end-to-end. También se recomienda definir OKR de analítica (latencia, confiabilidad, adopción) y planificar un roadmap incremental que comience con quick wins mientras se consolida la plataforma Lakehouse.

### Explicación con Técnica de Feynman
Imagina que debes construir una casa inteligente para datos. El Data Warehouse es como una sala de archivos muy ordenada; el Data Lake, un sótano gigante donde guardas de todo; y el Lakehouse, un sistema que conecta ambas cosas con puertas automáticas y sensores. En el proyecto final decides qué piezas usar: qué datos van directo a la sala ordenada, cuáles se quedan en el sótano y cómo las puertas inteligentes permiten que todos consulten la información correcta de forma segura y rápida. Tu trabajo es dibujar ese plano y explicar por qué cada decisión tiene sentido para tu empresa.

### Ejemplos Simples
*Tabla de decisión rápida (DW vs DL vs LH):*
```
| Criterio             | Data Warehouse | Data Lake | Lakehouse |
|----------------------|----------------|-----------|-----------|
| Datos estructurados  | Excelente      | Limitado  | Excelente |
| Datos no estructurados | Pobre       | Excelente | Muy bueno |
| Costos a gran escala | Medio         | Bajo      | Medio     |
| Governanza granular  | Alta          | Media     | Alta      |
| Workloads ML         | Limitado      | Excelente | Excelente |
```

*Consulta analítica final (Redshift o BigQuery):*
```sql
SELECT fecha, canal, SUM(ingresos) AS ingresos, SUM(costos) AS costos,
       SUM(ingresos) - SUM(costos) AS margen
FROM lakehouse_gold.ventas
WHERE fecha BETWEEN DATE_SUB(CURRENT_DATE(), INTERVAL 30 DAY) AND CURRENT_DATE()
GROUP BY fecha, canal
ORDER BY fecha;
```

### Casos de Uso
- E-commerce global que requiere reporting financiero certificado, dashboards near real-time y modelos de recomendación.
- Empresa de IoT industrial que combina telemetría streaming con datos maestros en DW y mantenimiento predictivo.
- Banco digital que necesita historiales auditables, detección de fraude y analítica self-service en una plataforma unificada.

### Ejemplo de Implementacion
1. Recopilar requerimientos funcionales y no funcionales (SLAs, compliance, presupuesto) con stakeholders de negocio y TI.  
2. Elaborar un diagrama detallado que muestre ingestión (batch/streaming), capas Bronze/Silver/Gold, catálogos, seguridad y herramientas de consumo.  
3. Definir el pipeline maestro: ingestion raw → curado → tablas Lakehouse → data marts analíticos; documentar dataflow, triggers y latencias.  
4. Crear un MVP implementando una fuente crítica (ej. ventas) usando IaC (Terraform/CloudFormation) y notebooks orquestados.  
5. Configurar monitoreo (CloudWatch, Stackdriver, Datadog) y tableros de calidad (Great Expectations, Monte Carlo) para asegurar confiabilidad.  
6. Preparar documentación final: ADRs, runbooks operativos, estimación de costos y plan de adopción por equipos de negocio.

### Comandos CLI o Web UI
- `terraform apply -var-file=prod.tfvars` para provisionar infraestructura reproducible del Lakehouse.
- `aws stepfunctions start-execution --state-machine-arn <arn> --input file://payload.json` para lanzar pipelines orquestados del proyecto.
- `gcloud dataflow jobs run etl-ventas --gcs-location gs://plantillas/etl-ventas.json` para ejecutar transformaciones en GCP.
- `databricks sql query execute --query-id <id>` para validar vistas analíticas desde el Lakehouse Gold.
- `powerbi update-datasource --workspace <ws> --name Lakehouse` (Power BI CLI) para refrescar dashboards del entregable final.

## Notas
### Cornell
<table>
  <tr><th>Pista / Pregunta</th><th>Notas</th></tr>
  <tr><td>Comparativa arquitecturas</td><td>DW = reporting estructurado; DL = flexibilidad; LH = convergencia con ACID.</td></tr>
  <tr><td>Elementos críticos del diseño</td><td>Ingesta, almacenamiento, procesamiento, catálogo, seguridad, observabilidad.</td></tr>
  <tr><td>Métricas del proyecto</td><td>Latencia, confiabilidad, adopción de usuarios, costos operativos.</td></tr>
  <tr><td>Roadmap</td><td>Comenzar con MVP, iterar hacia cobertura total, automatizar gobernanza.</td></tr>
</table>

### Outline Method
<table>
  <tr><th>Nivel</th><th>Idea</th></tr>
  <tr><td>I</td><td>Evaluación comparativa DW vs DL vs Lakehouse</td></tr>
  <tr><td>II</td><td>Diseño integral: ingestión, procesamiento, consumo, seguridad</td></tr>
  <tr><td>III</td><td>Pipelines y herramientas clave (IaC, orquestadores, BI)</td></tr>
  <tr><td>III</td><td>Monitoreo, calidad de datos y control de costos</td></tr>
  <tr><td>II</td><td>Entregables del proyecto final y roadmap</td></tr>
</table>

## Resumen
La semana final consolida los conceptos comparando arquitecturas y culmina con un diseño Lakehouse completo respaldado por argumentos técnicos. El proyecto resultante detalla flujos de ingestión, procesamiento y consumo, incorpora gobernanza y monitoreo, y brinda un plan incremental para llevar la plataforma a producción con confianza.
