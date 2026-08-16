#include <stdio.h>

int array(int a[], int size, int target)
{

 int found=0;

 for(int i = 0; i < size; i++)
	{
   	 if(a[i] == target)
 		{
        	 found =1;
    		}
	}
 return found;
}

int main()
{

 int a[] ={5, 8, 12, 20, 30};

 int target;
 printf("Enter the number to search : ");

 scanf("%d" , &target);

int found =  array(a, 5, target);

 if (found==0)
	{
	 printf("%d not found in the array\n", target);
	}
 else
	{
	 printf("%d found in the array\n", target);
	}
}
