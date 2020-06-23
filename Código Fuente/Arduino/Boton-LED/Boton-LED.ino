const int button = A3;
const int pin1 = 3;
const int pin2 = 4;
const int pin3 = 5;

int buttonState = 1;

int variable = 500;


void setup() {
  // put your setup code here, to run once:

pinMode(pin1, OUTPUT);
pinMode(pin2, OUTPUT);
pinMode(pin3, OUTPUT);

pinMode(button, INPUT);

}

void loop() {
  // put your main code here, to run repeatedly:

buttonState = digitalRead(button);

if (buttonState == HIGH){
  
    digitalWrite(pin1, HIGH);
  digitalWrite(pin2, HIGH);
  digitalWrite(pin3, HIGH);
  delay(variable);
  
    digitalWrite(pin1, LOW);
  digitalWrite(pin2, LOW);
  digitalWrite(pin3, LOW);
  delay(variable);
  
} else {
 
  digitalWrite(pin1, HIGH);
  delay(200);
  digitalWrite(pin2, HIGH);
  delay(350);
  digitalWrite(pin3, HIGH);
  delay(500);
  
      for ( int i = 0; i <5; i++){
      digitalWrite(pin1, LOW);
      digitalWrite(pin2, LOW);
      digitalWrite(pin3, LOW);
      delay(150);
      
      digitalWrite(pin1, HIGH);
      digitalWrite(pin2, HIGH);
      digitalWrite(pin3, HIGH);
      delay(150);

      digitalWrite(pin1, LOW);
      digitalWrite(pin2, LOW);
      digitalWrite(pin3, LOW);
      delay(150);
      
 
  }

}

}
