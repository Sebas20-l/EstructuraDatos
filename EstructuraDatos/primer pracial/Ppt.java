//Nombre: Sebastian Nevarez Romano
//Matricula: 14970
//06/02/2025
//piedra, papel o tijera
 
import java.util.Random;


public class Ppt
{
    public static void main(String args[]){
        String[] ppt ={"piedra","papel","tijera"};

        //genera un numero random
        Random rand = new Random();
        int indice = rand.nextInt(3);

        System.out.println("seleccionado: " + ppt[indice]);
}
}