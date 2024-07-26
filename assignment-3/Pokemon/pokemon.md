# Tarea3

## Contexto

Los juegos de Pokémon son una serie de videojuegos desarrollados por Game Freak y publicados por Nintendo y The Pokémon Company. 

En estos juegos, los jugadores asumen el rol de entrenadores cuyo objetivo es capturar y entrenar criaturas llamadas "pokémon" para competir en batallas contra otros entrenadores y líderes de gimnasio. Los juegos se centran en la exploración, el combate estratégico y la recolección. Estos son los atributos básicos que se utilizan para calcular cuánto daño hará un ataque en los juegos. Este dataset trata sobre los juegos de Pokémon (NO sobre las cartas de Pokémon ni Pokémon Go).

## Variables

1. ***\# (Número)***: Identificación única en la Pokédex.

2. ***Name (Nombre)***: Nombre del pokémon.

3. ***Type 1 (Tipo 1)***: Tipo principal, determina fortalezas y debilidades.

4. ***Type 2 (Tipo 2)***: Tipo secundario, si lo tiene.

5. ***Total***: Suma de todas las estadísticas base.

6. ***HP***: Puntos de salud, vitalidad en batalla.

7. ***Attack (Ataque)***: Fuerza en ataques físicos.

8. ***Defense (Defensa)***: Resistencia a ataques físicos.

9. ***Sp. Atk (Ataque Especial)***: Fuerza en ataques especiales.

10. ***Sp. Def (Defensa Especial)***: Resistencia a ataques especiales.

11. ***Speed (Velocidad)***: Determina el orden de ataque en batalla.

12. ***Generation (Generación)***: Juego en el que debutó.

13. ***Legendary (Legendario)***: Indica si es legendario, afectando su rareza y habilidades únicas.

## KMEANS - KMEDIANS - KMEDOIDS

1. Cargar y verificar integridad de los datos. Realizar curación si corresponde.

2. Graficar matriz de correlación y realizar un scatter_matrix con plotly.

3. Seleccionar los valores del dataset que son de utilidad para entrenar cada modelo.

4. Entrenar un modelo de KMEANS - KMEDIANS - KMEDOIDS y para cada uno de ellos:

    1. Mediante el método del codo, determinar el número de clústeres óptimo, explicar por que lo eligieron, con el gráfico correspondiente.

    2. Luego de determinar el número, entrenar con dicho número y realizar un grafico de radar para cada clúster que muestre todas las variables que utilizó para entrenar utilizando los centroides de cada algoritmo como valor representativo de cada clúster.

    3. Realizar un grafico scatter_matrix con plotly usando como parámetro color la variable clústeres.

    4. Tomar dos variables que prefieran (pero las mismas para comparar los 3 modelos) y graficar con una X el punto del centroide, medoide y median, según corresponda.

5. Sacar conclusiones al respecto:

    1. ¿Qué diferencias existen entre los diferentes clústeres que crearon los modelos?.
    
    2. ¿Tienen sentido las agrupaciones que hizo cada algoritmo? ***HINT***: Recuerde que siempre en los videojuegos siempre hay personajes que aguantan harto y atacan poco, otros que atacan mucho pero resisten poco, etc.

    3. Basándose en la métrica Silhouette y en los resultados visuales obtenidos, ¿Qué modelo realizó mejor el agrupamiento en clústeres?