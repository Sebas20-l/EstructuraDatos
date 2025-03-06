public class BubbleSortExample {
    // Método para ordenar un array usando Bubble Sort y contar comparaciones y operaciones
    public static int[] bubbleSort(int[] arr) {
        int n = arr.length;
        boolean swapped;
        int comparisons = 0; // Contador de comparaciones
        int operations = 0;  // Contador de intercambios

        for (int i = 0; i < n - 1; i++) {
            swapped = false;
            
            for (int j = 0; j < n - 1 - i; j++) {
                comparisons++; // Se realiza una comparación
                if (arr[j] > arr[j + 1]) {
                    // Intercambiar elementos si están en el orden incorrecto
                    int temp = arr[j];
                    arr[j] = arr[j + 1];
                    arr[j + 1] = temp;
                    swapped = true;
                    operations++; // Se cuenta el intercambio
                }
            }
            
            // Si no hubo intercambios, el array ya está ordenado
            if (!swapped) break;
        }

        // Imprimir número de comparaciones y operaciones
        System.out.println("Comparaciones: " + comparisons);
        System.out.println("Intercambios: " + operations);
        return arr;
    }

    // Método para imprimir un array
    public static void printArray(int[] arr) {
        for (int num : arr) {
            System.out.print(num + " ");
        }
        System.out.println();
    }
}

// Clase principal (no pública, porque el archivo se llama BubbleSortExample.java)
class SecondPartialMain {
    public static void main(String[] args) {
        // Peor caso: arreglo en orden inverso
        int[] arr = {10, 9, 8, 7, 6, 5, 4, 3, 2, 1};
        
        System.out.println("Array original:");
        BubbleSortExample.printArray(arr);
        
        System.out.println("Ordenando con Bubble Sort...");
        BubbleSortExample.bubbleSort(arr);
        
        System.out.println("Array ordenado:");
        BubbleSortExample.printArray(arr);

        // Cálculo de complejidad en el peor caso O(n^2)
        int n = arr.length;
        int maxComparisons = (n * (n - 1)) / 2; // Fórmula de comparaciones en Bubble Sort
        int maxSwaps = maxComparisons; // En el peor caso, cada comparación resulta en un intercambio

        System.out.println("\nCálculo de Big O:");
        System.out.println("O(n^2) comparaciones teóricas: " + maxComparisons);
        System.out.println("O(n^2) intercambios teóricos: " + maxSwaps);
    }
}

    