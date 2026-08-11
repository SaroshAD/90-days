#include <stdio.h> 

int main()
{

printf("Sum of Odd numbers\n");
 int i =1;
 int sum =0;
 do
	{
	 if(i%2!=0)
	 {
		sum=sum+i;
	 }
	 i++;
	}
 while(i<=10);
 printf("%d\n", sum);

printf("\nmultiplication table of 7\n");
 int t=7;
 int x=1;
 do
	{
	 printf("%d * %d = %d\n", t, x, t*x);
	 x++;
	}
 while(x<=10);
 

printf("\ncount digits\n");

int y=58342;
int count=0;
do
	{
	y=y/10;
	count++;
	}
while(y>0);



printf("\n%d ", count);
}
