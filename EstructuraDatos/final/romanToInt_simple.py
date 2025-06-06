#prblema 1-13leetcode
# Solución Simple
# Recorremos la cadena de derecha a izquierda y restamos si un número menor aparece antes que uno mayor.

def romanToInt_simple(s: str) -> int:
    # Mapeo de cada símbolo romano a su valor numérico
    roman = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }
    total = 0 # Resultado acumulado
    prev = 0 # Valor anterior para comparar si se suma o se resta

 # Recorremos la cadena desde el final al inicio
    for char in reversed(s):
        current = roman[char]  # Convertimos el símbolo a valor numérico
         # Si el valor actual es menor que el anterior, restamos
        if current < prev:
            total -= current
        else:
            total += current # Si no, sumamos
        prev = current  # Actualizamos el valor anterior

    return total

# Pruebas:
print(romanToInt_simple("III"))      # 3
print(romanToInt_simple("LVIII"))    # 58
print(romanToInt_simple("MCMXCIV"))  # 1994
# Complejidad:
# Tiempo: O(n)
# Espacio: O(1)

#Esta solución convierte números romanos a enteros utilizando un enfoque eficiente basado en una lectura de derecha a izquierda, y una comparación entre valores sucesivos.
#Se usa un diccionario (roman) para mapear cada símbolo romano a su valor numérico.
#Se recorre la cadena en orden inverso (de derecha a izquierda), porque en los números romanos, si un símbolo más pequeño aparece antes que uno mayor (por ejemplo, "IV" = 4), se realiza una resta. Si no, se suma normalmente.
#Se guarda un valor previo (prev) para hacer la comparación con el símbolo actual. Si el actual es menor que el previo, se resta del total; en caso contrario, se suma.
#Al final se devuelve el total acumulado.
#Este enfoque evita recorrer la cadena varias veces y no utiliza estructuras adicionales más allá de una tabla de mapeo y variables simples.

#Complejidad:
#Tiempo: O(n), donde n es la longitud de la cadena.
#Espacio: O(1), porque el espacio usado no depende del tamaño de la entrada, solo del diccionario fijo.