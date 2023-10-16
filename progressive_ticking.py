import plasma
from plasma import plasma_stick
import time
import random

number_of_leds = 50

random_starting_colour = random.random()*360

colour_array = []
for led in range (0, number_of_leds):
    colour_array.append(0)
    
counter = 1

led_strip = plasma.WS2812(number_of_leds, 0, 0, plasma_stick.DAT, color_order=plasma.COLOR_ORDER_RGB)

led_strip.start()

while True:

    for led in range(1, number_of_leds):
        if (counter % led == 0):
            if (colour_array[led-1] != 0):
                led_strip.set_hsv(led-1, colour_array[led-1], 1, 1)
                colour_array[led-1] += 0.2
            else:
                colour_array[led-1] = (random_starting_colour)
                led_strip.set_hsv(led-1, colour_array[led-1], 1, 1)
                colour_array[led-1] += 0.2
        else:
            led_strip.set_hsv(led-1, 0, 0, 0)
            

    counter += 1
    time.sleep(1)
