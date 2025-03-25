public class IndexdSearch {
    public static void main(String[] args) {
        int[] datos = {10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80};
        int[] indices = {0, 4, 8, 12}; // Índices auxiliares
        int buscar =45;
    
        int comparaciones = 0;
        int bloque = -1;
    
        // Búsqueda en el índice
        for (int i = 0; i < indices.length - 1; i++) {
            comparaciones++;
            if (datos[indices[i]] <= buscar && buscar < datos[indices[i + 1]]) { // 🔹 Corrección aquí
                bloque = i;
                break;
            }
        }
    
        // Verificar si el elemento está en el último bloque
        if (bloque == -1 && datos[indices[indices.length - 1]] <= buscar) {
            bloque = indices.length - 1;
        }
    
        // Si no se encontró un bloque válido
        if (bloque == -1) {
            System.out.println("Elemento no encontrado.");
            System.out.println("Comparaciones realizadas: " + comparaciones);
            return;
        }
    
        // Definir los límites del bloque (inicio y fin)
        int inicio = indices[bloque];
        int fin = (bloque == indices.length - 1) ? datos.length - 1 : indices[bloque + 1] - 1; // 🔹 Ajuste en el fin del rango
    
        // Búsqueda secuencial dentro del bloque identificado
        for (int i = inicio; i <= fin; i++) {
            comparaciones++;
            if (datos[i] == buscar) {
                System.out.println("Elemento encontrado en la posición: " + i);
                System.out.println("Comparaciones realizadas: " + comparaciones);
                return;
            }
        }
    
        System.out.println("Elemento no encontrado.");
        System.out.println("Comparaciones realizadas: " + comparaciones);
    }
}    