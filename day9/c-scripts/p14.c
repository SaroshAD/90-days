#include <stdio.h>

int main()
{
char word_1[] = "Programming";

int count = 0;
int x = 0;

while (word_1[x] != '\0')
{
    count++;
    x++;
}
printf("\nLength = %d\n", count);
}

