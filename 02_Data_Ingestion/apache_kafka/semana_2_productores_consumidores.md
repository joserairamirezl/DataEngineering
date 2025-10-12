# Semana 2: Productores, Consumidores y Configuración
## Texto
### Lectura
Los productores en Kafka controlan la durabilidad y el rendimiento mediante parámetros como `acks`, `retries`, `linger.ms` y `batch.size`. La clave del mensaje determina la partición destino, lo que permite ordenar eventos relacionados. Configurar `acks=all` asegura que el mensaje se replique en todas las réplicas sincronizadas antes de confirmarse, mientras que `acks=1` prioriza el throughput. Retries con backoff evitan pérdidas temporales cuando un broker falla.  
Los consumidores operan en grupos para escalar la lectura; cada partición se asigna a una única instancia dentro del grupo, asegurando procesamiento exclusivo. Los offsets representan la posición del consumidor y pueden confirmarse automáticamente (`enable.auto.commit`) o manualmente, lo cual es imprescindible cuando se buscan garantías *at-least-once* o *exactly-once*. Kafka proporciona herramientas para monitorizar lag y rebalances, lo que permite detectar cuellos de botella.  
Entender los modelos de entrega es esencial: *at-most-once* privilegia latencia pero puede perder mensajes; *at-least-once* reintenta y puede duplicar eventos que luego deben idempotenciarse; *exactly-once* combina transacciones y control sobre offsets, disponible en Kafka Streams y productores idempotentes con transacciones. Configurar correctamente clientes, serializadores y políticas de commits es la base para pipelines confiables.

### Explicación con Técnica de Feynman
Imagina que el productor es un mensajero que entrega paquetes a varios casilleros (particiones). Puede esperar confirmación de todos los guardias (réplicas), de uno solo o de ninguno, según cuánta seguridad quiera. El consumidor es otro mensajero que recoge paquetes de un casillero específico y marca en una libreta (offset) dónde se quedó. Si anota después de revisar el paquete, garantiza que nunca pierde uno, aunque podría revisarlo dos veces. Si anota antes, es más rápido pero puede dejar paquetes sin revisar.

### Ejemplos Simples
*Productor en Python con `kafka-python`:*
```python
from kafka import KafkaProducer
import json

producer = KafkaProducer(
    bootstrap_servers="localhost:9092",
    acks="all",
    retries=5,
    value_serializer=lambda v: json.dumps(v).encode("utf-8"),
)

event = {"order_id": 1, "status": "created"}
producer.send("orders", key=b"order-1", value=event)
producer.flush()
```

*Consumidor con commits manuales:*
```python
from kafka import KafkaConsumer
import json

consumer = KafkaConsumer(
    "orders",
    bootstrap_servers="localhost:9092",
    enable_auto_commit=False,
    value_deserializer=lambda v: json.loads(v.decode("utf-8")),
    group_id="orders-processing",
)

for message in consumer:
    process(message.value)  # función de negocio
    consumer.commit()
```

### Casos de Uso
- Procesar órdenes de compra distribuyendo particiones por `order_id`.
- Ingestar eventos de sensores críticos con `acks=all` y retries configurados.
- Balancear consumo de logs entre múltiples instancias de un microservicio.
- Mantener pipelines de analytics donde la relectura controlada garantiza consistencia.

### Ejemplo de Implementacion
1. Diseñar claves de partición alineadas con el patrón de acceso para evitar hotspots.  
2. Configurar productores con idempotencia (`enable.idempotence=true`) y ajustes de `acks`, `retries` y `linger.ms`.  
3. Desarrollar consumidores con commits manuales o sincronizados tras completar la lógica de negocio.  
4. Ejecutar múltiples instancias por grupo y observar rebalances y lag.  
5. Implementar idempotencia en downstream (deduplicación, claves naturales) para manejar retries.  
6. Documentar estrategias de error handling (DLQ, reintentos) y monitorear lag con métricas.

### Comandos CLI o Web UI
- `kafka-consumer-groups.sh --bootstrap-server <host>:9092 --group <grupo> --describe` para revisar lag y asignaciones.
- `kafka-console-producer.sh --producer-property acks=all --topic <topic> --bootstrap-server <host>:9092` para practicar con garantías elevadas.
- `kafka-configs.sh --alter --entity-type topics --entity-name <topic> --add-config min.insync.replicas=2` para reforzar consistencia.
- `kafka-reassign-partitions.sh --bootstrap-server <host>:9092 --reassignment-json-file plan.json --execute` para balancear particiones cuando se añaden brokers.
- `kafka-delete-records.sh --bootstrap-server <host>:9092 --offset-json-file offsets.json` para gestionar offsets en escenarios de limpieza controlada.

## Notas
### Cornell
<table>
  <tr><th>Pista / Pregunta</th><th>Notas</th></tr>
  <tr><td>acks y retries</td><td>Controlan confirmaciones y reenvíos; combinados con idempotencia evitan duplicados.</td></tr>
  <tr><td>Consumer groups</td><td>Comparten carga; partición asignada a un consumidor activo dentro del grupo.</td></tr>
  <tr><td>Offsets</td><td>Se pueden confirmar automática o manualmente; definen garantías de entrega.</td></tr>
  <tr><td>Modelos de entrega</td><td>At-most (puede perder), at-least (puede duplicar), exactly-once (transacciones).</td></tr>
</table>

### Outline Method
<table>
  <tr><th>Nivel</th><th>Idea</th></tr>
  <tr><td>I</td><td>Configuración avanzada de productores</td></tr>
  <tr><td>II</td><td>Semántica de confirmaciones y particionamiento</td></tr>
  <tr><td>III</td><td>Consumidores, grupos y commits de offsets</td></tr>
  <tr><td>III</td><td>Delivery semantics y patrones de idempotencia</td></tr>
  <tr><td>II</td><td>Operaciones de mantenimiento (lag, reassignment, cleanup)</td></tr>
</table>

## Resumen
La segunda semana profundiza en cómo productores y consumidores controlan la confiabilidad del pipeline. Ajustar `acks`, `retries`, particiones y commits de offsets permite alcanzar modelos de entrega robustos. Con prácticas de idempotencia y monitoreo de lag, Kafka garantiza ingestión continua y tolerante a fallos.
