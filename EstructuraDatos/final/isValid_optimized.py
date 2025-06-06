#problema3- 20leetcode
#Solución Optimizada (igual de eficiente, pero más limpia)

def isValid_optimized(s: str) -> bool:
    stack = [] # Creamos una pila vacía para guardar los paréntesis abiertos
    pair = {'(': ')', '{': '}', '[': ']'} # Diccionario con los pares válidos

    for char in s:
        if char in pair:
            stack.append(pair[char])  # guardamos lo que esperaríamos cerrar
        elif not stack or stack.pop() != char:
             # Si no hay nada en la pila o el cierre no coincide con lo esperado
            return False

    return not stack  # debe estar vacío al final

# Complejidad:
# Tiempo: O(n) | Espacio: O(n)

# Pruebas:
print(isValid_optimized("([{}])"))  # True
print(isValid_optimized("((("))     # False

#Esta función valida si una cadena compuesta por paréntesis ((), {}, []) está correctamente balanceada, es decir, si cada paréntesis de apertura tiene su correspondiente cierre en el orden correcto.
#La solución usa una estructura de pila (stack), que es ideal para problemas donde hay que verificar pares anidados en orden LIFO (último en entrar, primero en salir).

#¿Cómo funciona?
#Se crea un diccionario pair con los paréntesis de apertura como clave y sus respectivos cierres como valor. Esto permite acceder rápidamente al carácter de cierre esperado.
#Se recorre cada carácter en la cadena:
#Si es un paréntesis de apertura ((, {, [), en lugar de guardar el símbolo abierto, se guarda directamente el símbolo de cierre esperado en la pila.
#Si es un paréntesis de cierre (), }, ]), se verifica si:
#La pila está vacía (no hay apertura previa, lo que es inválido), o
#El símbolo que se saca de la pila no coincide con el cierre actual (también inválido).
#Al final, la pila debe estar vacía. Si no lo está, significa que quedaron paréntesis de apertura sin cerrar.

#¿Por qué es eficiente?
#Optimización importante: En lugar de guardar los símbolos abiertos, se guarda directamente lo que se espera cerrar. Esto simplifica la comparación: no se necesita buscar en el diccionario, solo se compara directamente.
#La solución es O(n) en tiempo, ya que cada carácter se recorre una sola vez.
#El espacio es también O(n) en el peor caso, si todos los caracteres son paréntesis abiertos.