# Variable-Rate LED Blinker (Raspberry Pi Pico & MicroPython)

An embedded systems project built with a Raspberry Pi Pico and MicroPython that uses an analog potentiometer to dynamically adjust the blink rate of an LED via analog-to-digital conversion (ADC).

## 🛠️ Hardware Used
* Raspberry Pi Pico
* Potentiometer (10k ohm)
* LED & Resistor (220 ohm)
* Breadboard & Jumper Wires

## 💻 Code Overview
```python
from machine import ADC, Pin
import time

pot = ADC(Pin(26))
led = Pin(15, Pin.OUT)

while True:
    adc_value = pot.read_u16()
    delay_time = (adc_value / 65535) * 0.95 + 0.05
    
    led.on()
    time.sleep(delay_time)
    led.off()
    time.sleep(delay_time)
