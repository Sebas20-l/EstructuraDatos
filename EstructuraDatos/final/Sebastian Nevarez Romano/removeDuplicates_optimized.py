#problema5- 26leetcode
#Solución Optimizada (dos punteros, todo en el mismo array)

def removeDuplicates_optimized(nums):
    if not nums:
        return 0 # Si la lista está vacía, no hay duplicados

    i = 0  # apunta al último valor único

 # Recorremos desde el segundo elemento hasta el final
    for j in range(1, len(nums)):
        # Si encontramos un valor diferente al que está en i
        if nums[j] != nums[i]:
            i += 1 # Movemos el puntero i
            nums[i] = nums[j]  # sobreescribimos con el nuevo valor único

    return i + 1 # Retornamos la cantidad de valores únicos

#Tiempo: O(n) | Espacio: O(1)

# Pruebas
nums1 = [1, 1, 2]
k1 = removeDuplicates_optimized(nums1)
print(k1, nums1[:k1])  # 2 [1, 2]

nums2 = [0,0,1,1,1,2,2,3,3,4]
k2 = removeDuplicates_optimized(nums2)
print(k2, nums2[:k2])  # 5 [0,1,2,3,4]

#La función removeDuplicates_optimized elimina duplicados de una lista ordenada en el lugar, usando un método de dos punteros para lograr eficiencia en tiempo y espacio:
#Primero, verifica si la lista está vacía; si es así, retorna 0 porque no hay elementos ni duplicados.

#Utiliza dos punteros:
#i apunta al índice del último elemento único encontrado.
#j recorre el arreglo desde el segundo elemento hacia adelante.
#Para cada elemento en la posición j:
#Compara el valor actual nums[j] con el valor en nums[i].
#Si son diferentes, significa que se encontró un nuevo valor único.
#Incrementa i para avanzar al siguiente índice donde se almacenará el valor único.
#Sobrescribe nums[i] con nums[j] para actualizar la lista con el nuevo valor.
#Al final, retorna i + 1 que representa la cantidad total de valores únicos en el arreglo modificado.

#Complejidad:
#Tiempo: O(n), ya que recorre el arreglo una sola vez.
#Espacio: O(1), porque modifica el arreglo en sitio y solo usa variables auxiliares constantes.

#Esta técnica es eficiente y no requiere espacio extra, ideal para trabajar con arreglos ordenados donde queremos eliminar duplicados sin usar estructuras adicionales.