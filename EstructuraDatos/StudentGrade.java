// Sebastian Nevarez Romano
//matricula:14970
//fecha: 11/02/2025


public class StudentGrade {
    

    public int calculatePartialGrade(int examScore, int homeworkScore){
        double FirstPartialGrade=(examScore*0.7+homeworkScore*0.3);
        return  (int) (FirstPartialGrade);
    
    }

    public int calculateFinalGrade(int firstPartial, int secondPartial, int thirdPartial, int finalExam) {
        double averagePartials = (firstPartial + secondPartial + thirdPartial) / 3.0;
        double finalScore = (averagePartials * 0.5) + (finalExam * 0.5);
        return (int) (finalScore);
    }
    
    public String checkFailureByAbsences(int totalHours, int absences) {
        double maxAllowedAbsences = totalHours * 0.1;
        if (absences < maxAllowedAbsences) {
            return "El alumno está reprobado por faltas.";
        } else {
            return "El alumno cumple con las asistencias mínimas.";
        }
    }
    public static void main(String[] args) {
        // Crear un objeto de la clase StudentGrade para llamar a los métodos
        StudentGrade student = new StudentGrade();
        
        // Calcular la calificación del parcial
        int partial1 = student.calculatePartialGrade(85, 90);
        System.out.println("Calificación del primer parcial: " + partial1);
    
        
        // Calcular la calificación final del semestre
        int finalGrade = student.calculateFinalGrade(80, 75, 90, 85);
        System.out.println("Calificación final del semestre: " + finalGrade);
    
        // Verificar el estatus de asistencia
        String attendanceStatus = student.checkFailureByAbsences(64, 7);
        System.out.println(attendanceStatus);
    }
}


