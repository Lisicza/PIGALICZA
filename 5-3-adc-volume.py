from machine import ADC, Pin
import time
LED_PINS = [6, 7, 8, 9, 10, 11, 12, 13] 
NUM_LEDS = len(LED_PINS)
ADC_CHANNEL = 0 
REFERENCE_VOLTAGE = 3.3 
adc = ADC(ADC_CHANNEL)  
leds = [] 
for pin_num in LED_PINS:
    led = Pin(pin_num, Pin.OUT)
    leds.append(led)
def adc_to_voltage(adc_value_u16):
    return (adc_value_u16 * REFERENCE_VOLTAGE) / 65535

def voltage_to_led_level(voltage):
    ratio = voltage / REFERENCE_VOLTAGE
    level_float = ratio * NUM_LEDS
    level = int(round(level_float))
    level = max(0, min(level, NUM_LEDS))
    return level

def update_leds(level):
    for i in range(NUM_LEDS):
        if i < level:
            leds[i].value(1)  # Зажигаем светодиод
        else:
            leds[i].value(0)  # Гасим светодиод

try:
    print("Запуск 'ADC -> LED Volume Meter'. Нажмите Ctrl+C для выхода.")
    while True:
        raw_value = adc.read_u16()
        voltage = adc_to_voltage(raw_value)
        led_level = voltage_to_led_level(voltage)
        update_leds(led_level)
        time.sleep_ms(10)
except KeyboardInterrupt:
    print("\nВыход из программы.")
    update_leds(0)