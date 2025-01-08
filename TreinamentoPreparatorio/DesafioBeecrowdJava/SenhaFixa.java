package DesafioBeecrowdJava;
import java.util.Objects;
import java.util.Scanner;

public class SenhaFixa {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        String senha, entrada;

        senha = "2002";

        entrada = sc.nextLine();

        while (!Objects.equals(entrada, senha)) {
            System.out.println("Senha Invalida");
            entrada = sc.nextLine();
        }

    }
}
