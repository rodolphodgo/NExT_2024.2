package DesafioBeecrowdJava;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Multiplos {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n1, n2;
        String entrada;

        entrada = sc.nextLine();

        String[] numerosArray = entrada.split(" ");
        List<Integer> numeros = new ArrayList<>();

        for (String num : numerosArray) {
            numeros.add(Integer.parseInt(num));
        }

        n1 = numeros.get(0);
        n2 = numeros.get(1);

        if (n1 % n2 == 0) {
            System.out.print("São Múltiplos");
        } else if (n2 % n1 == 0) {
            System.out.print("São Múltiplos");
        } else {
            System.out.print("Não são Múltiplos");
        }

        sc.close();

    }
}
