
#include <stdio.h>

int main()
{
	float temp;
	
	printf("Enter the Temperature : ");
	scanf("%f", &temp);
	
	if (temp >=40)
	{
		printf("Hot Day!\n");
	}
	else
	{
		printf("Pleasant Weather \n");
	}
}

