#include <stdio.h>

int subtract(int x, int y)
{
 return x-y;
}

int cube(int z)
{
 return z*z*z;
}

void greet()
{

printf("Hello, Robot!");
}



int main()
{
greet();

printf("\nThis is the result of subtraction %d\n",subtract(20, 8));


printf("This is the result of cube %d\n", cube(3));

}
