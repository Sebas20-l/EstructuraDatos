import java.util.Scanner;


public class GradeCalculationPartial {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Ingrese la calificación del examen parcial: ");
        double examen = scanner.nextDouble();

       
        System.out.print("Ingrese la calificación de las tareas: ");
        double tareas = scanner.nextDouble();

        double calificacionTotal = (examen * 0.7) + (tareas * 0.3);

        System.out.println("Calificación total: " + calificacionTotal);

        scanner.close();
    }
}

