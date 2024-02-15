import plasma
from plasma import plasma_stick
from pimoroni_i2c import PimoroniI2C
from breakout_ltr559 import BreakoutLTR559

import time
from random import randint
from set_colours import get_gradient

i2c = PimoroniI2C(plasma_stick.SDA, plasma_stick.SCL)

ltr = BreakoutLTR559(i2c)

number_of_leds = 50

lumin = 0.35

led_strip = plasma.WS2812(number_of_leds, 0, 0, plasma_stick.DAT, color_order=plasma.COLOR_ORDER_RGB)

def turn_on_led_at_index(index, colour_array, luminosity):
    led_strip.set_hsv(index,colour_array[index]['hue'],colour_array[index]['sat'],luminosity)

def turn_on_all_leds(colour_array, luminosity):
    for led_index in range(0,number_of_leds):
        turn_on_led_at_index(led_index, colour_array, luminosity)
        
def turn_off_led_at_index(index):
    led_strip.set_hsv(index, 0,0,0)

def turn_off_all_leds():
    for led_index in range(0,number_of_leds):
        turn_off_led_at_index(led_index)

led_strip.start()

while True:
    
    time.sleep(2)
    
    leds = get_gradient(number_of_leds)
    
    turn_on_all_leds(leds, lumin)

    time_elapsed = 0
    shuffled = False
    base_lux = ltr.get_reading()[BreakoutLTR559.LUX]
    #alternatively use proximity: reading[BreakoutLTR559.PROXIMITY]
    
    while (time_elapsed<=30):
        reading = ltr.get_reading()
        if reading is not None:
            shuffled = True
            
            if reading[BreakoutLTR559.LUX] < (0.66*base_lux) and time_elapsed <= 30:
                for count in range (0,250):
                    first_index_to_swap = randint(0,number_of_leds-1)
                    second_index_to_swap = randint(0,number_of_leds-1)
                    while first_index_to_swap == second_index_to_swap:
                        second_index_to_swap = randint(0,number_of_leds-1)
                    first_swap = leds[first_index_to_swap]
                    second_swap = leds[second_index_to_swap]
                    leds[second_index_to_swap] = first_swap
                    leds[first_index_to_swap] = second_swap
                    turn_on_led_at_index(first_index_to_swap, leds, lumin)
                    turn_on_led_at_index(second_index_to_swap, leds, lumin)
                    time.sleep(0.01)
                    time_elapsed += 0.01
                    count += 1
                    print(time_elapsed)
            else:
                time.sleep(0.2)
                time_elapsed += 0.2
            print(time_elapsed)
    
    if shuffled == True:
        
        time.sleep(2.5)
    
        swapped = True
        while swapped == True:
            swapped = False
            for index in range(0,number_of_leds):
                if index < number_of_leds-1:
                    this_led = leds[index]
                    next_led = leds[index+1]
                    if this_led['hue'] > next_led['hue']:
                        leds[index] = next_led
                        leds[index+1] = this_led
                        swapped = True
                        
                        turn_on_led_at_index(index, leds, lumin)
                        turn_on_led_at_index(index+1, leds, lumin)

            time.sleep(0.1)

        time.sleep(2.5)
        
    turn_off_all_leds()
    
    time.sleep(8)
