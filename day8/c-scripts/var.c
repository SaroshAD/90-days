#include <stdio.h>

int main(){


int age = 23;
float height = 175.5;
char grade = 'A' ;
int a;
int b;

printf("Your age is %d\n", age);

printf("your height is %.1f\n", height);

printf("Your grade is %c \n", grade);

printf("Enter furst number A :\n");
scanf("%d", &a);

printf("Enetr Second number B :\n");
scanf("%d", &b);

printf("the first number is A = %d\n", a);

printf("the second number is B = %d\n", b);

printf("Below are the arithmatic operations of 2 numbers:\n");

printf("The addition is %d + %d = %d\n ", a, b, a+b);

printf("The subtraction is %d - %d = %d\n", a, b, a-b);

printf("The multiplication is %d X %d = %d\n", a, b, a*b);

printf("the divisiopn is %d / %d = %.2f\n", a, b, (float)a/b);

return 0;
}


