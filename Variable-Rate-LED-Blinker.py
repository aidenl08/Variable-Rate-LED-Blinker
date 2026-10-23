from machine import ADC, Pin
import time

# Set up the potentiometer on ADC pin 26
pot = ADC(Pin(26))

# Set up the LED on GPIO pin 15
led = Pin(15, Pin.OUT)

while True:
    # 1. Read the potentiometer value (0 to 65535)
    adc_value = pot.read_u16()
    
    # 2. Convert that value into a delay time (0.05 and 1.0 seconds)
    delay_time = (adc_value / 65535) * 0.95 + 0.05
    
    # 3. Blink the LED using potentiometer delay
    led.on()
    time.sleep(delay_time)
    led.off()
    time.sleep(delay_time)
    
    #print the speed so you can see it change
    print("Blink delay:", delay_time)