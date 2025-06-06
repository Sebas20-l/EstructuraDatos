#problema2- 14leetcode
#Solución Optimizada
# Ordenamos las palabras y comparamos solo la primera y la última.

def longestCommonPrefix_optimized(strs: list[str]) -> str:
    if not strs:
        return ""

    # Ordenamos alfabéticamente
    strs.sort()
   # Solo comparamos la primera y la última palabra
    first = strs[0]
    last = strs[-1]
    i = 0

# Recorremos letra por letra mientras coincidan
    while i < len(first) and i < len(last) and first[i] == last[i]:
        i += 1
 # Devolvemos el prefijo común
    return first[:i]

# Complejidad:
# Tiempo: O(n log n + m), por la ordenación y comparación.
# Espacio: O(1)

# Pruebas:

print(longestCommonPrefix_optimized(["flower", "flow", "flight"]))  # "fl"
print(longestCommonPrefix_optimized(["dog", "racecar", "car"]))     # ""

#La función longestCommonPrefix_optimized busca el prefijo común más largo de una lista de cadenas utilizando un método más eficiente:

#Cómo funciona:
#Primero, verifica si la lista está vacía; si es así, regresa una cadena vacía.
#Ordena alfabéticamente la lista de palabras.
#Solo compara la primera y la última palabra de la lista ordenada.
#Esto es porque la diferencia máxima entre palabras estará entre la primera y la última en orden alfabético.
#Recorre carácter por carácter ambas palabras hasta encontrar una diferencia.
#Devuelve el prefijo común que hayan compartido ambas palabras al inicio.

#Complejidad:
#Tiempo: O(n log n + m), donde n es el número de palabras (por la ordenación) y m la longitud del prefijo común (por la comparación).
#Espacio: O(1), porque solo se usan variables adicionales constantes.
#Este enfoque reduce la cantidad de comparaciones necesarias y mejora la eficiencia al evitar comparar todas las palabras entre sí.


