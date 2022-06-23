String incomingByte ;

//values range from 0 to 255

int trial = 0; //which round is it
int actuator = 0; //which actuator is being used
int portlist[2] = {3, 9};   //order of pins

int b1val[18] = {231, 226, 217, 222, 237, 221, 215, 223, 244, 236, 229, 249, 243, 217, 230, 236, 221, 237};
int b2val[18] = {217, 217, 222, 246, 238, 247, 232, 227, 249, 233, 232, 224, 235, 243, 244, 244, 235, 229};
int b3val[18] = {225, 234, 227, 221, 228, 216, 242, 226, 226, 245, 241, 240, 248, 247, 245, 233, 223, 246};
int b4val[18] = {239, 226, 224, 246, 235, 239, 229, 215, 233, 234, 248, 234, 232, 240, 246, 225, 240, 240};
int b5val[18] = {230, 248, 218, 245, 227, 218, 230, 234, 229, 218, 228, 232, 216, 215, 239, 237, 238, 230};
int b6val[18] = {246, 229, 250, 232, 226, 233, 227, 230, 243, 247, 220, 221, 238, 231, 232, 223, 249, 218};
int b7val[18] = {229, 223, 216, 227, 232, 224, 236, 218, 228, 226, 229, 239, 250, 248, 234, 221, 227, 234};
int b8val[18] = {219, 222, 222, 215, 216, 235, 223, 237, 226, 236, 232, 241, 227, 228, 248, 217, 245, 244};
int b9val[18] = {217, 217, 223, 243, 249, 238, 230, 225, 231, 238, 239, 243, 226, 219, 245, 235, 234, 233};

void setup() {
  Serial.begin(9600);

  pinMode(3, OUTPUT);
  pinMode(5, OUTPUT);
  pinMode(9, OUTPUT);
  pinMode(10, OUTPUT);
}

void loop() {
  if (Serial.available() > 0) {
    incomingByte = Serial.readStringUntil('|');
    actuator = 0;
    String text = String(incomingByte);
    Serial.println(text);

    if (text.indexOf("starting") > -1) {
      Serial.println("PROGRAM STARTING ");
      trial = 0;
      actuator = 0;
    }

    if (text.indexOf("round") > -1) { //finds which round of information to get
      if (text.indexOf(" 1 ") > -1) {
        trial = 0;
      } if (text.indexOf(" 2 ") > -1) {
        trial = 1;
      } if (text.indexOf(" 3 ") > -1) {
        trial = 2;
      } if (text.indexOf(" 4 ") > -1) {
        trial = 3;
      } if (text.indexOf(" 5 ") > -1) {
        trial = 4;
      } if (text.indexOf(" 6 ") > -1) {
        trial = 5;
      } if (text.indexOf(" 7 ") > -1) {
        trial = 6;
      } if (text.indexOf(" 8 ") > -1) {
        trial = 7;
      } if (text.indexOf(" 9 ") > -1) {
        trial = 8;
      } if (text.indexOf(" 10 ") > -1) {
        trial = 9;
      } if (text.indexOf(" 11 ") > -1) {
        trial = 10;
      } if (text.indexOf(" 12 ") > -1) {
        trial = 11;
      } if (text.indexOf(" 13 ") > -1) {
        trial = 12;
      } if (text.indexOf(" 14 ") > -1) {
        trial = 13;
      } if (text.indexOf(" 15 ") > -1) {
        trial = 14;
      } if (text.indexOf(" 16 ") > -1) {
        trial = 15;
      } if (text.indexOf(" 17 ") > -1) {
        trial = 16;
      } if (text.indexOf(" 18 ") > -1) {
        trial = 17;
      }
      Serial.println("trial");
      Serial.print(trial);
    }

    if (trial < 19) {
      if (text.indexOf("b1") > -1) {
        Serial.println("b1");
        analogWrite(portlist[actuator], b1val[trial]);
        actuator += 1;
      } if (text.indexOf("b2") > -1) {
        Serial.println("b2");
        analogWrite(portlist[actuator], b2val[trial]);
        actuator += 1;
      } if (text.indexOf("b3") > -1) {
        Serial.println("b3");
        analogWrite(portlist[actuator], b3val[trial]);
        actuator += 1;
      } if (text.indexOf("b4") > -1) {
        Serial.println("b4");
        analogWrite(portlist[actuator], b4val[trial]);
        actuator += 1;
      } if (text.indexOf("b5") > -1) {
        Serial.println("b5");
        analogWrite(portlist[actuator], b5val[trial]);
        actuator += 1;
      } if (text.indexOf("b6") > -1) {
        Serial.println("b6");
        analogWrite(portlist[actuator], b6val[trial]);
        actuator += 1;
      } if (text.indexOf("b7") > -1) {
        Serial.println("b7");
        analogWrite(portlist[actuator], b7val[trial]);
        actuator += 1;
      } if (text.indexOf("b8") > -1) {
        Serial.println("b8");
        analogWrite(portlist[actuator], b8val[trial]);
        actuator += 1;
      } if (text.indexOf("b9") > -1) {
        Serial.println("b9");
        analogWrite(portlist[actuator], b9val[trial]);
        actuator += 1;
      } else {
        //    Serial.println("not found");
        //    continue;
      }

    }
  }
}
