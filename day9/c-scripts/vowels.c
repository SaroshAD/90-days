#include <stdio.h>

int main()
{
 char word[100];
 printf("Enter a string : ");
 scanf("%s",word);

 int i=0;
 int vowels=0;
 while(word[i]!='\0')
	{
	 if (word[i]=='A' || word[i]=='a' || word[i]=='E' || word[i]=='e' || word[i]=='I' || word[i]=='i' || word[i]=='O' || word[i]=='o' || word[i]=='U' || word[i]=='u')
	 {
	  vowels++;
	}
	i++;
	}


printf("\nVowels = %d .\n", vowels);

}
