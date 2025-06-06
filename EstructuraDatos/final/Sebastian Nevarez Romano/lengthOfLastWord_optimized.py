#problema10- 58leetcode
# Solución Optimizada (recorrido desde el final)

def lengthOfLastWord_optimized(s):
    length = 0                       # Inicializamos el contador de longitud en 0
    i = len(s) - 1                   # Empezamos desde el último índice de la cadena

    # Ignorar los espacios del final
    while i >= 0 and s[i] == ' ':
        i -= 1                      # Retrocedemos hasta encontrar un carácter que no sea espacio

    # Contar la última palabra
    while i >= 0 and s[i] != ' ':
        length += 1                # Incrementamos el contador por cada carácter de la última palabra
        i -= 1                     # Retrocedemos por la cadena

    return length                  # Devolvemos la longitud calculada

# Tiempo: O(n) | Espacio: O(1)


# Pruebas
print(lengthOfLastWord_optimized("Hello World"))          # 5
print(lengthOfLastWord_optimized("   fly me   to   the moon  "))  # 4
print(lengthOfLastWord_optimized("luffy is still joyboy")) # 6

#Esta solución optimizada calcula la longitud de la última palabra sin dividir la cadena ni usar espacio extra:

#Se empieza desde el final de la cadena y se ignoran los espacios en blanco finales.
#Luego se cuenta la cantidad de caracteres de la última palabra hasta encontrar un espacio o el inicio de la cadena.
#Al usar índices y contadores simples, se evita crear listas o cadenas adicionales.

#Complejidad:
#Tiempo: O(n), porque en el peor caso se recorre la cadena una vez desde el final hacia el inicio.
#Espacio: O(1), ya que solo se usan variables simples para el conteo y el índice, sin estructuras adicionales.