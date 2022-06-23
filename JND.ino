String incomingByte ;    

// Output pin to transistor base
int outPin = 3;


// Variable to hold speed value
int speedVal;

void setup()
{
    // Setup transistor pin as output
    Serial.begin(9600);
    pinMode(outPin, OUTPUT);

}

void loop(){
  if (Serial.available() > 0) {
  incomingByte = Serial.readStringUntil('|'); 
  String text = String(incomingByte);  
  int value = text.toInt();
  Serial.println(value);
  
  analogWrite(outPin, value);
  

//  
//  // Read values from potentiometer
//  speedVal = analogRead(potIn);
//  
//  // Map value to range of 0-255
//  speedVal = map(speedVal, 0, 1023, 0, 255);
//  
//  // Write PWM to transistor
//  analogWrite(outPin, speedVal);
//  
//  delay(20);
//  
}
}
