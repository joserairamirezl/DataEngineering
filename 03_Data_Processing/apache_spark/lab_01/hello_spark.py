from pyspark.sql import SparkSession

# 1. Crear la sesión Spark
spark = SparkSession.builder \
    .appName("HolaMundoSpark") \
    .getOrCreate()

# 2. Crear un DataFrame simple
datos = [("José", 30), ("María", 25), ("Raúl", 40)]
df = spark.createDataFrame(datos, ["nombre", "edad"])

# 3. Mostrar resultados
print("✅ Hola mundo desde PySpark")
df.show()

# Mantener el contexto vivo 30 segundos para ver la UI
print("Abre tu navegador en http://localhost:4040 (Spark UI)")
sleep(30)


# 4. Finalizar sesión
spark.stop()
