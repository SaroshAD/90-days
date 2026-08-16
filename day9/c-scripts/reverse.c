#include <stdio.h> 

int main()
{

char word[100];

printf("Enter a string : ");
scanf("%s",word);
int length=0;
for(int i=0; word[i]!='\0'; i++)
	{ 
	 length++;
	}

for (int x=length-1; x>=0; x--)
	{
	 printf("%c ",word[x]);
	}
}
