#include <stdio.h>

int main()
{

 int number;
 int isPrime=1;
 printf("Enter a number:");

 scanf("%d", &number);

for(int i = 2; i < number; i++)
{
    if(number % i == 0)
    {
	isPrime = 0;
    }

}
if(isPrime == 1)
{
    printf("\nThe number %d is a Prime number.\n",number);
}
else
{
    printf("The number %d is not a Prime number.\n",number);
}
}
