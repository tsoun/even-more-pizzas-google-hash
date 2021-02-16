#include <stdio.h>
#include <stdlib.h>
#include <strings.h>

void readInput(FILE *, int *, int **, int **, char ****);
int main()
{
    FILE *input, *output;
    int numOfPizzas, *teams, *numOfIngredients;
    char ***ingredients;

    input = fopen("input.txt", "r");
    output = fopen("output.txt", "w+");

    readInput(input, &numOfPizzas, &teams, &numOfIngredients, &ingredients);
    return 0;
}

void readInput(FILE *fp, int *numOfPizzas, int **teams, int **numOfIngredients, char ****ingredients)
{
    *teams = malloc(3 * sizeof(int));
    char *ingredient;
    ingredient = malloc(sizeof(char) * 10);
    int i, j;

    fscanf(fp, "%d %d %d %d", numOfPizzas, &(*teams)[0], &(*teams)[1], &(*teams)[2]);
    *ingredients = malloc(*numOfPizzas * sizeof(char **));
    *numOfIngredients = malloc(*numOfPizzas * sizeof(int));
    for (i = 0; i < *numOfPizzas; i++)
    {
        fscanf(fp, "%d", &(*numOfIngredients)[i]);
        (*ingredients)[i] = malloc(sizeof(char *) * (*numOfIngredients)[i]);
        for (j = 0; j < (*numOfIngredients)[i]; j++)
        {
            fscanf(fp, "%s", ingredient);
            (*ingredients)[i][j] = malloc(strlen(ingredient) + 1);
            strcpy((*ingredients)[i][j], ingredient);
        }
    }
    return;
}
