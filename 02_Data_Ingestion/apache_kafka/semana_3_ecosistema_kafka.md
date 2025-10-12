# Semana 3: Ecosistema Kafka y Procesamiento de Datos
## Texto
### Lectura
El ecosistema de Kafka extiende sus capacidades más allá del bus de eventos. Kafka Connect simplifica la integración con sistemas externos mediante conectores *source* y *sink* listos para usar, administrados con configuraciones declarativas. Permite escalar workers distribuidos y gestionar transformaciones simples sin escribir código personalizado. Kafka Streams habilita procesamiento en tiempo real dentro de aplicaciones Java/Scala utilizando la API Streams DSL o Processor API, soportando operaciones stateful, joins y ventanas. Alternativas como ksqlDB (KSQL) ofrecen una capa SQL para consultas continuas sobre tópicos.  
Para asegurar compatibilidad de esquemas, herramientas como Confluent Schema Registry permiten versionar Avro, JSON Schema o Protobuf y validar compatibilidad evolutiva. Esto evita romper consumidores cuando cambian los eventos. Adicionalmente, la integración con frameworks como Apache Spark, Flink o herramientas de BI/ELT habilita pipelines avanzados que generan insights en tiempo real o alimentan data lakes. Visualizadores como Kafdrop y Conduktor aportan diagnósticos y monitoreo intuitivo.  
Adoptar estas herramientas requiere comprender despliegues distribuidos, configuración de workers, temas internos (como `__consumer_offsets`, `__connect-offsets`) y políticas de seguridad/coordinación (REST API Connect, RBAC, TLS). Con una base sólida, se pueden construir pipelines robustos y componibles.

### Explicación con Técnica de Feynman
Piensa que Kafka es una autopista. Kafka Connect son las rampas que permiten que diferentes ciudades (bases de datos, APIs, archivos) se conecten sin construir carreteras propias. Kafka Streams es un conjunto de talleres sobre la autopista donde los datos se combinan o transforman mientras circulan. El Schema Registry es el manual que asegura que todas las ciudades entiendan el formato de los mensajes para que nadie reciba un paquete incomprensible.

### Ejemplos Simples
*Configuración de Kafka Connect (standalone) para leer un CSV y publicarlo:*
```properties
name=file-source
connector.class=FileStreamSource
tasks.max=1
file=/data/ventas.csv
topic=ventas_raw
```

*Consulta ksqlDB para filtrar transacciones sospechosas:*
```sql
CREATE STREAM transacciones_sospechosas AS
SELECT id, monto, pais
FROM transacciones_stream
WHERE monto > 10000
EMIT CHANGES;
```

*Topología básica en Kafka Streams (Java DSL):*
```java
StreamsBuilder builder = new StreamsBuilder();
KStream<String, String> source = builder.stream("ventas_raw");
KStream<String, String> clean = source
    .filter((key, value) -> value.contains("APROBADA"));
clean.to("ventas_filtradas");
```

### Casos de Uso
- Replicar datos de PostgreSQL a Kafka y luego a un data lake mediante conectores Debezium y S3 sink.
- Construir pipelines de detección de fraude en tiempo real con Kafka Streams y tablas de referencia en RocksDB.
- Transformar flujos de IoT con ksqlDB aplicando agregaciones por ventanas temporales.
- Habilitar gobernanza de esquemas para APIs de eventos compartidos entre múltiples equipos.

### Ejemplo de Implementacion
1. Desplegar Kafka Connect en modo standalone o distributed, configurando almacenamiento de offsets y status.  
2. Registrar conectores con configuraciones REST, estableciendo transformaciones simples (Single Message Transform).  
3. Configurar Schema Registry y actualizar productores/consumidores para registrar esquemas y validar compatibilidad.  
4. Crear aplicaciones Kafka Streams o ksqlDB que enriquezcan datos y publiquen en tópicos derivados.  
5. Integrar herramientas de visualización (Kafdrop, Conduktor) para monitorear tópicos y lags.  
6. Automatizar despliegues y configuraciones con IaC o pipelines CI/CD para mantener consistencia.

### Comandos CLI o Web UI
- `curl -X POST -H "Content-Type: application/json" --data @connector.json http://localhost:8083/connectors` para registrar conectores (REST Connect).
- `connect-distributed.sh config/connect-distributed.properties` para iniciar workers distribuidos.
- `kafka-avro-console-producer --topic <topic> --broker-list <host>:9092 --property value.schema='{"type":"record","name":"Evento","fields":[{"name":"id","type":"string"}]}'` para publicar mensajes con Schema Registry.
- `ksql http://localhost:8088` para entrar a la consola interactiva de ksqlDB.
- `kafka-streams-application-reset.sh --application-id <app-id> --bootstrap-servers <host>:9092 --input-topics <topics>` para reiniciar estado de una aplicación Streams.

## Notas
### Cornell
<table>
  <tr><th>Pista / Pregunta</th><th>Notas</th></tr>
  <tr><td>Kafka Connect</td><td>Framework declarativo para integrar sistemas externos mediante conectores.</td></tr>
  <tr><td>Kafka Streams</td><td>Procesamiento embebido en aplicaciones; soporta estado y ventanas.</td></tr>
  <tr><td>Schema Registry</td><td>Versionado y compatibilidad de esquemas Avro/JSON/Protobuf.</td></tr>
  <tr><td>Herramientas adicionales</td><td>KSQL para SQL streaming, Kafdrop/Conduktor para visualización.</td></tr>
</table>

### Outline Method
<table>
  <tr><th>Nivel</th><th>Idea</th></tr>
  <tr><td>I</td><td>Ecosistema Kafka: visión general</td></tr>
  <tr><td>II</td><td>Kafka Connect: conectores source/sink y despliegue</td></tr>
  <tr><td>III</td><td>Schema Registry y gobierno de eventos</td></tr>
  <tr><td>III</td><td>Kafka Streams / ksqlDB para procesamiento</td></tr>
  <tr><td>II</td><td>Integraciones y observabilidad complementaria</td></tr>
</table>

## Resumen
La tercera semana explora herramientas que convierten a Kafka en una plataforma integral de ingestión y procesamiento. Conectores, Streams y Schema Registry permiten mover, transformar y gobernar datos en tiempo real, habilitando integraciones con sistemas empresariales y analítica avanzada sin replicar esfuerzos manuales.
