package DesafioBeecrowdJava;
import java.util.Scanner;

public class SomaSimples {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int A, B, SOMA;

        A = sc.nextInt();
        B = sc.nextInt();

        SOMA = A + B;

        System.out.printf("SOMA = %d", SOMA);
    }
}
