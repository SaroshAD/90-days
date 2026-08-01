#include <stdio.h>

int main(){


int a;
int b;

printf("Enter First number : ");
scanf("%d", &a);
printf("Enter the second number : ");
scanf("%d", &b);



printf("\n\n\nAddition : %d + %d = %d. \n\nSubtraction : %d - %d = %d. \n\nMultiplication : %d X %d = %d.\n\n", a, b, a+b, a, b, a-b, a, b, a*b);

printf("Division : %d / %d = %d.\n\nModulus : %d mod %d = %d.\n", a, b, a/b, a, b, a%b);

}
