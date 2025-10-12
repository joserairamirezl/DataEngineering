# Semana 4: Escalabilidad, Tuning y Proyecto Final
## Texto
### Lectura
Escalar Kafka implica dimensionar particiones, réplicas y hardware para soportar throughput creciente y tolerancia a fallos. Cada partición se replica en brokers diferentes; mantener `min.insync.replicas` alineado con el factor de replicación protege contra pérdida de datos en fallos. Ajustes como `num.network.threads`, `num.io.threads` y `socket.buffer.size` ayudan a optimizar el rendimiento. La retención de datos puede gestionarse por tiempo (`retention.ms`) o tamaño (`retention.bytes`), permitiendo balancear requisitos de auditoría y costos de almacenamiento.  
El monitoreo continuo con JMX, Prometheus y Grafana permite observar métricas clave: lag de consumidores, throughput, tiempos de replicación y estado de ISR. Los logs de brokers y controlador ayudan a diagnosticar rebalances, GC o throttling. Para seguridad, Kafka soporta autenticación SASL/SSL, autorización basada en ACLs y cifrado en tránsito. Integrar estas medidas es imprescindible antes de entornos productivos.  
El proyecto final sintetiza estos conceptos construyendo un pipeline end-to-end: productores fiables, tópicos particionados, procesamiento en Streams/KSQL y sinks mediante Connect. A ello se suman runbooks de operación, diagramas de arquitectura, pruebas de resiliencia y estrategias de costo.

### Explicación con Técnica de Feynman
Imagina que Kafka es una línea de producción. Para que funcione sin detenerse, duplicas estaciones (réplicas) y asignas supervisores que se aseguran de que todas trabajen al mismo ritmo. Colocas sensores que miden cuántas piezas entran y salen y alarmas que avisan si una estación se detiene. Las reglas de acceso garantizan que solo el personal autorizado toque las máquinas. El proyecto final es como diseñar toda la línea, probando que aguante la demanda y documentando qué hacer si algo falla.

### Ejemplos Simples
*Fragmento de configuración `server.properties` para tuning:*
```properties
num.partitions=6
default.replication.factor=3
min.insync.replicas=2
log.retention.hours=168
compression.type=snappy
num.network.threads=3
num.io.threads=8
socket.send.buffer.bytes=102400
socket.receive.buffer.bytes=102400
```

*Script para simular resiliencia al apagar un broker:*
```bash
# Identificar broker y detener contenedor
docker stop broker-2

# Verificar estado ISR
kafka-topics.sh --describe --topic transacciones --bootstrap-server localhost:9092 | grep ISR

# Reiniciar y confirmar recuperación
docker start broker-2
```

### Casos de Uso
- Plataforma de pagos que exige latencia constante y retención de 7 días con replicación triple.
- Sistema IoT masivo que ajusta retención por tamaño y aplica compresión para optimizar costos.
- Organización regulada que implementa ACLs por tópico y monitoreo centralizado vía Grafana.
- Proyecto final de ingestión en tiempo real con dashboards que muestran KPIs de negocio.

### Ejemplo de Implementacion
1. Definir el proyecto final (por ejemplo, pipeline de transacciones) con requerimientos de SLA, retención y seguridad.  
2. Dimensionar tópicos y particiones según throughput estimado, configurando replicación y políticas de retención.  
3. Implementar productores idempotentes, consumidores monitorizados y procesamiento intermedio (Streams/KSQL).  
4. Desplegar Kafka Connect para enviar resultados a un sink (S3, PostgreSQL o Elasticsearch).  
5. Configurar Prometheus JMX Exporter y dashboards en Grafana para métricas de brokers y lag.  
6. Ejecutar pruebas de resiliencia (failover de broker, cambios de retención) y documentar runbooks operativos.

### Comandos CLI o Web UI
- `kafka-configs.sh --alter --entity-type brokers --entity-name <id> --add-config log.retention.ms=604800000` para ajustar retención sin reinicio.
- `kafka-preferred-replica-election.sh --bootstrap-server <host>:9092` para restaurar líderes tras mantenimiento.
- `kafka-acls.sh --add --allow-principal User:analitica --operation Read --topic ventas_gold --bootstrap-server <host>:9092` para definir permisos.
- `kafka-consumer-groups.sh --bootstrap-server <host>:9092 --group <grupo> --describe` para monitorizar lag durante pruebas de estrés.
- `prometheus --config.file=prometheus.yml` y `grafana-server` para levantar monitoreo del clúster (comandos principales).

## Notas
### Cornell
<table>
  <tr><th>Pista / Pregunta</th><th>Notas</th></tr>
  <tr><td>Escalabilidad</td><td>Más particiones, replicación adecuada y tuning de threads/socket para throughput.</td></tr>
  <tr><td>Retención</td><td>Definir políticas por tiempo o tamaño según requisitos legales y costos.</td></tr>
  <tr><td>Monitoreo</td><td>Prometheus + Grafana, métricas de lag, ISR, tasas de mensajes.</td></tr>
  <tr><td>Seguridad</td><td>SASL/SSL, ACLs por tópico, cifrado en tránsito y autenticación centralizada.</td></tr>
</table>

### Outline Method
<table>
  <tr><th>Nivel</th><th>Idea</th></tr>
  <tr><td>I</td><td>Dimensionamiento y tuning del clúster</td></tr>
  <tr><td>II</td><td>Retención, replicación y resiliencia</td></tr>
  <tr><td>III</td><td>Monitoreo y observabilidad con Prometheus/Grafana</td></tr>
  <tr><td>III</td><td>Seguridad: autenticación y autorización</td></tr>
  <tr><td>II</td><td>Proyecto final: pipeline end-to-end y pruebas de failover</td></tr>
</table>

## Resumen
La cuarta semana integra escalabilidad, seguridad y operación para llevar Kafka a producción. Afinar configuraciones de brokers, establecer monitoreo, aplicar políticas de retención y ejecutar pruebas de resiliencia permiten entregar un proyecto final listo para entornos exigentes, con runbooks claros y garantías de disponibilidad.
