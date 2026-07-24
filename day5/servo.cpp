#include <Servo.h>   //first include the servo library
Servo myservo;   //create servo object to control a servo

void setup()
{
  myservo.attach(9);  //attach the servo to a PWM pin 9 on ardyuino
}

void loop()
{
  myservo.write(0); //set the servo to 0 degree
  delay(500); 
  myservo.write(90); //set the servo to 90 degree
  delay(500);
  myservo.write(180); //set the servo to 180 degree
  delay(500);
}