#ifndef COMMANDER_H
#define COMMANDER_H

#include <vector>
#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>
#include <SPI.h>
#include "window.h"
#include "debugging_w.h"

#define SCREEN_WIDTH 128
#define SCREEN_HEIGHT 64
#define OLED_DC     16
#define OLED_RST    17
#define OLED_CS     19

class commander{
  private:
    Adafruit_SSD1306 display;
    std::vector<int> input_v;
    std::vector<window*> window_v;
    int current_window_number;
  public:
    commander();
    ~commander();

    bool set_input_v();
    bool process();
};

#endif