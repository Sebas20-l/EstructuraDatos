import java.util.LinkedList;
import java.util.Queue;

public class EjemploCola {
    private Queue<String> cola;

    public EjemploCola() {
        cola = new LinkedList<>();
    }

    public void agregarCliente(String cliente) {
        cola.Enqueue(elemento);
    }

    public String verClienteAlFrente() {
        return cola.peek();
    }

    public String atenderCliente() {
        return cola.poll();
    }

    public void mostrarCola() {
        System.out.println("Cola actual: " + cola);
    }
}
