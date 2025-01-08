package DesafioBeecrowdJava;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class TipoeCombustivel {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        List<Integer> opcao1 = new ArrayList<>();
        List<Integer> opcao2 = new ArrayList<>();
        List<Integer> opcao3 = new ArrayList<>();
        int entrada;

        entrada = 1;

        while (entrada != 4){
            entrada = sc.nextInt();
            if (entrada == 1){
                opcao1.add(entrada);
            } else if (entrada == 2){
                opcao2.add(entrada);
            } else if (entrada == 3){
                opcao3.add(entrada);
            }
        }
        System.out.printf("MUITO OBRIGADO\nAlcool: %d\nGasolina: %d\nDiesel: %d", opcao1.size(), opcao2.size(), opcao3.size());
    }
}
