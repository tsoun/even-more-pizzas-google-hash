package Pizzeria;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Pizza {
    public int numOfIngredients;
    public List<String> ingredients;

    public Pizza(int numOfIngredients, List<String> ingredients) {
        this.numOfIngredients = numOfIngredients;
        this.ingredients = ingredients;
    }

    public String showIngredients() {
        return String.join(" ", this.ingredients);
    }

    public void printIngredients() {
        for (String ingredient : ingredients) {
            System.out.println(ingredient);
        }
    }
}
