#define led_pin 1
#define FALSE 0
#define TRUE 1

void setup() {
  pinMode(led_pin, OUTPUT);
  Serial.begin(9600);
}
void loop() {
  while (Serial.available() > 0){
    int value = Serial.read();
    if (value == FALSE){
      digitalWrite(led_pin, LOW);
    }
    else if (value == TRUE){
      digitalWrite(led_pin, HIGH);
    }
  }
}
