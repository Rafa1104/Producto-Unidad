
#include <Wire.h>

int receivedValue = 0;
int LEDPin = 13;
int buttonPin = 10;
int isSelected = false;
int buttonState = 0;

void setup() {
  
  Wire.begin(); 
  Serial.begin(9600);

  
  pinMode(LEDPin, OUTPUT);
  pinMode(buttonPin, INPUT);
}

void loop() {

  
  Wire.requestFrom(9, 1);

  while (Wire.available()) { 
    receivedValue = Wire.read(); 
    Serial.println(receivedValue);        
  }

  
  buttonState = digitalRead(buttonPin);
  if(buttonState == HIGH){
    isSelected = !isSelected;
    delay(500);
  }

  
  if(receivedValue == 1){
    digitalWrite(LEDPin, HIGH);
  } else {
    digitalWrite(LEDPin, LOW);
  }

   
  Wire.beginTransmission(9); 
  Wire.write(isSelected);              
  Wire.endTransmission();    
  delay(100);
}
