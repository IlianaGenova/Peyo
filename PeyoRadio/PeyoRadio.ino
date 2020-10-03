void setup() {
  // put your setup code here, to run once:
  pinMode(A3,INPUT_PULLUP);
  //Initiate Serial communication.
  Serial.begin(9600);

}

void loop() {
  // put your main code here, to run repeatedly:
 int a;
  a = analogRead(A3);
  
  Serial.println(a);
  delay(100);
}
