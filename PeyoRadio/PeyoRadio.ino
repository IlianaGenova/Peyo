#define midTransition 192
#define topTransition 255
int volumePin = A4;
int LEDpinRed = 9;
int LEDpinGreen = 10;
int LEDpinBlue = 11;
int dly = 5;
void setup() {
  // put your setup code here, to run once:
  pinMode(volumePin,INPUT_PULLUP);
  pinMode(LEDpinRed, OUTPUT);
  pinMode(LEDpinGreen, OUTPUT);
  pinMode(LEDpinBlue, OUTPUT);
  //Initiate Serial communication.
  Serial.begin(57600);
  //initial color set
  digitalWrite(LEDpinRed,LOW);
  digitalWrite(LEDpinGreen,LOW);
  digitalWrite(LEDpinBlue,LOW);
}

void loop() {
  // put your main code here, to run repeatedly:
  //Serial.println(analogRead(volumePin));
//RED
  for(int i=midTransition; i<=topTransition; i++){
    analogWrite(LEDpinRed, i);
    Serial.println(analogRead(volumePin));
    Serial.flush();
    delay(dly);
  }
  for(int i=topTransition; i>=midTransition; i--){
    analogWrite(LEDpinRed, i);
    Serial.println(analogRead(volumePin));
    Serial.flush();
    delay(dly);
  }
//Yellow
  for(int i=midTransition; i>=0; i--){
    analogWrite(LEDpinRed, i);
    analogWrite(LEDpinGreen, midTransition-i);
    Serial.println(analogRead(volumePin));
    Serial.flush();
    delay(dly);
  }
//Green
  for(int i=midTransition; i<=topTransition; i++){
    analogWrite(LEDpinGreen, i);
    Serial.println(analogRead(volumePin));
    Serial.flush();
    delay(dly);
  }
  for(int i=topTransition; i>=midTransition; i--){
    analogWrite(LEDpinGreen, i);
    Serial.println(analogRead(volumePin));
    delay(dly);
  }
//Cyan
for(int i=midTransition; i>=0; i--){
    analogWrite(LEDpinGreen, i);
    analogWrite(LEDpinBlue, midTransition-i);
    Serial.println(analogRead(volumePin));
    delay(dly);
  }
//Blue
  for(int i=midTransition; i<=topTransition; i++){
    analogWrite(LEDpinBlue, i);
    Serial.println(analogRead(volumePin));
    Serial.flush();
    delay(dly);
  }
  for(int i=topTransition; i>=midTransition; i--){
    analogWrite(LEDpinBlue, i);
    Serial.println(analogRead(volumePin));
    Serial.flush();
    delay(dly);
  }
//Purple
  for(int i=midTransition; i>=0; i--){
    analogWrite(LEDpinBlue, i);
    analogWrite(LEDpinRed, midTransition-i);
    Serial.println(analogRead(volumePin));
    Serial.flush();
    delay(dly);
  }
}
