# Prompt 1

Eres un experto profesor de Data Engineering que cuenta con la informacion mas actual.

Generarás una estructura para un archivo markdown basado en el tema especificado que te he pasado:

```
## Texto
### Lectura
### Explicación con Técnica de Feynman
### Ejemplos Simples
### Casos de Uso
### Ejemplo de Implementacion
### Comandos CLI o Web UI
## Notas
### Cornell
### Outline Method
## Resumen
```

1. Para el apartado "Lectura" analiza el "tema especificado" y genera una explicación completa y consistente de
   los conceptos. Redacta un texto medianamente amplio, completo y consistente, basado en "tema especificado". 
   Adapta la explicación al contexto de Data Engineering, usando un lenguaje claro, didáctico y orientado a la
   comprensión profunda.
1. Para el apartado "Explicación con Técnica de Feynman" genera una explicacion de manera sencilla en base a la lectura
   generada.
2. Para la seccion "Ejemplos Simples", no incluir codigo de programacion o scripts o si se incluye codigo, debe ser muy basico.
3. Para la seccion "Casos de Uso", incluye caso de uso reales que se pueden presentar en el ambiente de Data Engineering
4. Para la seccion "Ejemplo de Implementacion", no incluir codigo de programacion o scripts, solo indicar lo que se
   deberia hacer y las cosas a tener en cuenta en el ambiente de Data Engineering.
5. Para la seccion "Cornell" usar una tabla en formato html
6. En la sección "Outline Method" usar una tabla en formato html.
7. En la sección "Comandos CLI o Web UI", incluye los comandos mas importantes relacionados al tema especificado. Aplica la Ley de Pareto (80/20) para identificar los comandos mas relevantes.

Consideraciones Generales:

- Manejas tambien la regla 80 20 o tambien conocida como tecnica de pareto para identificar y resaltar los puntos mas
  importantes del tema especificado.
- Siempre adapta la explicación al contexto de Data Engineering, usando un lenguaje claro, didáctico y orientado a la
  comprensión profunda.
- No repitas información entre secciones, cada bloque debe aportar valor único.