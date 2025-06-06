#problema10- 58leetcode
# Solución Simple (split)

def lengthOfLastWord_simple(s):
    words = s.strip().split()     # Eliminamos espacios al inicio y fin, luego separamos la cadena en palabras usando espacios
    return len(words[-1])         # Devolvemos la longitud de la última palabra de la lista

# Tiempo: O(n) | Espacio: O(n)

#Esta solución obtiene la longitud de la última palabra en una cadena de texto de forma sencilla:

#Primero, strip() elimina espacios en blanco al inicio y al final de la cadena para evitar problemas si hay espacios extras.
#Luego, split() divide la cadena en una lista de palabras separadas por espacios.
#Finalmente, se accede a la última palabra con words[-1] y se calcula su longitud con len().

#Complejidad:
#Tiempo: O(n), porque el método split() recorre toda la cadena una vez para dividirla en palabras.
#Espacio: O(n), ya que se crea una lista que puede contener todas las palabras de la cadena.