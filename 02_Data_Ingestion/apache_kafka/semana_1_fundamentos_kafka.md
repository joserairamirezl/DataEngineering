# Semana 1: Fundamentos y Arquitectura de Apache Kafka
## Texto
### Lectura
Apache Kafka es una plataforma distribuida de mensajería orientada a eventos que permite procesar flujos de datos en tiempo real con alta resiliencia. Su arquitectura se basa en clústeres de brokers que almacenan mensajes dentro de tópicos, los cuales se dividen en particiones para lograr paralelismo y balanceo de carga. Cada mensaje se identifica por un offset inmutable, lo que facilita el reprocessado y la tolerancia a fallos. La comunicación sigue el patrón publish-subscribe: productores publican mensajes en tópicos y consumidores los leen de manera secuencial.  
ZooKeeper coordinaba la metadata histórica del clúster (en Kafka clásicos), pero las versiones modernas integran su propio controller quorum para simplificar la operación. La durabilidad se obtiene replicando particiones entre brokers, mientras que el throughput se optimiza con escritura secuencial a disco y transferencia por lotes. Estas propiedades hacen que Kafka destaque frente a colas tradicionales (RabbitMQ) o servicios administrados como Kinesis.  
Para iniciar con Kafka es clave comprender su ecosistema mínimo: instalarlo localmente (bare metal, Docker o contenedores administrados), crear tópicos con el tamaño y factor de replicación correctos, y validar el flujo de mensajes mediante productores y consumidores de consola. Estos fundamentos cimentan los pipelines de ingestión y streaming más complejos.

### Explicación con Técnica de Feynman
Imagina Kafka como una pizarra magnética gigante dividida en columnas (particiones). Cada vez que alguien (productor) escribe una tarjeta con información, la pega en la columna correspondiente. Las tarjetas se quedan allí, en orden, y cada equipo (consumidor) puede leerlas desde donde necesite gracias a un marcador que indica el último mensaje visto. Si se pierde la tarjeta o alguien necesita revisarla, basta con volver al punto exacto porque la pizarra mantiene el historial. Varias pizarras idénticas (réplicas) aseguran que la información no se pierda si una falla.

### Ejemplos Simples
*Docker Compose mínimo para Kafka y ZooKeeper:*
```yaml
version: "3.8"
services:
  zookeeper:
    image: confluentinc/cp-zookeeper:7.5.0
    environment:
      ZOOKEEPER_CLIENT_PORT: 2181
  kafka:
    image: confluentinc/cp-kafka:7.5.0
    depends_on:
      - zookeeper
    environment:
      KAFKA_BROKER_ID: 1
      KAFKA_ZOOKEEPER_CONNECT: zookeeper:2181
      KAFKA_LISTENERS: PLAINTEXT://0.0.0.0:9092
      KAFKA_ADVERTISED_LISTENERS: PLAINTEXT://localhost:9092
```

*Producción y consumo de mensajes desde consola:*
```bash
# Crear topic
kafka-topics.sh --create --topic demo --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1

# Producir
kafka-console-producer.sh --topic demo --bootstrap-server localhost:9092

# Consumir
kafka-console-consumer.sh --topic demo --bootstrap-server localhost:9092 --from-beginning
```

### Casos de Uso
- Ingestar eventos de aplicaciones web y móviles para analítica en tiempo real.
- Centralizar logs de microservicios y distribuirlos a sistemas downstream.
- Gestionar flujos de datos IoT con alta frecuencia y baja latencia.
- Sincronizar información entre servicios con arquitectura orientada a eventos.

### Ejemplo de Implementacion
1. Provisionar infraestructura local o en la nube (Docker Compose, EC2, Kubernetes).  
2. Configurar brokers con propiedades básicas (`listeners`, `log.dirs`, `num.partitions`).  
3. Crear tópicos iniciales definiendo particiones y factor de replicación según el SLA.  
4. Validar el flujo publish-subscribe con productores y consumidores de consola.  
5. Documentar nomenclatura de tópicos, convenciones de claves y políticas de retención.  
6. Configurar observabilidad básica (logs, métricas JMX) para evaluar el rendimiento.

### Comandos CLI o Web UI
- `kafka-topics.sh --describe --topic <topic> --bootstrap-server <host>:9092` para inspeccionar particiones y réplicas.
- `kafka-storage.sh format --config server.properties --cluster-id <id>` para inicializar almacenamiento en nuevas instalaciones (Kafka 2.8+).
- `docker compose up -d` para levantar rápidamente un entorno local de práctica.
- `kafka-broker-api-versions.sh --bootstrap-server <host>:9092` para verificar compatibilidad entre clientes y brokers.
- `kafka-metadata-shell.sh --snapshot /tmp/__cluster_metadata-0.snapshot` para explorar metadata (controlador KRaft).

## Notas
### Cornell
<table>
  <tr><th>Pista / Pregunta</th><th>Notas</th></tr>
  <tr><td>Componentes clave</td><td>Broker, topic, partición, offset, productor, consumidor, controller.</td></tr>
  <tr><td>¿Por qué Kafka es rápido?</td><td>Escrituras secuenciales, replicación, batching, compresión opcional.</td></tr>
  <tr><td>Publish-subscribe</td><td>Productores escriben en tópicos; consumidores leen en orden y pueden reprocessar.</td></tr>
  <tr><td>Comparativa</td><td>Kinesis/Pulsar manejan particionado similar; RabbitMQ orientado a colas tradicionales.</td></tr>
</table>

### Outline Method
<table>
  <tr><th>Nivel</th><th>Idea</th></tr>
  <tr><td>I</td><td>Introducción a Kafka y patrón publish-subscribe</td></tr>
  <tr><td>II</td><td>Arquitectura distribuida: brokers, particiones, offsets</td></tr>
  <tr><td>III</td><td>Instalación base (Docker, local) y configuración esencial</td></tr>
  <tr><td>III</td><td>Flujo inicial productor-consumidor y validaciones</td></tr>
  <tr><td>II</td><td>Buenas prácticas iniciales y observabilidad</td></tr>
</table>

## Resumen
La primera semana establece los fundamentos de Apache Kafka: arquitectura distribuida, tópicos particionados y el flujo publish-subscribe. Instalar un clúster de práctica, crear tópicos y probar productores y consumidores de consola permite entender cómo Kafka garantiza durabilidad y escalabilidad desde sus componentes básicos.
