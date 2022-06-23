String incomingByte ;    

// Output pin to transistor base
int mag1 = 3;
int mag2 = 9;


// Variable to hold speed value
int speedVal;

void setup()
{
    // Setup transistor pin as output
    Serial.begin(9600);
    pinMode(mag1, OUTPUT);
    pinMode(mag2, OUTPUT);

}

void loop(){
  if (Serial.available() > 0) {
  incomingByte = Serial.readStringUntil('\n'); 
  String text = String(incomingByte);
  Serial.println(text);
  
  int value = text.toInt();
  
  analogWrite(mag1, value);
  analogWrite(mag2, value);

  }
}
