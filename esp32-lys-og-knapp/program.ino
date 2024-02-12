#define BUTTON_PIN 12
#define LED_PIN 10

int ledState = LOW;
int previousSwitchState = LOW;

void setup() {
    Serial.begin(9600);
    pinMode(BUTTON_PIN, INPUT_PULLDOWN);
    pinMode(LED_PIN, OUTPUT);
}

void loop() {
    int currentState = digitalRead(BUTTON_PIN);

    if (currentState == HIGH && previousSwitchState == LOW) {
        if (ledState == HIGH) {
            ledState = LOW;
        } else {
            ledState = HIGH;
        }
    }

    digitalWrite(LED_PIN, ledState);
    previousSwitchState = currentState;
}
