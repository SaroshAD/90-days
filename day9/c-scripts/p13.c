#include <stdio.h>

int main()
{
char word[] = "Embedded";
int count = 0;

int i= 0;

while(word[i]!='\0')
	{
	 if (word[i]!='a' && word[i] != 'e' && word[i] != 'E' && word[i] != 'i' && word[i] != 'o' && word[i] != 'u' )
		{
		 count++;
		}
	 i++;
	
	}
printf("%d", count);
}
