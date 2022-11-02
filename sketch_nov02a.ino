#define DATA_PIN 2
#define DATA_LEVEL LOW
#define SPACE_LEVEL HIGH
#define DATA true
#define SPACE false
#define DASH_DURATION 3 
#define DOT_DURATION 1
#define TU 100

long start_data, start_space;
long duration[20];
bool color[20];
int index = 0;
int previos = SPACE_LEVEL;
String CODES[] = {".-", "--.."};
char LETTERS[] = {'A', 'Z'};
int NLETTRERS = 2;

void setup() { 
   pinMode(DATA_PIN, INPUT);
   
}

void loop() {
    fill_array();
    decode_letter();
    Serial.begin(9600);
  }

void decode_letter(){
  for(int i=0; i<index; i++){
      if (duration[i] == DASH_DURATION and color[i] == SPACE){
        String code = "";
        for (int j = 0; j<i; j++){
          if(duration[j] == DASH_DURATION and color[j] == DATA){
             code += '-';
          }
          if(duration[j] == DASH_DURATION and color[j] == DATA){
             code += '.';
          }
          duration[j] = 0;
        }
        duration[i] = 0;
        for (int iletter = 0; iletter < NLETTRERS; iletter++){
          if (code == CODES[iletter]){
            Serial.println(LETTERS[iletter]);
          }
        }
      }
    }
    index = 0;
}
void fill_array(){
  int current = digitalRead(DATA_PIN);
  if (current == DATA_LEVEL and previos == SPACE_LEVEL){
    start_data = millis();
    duration[index] = (millis() - start_space + 0.5 * TU) / TU;
    color[index] = SPACE;
    index++;
  }
  if (current == SPACE_LEVEL and previos == DATA_LEVEL){
    start_data = millis();
    duration[index] = (millis() - start_data + 0.5 * TU) / TU;
    color[index] = DATA;
    index++;  
}
  previos = current;
}
