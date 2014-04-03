#include <stdio.h>

int main(void)
{
    int numbers[] = {1, 2, 3, 4, 5};
    int sum = 0;
    int i = 0;
    int len = sizeof(numbers) / sizeof(int);

    while(i < len)
    {
        sum = sum + numbers[i];
        i++;
    }

    printf("sum: %d\n", sum);
    return 0;
}