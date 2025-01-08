package DesafioBeecrowdJava;
import java.util.Scanner;
import java.util.ArrayList;
import java.util.List;

public class Idades {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int entrada = 0;
        int soma;
        List<Integer> idades = new ArrayList<>();

        while (entrada >= 0) {
            entrada = sc.nextInt();
            if (entrada >= 0) {
                idades.add(entrada);
            }
        }

        soma = idades.stream()
               .mapToInt(Integer::intValue)
               .sum();

        System.out.printf("%.2f", (double) soma / idades.size());

    }
}
