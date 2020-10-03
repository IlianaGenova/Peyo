int volumePin = A3;
int LEDpinRed = 9;
int LEDpinGreen = 10;
int LEDpinBlue = 11;
int dly = 8;
void setup() {
  // put your setup code here, to run once:
  pinMode(volumePin,INPUT_PULLUP);
  pinMode(LEDpinRed, OUTPUT);
  pinMode(LEDpinGreen, OUTPUT);
  pinMode(LEDpinBlue, OUTPUT);
  //Initiate Serial communication.
  Serial.begin(9600);
  digitalWrite(LEDpinRed,LOW);
  digitalWrite(LEDpinGreen,LOW);
  digitalWrite(LEDpinBlue,LOW);
}

void loop() {
  // put your main code here, to run repeatedly:
  //Serial.println(analogRead(volumePin));
//RED
  for(int i=192; i<=255; i++){
    analogWrite(LEDpinRed, i);
    Serial.println(analogRead(volumePin));
    delay(dly);
  }
  for(int i=255; i>=192; i--){
    analogWrite(LEDpinRed, i);
    Serial.println(analogRead(volumePin));
    delay(dly);
  }
//Yellow
  for(int i=192; i>=0; i--){
    analogWrite(LEDpinRed, i);
    analogWrite(LEDpinGreen, 192-i);
    Serial.println(analogRead(volumePin));
    delay(dly);
  }
//Green
  for(int i=192; i<=255; i++){
    analogWrite(LEDpinGreen, i);
    Serial.println(analogRead(volumePin));
    delay(dly);
  }
  for(int i=255; i>=192; i--){
    analogWrite(LEDpinGreen, i);
    Serial.println(analogRead(volumePin));
    delay(dly);
  }
//Cyan
for(int i=192; i>=0; i--){
    analogWrite(LEDpinGreen, i);
    analogWrite(LEDpinBlue, 192-i);
    Serial.println(analogRead(volumePin));
    delay(dly);
  }
//Blue
  for(int i=192; i<=255; i++){
    analogWrite(LEDpinBlue, i);
    Serial.println(analogRead(volumePin));
    delay(dly);
  }
  for(int i=255; i>=192; i--){
    analogWrite(LEDpinBlue, i);
    Serial.println(analogRead(volumePin));
    delay(dly);
  }
//Purple
  for(int i=192; i>=0; i--){
    analogWrite(LEDpinBlue, i);
    analogWrite(LEDpinRed, 192-i);
    Serial.println(analogRead(volumePin));
    delay(dly);
  }
}
