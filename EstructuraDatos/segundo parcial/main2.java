

public class main2 {
        public static void main(String[] args) {
            // Crear una instancia de Capitales
            HashMapExample miCapitales = new HashMapExample();
    
            // Llamar a los métodos
            System.out.println("La capital de Alemania es: " + miCapitales.obtenerCapital("Germany"));
            System.out.println("La capital de México es: " + miCapitales.obtenerCapital("Mexico"));
    
            System.out.println("\nLista de todas las capitales:");
            miCapitales.mostrarCapitales();
        }
    }

    

