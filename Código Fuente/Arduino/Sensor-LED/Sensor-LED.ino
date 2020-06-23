int sensor = A5;
int led_1= 3;
int led_2 = 5;
int led_3 = 6;


int Sensor_Value = 0;


void setup()
{
  
  
  pinMode(led_1, OUTPUT);
  pinMode(led_2, OUTPUT);
  pinMode(led_3, OUTPUT);
 
  
  pinMode(sensor, INPUT);
  Serial.begin(9600);
}

void loop()
{
  Sensor_Value = analogRead(A5);
  Serial.println(Sensor_Value);
  
  analogWrite(led_1, map(Sensor_Value, 0, 1023, 0, 255));
  analogWrite(led_2, map(Sensor_Value, 0, 1023, 0, 255));
  analogWrite(led_3, map(Sensor_Value, 0, 1023, 0, 255));
  delay(100);
  
  
  
  
}
