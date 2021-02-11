import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Scanner;
import Pizzeria.*;

public class App {

    public static void main(String[] args) throws Exception {
        int n = 0;
        Scanner scanner = new Scanner(System.in);
        List<String> firstLine = new ArrayList<String>(Arrays.asList(scanner.nextLine().split(" ")));
        int M = Integer.parseInt(firstLine.get(0));
        List<Pizza> pizzas = new ArrayList<Pizza>();

        for (int i = 0; i < M; i++) {
            List<String> ingredients = new ArrayList<String>(Arrays.asList(scanner.nextLine().split(" ")));
            int num = Integer.parseInt(ingredients.get(0));
            ingredients.remove(0);
            pizzas.add(new Pizza(num, ingredients));
        }

        for (Pizza pizza : pizzas) {
            System.out.println("Pizza number " + ++n + "\tingr.: " + pizza.showIngredients());
        }

        scanner.close();
    }
}
