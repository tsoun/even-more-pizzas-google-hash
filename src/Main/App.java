package Main;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Scanner;
import Pizzeria.*;

public class App {

    public static void main(String[] args) throws Exception {
        Scanner scanner = new Scanner(System.in);
        List<String> numOfTeams = new ArrayList<String>(Arrays.asList(scanner.nextLine().split(" ")));
        int numOfPizzas = Integer.parseInt(numOfTeams.get(0));
        numOfTeams.remove(0);

        List<Team> teams = new ArrayList<Team>();
        List<Pizza> pizzas = new ArrayList<Pizza>();

        for (String team : numOfTeams) {
            teams.add(new Team(Integer.parseInt(team)));
        }

        for (int i = 0; i < numOfPizzas; i++) {
            List<String> ingredients = new ArrayList<String>(Arrays.asList(scanner.nextLine().split(" ")));
            int num = Integer.parseInt(ingredients.get(0));
            ingredients.remove(0);
            pizzas.add(new Pizza(num, ingredients));
        }
        calculateMaxDifferentIngredients(pizzas, teams.get(0));
        scanner.close();
    }

    private static void printPizzas(List<Pizza> pizzas) {
        int n = 0;
        for (Pizza pizza : pizzas) {
            System.out.println("Pizza number " + ++n + "\tingr.: " + pizza.showIngredients());
        }
    }

    private static void printTeams(List<Team> teams) {
        int n = 0;
        for (Team team : teams) {
            System.out.println("Team number " + ++n + "\tparticipants.: " + team.members());
        }
    }

    private static void calculateMaxDifferentIngredients(List<Pizza> pizzas, Team team) {
        int members = team.members(), maxDiffIngr, uniqueIngrs = 0, diffIngr = 0;
        List<Pizza> selectedPizzas = new ArrayList<Pizza>();
        List<Pizza> newSelectedPizzas = new ArrayList<Pizza>();
        List<String> uniqueIngr = new ArrayList<String>();

        System.out.println(pizzas);

        for (int member = 0; member < members; member++) {
            uniqueIngrs = 0;
            for (Pizza pizza : pizzas) {
                if (selectedPizzas.contains(pizza)) {
                    continue;
                }
                for (Pizza selectedPizza : selectedPizzas) {
                    for (String ingredient : selectedPizza.ingredients) {
                        if (uniqueIngr.contains(ingredient) == false) {
                            uniqueIngrs++;
                            uniqueIngr.add(ingredient);
                        }
                    }
                }
                maxDiffIngr = uniqueIngrs;
                diffIngr = uniqueIngrs;
                for (String ingredient : pizza.ingredients) {
                    if (uniqueIngr.contains(ingredient)) {
                        diffIngr++;
                    }
                }
                if (maxDiffIngr <= diffIngr) {
                    if (newSelectedPizzas.size() != 0) {
                        newSelectedPizzas.remove(newSelectedPizzas.size() - 1);
                    }
                    newSelectedPizzas.add(pizza);
                    maxDiffIngr = diffIngr;
                }

            }
            if (newSelectedPizzas.size() != 0) {
                selectedPizzas.add(newSelectedPizzas.get(newSelectedPizzas.size() - 1));
            }
        }
        System.out.println(selectedPizzas);
    }
}