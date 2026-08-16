#include <stdio.h>
int main()
{
int a = 0;
int b = 1;
int next;

int terms;
printf("Enter number of terms : ");

scanf("%d", &terms);


for(int i=0; i<terms; i++)
	{
	 printf("%d ", a);
	 next = a+b;
	 a=b;
	 b=next;
	}
}
