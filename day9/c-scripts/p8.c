#include <stdio.h>

int main()
{
 int a[5]={4, 8, 12, 16, 20};
 int largest=a[0];
 for(int i=1; i<5; i++)
	{
	 if(a[i]>largest)
		{
		 largest=a[i];
		}
	}
 printf("%d \n", largest);

 int b[5]={10, 15, 20, 25, 30};
 int count=0;
 for(int x=0; x<5; x++)
	{
	 if(b[x]>20)
		{
		 count++;
		}
	}
 printf("%d ", count);
}
