
#include <stdio.h>

int main()
{
	float balance;
	
	printf("Enter Your Bank Balance : ");
	scanf("%f", &balance);
	
	if (balance >=10000)
	{
		printf("Premiun Account\n");
	}
	else if (balance >= 5000)
	{
		printf("Standard Account \n");
	}
	else if (balance >= 1000)
	{
		printf("Basic Account \n");
	}
	else
	{
		printf("Low Balance\n");
	}

	printf("\n\nYour Current Balance is %.1f .", balance);
	
	float withdraw;
	printf("\n\nEnter the amount to withdraw :");
	scanf("%f",&withdraw);
	
	if (withdraw <= 0)
	{
		printf("\nEntered amount is less than 0!\n");
	}
	else if (withdraw>balance)
	{
		printf("\nInsufficient balance\n");
	}

	else if (withdraw< balance)
	{
		printf("\n%.1f Cash Withdrawn !.\nNow Your current balance is %.1f rupees.\n", withdraw, balance-withdraw);
	}

	return 0;
}

