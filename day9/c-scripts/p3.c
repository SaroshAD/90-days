#include <stdio.h>

int main()
{
 int i =1;
 while(i<=100)
	{
	 if(i%10==0)
		{
		  printf("%d ", i);
		}
	 i++;
	}

 int x=1;
 int sum=0;
 while(x<=20)
	{
	 if (x%2==0)
		{
		  sum=sum+x;
		}
	 x++;
	}
printf("\nsum = %d\n",sum);


int y = 5;
int result=1;
while (y>=1)
{
	result=result*y;
	y--;
}
printf("\nfactorial of 5 is %d ", result);


}
