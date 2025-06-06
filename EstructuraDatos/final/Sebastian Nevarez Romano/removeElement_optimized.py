#problema6- 27leetcode
#Solución Optimizada (in-place con puntero)

def removeElement_optimized(nums, val):
    k = 0  # índice donde vamos a colocar el siguiente valor que no sea `val`

    for i in range(len(nums)): # recorremos todos los índices de nums
        if nums[i] != val: # si el valor actual no es `val
            nums[k] = nums[i] # copiamos el valor a la posición k
            k += 1 # incrementamos k para la siguiente posición válida

    return k # retornamos la cantidad de valores distintos a val la nueva longitud

#Tiempo: O(n) | Espacio: O(1)


# Pruebas
nums1 = [3,2,2,3]
k1 = removeElement_optimized(nums1, 3)
print(k1, nums1[:k1])  # 2 [2,2]

nums2 = [0,1,2,2,3,0,4,2]
k2 = removeElement_optimized(nums2, 2)
print(k2, nums2[:k2])  # 5 [0,1,3,0,4]



#La función removeElement_optimized elimina todas las ocurrencias de un valor val de la lista nums modificándola directamente sin usar memoria extra, devolviendo la nueva longitud de la lista sin esos valores.

#Cómo funciona:
#Se utiliza un índice k que apunta a la posición donde se colocará el siguiente elemento que no sea igual a val.
#Se recorre la lista con otro índice i y cada vez que se encuentra un elemento diferente de val, se copia ese elemento a la posición k y se incrementa k.
#Al final, k indica la cantidad de elementos distintos de val y todos esos elementos quedan al inicio de la lista.

#Complejidad:
#Tiempo: O(n) → Se recorre el arreglo una sola vez.
#Espacio: O(1) → Se modifican los valores en el mismo arreglo, sin usar memoria adicional.