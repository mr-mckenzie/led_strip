import plasma
from plasma import plasma_stick
import random
import time

# set number of LEDs
number_of_leds = 50

# WS2812 / NeoPixel™ LEDs
led_strip = plasma.WS2812(number_of_leds, 0, 0, plasma_stick.DAT, color_order=plasma.COLOR_ORDER_RGB)

led_strip.start()

time.sleep(5)

while True:

    #50 is the bottom of the tower
    #0 is the top of the tower
    
    starting_led = random.randint(46,50)
    step = 7
    print('first led is ' + str(starting_led))
    while starting_led > 5:
        if (starting_led <=45):
            led_strip.set_hsv(starting_led + step, 0, 0, 0)
        led_strip.set_hsv(starting_led, 0, 0.1, 0.1)
        
        starting_led -= step
        time.sleep(0.1)
        
    starting_led += step
    print('bang_led is ' + str(starting_led))
    
    led_strip.set_hsv(starting_led, 0, 0, 0)
    time.sleep(0.3)

    random_colour = random.random()
    random_saturation = random.uniform(0.65,1.0)
    brightness = 0.8
    upper_led = 0
    lower_led = starting_led + 5
    run = 0
    sleep = 0.15
        
    for x in range(lower_led, number_of_leds):
        led_strip.set_hsv(x, random_colour, 0, 0)
    while brightness > 0.2:
        for unlit_led in range(0, upper_led):
            led_strip.set_hsv(unlit_led, random_colour, 0, 0)
        for lit_led in range(upper_led, lower_led):
            if (run > 3):
                if (lit_led % 3 == 0):
                    led_strip.set_hsv(lit_led, random_colour, random_saturation, brightness)
                else:
                    led_strip.set_hsv(lit_led, random_colour, 0, 0)
            else:
                led_strip.set_hsv(lit_led, random_colour, random_saturation, brightness)
        
        if run == 0:
            time.sleep(0.7)
        
        run += 1
        sleep += 0.01
        time.sleep(sleep)
        brightness -= 0.05
        lower_led += 2
        upper_led += 3
        
        if lower_led < 0:
            brightness = 0
    
    for led in range(0, 50):
        led_strip.set_hsv(led, random_colour, 0, 0)
                
    time.sleep(45)