#include <stdio.h>

int main()
{
char word[] = "Embedded";

int size=sizeof(word);

for(int i=size-2; i>=0; i--)

	{

	 printf("%c ", word[i]);

	}

char word_1[] = "Robot";

int count = 0;
int x = 0;

while (word_1[x] != '\0')
{
    count++;
    x++;
}
printf("\nLength = %d\n", x);
}
