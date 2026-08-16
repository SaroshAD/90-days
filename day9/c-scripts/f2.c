#include <stdio.h>

int multiply(int a, int b)
{
 return a*b;
}

int isEven(int n)
{
 if (n %2==0)
	{
	 return 1;
	}
 return 0;
}

int largest(int a, int b)
{
 if (a>b)
	{
	 return a;
	}
 else
	{
	 return b;
	}
}

int main()
{

int a;
int b;
int x;
printf("Enter the first number: ");
scanf("%d", &a);

printf("\nEnter the second number: ");
scanf("%d", &b);

printf("\n The largest number is %d\n", largest(a, b));

printf("\nThe multiplication of %d and %d is %d \n", a, b, multiply(a, b));

printf("\nEnter the number: \n");
scanf("%d",&x);

printf("Is even : %d", isEven(x));



}
