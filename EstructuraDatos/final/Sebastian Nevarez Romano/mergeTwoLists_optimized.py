#problema4- 21leetcode
# Definimos la estructura de nodo para usar en el entorno local
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
#Solución Optimizada (reutilizar nodos existentes)

def mergeTwoLists_optimized(list1, list2):
    dummy = ListNode(-1) # Nodo ficticio para iniciar la lista resultado
    current = dummy # Puntero que se usará para construir la lista

   # Mientras ambas listas tengan nodos
    while list1 and list2:
        if list1.val < list2.val:
            current.next = list1 # Apuntamos al nodo actual de list1
            list1 = list1.next  # Avanzamos en list1
        else:
            current.next = list2 # Apuntamos al nodo actual de list2
            list2 = list2.next # Avanzamos en list2
        current = current.next # Avanzamos en la lista resultado

# Cuando una lista se acaba, apuntamos al resto de la otra
    current.next = list1 if list1 else list2
    return dummy.next

# Tiempo: O(n + m) | Espacio: O(1) (se reutilizan nodos)


# Función de ayuda para imprimir listas en pruebas
def print_list(head):
    res = []
    while head:
        res.append(head.val)
        head = head.next
    print(res)

# Pruebas básicas
l1 = ListNode(1, ListNode(2, ListNode(4)))
l2 = ListNode(1, ListNode(3, ListNode(4)))

merged = mergeTwoLists_optimized(l1, l2)
print_list(merged)  # [1, 1, 2, 3, 4, 4]

#Esta solución resuelve el problema de fusionar dos listas enlazadas ordenadas reutilizando los mismos nodos de las listas de entrada, sin crear nodos nuevos, lo que permite optimizar el uso de memoria.

#¿Qué hace?
#Fusiona list1 y list2 en una única lista ordenada usando los nodos originales, lo que permite que la solución use espacio constante (O(1)).

#¿Cómo lo hace?
#Se crea un nodo ficticio (dummy) que funciona como punto de partida para la lista resultado. Este nodo facilita la construcción sin preocuparse por el primer elemento.
#Se usa un puntero current para construir la lista final.
#Mientras ambas listas tengan elementos:
#Compara los valores actuales de list1 y list2.
#Apunta current.next directamente al nodo más pequeño, en lugar de crear uno nuevo.
#Avanza en la lista de la cual tomó el nodo.
#También avanza current para seguir construyendo la lista.
#Al finalizar el bucle, una lista puede seguir teniendo nodos (la otra ya se agotó). Como están ordenados, se puede conectar el resto directamente (current.next = list1 if list1 else list2).
#Se retorna dummy.next, que es el inicio real de la lista combinada (ignorando el nodo ficticio).