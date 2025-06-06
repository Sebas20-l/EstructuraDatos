#problema 1- 13leetcode
# Solución Optimizada
# Recorremos de izquierda a derecha y comparamos el símbolo actual con el siguiente.

 # Diccionario con los valores de cada símbolo romano
def romanToInt_optimized(s: str) -> int:
    roman = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }
    total = 0 # Variable para acumular el valor total
    i = 0  # Índice para recorrer la cadena 's'

    while i < len(s): # Mientras no lleguemos al final de la cadena
      # Si no estamos en el último símbolo y el valor actual es menor que el siguiente,
        # significa que debemos restar (ejemplo: IV = 5 - 1)
        if i + 1 < len(s) and roman[s[i]] < roman[s[i + 1]]:
             # Sumamos la diferencia del siguiente menos el actual
            total += roman[s[i + 1]] - roman[s[i]]
            i += 2 # Avanzamos dos posiciones porque procesamos un par de símbolos
        else:
             # Si no es un caso de resta, simplemente sumamos el valor del símbolo actual
            total += roman[s[i]]
            i += 1 # Avanzamos una posición

    return total

# Complejidad:
# Tiempo: O(n)
# Espacio: O(1)

# Pruebas:

print(romanToInt_optimized("III"))      # 3
print(romanToInt_optimized("LVIII"))    # 58
print(romanToInt_optimized("MCMXCIV"))  # 1994

#La función romanToInt_optimized convierte un número romano dado como cadena en su equivalente decimal. Para esto, recorre la cadena de izquierda a derecha comparando el valor del símbolo actual con el siguiente:
#Si el símbolo actual es menor que el siguiente, significa que debemos restar (por ejemplo, IV es 5 - 1 = 4), por lo que sumamos la diferencia y saltamos ambos símbolos.
#Si no, simplemente sumamos el valor del símbolo actual.
#Esta estrategia permite manejar correctamente los números romanos que incluyen restas y los que no, en un solo recorrido lineal.
#La complejidad temporal es O(n), siendo n la longitud de la cadena, porque cada símbolo se procesa una vez o dos si es parte de un par especial. La complejidad espacial es O(1), ya que usamos un diccionario fijo para los símbolos romanos.