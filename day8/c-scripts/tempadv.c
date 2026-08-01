
#include <stdio.h>

int main()
{
	float temp;
	
	printf("Enter the Temperature : ");
	scanf("%f", &temp);
	
	if (temp >=40)
	{
		printf("Very Hot Day!\n");
	}
	else if (temp>=30)
	{
		printf("Hot Weather \n");
	}
	else if (temp>=20)
	{
		printf("Pleasant Weather \n");
	}
	else
	{
		printf("cold Weather \n");
	}
}


