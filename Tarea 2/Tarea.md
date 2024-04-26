# Tarea 2

## Clasificación

### Información

Todos los datos provienen de una medición continua de EEG con el Emotiv EEG Neuroheadset. La duración de la medición fue de 117 segundos. El estado del ojo fue detectado a través de una cámara durante la medición de EEG y luego agregado manualmente al archivo después de analizar los fotogramas del video. '1' indica el estado de ojos cerrados y '0' el estado de ojos abiertos. Todos los valores están en orden cronológico con el primer valor medido en la parte superior de los datos.

Las características corresponden a 14 mediciones de EEG del auricular, originalmente etiquetadas como AF3, F7, F3, FC5, T7, P, O1, O2, P8, T8, FC6, F4, F8, AF4, en ese orden.

***NO OLVIDAR***

0 -> OJO ABIERTO 1 -> OJO CERRADO

### Enunciado

Para efectos de esta Tarea, usar el dataset EEG_eyes_classification.csv , del cual no se investigará a que corresponde cada variable por lo que están renombradas, además note que la columna 'Class' se encuentra mal etiquetada, el valor b'1' corresponde al 0 y el valor b'2' corresponde a 1. Cualquier otro valor atípico que encuentre, manéjelo como encuentre necesario.Cargar Datos y realizar limpieza de estos: manejar valores nulos, identificar el tipo de cada uno de las columnas y corregir lo que se encuentre mal en caso de ser necesario. HINT: Calcular el porcentaje de valores por columna puede ser de gran ayuda para tomar decisiones, no tenga miedo a eliminar lo que no sirve, en cuanto mantenga la integridad del dataset.

1. **Cargar Datos y realizar limpieza de estos:** manejar valores nulos, identificar el tipo de cada uno de las columnas y corregir lo que se encuentre mal en caso de ser necesario. HINT: Calcular el porcentaje de valores por columna puede ser de gran ayuda para tomar decisiones, no tenga miedo a eliminar lo que no sirve, en cuanto mantenga la integridad del dataset.

2. ***Balanceo de datos:*** Se debe dejar ambas clases con el mismo numero de ocurrencias de cada una de las clases en el dataset. HINT: la creación de nuevos datos a partir de métricas o probabilidades puede ser peligrosa si no se conoce el origen de los datos.

3. ***Estandarización de datos:*** Realizar la estandarización de datos correspondiente para que los datos tengan la misma escala.

4. ***Separación de datos:*** Realizar la separación del dataset en 3 partes: 60% Train, 20% Test y 20% Validation, manteniendo la proporción de clases en cada uno de estas separaciones. ***HINT***: Ciertas bibliotecas tienen parámetros para dejar la separación balanceada y además puede elegir en que proporción dejara separa el dataset.

5. ***Entrenamiento:*** Se deben entrenar 3 modelos de clasificación, Random Forest, Desicion Tree y regresión logística, en primer lugar con los hiperparámetros default y luego realizando una optimización de hiperparámetros, ya se a mano o con alguna biblioteca. En cada entrenamiento utilizar metricas correspondientes para ***Hint***: Si quiere ocupar una biblioteca se recomienda utilizar RandomizedSearchCV, GridSearchCV u Optuna siendo esta ultima la mas completa, pero también mas compleja (Puntos extra <https://optuna.org/>).

6. Elija un modelo y explique por qué encuentra que es el mejor de los tres en base a los resultados obtenidos. Además muestre cuales fueron las características (variables) mas importantes según dicho modelo, al momento de hacer su predicción.

7. Realice un grafico de los datos predichos por su modelo óptimo vs datos reales

## Regresión

### Información

El Conjunto de Datos de Desempeño Estudiantil es un conjunto de datos diseñado para examinar los factores que influyen en el desempeño académico de los estudiantes. El conjunto de datos consta de 10,000 registros estudiantiles, donde cada registro contiene información sobre varios predictores y un índice de desempeño.

El conjunto de datos Student_Performance.csv tiene como objetivo proporcionar información sobre la relación entre las variables predictoras y el índice de desempeño. Los investigadores y analistas de datos pueden utilizar este conjunto de datos para explorar el impacto de las horas de estudio, los puntajes anteriores, las actividades extracurriculares, las horas de sueño y las preguntas de muestra en el desempeño estudiantil.

### Variables

1. ***Hours Studied:*** El número total de horas dedicadas al estudio por cada estudiante.

2. ***Previous Scores:*** Los puntajes obtenidos por los estudiantes en exámenes previos.

3. ***Extracurricular Activities:*** Si el estudiante participa en actividades extracurriculares (Sí o No).

4. ***Sleep Hours:*** El número promedio de horas de sueño que el estudiante tuvo por día

5. ***Sample Question Papers Practiced:*** El número de preguntas de muestra que el estudiante practicó.

### Variable Objetivo

***Performance Index:*** Una medida del desempeño general de cada estudiante. El índice de desempeño representa el desempeño académico del estudiante y ha sido redondeado al entero más cercano. El índice varía de 10 a 100, siendo valores más altos indicativos de un mejor desempeño.

1. Cargar y revisar integridad de dataset

2. Realizar graficos en plotly express de correlacion del dataset completo y un scater para cada una de las dimensiones. A partir de lo graficado sacar 3 conclusiones que a su parecer son importantes o llamativas en relación.

3. Realizar la estandarización de datos correspondiente para que los datos tengan la misma escala.

4. Realizar la separación del dataset en 3 partes: 60% Train, 20% Test y 20% Validation HINT: Ciertas bibliotecas no tienen la separación en 3 conjuntos directamente pero podrías utilizar múltiples veces una que separe en 2 conjuntos preservando las proporciones dadas. TIP: El fin de la data de validacion es que prueben los distintos hiperparámetros, para que el modelo no tenga un overfitting al probar la data de test.

5. Entrenar 3 modelos de regresion; Linear Regression, Random Forest Regressor y decision tree regressor, evaluar con metricas correspondientes. Luego optimizar los hiperparamétros de cada uno y volver a evaluar.

6. Escoger el mejor modelo con sus mejores hiperparamétros en base a los resultados y su criterio. Muestre cuales fueron las características (variables) mas importantes según dicho modelo, al momento de hacer su predicción.

7. Realice un grafico de los datos predichos por su modelo óptimo vs datos reales dando una breve explicación a lo que ve

