
#include <Wire.h>

int LED = 13;
bool valueReceived;
int isOn = 0; 

void setup() {
  
  Serial.begin(9600);
  
  pinMode (LED, OUTPUT);
  
  Wire.begin(9); 
  
  Wire.onReceive(receiveEvent);
  
  Wire.onRequest(requestEvent);
}

void receiveEvent(bool bytes) {
  
  valueReceived = Wire.read();
   
  Serial.println(valueReceived);
  
  if(valueReceived){
    isOn = 1;
  }
  else{
    isOn = 0;
  }
}

void requestEvent(){
  
  Wire.write(isOn);
}

void loop() {
  
  if(isOn){
    digitalWrite(LED, HIGH);
  }
  else{
    digitalWrite(LED, LOW);
  }
}
