String incomingByte ;    

//values range from 0 to 255

int trial = 0; //which round is it
int actuator = 0; //which actuator is being used
int portlist[4] = {3, 5, 9, 10};   //order of pins 

int b1val[7] = {200, 10, 50, 120, 0, 50, 255};
int b2val[7] = {255, 10, 50, 120, 0, 50, 0};
int b3val[7] = {0, 255, 50, 120, 0, 50, 255};
int b4val[7] = {10, 100, 50, 120, 0, 20, 70};
int b5val[7] = {0, 10, 50, 0, 0, 50, 30};
int b6val[7] = {70, 255, 50, 120, 0, 50, 255};
int b7val[7] = {0, 10, 50, 120, 0, 50, 0};
int b8val[7] = {80, 80, 50, 10, 50, 50, 255};
int b9val[7] = {0, 10, 80, 120, 0, 50, 100};
 
void setup() {
  Serial.begin(9600);
    
  pinMode(3,OUTPUT);
  pinMode(5,OUTPUT);
  pinMode(9,OUTPUT);
  pinMode(10,OUTPUT);
}

void loop() {  
  if (Serial.available() > 0) {
  incomingByte = Serial.readStringUntil('|'); 
  actuator = 0; 
  String text = String(incomingByte);  
  Serial.println(text);

  if(text.indexOf("starting") > -1) {
    Serial.println("PROGRAM STARTING ");
    trial = 0;
    actuator = 0;
  }
  
  if(text.indexOf("round") > -1) {  //finds which round of information to get
    if(text.indexOf(" 1 ") > -1) {
      trial = 0;
    } if(text.indexOf(" 2 ") > -1) {
      trial = 1; 
    } if(text.indexOf(" 3 ") > -1) {
      trial = 2;
    } if(text.indexOf(" 4 ") > -1) {
      trial = 3;
    } if(text.indexOf(" 5 ") > -1) {
      trial = 4;
    } if(text.indexOf(" 6 ") > -1) {
      trial = 5;
    } if(text.indexOf(" 7 ") > -1) {
      trial = 7;
    }
    Serial.println("trial");
    Serial.print(trial);
  }  

  if (trial < 8) {  
  if(text.indexOf("b1") > -1) {
    Serial.println("b1");
    analogWrite(portlist[actuator],b1val[trial]);
    actuator += 1; 
  } if (text.indexOf("b2") > -1) {
    Serial.println("b2");
    analogWrite(portlist[actuator],b2val[trial]);
    actuator += 1; 
  } if (text.indexOf("b3") > -1) {
    Serial.println("b3");
    analogWrite(portlist[actuator],b3val[trial]);
    actuator += 1; 
  } if (text.indexOf("b4") > -1) {
    Serial.println("b4");
    analogWrite(portlist[actuator],b4val[trial]);
    actuator += 1; 
  } if (text.indexOf("b5") > -1) {
    Serial.println("b5");
    analogWrite(portlist[actuator],b5val[trial]);
    actuator += 1; 
  } if (text.indexOf("b6") > -1) {
    Serial.println("b6");
    analogWrite(portlist[actuator],b6val[trial]);
    actuator += 1; 
  } if (text.indexOf("b7") > -1) {
    Serial.println("b7");
    analogWrite(portlist[actuator],b7val[trial]);
    actuator += 1; 
  } if (text.indexOf("b8") > -1) {
    Serial.println("b8");
    analogWrite(portlist[actuator],b8val[trial]);
    actuator += 1; 
  } if (text.indexOf("b9") > -1) {
    Serial.println("b9");
    analogWrite(portlist[actuator],b9val[trial]);
    actuator += 1; 
  } else {
//    Serial.println("not found");
//    continue;
  }

  }
  } 
}
