#include <NewPing.h>

#define TRIGGER_PIN 7
#define TRIGGER_PIN_ALT 12
#define ECHO_PIN 8
#define ECHO_PIN_ALT 13
#define MAX_DISTANCE 400

NewPing sonar(TRIGGER_PIN, ECHO_PIN, MAX_DISTANCE); // NewPing setup of pins and maximum distance.
//NewPing sonar(TRIGGER_PIN_ALT, ECHO_PIN_ALT, MAX_DISTANCE_ALT);

void setup() {
   Serial.begin(9600);
}

void loop() {
   delay(2);
   unsigned int uS = sonar.ping_median();
   unsigned int dist = sonar.convert_cm(uS);
   Serial.println("[0," + dist);
}
