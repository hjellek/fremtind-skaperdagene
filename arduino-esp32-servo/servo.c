// Importer riktig bibliotek for brikken du bruker
// Begge kan installeres via Library Manager i Arduino IDE
// https://docs.arduino.cc/software/ide-v1/tutorials/installing-libraries/
#include <ESP32Servo.h>
// #include <Servo.h>

#define SERVO_PIN 26 // ESP32 pin GPIO26 connected to servo motor
#define POT_PIN 12 // Pin for tilkobling av potentiometer

int val;
Servo servoMotor;

void setup() {
    pinMode(POT_PIN, INPUT);
    servoMotor.attach(SERVO_PIN);  // attaches the servo on ESP32 pin
}

void loop() {
    servoWithPotentiometer();
}

void servoWithPotentiometer() {
  val = analogRead(potpin);            // reads the value of the potentiometer (value between 0 and 4096)
  val = map(val, 0, 4095, 0, 180);     // scale it to use it with the servo (value between 0 and 180)
  // Endre denne     ^    til 1023 på vanlig Arduino
  servoMotor.write(180-val);                  // sets the servo position according to the scaled value
  delay(15);    
}

// Se koblingsdiagram og veiledning her: https://esp32io.com/tutorials/esp32-servo-motor