import java.util.*;

public class GrafoBFS {

    // Clase Grafo
    static class Grafo {
        private Map<Integer, List<Integer>> adyacencias;

        public Grafo() {
            adyacencias = new HashMap<>();
        }

        public void agregarArista(int origen, int destino) {
            adyacencias.putIfAbsent(origen, new ArrayList<>());
            adyacencias.putIfAbsent(destino, new ArrayList<>());

            adyacencias.get(origen).add(destino);
            adyacencias.get(destino).add(origen); // Como es no dirigido
        }

        public void bfs(int inicio) {
            Set<Integer> visitados = new HashSet<>();
            Queue<Integer> cola = new LinkedList<>();

            visitados.add(inicio);
            cola.add(inicio);

            System.out.println("Recorrido BFS desde el nodo " + inicio + ":");

            while (!cola.isEmpty()) {
                int actual = cola.poll();
                System.out.print(actual + " ");

                for (int vecino : adyacencias.getOrDefault(actual, new ArrayList<>())) {
                    if (!visitados.contains(vecino)) {
                        visitados.add(vecino);
                        cola.add(vecino);
                    }
                }
            }

            System.out.println(); // Salto de línea final
        }
    }

    // Método main
    public static void main(String[] args) {
        Grafo grafo = new Grafo();

       
        grafo.agregarArista(0, 1);
        grafo.agregarArista(0, 2);
        grafo.agregarArista(1, 3);
        grafo.agregarArista(2, 3);

        // Realizamos BFS desde el nodo 0
        grafo.bfs(0);
    }
}
