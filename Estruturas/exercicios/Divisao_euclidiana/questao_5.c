#include <stdio.h>
#include <locale.h>
int main(void)
{
    setlocale(LC_ALL, "");
    int i, resto, n1, n2;
    printf("Digite os números que você queira saber a sequência que os liga.\n");
    scanf("%d%d", &n1, &n2);
    for (i = n1; i <= n2; i++)
    {
        resto = i % 6;         
        if (resto == 0)                                
        {
            printf("%d → ", i);
        }
        else if (resto == 1)
        {
            printf("%d ↓ ", i);
        }
        else if (resto == 2)
        {
            printf("%d ↗ ", i);
        }
        else if (resto == 3)
        {
            printf("%d ↓ ", i);
        }
        else if (resto == 4)
        {
            printf("%d → ", i);
        }
        else if (resto == 5)
        {
            printf("%d ↑ ", i);
        }
    }
    printf("\n");
    return 0;
}
