
int led = 9;  //it is connected to PWM pin 9 of arduino 
void setup()
{
  pinMode(led, OUTPUT);
}

void loop()
{
  for (int i=0; i<=255; i++)   //for the fading in of led while turning on 
  {
   analogWrite(led , i);
   delay(8);
  }
  for (int i=255; i>=0; i--)     //for the fading off of led while turning off 
  {
    analogWrite(led, i);
    delay(8);
  }
}