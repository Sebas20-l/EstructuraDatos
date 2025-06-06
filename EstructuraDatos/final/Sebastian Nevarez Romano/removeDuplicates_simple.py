#problema5- 26leetcode
#Solución Simple (usar lista auxiliar) — NO cumple el requisito de hacerlo "in-place"

def removeDuplicates_simple(nums):
    unique = [] # Lista auxiliar para guardar los elementos únicos
    for num in nums:
         # Recorremos el arreglo original
        if not unique or num != unique[-1]:
            unique.append(num)  # Agregamos el valor único

    # Copiamos los valores únicos de vuelta al array original
    for i in range(len(unique)):
        nums[i] = unique[i]

    return len(unique) # Retornamos la cantidad de elementos únicos

# Tiempo: O(n) | Espacio: O(n)

#Este código resuelve el problema de eliminar duplicados en un arreglo ordenado, pero NO lo hace en el lugar (in-place), ya que usa memoria adicional.

#¿Qué hace?
#Toma una lista ordenada nums y elimina los elementos duplicados, dejando sólo una aparición de cada valor. Luego, copia los elementos únicos de nuevo a nums.

#¿Cómo lo hace?
#Se crea una lista auxiliar vacía llamada unique.
#Se recorre cada elemento en nums:
#Si unique está vacía, o si el número actual num es distinto al último agregado (unique[-1]), se considera único y se agrega.
#Una vez terminada la recolección de elementos únicos, se copian uno por uno a nums, sobrescribiendo sus valores originales.
#Se retorna la cantidad de elementos únicos, que es len(unique).

#¿Por qué no es válida como solución final?
#Aunque el algoritmo funciona correctamente, viola la restricción del problema, que indica que debe realizarse la operación in-place, es decir, sin usar memoria adicional significativa. Aquí usamos una lista auxiliar que puede crecer hasta tamaño n.

#Complejidad:
#Tiempo: O(n) — se recorren todos los elementos una vez para filtrar y otra vez para copiar.
#Espacio: O(n) — por la lista auxiliar unique.