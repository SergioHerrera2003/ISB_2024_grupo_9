# Introducción a la Matriz de Confusión

## ¿Qué es una Matriz de Confusión?

Una matriz de confusión es una herramienta fundamental en el campo del aprendizaje automático y la estadística. Se utiliza principalmente para evaluar el rendimiento de un modelo de clasificación. Esta matriz presenta de manera tabular la comparación entre los valores reales y los valores predichos por el modelo, permitiendo así un análisis detallado de sus errores.

## Estructura de la Matriz de Confusión

La matriz de confusión es una tabla cuadrada que tiene el siguiente formato en el caso de un problema de clasificación binaria:

|                | Predicción Positiva | Predicción Negativa |
|----------------|---------------------|---------------------|
| **Real Positivo** | Verdaderos Positivos (TP) | Falsos Negativos (FN) |
| **Real Negativo** | Falsos Positivos (FP)     | Verdaderos Negativos (TN) |

- **Verdaderos Positivos (TP)**: Número de ejemplos positivos correctamente clasificados como positivos.
- **Falsos Negativos (FN)**: Número de ejemplos positivos incorrectamente clasificados como negativos.
- **Falsos Positivos (FP)**: Número de ejemplos negativos incorrectamente clasificados como positivos.
- **Verdaderos Negativos (TN)**: Número de ejemplos negativos correctamente clasificados como negativos.

## Métricas Derivadas de la Matriz de Confusión

A partir de la matriz de confusión, se pueden calcular varias métricas de rendimiento importantes, tales como:

1. **Exactitud (Accuracy)**:
   \[
   \text{Exactitud} = \frac{TP + TN}{TP + TN + FP + FN}
   \]

2. **Precisión (Precision)**:
   \[
   \text{Precisión} = \frac{TP}{TP + FP}
   \]

3. **Sensibilidad (Recall) o Tasa de Verdaderos Positivos**:
   \[
   \text{Sensibilidad} = \frac{TP}{TP + FN}
   \]

4. **Especificidad (Specificity) o Tasa de Verdaderos Negativos**:
   \[
   \text{Especificidad} = \frac{TN}{TN + FP}
   \]

5. **F1 Score**:
   \[
   F1 = 2 \cdot \frac{\text{Precisión} \cdot \text{Sensibilidad}}{\text{Precisión} + \text{Sensibilidad}}
   \]

## Importancia de la Matriz de Confusión

La matriz de confusión no solo ayuda a entender cuántos errores está cometiendo un modelo, sino también el tipo de errores. Esto es crucial en muchos campos, como en la detección de enfermedades, donde el costo de un falso negativo puede ser significativamente diferente del costo de un falso positivo.

## Ejemplo

Supongamos que tenemos un modelo que predice si un correo electrónico es spam o no. Después de probar nuestro modelo, obtenemos la siguiente matriz de confusión:

|                | Predicción Spam | Predicción No Spam |
|----------------|-----------------|--------------------|
| **Spam Real**      | 50              | 10                 |
| **No Spam Real**   | 5               | 100                |

- TP = 50 (correos spam correctamente identificados)
- FN = 10 (correos spam no identificados)
- FP = 5 (correos no spam identificados como spam)
- TN = 100 (correos no spam correctamente identificados)

A partir de estos valores, podemos calcular las métricas mencionadas anteriormente para evaluar el rendimiento de nuestro modelo.

## Conclusión

La matriz de confusión es una herramienta poderosa para el análisis de modelos de clasificación. Nos permite ver no solo cuántos errores comete el modelo, sino también el tipo de errores, lo cual es esencial para muchas aplicaciones prácticas.

# Matrices creadas en el Laboratorio

[Matriz de Confusión de Sergio Herrera](../Matriz%20de%20Confusión/SergioHerreraMatrizConfusion.docx)