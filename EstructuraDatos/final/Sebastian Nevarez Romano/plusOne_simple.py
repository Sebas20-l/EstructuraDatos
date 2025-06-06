#problema9- 66leetcode
# Solución Simple (convertir a entero)

def plusOne_simple(digits):
    num = int("".join(str(d) for d in digits))    # Convertimos la lista de dígitos en un string, luego a entero
    num += 1                                       # Sumamos 1 al número entero
    return [int(d) for d in str(num)]              # Convertimos el número resultante de nuevo en lista de dígitos

# Tiempo: O(n) por las conversiones | Espacio: O(n)

#Esta solución convierte la lista de dígitos que representan un número entero en una cadena, luego en un número entero, le suma uno y finalmente convierte el resultado de nuevo en una lista de dígitos.

#Funcionamiento:
#Se usa un generador para convertir cada dígito de la lista a cadena y concatenarlos en un solo string.
#Se transforma ese string en un entero con int().
#Se suma 1 al entero resultante.
#Se convierte el entero modificado en string para poder dividirlo nuevamente en dígitos individuales.
#Se usa una lista por comprensión para transformar cada carácter en un entero, devolviendo la lista actualizada.

#Complejidad:
#Tiempo: O(n), donde n es el número de dígitos, porque cada conversión y procesamiento recorre la lista o el string completo.
#Espacio: O(n), ya que se crean nuevas estructuras de datos (string y lista).