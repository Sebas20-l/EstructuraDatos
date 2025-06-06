#problema8- 35leetcode
# Solución Simple (búsqueda lineal)

def searchInsert_simple(nums, target):
    for i in range(len(nums)):        # Recorremos la lista nums desde el índice 0 hasta el final
        if nums[i] >= target:          # Si encontramos un número mayor o igual al target,
            return i                   # retornamos ese índice como la posición donde se debe insertar o ya existe
    return len(nums)                   # Si no encontramos ningún número mayor o igual, el target va al final

# Tiempo: O(n) | Espacio: O(1)


#Este algoritmo busca la posición donde se debe insertar un número target en una lista ordenada nums para mantener el orden ascendente.

#Cómo funciona:
#Recorre la lista desde el principio y compara cada elemento con el target.
#Cuando encuentra el primer número que es igual o mayor que el target, devuelve ese índice, porque ahí es donde debería insertarse el target.
#Si ninguno cumple esta condición, significa que el target es mayor que todos los números en la lista, así que se debe insertar al final. Por eso retorna la longitud de la lista.

#Complejidad:
#Tiempo: O(n) en el peor caso, ya que puede recorrer toda la lista.
#Espacio: O(1) porque no usa espacio extra, solo variables temporales.