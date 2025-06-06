#problema3- leetcode20
# Solución Simple
# Usamos una pila (stack) para apilar los paréntesis que abrimos
# y los vamos cerrando en el orden correcto.

def isValid_simple(s: str) -> bool:
    stack = [] # Usamos una pila para almacenar los paréntesis de apertura
    mapping = {')': '(', '}': '{', ']': '['} # Mapeo de cierre → apertura

    for char in s:
        if char in mapping.values():  # si es un paréntesis de apertura
            stack.append(char)
        elif char in mapping:  # si es de cierre
            if not stack or stack[-1] != mapping[char]:
                return False
            stack.pop() # Si hace match, eliminamos el paréntesis abierto
        else:
            return False  # si hay un carácter inválido

    return len(stack) == 0 # Si la pila está vacía, está balanceado

# Pruebas:
print(isValid_simple("()[]{}"))  # True
print(isValid_simple("(]"))      # False

# Complejidad:
# Tiempo: O(n) | Espacio: O(n)  (por la pila)

#La función isValid_simple verifica si una cadena de paréntesis está correctamente balanceada usando una pila (stack):
#Se utiliza una pila para almacenar los paréntesis de apertura que se encuentran mientras recorremos la cadena.
#Se define un diccionario mapping que relaciona cada paréntesis de cierre con su correspondiente paréntesis de apertura.

#Para cada carácter en la cadena:
#Si es un paréntesis de apertura ((, {, [), se agrega a la pila.
#Si es un paréntesis de cierre (), }, ]), se verifica si la pila está vacía o si el último paréntesis agregado a la pila no corresponde al paréntesis de apertura esperado. Si alguno de estos casos ocurre, la cadena no está balanceada y se retorna False.
#Si el paréntesis de cierre hace "match" con el último paréntesis de apertura, se elimina el último elemento de la pila.
#Si hay cualquier carácter que no es un paréntesis válido, se retorna False.
#Al finalizar el recorrido, si la pila está vacía, significa que todos los paréntesis de apertura fueron correctamente cerrados en orden, por lo que la cadena es válida y se retorna True. Si la pila no está vacía, la cadena está desequilibrada y se retorna False.

#Complejidad:
#Tiempo: O(n), donde n es la longitud de la cadena, porque cada carácter se procesa una vez.
#Espacio: O(n), debido al uso de la pila que en el peor caso puede almacenar todos los paréntesis de apertura.