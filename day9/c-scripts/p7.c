#include <stdio.h>

int main()
{
 int a[5]={5, 10, 15, 20, 25};
 int sum=0;
 for(int i=0; i<5; i++)
	{
	 sum=sum+a[i];
	}
 printf("%d \n", sum);

 int b[10]={1,2,3,4,5,6,7,8,9,10};
 for(int x=0; x<10; x++)
	{
	 if(b[x]%2==0)
		{
		 printf("%d ",b[x]);
		}
	}

}
