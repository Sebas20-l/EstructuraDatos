#problema7- 28leetcode
# Solución Simple (usar slicing)

def strStr_simple(haystack: str, needle: str) -> int:
    for i in range(len(haystack) - len(needle) + 1): # Recorremos cada posible inicio donde 'needle' podría caber en 'haystack'
        if haystack[i:i+len(needle)] == needle: # Comparamos el segmento de 'haystack' con la longitud de 'needle' con 'needle'
            return i # Si coinciden, devolvemos la posición inicial donde se encontró
    return -1    # Si no se encontró ninguna coincidencia, devolvemos -1

#  Tiempo: O(n * m) en el peor caso | Espacio: O(1)


#La función strStr_simple implementa una búsqueda sencilla del primer índice en la cadena haystack donde comienza la subcadena needle. Si needle no aparece en haystack, la función devuelve -1.

#Cómo funciona:
#Se recorre la cadena haystack desde el índice 0 hasta len(haystack) - len(needle) para no exceder los límites al hacer la comparación.
#En cada iteración, se toma un segmento de haystack del mismo tamaño que needle y se compara directamente con needle.
#Si las dos cadenas coinciden, se retorna el índice actual, que es el primer lugar donde se encuentra needle.
#Si termina el ciclo sin encontrar coincidencia, se retorna -1, indicando que needle no está en haystack.

#Complejidad:
#Tiempo: En el peor caso, la comparación de subcadenas puede tomar hasta O(m) donde m es la longitud de needle. Como el ciclo puede recorrer hasta n-m+1 posiciones, la complejidad total es O(n * m).
#Espacio: O(1), porque no se usa espacio adicional significativo, solo variables para índices.