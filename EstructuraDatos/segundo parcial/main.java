public class main {
    
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

//public static void main(String args[]) {
    int peorCaso[] = {9, 8, 7, 6, 5, 4, 3, 2, 1,0};
    int mejorCaso[] = {0,1, 2, 3, 4, 5, 6, 7, 8, 9};
    
    System.out.println("Peor Caso:");
    int operacionesPeor = insertionSort(peorCaso);
    for (int num : peorCaso) {
        System.out.print(num + " ");
    }
    System.out.println("\nOperaciones realizadas: " + operacionesPeor);
    
    System.out.println("\nMejor Caso:");
    int operacionesMejor = insertionSort(mejorCaso);
    for (int num : mejorCaso) {
        System.out.print(num + " ");
    }
    System.out.println("\nOperaciones realizadas: " + operacionesMejor);
}


//public static void main(String args[]) {
    int peorCaso[] = {5, 4, 3, 2, 1};
    int mejorCaso[] = {1, 2, 3, 4, 5};
    
    System.out.println("Peor Caso:");
    int operacionesPeor = selectionSort(peorCaso);
    for (int num : peorCaso) {
        System.out.print(num + " ");
    }
    System.out.println("\nOperaciones realizadas: " + operacionesPeor);
    
    System.out.println("\nMejor Caso:");
    int operacionesMejor = selectionSort(mejorCaso);
    for (int num : mejorCaso) {
        System.out.print(num + " ");
    }
    System.out.println("\nOperaciones realizadas: " + operacionesMejor);
}

