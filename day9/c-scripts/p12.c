#include <stdio.h>

int main()
{
char word[] = "Robot";
int count = 0;

int i= 0;

while(word[i]!='\0')
	{
	 if (word[i]=='o')
		{
		 count++;
		}
	 i++;
	
	}
printf("The character o has been used %d times.\n", count);

char word1[] = "Arduino";

int x =0;
int counts=0;
while (word1[x]!='\0')
	{
	 if (word1[x] == 'A' || word1[x] == 'a' || word1[x] == 'e'|| word1[x] == 'i' || word1[x] == 'o' || word1[x] == 'u')
		{

		 counts++;
		}
	 x++;
	}
printf("\n the vowel used are %d.\n", counts);
}
