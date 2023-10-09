import plasma
from plasma import plasma_stick
import random
import time

# set number of LEDs
number_of_leds = 50

# WS2812 / NeoPixel™ LEDs
led_strip = plasma.WS2812(number_of_leds, 0, 0, plasma_stick.DAT, color_order=plasma.COLOR_ORDER_RGB)

led_strip.start()

while True:
    
    time.sleep(5)

    led_strip.set_hsv(50, 0, 0.1, 0.1)
    time.sleep(0.1)
    led_strip.set_hsv(50, 0, 0 ,0)
    led_strip.set_hsv(45, 0, 0.1, 0.1)
    time.sleep(0.1)
    led_strip.set_hsv(45, 0, 0 ,0)
    led_strip.set_hsv(40, 0, 0.1, 0.1)
    time.sleep(0.1)
    led_strip.set_hsv(40, 0, 0 ,0)
    led_strip.set_hsv(30, 0, 0.1, 0.1)
    time.sleep(0.1)
    led_strip.set_hsv(30, 0, 0, 0)
    led_strip.set_hsv(15, 0, 0.1 ,0.1)
    time.sleep(0.1)
    led_strip.set_hsv(15, 0, 0, 0)
    led_strip.set_hsv(6, 0, 0.1 ,0.1)
    time.sleep(0.1)
    led_strip.set_hsv(6, 0, 0, 0)
    led_strip.set_hsv(4, 0, 0.1 ,0.1)
    time.sleep(0.1)
    led_strip.set_hsv(4, 0, 0, 0)
    led_strip.set_hsv(0, 0, 0.1 ,0.1)
    time.sleep(0.2)
    led_strip.set_hsv(0, 0, 0 ,0)
    time.sleep(0.3)

    random_colour = random.random()
    random_saturation = random.uniform(0.65,1.0)
    brightness = 0.75
    lower_led = 0
    upper_led = 7
    first_run = True
    sleep = 0.15
        
    for x in range(upper_led, number_of_leds):
        led_strip.set_hsv(x, random_colour, random_saturation, 0)
    while brightness > 0.15:
        for i in range(0, lower_led):
            led_strip.set_hsv(i, random_colour, 0, 0)
        for i in range(lower_led, upper_led):
            led_strip.set_hsv(i, random_colour, random_saturation, brightness)
        
        if first_run == True:
            time.sleep(0.7)
            first_run = False
        time.sleep(sleep)

        sleep += 0.01
        brightness -= 0.05
        lower_led += 2
        upper_led += 2
    
    for i in range(0, 50):
                led_strip.set_hsv(i, random_colour, 0, 0)
                
    time.sleep(40)