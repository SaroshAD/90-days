#include <stdio.h> 

int main()
{

printf("Printing number  from 10 - 1\n");
 int i =10;
 do
	{
	 printf("%d ", i);
	 i--;
	}
 while(i>=1);


printf("\nprinting addition of numbers from 1-10\n");
 int x=1;
 int sum=0;
 do
	{
	 sum=sum+x;
	 x++;
	}
 while(x<=10);
 
 printf("%d", sum);

printf("\nprinting even numbers\n");

int y=1;
do
	{
	 if (y%2==0)
		{
		printf("%d ", y);
		}
	 y++;
	}
while(y<=20);
}

