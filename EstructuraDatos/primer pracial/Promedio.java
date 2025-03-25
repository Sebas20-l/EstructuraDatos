//autor: Sebastian Nevarez Romano
//Matricula: 14970
// 05/02/2025
//suma de promedios

public class Promedio{
    public static void main(String[] args) {

    //declarando el arreglo double
    double[] numeros= {85,90,72};

    //hacer suma
    double suma= 0.0;

    //uso de cilco for 
    for (int i = 0; i < numeros.length; i++) {
        suma+= numeros[i];
        System.out.println("La calificacion es "+(i+1)+"."+ numeros[i]);
    }

    //hacer la division
    double promedio=suma/numeros.length;

    //imprimiendo los resultados
    System.out.println("suma total:" + suma);
    System.out.println("promedio:" + promedio);


    

    }
}


       