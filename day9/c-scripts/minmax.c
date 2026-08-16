#include <stdio.h>

int findMin(int a[], int size)
{

 int min=a[0];
 int i=0;
 while(i<size)
	{
	 if(min>a[i])
		{
		 min=a[i];
		}
	i++;
	}

return min;
}

int findMax(int a[], int size)
{

 int max=a[0];
 int i=0;
 while(i<size)
	{
	 if(max<a[i])
		{
		 max=a[i];
		}
	i++;
	}

return max;
}


int main()
{

 int a[] = {10, 4, 25, 7, 2, 18};


 int min=findMin(a, 6);
 int max= findMax(a, 6);


printf("\nMinimum = %d \n\nMaximum = %d \n", min, max);

}


