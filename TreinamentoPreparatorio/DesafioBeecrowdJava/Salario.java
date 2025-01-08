package DesafioBeecrowdJava;
import java.util.Scanner;

public class Salario {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int numero, horas;
        double valor, salario;

        numero = sc.nextInt();
        horas = sc.nextInt();
        valor = sc.nextDouble();

        salario = valor * horas;

        System.out.printf("NUMBER %d\n", numero);
        System.out.printf("SALARY = U$ %.2f", salario);

    }
}
