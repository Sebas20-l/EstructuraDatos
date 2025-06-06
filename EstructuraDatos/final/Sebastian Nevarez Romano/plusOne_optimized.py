#problema9- 66leetcode
# Solución Optimizada (sin convertir a entero)

def plusOne_optimized(digits):
    n = len(digits)              # Guardamos la longitud de la lista

    for i in reversed(range(n)):    # Recorremos la lista desde el último dígito hacia el primero
        if digits[i] < 9:            # Si el dígito es menor que 9,
            digits[i] += 1           # simplemente sumamos 1 a ese dígito
            return digits            # y devolvemos la lista modificada inmediatamente
        digits[i] = 0                # Si el dígito es 9, lo ponemos a 0 y seguimos el ciclo para sumar el acarreo

    return [1] + digits              # Si todos los dígitos eran 9, agregamos un 1 al inicio de la lista

# Tiempo: O(n) | Espacio: O(1) si se modifica en el lugar


# Pruebas
print(plusOne_optimized([1,2,3]))   # [1,2,4]
print(plusOne_optimized([9,9,9]))   # [1,0,0,0]
print(plusOne_optimized([0]))       # [1]

#Esta solución optimizada incrementa un número representado como una lista de dígitos sin convertirlo a entero, evitando así problemas con números muy grandes y mejorando la eficiencia en espacio.

#Funcionamiento:
#Se recorre la lista desde el final hacia el inicio para simular la suma del uno como si se hiciera a mano.
#Si el dígito actual es menor que 9, se incrementa en 1 y se retorna la lista, ya que no hay acarreo.
#Si el dígito es 9, se cambia a 0 y el ciclo continúa para sumar el acarreo al siguiente dígito a la izquierda.
#Si se recorren todos los dígitos y todos son 9 (por ejemplo, 999), se crea una nueva lista con un 1 al inicio seguida de ceros.

#Complejidad:
#Tiempo: O(n), donde n es el número de dígitos, porque en el peor caso se recorre toda la lista.
#Espacio: O(1) en la mayoría de los casos porque se modifica la lista en sitio, salvo cuando hay que agregar un dígito extra (como en 999 → 1000).