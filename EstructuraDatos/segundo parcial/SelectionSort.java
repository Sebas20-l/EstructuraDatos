public class SelectionSort {
    public static int selectionSort(int arr[]) {
        int n = arr.length;
        int operaciones = 0;
        for (int i = 0; i < n - 1; i++) {
            int minIndex = i;
            for (int j = i + 1; j < n; j++) {
                if (arr[j] < arr[minIndex]) {
                    minIndex = j;
                }
                operaciones++; // Cuenta comparaciones
            }
            // Intercambio de elementos
            int temp = arr[minIndex];
            arr[minIndex] = arr[i];
            arr[i] = temp;
            operaciones += 3; // Cuenta las 3 asignaciones del intercambio
            
            // Imprimir el estado del arreglo en cada iteración
            System.out.print("Iteración " + (i + 1) + ": ");
            for (int num : arr) {
                System.out.print(num + " ");
            }
            System.out.println();
        }
        return operaciones;
    }
    
    public static void main(String args[]) {
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
}