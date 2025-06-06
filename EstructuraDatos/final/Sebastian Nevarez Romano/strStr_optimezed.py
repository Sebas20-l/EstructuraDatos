#problema7- 28leetcode
# Solución Optimizada (algoritmo de Knuth-Morris-Pratt - KMP)

def build_kmp_table(needle):
    lps = [0] * len(needle)   # Inicializamos la lista lps Longest Prefix Suffix con ceros
    length = 0                 # Longitud del prefijo más largo que es también sufijo
    i = 1                       # Empezamos desde el segundo carácter índice 1
    while i < len(needle): # Recorremos el patrón completo
        if needle[i] == needle[length]: # Si el carácter actual coincide con el carácter en la posición 'length'
            length += 1                  # Incrementamos la longitud del prefijo-sufijo
            lps[i] = length              # Guardamos este valor en lps para la posición actual
            i += 1                       # Avanzamos al siguiente carácter
        else:
            if length > 0:               # Si no coincide y length es mayor a cero,
                length = lps[length-1]   # retrocedemos al valor anterior guardado en lps para intentar encontrar otro prefijo
            else:
                lps[i] = 0               # Si length es cero, no hay prefijo-sufijo para este índice
                i += 1                    # Avanzamos
    return lps                            # Devolvemos la tabla lps construida

def strStr_optimized(haystack: str, needle: str) -> int:
    if not needle:                # Caso especial: si needle es cadena vacía
        return 0                   # El índice es 0 por definición

    lps = build_kmp_table(needle)      # Construimos la tabla lps para needle
    i = j = 0                         # i recorre haystack, j recorre needle

    while i < len(haystack):                  # Recorremos toda la cadena principal
        if haystack[i] == needle[j]:           # Si los caracteres coinciden
            i += 1                             # Avanzamos ambos punteros
            j += 1
            if j == len(needle):               # Si j llega al final del patrón
                return i - j                   # Retornamos la posición donde comenzó la coincidencia
        else:
            if j > 0:                      # Si hay un fallo y j > 0
                j = lps[j - 1]              # Ajustamos j a la posición indicada en lps para no reiniciar completamente
            else:
                i += 1                      # Si j == 0, avanzamos i para seguir buscando
    return -1                                 # No se encontró el patrón en la cadena

#Tiempo: O(n + m) | Espacio: O(m)


# Pruebas
print(strStr_optimized("hello", "ll"))        # 2
print(strStr_optimized("leetcode", "leeto"))  # -1

#Esta solución implementa el algoritmo Knuth-Morris-Pratt KMP para encontrar el índice de la primera aparición de una subcadena needle dentro de otra cadena más grande haystack. A diferencia de la búsqueda simple, KMP mejora la eficiencia evitando retroceder el índice de la cadena principal cuando ocurre un fallo.

#Cómo funciona:
#Construcción de la tabla LPS Longest Prefix Suffix: La función build_kmp_table calcula para cada posición del patrón el tamaño del prefijo más largo que también es sufijo. Esto permite saber dónde reiniciar la comparación en caso de fallo sin retroceder en la cadena principal.
#Búsqueda del patrón en la cadena: La función strStr_optimized recorre la cadena haystack y el patrón needle simultáneamente. Cuando encuentra un fallo en la comparación, usa la tabla LPS para mover el puntero del patrón a una posición previa donde pueda continuar la búsqueda, sin retroceder en haystack.

#Complejidad:
#Tiempo: O(n + m), siendo n la longitud de haystack y m la longitud de needle. Esto es más eficiente que la solución simple porque evita comparar caracteres repetidos innecesariamente.
#Espacio: O(m) debido al almacenamiento de la tabla LPS.