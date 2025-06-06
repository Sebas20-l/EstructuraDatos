#problema6- 27leetcode
# Solución Simple (crear nuevo arreglo y copiar) 

def removeElement_simple(nums, val):
    result = [x for x in nums if x != val] # Creamos una nueva lista con todos los elementos de nums que no son iguales a val usando comprensión de listas.

    # Copiar de vuelta los valores a nums
    for i in range(len(result)): # Recorremos cada índice en la lista filtrada result.
        nums[i] = result[i]  # Copiamos el elemento de result a la posición correspondiente en la lista original nums, sobrescribiendo los valores originales.

    return len(result) # Devolvemos la longitud de la lista result, que representa la cantidad de elementos que no son val.

# Tiempo: O(n) | Espacio: O(n)

#La función removeElement_simple recibe una lista nums y un valor val, y elimina todas las ocurrencias de val en la lista, devolviendo la nueva longitud de la lista sin esos valores.

#Cómo funciona:
#Primero, se crea una lista nueva llamada result que contiene todos los elementos de nums que no son iguales a val. Esto se logra con una comprensión de listas que filtra los valores no deseados.
#Después, para mantener la estructura original (modificar la lista nums en sitio), se copian los elementos filtrados de result de vuelta a nums uno por uno, reemplazando los valores originales.
#Finalmente, la función devuelve la longitud de la lista result, que representa la cantidad de elementos que no son val.

#Complejidad:
#Tiempo: O(n), ya que se recorre la lista original para filtrar los elementos y después para copiarlos.
#Espacio: O(n), porque se crea una lista auxiliar result que puede llegar a tener casi todos los elementos de nums.