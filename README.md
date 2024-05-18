# Codificacion
Codificación de Algoritmos con Arreglos en PYTHON

## BUSQUEDA

Este proyecto aborda la gestión de una lista de trabajadores, cada uno con su nombre, trabajo y sueldo. Se ha desarrollado un programa en Python que permite al usuario interactuar con esta lista de trabajadores para encontrar el trabajador con el sueldo más alto o el sueldo más bajo.

## Problemas Abordados

1. **Gestión de Información de Trabajadores:** Almacenar y organizar información de trabajadores en una estructura de datos adecuada.
2. **Interacción con el Usuario:** Permitir al usuario realizar consultas específicas sobre los sueldos de los trabajadores.
3. **Búsqueda de Sueldo Más Alto/Bajo:** Implementar algoritmos que encuentren y muestren el trabajador con el sueldo más alto y el trabajador con el sueldo más bajo.

## Algoritmos Implementados

1. **Búsqueda del Sueldo Más Bajo:**
    - Se utiliza la función `min()` para encontrar el sueldo más bajo en la lista de trabajadores.
    - Luego, se filtra la lista para encontrar todos los trabajadores con ese sueldo.

2. **Búsqueda del Sueldo Más Alto:**
    - Se utiliza la función `max()` para encontrar el sueldo más alto en la lista de trabajadores.
    - Luego, se filtra la lista para encontrar todos los trabajadores con ese sueldo.

## Instrucciones para Ejecutar el Código

1. **Pasos para Ejecutar el Programa:**
    - Guarde el código en un archivo llamado `trabajadores.py`.
    - Abra una terminal o línea de comandos.
    - Ejecute el programa con el comando:
      ```bash
      python trabajadores.py
      ```
/
2. **Interacción con el Programa:**
    - Al ejecutar el programa, se le mostrará un menú con dos opciones:
      ```
      Hola, ¿qué quieres hacer?
      1. Ver el sueldo más bajo
      2. Ver el sueldo más alto
      Elige una opción (1 o 2):
      ```
    - Introduzca `1` para ver el trabajador con el sueldo más bajo o `2` para ver el trabajador con el sueldo más alto.

## ORDENAR

Este proyecto aborda la gestión y ordenación de una lista de trabajadores, cada uno con su nombre, trabajo y sueldo. Se ha desarrollado un programa en Python que permite al usuario ordenar esta lista de trabajadores ya sea por nombre o por sueldo.

## Problemas Abordados

1. **Gestión de Información de Trabajadores:** Almacenar y organizar información de trabajadores en una estructura de datos adecuada.
2. **Interacción con el Usuario:** Permitir al usuario elegir cómo quiere ordenar la lista de trabajadores.
3. **Algoritmo de Ordenación:** Implementar un algoritmo de ordenación (selección) para ordenar la lista de trabajadores por una clave específica (nombre o sueldo).

## Algoritmos Implementados

1. **Algoritmo de Ordenación por Selección:**
    - Se utiliza un algoritmo de selección para ordenar la lista de trabajadores.
    - El algoritmo encuentra el elemento mínimo en el resto de la lista y lo intercambia con el primer elemento no ordenado.

## Instrucciones para Ejecutar el Código

2. **Pasos para Ejecutar el Programa:**
    - Guarde el código en un archivo llamado `ordenar_trabajadores.py`.
    - Navegue hasta el directorio donde guardó el archivo `ordenar_trabajadores.py`.
    - Ejecute el programa con el comando:
      ```bash
      python ordenar_trabajadores.py
      ```

3. **Interacción con el Programa:**
    - Al ejecutar el programa, se le mostrará un menú con dos opciones:
      ```
      Hola, ¿qué quieres hacer?
      1. Ordenar por nombre
      2. Ordenar por sueldo
      Elige 1 o 2:
      ```
    - Introduzca `1` para ordenar la lista de trabajadores por nombre o `2` para ordenar la lista por sueldo.
    - El programa mostrará la lista de trabajadores ordenada según la opción elegida.
