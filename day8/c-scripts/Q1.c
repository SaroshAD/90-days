#include <stdio.h>

int main(){

char name[50];
int age;
int height;
char blood[4];
printf("Enter Your name :  ");
scanf("%s", name);
printf("Enter Your Age :  ");
scanf("%d", &age);
printf("Enter Your height :  ");
scanf("%d", &height);
printf("Enter Your blood-group :  ");
scanf("%s", blood);
printf("\n\n\nHello, %s\n", name);
printf("Age : %d \nHeight : %d \nBlood-group : %s\n", age, height, blood);
}
