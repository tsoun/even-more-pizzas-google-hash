#include <stdio.h>
#include <stdlib.h>

void perms(int, int, int, int, int ***, int *);
int calculateSum(int, int *, int *);
int main()
{
    int pizzas, **x, *coef;
    int index = 0;
    pizzas = 5;
    coef = malloc(sizeof(int) * 4); // coef := the number of pizzas each i-member team would get if it happens to be delivered pizzas
    coef[0] = 2;
    coef[1] = 3;
    coef[2] = 3;
    coef[3] = 4;
    x = malloc(sizeof(int *));
    *x = malloc(sizeof(int) * 4);
    perms(index, 4, 4, pizzas, &x, coef);
    printf("Hello it's all ok.\n"); //fck gdb
    return 0;
}

void perms(int index, int n, int t, int pizzas, int ***x, int *coef)
{
    for (int i = 0; i < 2; i++)
    {
        *(*(*x + index) + t - n) = i;
        if (n == 0)
        {
            if (calculateSum(t, *(*x + index), coef) <= pizzas)
            {
                *x = realloc(*x, sizeof(int *) * (index + 2));
                *(*x + index + 1) = malloc(sizeof(int) * 4);
                printf("Successful combination. %d %d %d %d\n", *(*(*x + index)), *(*(*x + index) + 1), *(*(*x + index) + 2), *(*(*x + index) + 3));
                //a successful combination, eg for 1 2 1, then it is
                //2 pizzas for the 2-member team and 3 pizzas for the
                //3-member team (given FIVE pizzas available).
                index++;
            }
        }
        else
        {
            perms(index, n - 1, 4, pizzas, x, coef);
        }
    }
    return;
}

int calculateSum(int t, int *x, int *coef)
{
    int sum = 0;
    for (int i = 0; i < t; i++)
    {
        sum += *(coef + i) * *(x + i);
    }
    return sum;
}