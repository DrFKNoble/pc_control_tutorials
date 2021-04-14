byte led {13};

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);

  pinMode(led, OUTPUT);
  digitalWrite(led, HIGH);
  
}

void loop() {
  // put your main code here, to run repeatedly:

  if (Serial.available() >= 2)
  {
    char buffer[3] {};

    Serial.readBytes(buffer, 3);

    int pin {atoi(buffer)};

    switch(pin)
    {
      case 13: {
        digitalWrite(led, !digitalRead(led));
        Serial.println(digitalRead(led));
        break;
      }
    }
   
    
  }

}
