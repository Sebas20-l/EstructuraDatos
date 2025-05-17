public class ArbolBinario {

    // Clase Nodo
    static class Nodo {
        int valor;
        Nodo izquierda;
        Nodo derecha;

        Nodo(int valor) {
            this.valor = valor;
            izquierda = null;
            derecha = null;
        }
    }

    // Función para sumar los nodos
    public static int sumarNodos(Nodo raiz) {
        if (raiz == null) {
            return 0;
        }
        return raiz.valor + sumarNodos(raiz.izquierda) + sumarNodos(raiz.derecha);
    }

    // Función principal
    public static void main(String[] args) {
        

        Nodo raiz = new Nodo(10);
        raiz.izquierda = new Nodo(5);
        raiz.derecha = new Nodo(3);
        raiz.izquierda.izquierda = new Nodo(2);
        raiz.izquierda.derecha = new Nodo(1);

        int suma = sumarNodos(raiz);
        System.out.println("Suma total de los nodos: " + suma); // Resultado esperado: 21
    }
}