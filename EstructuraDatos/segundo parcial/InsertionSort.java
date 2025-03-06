public class InsertionSort {
    public static int insertionSort(int arr[]) {
        int n = arr.length;
        int operaciones = 0;
        for (int i = 1; i < n; i++) {
            int key = arr[i];
            int j = i - 1;
            while (j >= 0 && arr[j] > key) {
                arr[j + 1] = arr[j];
                j = j - 1;
                operaciones++;
            }
            arr[j + 1] = key;
            operaciones++;
        }
        return operaciones;
    } 




    
    public static void main(String args[]) {
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
}