#problema8- 35leetcode
# Solución Optimizada (búsqueda binaria)

def searchInsert_optimized(nums, target):
    left, right = 0, len(nums) - 1        # Inicializamos los punteros al inicio y al final de la lista

    while left <= right:                  # Mientras el rango sea válido
        mid = (left + right) // 2         # Calculamos el índice medio para dividir la lista

        if nums[mid] == target:           # Si el elemento medio es el target, retornamos su índice
            return mid
        elif nums[mid] < target:          # Si el valor medio es menor que el target,
            left = mid + 1                # ajustamos el límite izquierdo para buscar en la mitad derecha
        else:                        # Si es mayor,
            right = mid - 1               # ajustamos el límite derecho para buscar en la mitad izquierda

    return left                       # Si no encontramos el target, left indica la posición correcta para insertarlo

# Tiempo: O(log n) | Espacio: O(1)


# Pruebas
print(searchInsert_optimized([1,3,5,6], 5))  # 2
print(searchInsert_optimized([1,3,5,6], 2))  # 1
print(searchInsert_optimized([1,3,5,6], 7))  # 4


#Esta solución utiliza búsqueda binaria para encontrar la posición de inserción de un elemento target en una lista ordenada nums, con mayor eficiencia que la búsqueda lineal.

#Funcionamiento:
#Se inicializan dos punteros: left al inicio y right al final de la lista.
#Mientras el rango entre left y right sea válido:
#Se calcula el índice medio mid.
#Si el valor en mid es igual a target, retornamos mid.
#Si el valor en mid es menor que target, se mueve left a la derecha para buscar en la mitad superior.
#Si es mayor, se mueve right a la izquierda para buscar en la mitad inferior.
#Si el bucle termina sin encontrar el target, el puntero left indicará la posición donde se debe insertar para mantener el orden.

#Complejidad:
#Tiempo: O(log n), ya que en cada iteración reduce el rango de búsqueda a la mitad.
#Espacio: O(1), porque usa variables constantes y no estructuras adicionales.