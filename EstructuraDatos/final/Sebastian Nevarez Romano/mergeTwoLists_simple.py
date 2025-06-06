#problema4- 21leetcode
# Definimos la estructura de nodo para usar en el entorno local
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Solución Simple (crear nueva lista uniendo nodos nuevos)

def mergeTwoLists_simple(list1, list2):
    dummy = ListNode(-1) # Nodo ficticio para empezar la nueva lista
    current = dummy # Puntero para agregar nodos a la nueva lista

 # Mientras ambas listas tengan nodos
    while list1 and list2:
        if list1.val < list2.val:
            current.next = ListNode(list1.val) # Agregamos nuevo nodo con valor de list1
            list1 = list1.next # Avanzamos en list1
        else:
            current.next = ListNode(list2.val) # Agregamos nuevo nodo con valor de list2
            list2 = list2.next   # Avanzamos en list2
        current = current.next # Avanzamos en la nueva lista

    # Añadir lo que quede de una lista
    while list1:
        current.next = ListNode(list1.val)
        list1 = list1.next
        current = current.next
    while list2:
        current.next = ListNode(list2.val)
        list2 = list2.next
        current = current.next

    return dummy.next # Retornamos la lista sin el nodo ficticio

#tiempo: O(n + m) | Espacio: O(n + m)  (por nodos nuevos)

#Este algoritmo resuelve el problema de fusionar dos listas enlazadas ordenadas en una nueva lista también ordenada.
#Se implementa una solución simple que crea una nueva lista enlazada desde cero, copiando los valores de los nodos de las listas originales (list1 y list2), sin reutilizar sus nodos. Esto es útil cuando no se desea modificar las listas de entrada.

#¿Cómo funciona?
#Se crea un nodo ficticio (dummy) que servirá como punto de inicio para construir la nueva lista. Este nodo es útil porque evita condiciones especiales para el primer nodo real.
#Se utiliza un puntero current para ir construyendo la lista resultante.
#Se recorre simultáneamente list1 y list2:
#Se compara el valor actual de cada lista.
#Se crea un nuevo nodo con el menor valor y se añade a la lista resultante.
#Se avanza en la lista de la cual se extrajo el valor.
#Cuando una de las listas se termina, se copian todos los nodos restantes de la otra lista.
#Finalmente, se retorna dummy.next, que es el inicio real de la lista fusionada (ignorando el nodo ficticio).

#Ejemplo:
#Si list1 = 1 -> 3 -> 5 y list2 = 2 -> 4 -> 6, la función crea una nueva lista: 1 -> 2 -> 3 -> 4 -> 5 -> 6.

#Complejidad:
#Tiempo: O(n + m), donde n y m son las longitudes de las dos listas. Se recorre cada nodo una sola vez.
#Espacio: O(n + m), ya que se crean nuevos nodos para cada elemento de ambas listas.

