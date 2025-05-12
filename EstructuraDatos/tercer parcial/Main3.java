public class Main3 {
  
    
    /*public class Main {
        public static void main(String[] args) {
            SinglyLinkedList list = new SinglyLinkedList();
    
            list.insert(10);
            list.insert(20);
            list.insert(30);
    
            System.out.println("List:");
            list.display();
    
            System.out.println("Is 20 in the list? " + list.search(20));
    
            list.delete(20);
    
            System.out.println("After deleting 20:");
            list.display();
        }
     }*/
    
    public static void main(String[] args) {
        EjemploCola miCola = new EjemploCola();

        miCola.agregarCliente("Cliente 1");
        miCola.agregarCliente("Cliente 2");
        miCola.agregarCliente("Cliente 3");
        miCola.agregarCliente("Cliente 4");
        

        System.out.println("Cliente al frente: " + miCola.verClienteAlFrente());
        System.out.println("Atendiendo a: " + miCola.atenderCliente());
        System.out.println("Atendiendo a: " + miCola.atenderCliente());
        System.out.println("Cliente al frente ahora: " + miCola.verClienteAlFrente());

        miCola.mostrarCola();
    

/*public static void main(String[] args) {
    
}*/
}
}

