package DesafioBeecrowdJava;
import java.util.Scanner;

public class Distancia {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);

        int dist, tempo;

        dist = sc.nextInt();
        tempo = dist * 2;

        System.out.printf("%d minutos", tempo);

        sc.close();
    }
}
