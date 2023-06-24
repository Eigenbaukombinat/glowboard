#include <SPI.h>
#include <MD_MAX72xx.h>
#include "main.h"

// max7219 stuff
#define MAX_DEVICES	1
#define HARDWARE_TYPE MD_MAX72XX::GENERIC_HW
#define CLK_PIN   18  
#define DATA_PIN  23  
#define CS_PIN    5 
MD_MAX72XX mx = MD_MAX72XX(HARDWARE_TYPE, CS_PIN, MAX_DEVICES);

uint8_t current_bitmap[1024][8];
uint8_t next_bitmap[1024][8];


// initial delay time in microseconds bewteen columns (for highest resolution of 1024 columns),
// influences the "width" of a column
int delay_time_base = 90000; 

// stepper pin defition
const int stepPin = 21; 
const int dirPin = 22;

// limit switches
const int limitPinL = 12;
const int limitPinR = 14;

// setup pwm for stepper step generation
const int PWMFreq = 600; /* Hz */
const int PWMChannel = 0;
const int PWMResolution = 10;
const int MAX_DUTY_CYCLE = (int)(pow(2, PWMResolution) - 1);

// initial direction
int dirState = LOW;

// sync stuff
int last_sync;
hw_timer_t *ColTimer = NULL;


void IRAM_ATTR drawCol() {
  // calculate position in current bitmap array using delay_time_base and
  // time passed since last_sync and current direction, and draw it
  // it might also be possible to use timerAlarmRead to get the elapsed time 
  // since last calibration (because the timer is maybe restarted from 0 there)
  int now = millis() * 1000;
  int elapsed = now - last_sync;
  int position = elapsed / delay_time_base;
  if (dirState == LOW) {
    position = 1024 - position;
  }
  for (int i=0; i<8; i++) {
      mx.setRow(i, current_bitmap[position][7-i]);
  }
}



void calibrate() {
    int now = millis() * 1000;
    int time_all_cols = now - last_sync;
    // this is actually debouncing the limit switches ;)
    if (time_all_cols < 10000) {
      return;
    }
    delay_time_base = time_all_cols / 1024;
    last_sync = millis() * 1000;
    timerAlarmWrite(ColTimer, delay_time_base, true);
}

void IRAM_ATTR limitL() {
    calibrate();
    dirState = HIGH;
    digitalWrite(dirPin, dirState);
}

void IRAM_ATTR limitR() {
    calibrate();
    dirState = LOW;
    digitalWrite(dirPin, dirState);
}


void setup() {
  // configure pins  
  pinMode(limitPinL, INPUT_PULLUP);
  pinMode(limitPinR, INPUT_PULLUP);
  attachInterrupt(digitalPinToInterrupt(limitPinL), limitL, FALLING);
  attachInterrupt(digitalPinToInterrupt(limitPinR), limitR, FALLING);
  pinMode(dirPin, OUTPUT);
  pinMode(stepPin, OUTPUT);
  // output initial direction
  digitalWrite(dirPin, dirState);
  // setup and start pwm for step generation
  ledcSetup(PWMChannel, PWMFreq, PWMResolution);
  ledcAttachPin(stepPin, PWMChannel);
  ledcWrite(PWMChannel, MAX_DUTY_CYCLE/2.8);
  // register column draw timer
  ColTimer = timerBegin(0, 80, true);
  timerAttachInterrupt(ColTimer, &drawCol, true);
  timerAlarmWrite(ColTimer, delay_time_base, true);
  timerAlarmEnable(ColTimer);
  // initialize max7219
  mx.begin();
  mx.clear();
  // save initial timing 
  last_sync = millis() * 1000;
  // todo: wifi + webserver stuff
  // https://raphaelpralat.medium.com/example-of-json-rest-api-for-esp32-4a5f64774a05
  // copy initial bitmap to current
  for (uint8_t j=0; j<256; j++) {
    for (int x=0; x<(1024/256); x++) {
      for (int i=0; i<8; i++) {
        current_bitmap[j+x][i] = initial_bitmap[j][i];
      }
    }
  }
}

void loop() {
}