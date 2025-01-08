package DesafioBeecrowdJava;
import java.util.Scanner;

public class GastodeCombustivel {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        double tempo, velocidade, distancia, litros, kml;

        tempo = sc.nextDouble();
        velocidade = sc.nextDouble();

        kml = 12;
        distancia = tempo * velocidade;
        litros = distancia / kml;

        System.out.printf("%.3f", litros);

        sc.close();

    }
}
