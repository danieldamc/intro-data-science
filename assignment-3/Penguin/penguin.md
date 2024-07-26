# Tarea3

## Contexto

El dataset de pingüinos, conocido como "Penguin Dataset: The New Iris", proporciona datos sobre tres especies de pingüinos (Adelie, Chinstrap, y Gentoo) recolectados en las islas Palmer de la Antártida. Este dataset es utilizado como alternativa al famoso dataset Iris para la enseñanza de técnicas de clasificación, aunque en este caso se utilizará en el ámbito de aprendizaje no supervisado

## Variables

1. ***Species (Especie)***: Especie del pingüino (Adelie, Chinstrap, Gentoo).
2. ***Island (Isla)***: Isla donde se recolectaron los datos (Biscoe, Dream, Torgersen). 

3. ***Culmen Length (Longitud del Pico)***: Longitud del pico en milímetros.

4. ***Culmen Depth (Profundidad del Pico)***: Profundidad del pico en milímetros. 

5. ***Flipper Length (Longitud de Aletas)***: Longitud de las aletas en milímetros.

6. ***Body Mass (Masa Corporal)***: Masa corporal en gramos.

7. ***Sex (Sexo)***: Sexo del pingüino.

8. ***Year (Año)***: Año en el que se recolectaron los datos.

## KNN DBSCAN GAUSSIAN MIXTURE

1. Cargar y verificar integridad de los datos. Realizar curación si corresponde.

2. Crear un scatter_matrix de las variables numéricas reales y con parámetro color igual a la columna species. TIP: Este va a ser la mejor forma de comparar visualmente los modelos entrenados.

3. Estandarizar datos

4. Probar modelo Gaussian Mixture con el numero de clústeres igual a la cantidad de especies de pingüinos. Comparar el accuracy de los resultados, interpretando visualmente a que especie corresponde cada clúster. Para lo anterior, se debe realizar un scatter matrix con el parámetro color igual a los clúster. Imprimir la métrica Sillohuete y matriz de confusión correspondiente. Comente acerca de los resultados.

5. Entrenar un modelo KNN,

    1. Separe train y test con el numero de especies estratificado (prefiera usar el parámetro stratify de train_test_split en vez de hacerlo a mano).
    
    2. Realice una búsqueda del mejor n_neighbors en base a la métrica Sillohuete, en un rango de 1 a 30 y grafique los resultados. Si los valores convergen utilice el primer resultado mas alto.

    3. Entrene el modelo con el mejor n_neighbors obtenido. Imprima el mejor valor n_neighbors, métrica Sillohuette de los resultados y accuracy del conjunto de test.

    4. Finalmente encuentre la distancia promedio de los n_neighbors y guardela en una variable llamada 'epsilon'. Esta se usará para ajustar el DBSCAN

6. Entrene un modelo de DBSCAN con el hiperparámetro eps igual a la variable 'epsilon' anteriormente obtenida, ahora basándose en la métrica Sillohuette, pruebe valores de min_samples de 1 a 15 y grafique. Entrene el modelo con el mejor valor y realice un scatter matrix con el parámetro color igual a los clúster. Comente sus Resultados