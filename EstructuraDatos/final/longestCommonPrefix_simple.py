#problema2- 14leetcode
# Solución Simple
# Tomamos la primera palabra y comparamos letra por letra con las demás.

def longestCommonPrefix_simple(strs: list[str]) -> str:
    # Si la lista está vacía, regresamos cadena vacía
    if not strs:
        return ""
# Tomamos el primer string como prefijo inicial
    prefix = strs[0]
# Recorremos los siguientes strings
    for word in strs[1:]:
        i = 0
       # Mientras el string actual no empiece con el prefijo,
        # recortamos el prefijo quitamos último carácter
        while i < len(prefix) and i < len(word) and prefix[i] == word[i]:
            i += 1
        prefix = prefix[:i]
        if prefix == "":
            break

    return prefix
print(longestCommonPrefix_simple(["flower", "flow", "flight"]))  # "fl"
print(longestCommonPrefix_simple(["dog", "racecar", "car"]))     # ""

# Complejidad:
# Tiempo: O(n * m), donde n = número de palabras, m = longitud del prefijo.
# Espacio: O(1)

#La función longestCommonPrefix_simple recibe una lista de cadenas y busca el prefijo común más largo que aparece al inicio de todas las palabras.

#Cómo funciona:
#Primero, verifica si la lista está vacía; si es así, regresa una cadena vacía porque no hay prefijo posible.
#Usa el primer string de la lista como prefijo inicial.
#Luego, compara ese prefijo con cada una de las demás palabras de la lista:
#Para cada palabra, compara carácter por carácter con el prefijo mientras sean iguales.
#Si encuentra una diferencia, recorta el prefijo hasta la posición donde coincidían los caracteres.
#Si en algún momento el prefijo queda vacío, termina el proceso porque no existe ningún prefijo común.
#Al final, retorna el prefijo común más largo encontrado.

#Complejidad:
#Tiempo: O(n * m), donde n es el número de palabras y m la longitud del prefijo común, porque en el peor caso comparamos cada carácter de cada palabra.
#Espacio: O(1), solo se usa espacio constante adicional para variables.
#Esta solución es intuitiva y sencilla, adecuada para entender el concepto básico de búsqueda de prefijos comunes.