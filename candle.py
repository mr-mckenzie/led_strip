import plasma
from plasma import plasma_stick
import time
import random

# number of LEDs
number_of_leds = 50

# WS2812 / NeoPixel™ LEDs
led_strip = plasma.WS2812(number_of_leds, 0, 0, plasma_stick.DAT, color_order=plasma.COLOR_ORDER_RGB)

led_strip.start()

x = 0
topLimit = 2
counter = 0

while True:
    print(f'cycle {counter} starting')
    for y in range(0, topLimit):
        led_strip.set_hsv(y, 0, 0, 0)

    for i in range(topLimit, number_of_leds):
        led_strip.set_hsv(i, 0.2, 0.4, 0.15)
        
    randomFlickerOne = random.randint(50, 150)
    randomFlickerTwo = random.randint(200, 300)
    randomFlickerThree = random.randint(350, 450)
    randomFlickerFour = random.randint(500, 590)
    
    for i in range(topLimit-2, topLimit):
            led_strip.set_hsv(i, random.uniform(0.12, 0.15), random.uniform(0.75,0.9), random.uniform(0.5, 0.75))

    while x < 600:
        
        while ((x >= randomFlickerOne and x <= randomFlickerOne+10) or (x >= randomFlickerTwo and x <= randomFlickerTwo+10) or (x >= randomFlickerThree and x <= randomFlickerThree+10) or (x >= randomFlickerFour and x <= randomFlickerFour+10)):
            for j in range(topLimit-2, topLimit):
                led_strip.set_hsv(j, random.uniform(0.12, 0.15), random.uniform(0.75,0.9), random.uniform(0.5, 0.75))
                time.sleep(0.1) 
                x += 1
                
        time.sleep(0.1)
        x += 1
    
    topLimit += 1
    x = 0
    counter += 1
    
    if (topLimit == 50):
        topLimit = 2
