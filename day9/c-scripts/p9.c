#include <stdio.h>

int main()
{
 int a[5]={25, 10, 40, 5, 30};
 int smallest=a[0];
 for(int i=1; i<5; i++)
	{
	 if(a[i]<smallest)
		{
		 smallest=a[i];
		}
	}
 printf("%d \n", smallest);

 int b[5]={10, 20, 30, 40, 50};
 int sum=0;
 int count=0;
 for(int x=0; x<5; x++)
	{
	 sum=sum+b[x];
	 count++;
	}
 printf("%d ",sum/count);


 int c[6]={10, 20, 30, 40, 50, 60};
 int num;
 int found=0;

 printf("\n\nEnter the number to find in list: ");
 scanf("%d",&num);
 for(int y=0; y<6; y++)
	{
	 if (num==c[y])
		{
		 found++;
		}
	}
if(found==1)
	{
	 printf("Element found.");
	}
else
	{
	 printf("element not found");
	}
}
