#include <stdio.h>


int arraySum(int a[], int size)
{
 int sum =0;

 for(int i=0; i< size; i++)
	{
	 sum=sum+a[i];
	}
 return sum;
}

int findLargest(int a[], int size)
{
 int largest = a[0];
 for(int x=0; x<size; x++)
	{
	 if(a[x]>largest)
		{
		 largest=a[x];
		}
	}
 return largest;
}

int countEven(int b[], int size)
{
 int count = 0;
 for(int y=0; y<size; y++)
	{
	 if (b[y]%2==0)
		{
		 count++;
		}
	}
 return count;
}


int main()
{
 int a[5] = {10, 20, 30, 40, 50};
 int b[5] = {2, 7, 10, 13, 18};
 printf("\nsum = %d\n", arraySum(a, 5));
 printf("\nlargest = %d\n", findLargest(a, 5));
 printf("\nTotal count of even numbers are %d", countEven(b, 5));
}
