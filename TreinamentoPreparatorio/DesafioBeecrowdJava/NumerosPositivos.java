package DesafioBeecrowdJava;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class NumerosPositivos {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        double entrada;
        List<Double> numeros = new ArrayList<>();

        for (int i = 1; i <= 6; i++) {
            entrada = sc.nextDouble();
            if (entrada > 0) {
                numeros.add(entrada);
            }
        }

        System.out.printf("%d números positivos", numeros.size());

    }
}
