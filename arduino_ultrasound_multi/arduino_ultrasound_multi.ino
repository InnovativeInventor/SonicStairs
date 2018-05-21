#include <NewPing.h>
#include <LiquidCrystal.h>

#define TRIGGER_PIN 7
#define TRIGGER_PIN_ALT 10
#define TRIGGER_PIN_ALT_1 6
#define TRIGGER_PIN_ALT_2 3


#define ECHO_PIN 8
#define ECHO_PIN_ALT 9
#define ECHO_PIN_ALT_1 5
#define ECHO_PIN_ALT_2 2

#define MAX_DISTANCE 800
#define SONAR_NUM 4

LiquidCrystal lcd(A2,A1,A5,A4,A3,A0);
//NewPing sonar(TRIGGER_PIN, ECHO_PIN, MAX_DISTANCE); // NewPing setup of pins and maximum distance.
//NewPing sonar(TRIGGER_PIN_ALT, ECHO_PIN_ALT, MAX_DISTANCE_ALT);


NewPing sonar[SONAR_NUM] = {   // Sensor object array.
  NewPing(TRIGGER_PIN, ECHO_PIN, MAX_DISTANCE), // Each sensor's trigger pin, echo pin, and max distance to ping.
  NewPing(TRIGGER_PIN_ALT, ECHO_PIN_ALT, MAX_DISTANCE),
  NewPing(TRIGGER_PIN_ALT_1, ECHO_PIN_ALT_1, MAX_DISTANCE),
  NewPing(TRIGGER_PIN_ALT_2, ECHO_PIN_ALT_2, MAX_DISTANCE)
};
int i = 0;

void setup() {
   Serial.begin(9600);
   lcd.begin(16, 2);
   lcd.clear();
}
 
void loop() {
   delay(10);
   unsigned int uS = sonar[i%SONAR_NUM].ping_median();
   unsigned int dist = sonar[i%SONAR_NUM].convert_cm(uS);

   String stringSerial = '[' + String(i%SONAR_NUM) + ',' + String(dist) + ']';
   Serial.println(stringSerial);
   
   lcd.clear();
   if ( i%SONAR_NUM == 0 )
   {
     lcd.setCursor(0,0);
     lcd.print(dist);
   } else if( i%SONAR_NUM == 1 ) {
      lcd.setCursor(4,0);
      lcd.print(dist);
   } else if( i%SONAR_NUM == 2 ) {
      lcd.setCursor(9,0);
      lcd.print(dist);
   } else if( i%SONAR_NUM == 3 ) {
      lcd.setCursor(12,0);
      lcd.print(dist);
   } else {
      lcd.setCursor(0,0);
      lcd.print("Error");
      exit(1);
   }
   
   lcd.setCursor(0,1);
   lcd.print("Made by Max Fan");

   i+=1;
}
