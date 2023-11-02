import java.util.Stack;
import java.util.Scanner;

public class problema6{

    public static boolean EsNumero(String cadena) {

        boolean resultado;

        try {
            Integer.parseInt(cadena);
            resultado = true;
        } catch (NumberFormatException excepcion) {
            resultado = false;
        }

        return resultado;
    }

    public static void main(String[] args) {
        Stack<String> biblioteca = new Stack<>();
        Stack<String> mesa = new Stack<>();
        Stack <String> ultimo = new Stack<>();
        Scanner entrada = new Scanner(System.in);
        
        System.out.println("Ingrese un número entero:");
        String n = entrada.nextLine();

        //
        // Validación de entrada
        //

        while(!EsNumero(n)){
            System.out.println("Ingrese un número entero:");
            n = entrada.nextLine();
        }

        while(Integer.parseInt(n) < 2){
            System.out.println("Ingrese un número mayor a 1");
            n = entrada.nextLine();
        }

        //
        // Llenado de la pila
        //

        for (int i = 0; i < Integer.parseInt(n); i++) {
            int libro = (int)(Math.random()*3+1);
            System.out.println(libro);
        }
    }
}
