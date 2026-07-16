#include <Servo.h>   //first include the servo library

Servo myservo;   //create servo object to control a servo
int pot_pin = A0; //analog pin to which potentiometer is connected
void setup()
{
  myservo.attach(9);  //attach the servo to a PWM pin 9 on ardyuino
  pinMode(pot_pin, INPUT); //set the potentiometer pin as input
}

void loop()
{
  int pot_value = analogRead(pot_pin); //read the potentiometer value
  int angle = map(pot_value, 0, 1023, 0, 180); //map the potentiometer value to servo angle
  myservo.write(angle); //set the servo to the mapped angle
  delay(15); //wait for the servo to reach the position
}