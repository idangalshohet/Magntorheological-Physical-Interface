/*
  Transistor Switch Demonstration
  transistor-switch-demo.ino
  Demonstrates use of BJT to switch 6-volt incandescent lamp
  Uses pushbutton for input

  DroneBot Workshop 2019
  https://dronebotworkshop.com
*/

// Output pin to transistor base
int outPin = 5;

// Input pin from pushbutton
int buttonPin = 3;

// Pushbutton value
int buttonVal;

void setup()
{
    // Setup transistor pin as output
    pinMode(outPin, OUTPUT);
    
    // Setup pushbutton pin as input
    pinMode(buttonPin, INPUT);
    
    // Make sure transistor is off
    digitalWrite(outPin, LOW);

}

void loop()
{

  //Read pushbutton input
  buttonVal = digitalRead(buttonPin);
  
  //Check button position
  
  if (buttonVal == HIGH) {
    // Button is not pressed, turn off lamp
    digitalWrite(outPin, LOW);
    delay(20);
  } else {
    // Button is pressed, turn on lamp for 5 seconds
    digitalWrite(outPin, HIGH);
    delay(5000);
    digitalWrite(outPin, LOW);
    }
    
  
  
}
