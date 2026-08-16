#include <stdio.h>

void swap(int *a, int *b)
{
    int temp;

    temp = *a;
    *a = *b;
    *b = temp;
}


int main()
{

 int a;
 int b;

 printf("Enter the first number: ");
 scanf("%d", &a);

 printf("\nEnter the second number: ");
 scanf("%d", &b);

 printf("\nbefore swap:\na = %d \nb = %d \n", a, b);


 swap(&a, &b);

  printf("\nAfter swap:\na = %d \nb = %d \n", a, b);
}
