#include "debugging_w.h"

debugging_w::debugging_w() : window() {
  pinMode(BUTTON_PIN_1, INPUT_PULLUP);
  pinMode(BUTTON_PIN_2, INPUT_PULLUP);
  pinMode(BUTTON_PIN_3, INPUT_PULLUP);
  pinMode(BUTTON_PIN_4, INPUT_PULLUP);
  analogReadResolution(12);
}

debugging_w::~debugging_w(){};

bool debugging_w::draw(){
  display->setCursor(0, 0);
  display->println("I am debugging_window");
  display->display();
  return true;
}

bool debugging_w::process_command(std::vector<int> input_v){
  return true;
}