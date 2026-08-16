#include <stdio.h>

int add(int a, int b);

int main()
{
    printf("%d", add(10, 20));
}

int add(int a, int b)
{
    return a + b;
}
