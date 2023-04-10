#include <SPI.h>
#include <MD_MAX72xx.h>

// max7219 stuff

#define MAX_DEVICES	1
#define HARDWARE_TYPE MD_MAX72XX::GENERIC_HW
#define CLK_PIN   18  
#define DATA_PIN  23  
#define CS_PIN    5 
MD_MAX72XX mx = MD_MAX72XX(HARDWARE_TYPE, CS_PIN, MAX_DEVICES);

// initial delay time bewteem columns, influences the "width" of a column
// XXX needs to be calibrated on every direction switch
int  delayTime = 90; 

// stepper pin defition
const int stepPin = 21; 
const int dirPin = 22;

// limits switches
// XXX need seperate pins for left/right, to be able to do "column count"
const int limitPin = 12;

// setup pwm for stepper step generation
const int PWMFreq = 600; /* Hz */
const int PWMChannel = 0;
const int PWMResolution = 10;
const int MAX_DUTY_CYCLE = (int)(pow(2, PWMResolution) - 1);

// initial direction
int dirState = LOW;
int lastNewDir = HIGH;

void checkLimits() {
  byte limitState = digitalRead(limitPin);
  int newDir;
  if (limitState == HIGH) {
    if (dirState == LOW) { 
      newDir = HIGH;
    } else {
      newDir = LOW;
    }
    digitalWrite(dirPin, newDir);
    dirState = newDir;
  }
}

#define BITMAP_SIZE 8

const uint8_t bitmap[BITMAP_SIZE][8] = {
  { 0x88, 0x88, 0x88, 0x88, 0x88, 0x88, 0x88, 0x88 },
  { 0x88, 0x88, 0x88, 0x88, 0x88, 0x88, 0x88, 0x88 },
  { 0x44, 0x44, 0x44, 0x44, 0x44, 0x44, 0x44, 0x44 },
  { 0x44, 0x44, 0x44, 0x44, 0x44, 0x44, 0x44, 0x44 },
  { 0xbb, 0xbb, 0xbb, 0xbb, 0xbb, 0xbb, 0xbb, 0xbb },
  { 0xbb, 0xbb, 0xbb, 0xbb, 0xbb, 0xbb, 0xbb, 0xbb },
  { 0x22, 0x22, 0x22, 0x22, 0x22, 0x22, 0x22, 0x22 },
  { 0x22, 0x22, 0x22, 0x22, 0x22, 0x22, 0x22, 0x22 },
};


void draw_bitmap() {
  // do we need clear here?
  mx.clear();
  for (uint8_t j=0; j<BITMAP_SIZE; j++) {
    for (uint8_t i=0; i<8; i++) {
      mx.setColumn(i, bitmap[j][i]);
    }
    mx.control(MD_MAX72XX::UPDATE, MD_MAX72XX::ON);
    mx.control(MD_MAX72XX::UPDATE, MD_MAX72XX::OFF);
    delay(delayTime);  
    // no longer needed when using interrput? 
    // checkLimits();
  }
}


void IRAM_ATTR toggleLimit() {
  checkLimits();
}


void setup() {
  // configure pins  
  pinMode(limitPin, INPUT);
  attachInterrupt(limitPin, toggleLimit, CHANGE);
  pinMode(dirPin, OUTPUT);
  pinMode(stepPin, OUTPUT);
  // output initial direction
  digitalWrite(dirPin, dirState);
  // setup and start pwm for step generation
  ledcSetup(PWMChannel, PWMFreq, PWMResolution);
  ledcAttachPin(stepPin, PWMChannel);
  ledcWrite(PWMChannel, MAX_DUTY_CYCLE/2.8);
  // initialize max7219
  mx.begin();
}

void loop() {
  draw_bitmap();
}