//Sebastian Nevarez Romano
//Matricula:14970
//18/02/2025

public class ExerciseParNone {
    public static void main(String[] args) {
        int[] numeros = {
            0, 2, 5, 8, 11, 14, 17, 20, 23, 26, 
            29, 32, 35, 38, 41, 44, 47, 50, 53, 56, 
            59, 62, 65, 68, 71, 74, 77, 80, 83, 86, 
            89, 92, 95, 98, 0, 3, 6, 9, 12, 15, 
            18, 21, 24, 27, 30, 33, 36, 39, 42, 45
        };

        // Llamamos al método contarNumeros y le pasamos el array
        contarNumeros(numeros);
    }

    public static void contarNumeros(int[] numeros) {
        // Definimos los contadores dentro del método
        int pares = 0;
        int nones = 0;
        int zeros = 0;

        for (int num : numeros) {
            if (num == 0) {
                zeros++;
            } else if (num % 2 == 0) {
                pares++;
            } else {
                nones++;
            }
        }

        // Imprimimos los resultados
        System.out.println("Total de números pares: " + pares);
        System.out.println("Total de números nones: " + nones);
        System.out.println("Total de ceros: " + zeros);
    }
}
    
    
    


