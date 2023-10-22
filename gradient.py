import plasma
from plasma import plasma_stick
from random import uniform
from random import randint
import time

number_of_leds = 50

led_strip = plasma.WS2812(number_of_leds, 0, 0, plasma_stick.DAT, color_order=plasma.COLOR_ORDER_RGB)

def random(led_array = None):
    lit_array = []
    for i in range(0,50):
        lit_array.append(i)
        
    for i in range(0,50):
        random_position = randint(0, len(lit_array)-1)
        if (led_array != None):
            led_strip.set_hsv(lit_array[random_position], led_array[lit_array[random_position]]['hue'], led_array[lit_array[random_position]]['sat'], lumin)
        else:
            led_strip.set_hsv(lit_array[random_position], 0,0,0)
        time.sleep(0.075)
        del lit_array[random_position]

def downward_rows(led_array = None):
    for i in range(0, 50):
        if (led_array != None):
            led_strip.set_hsv(i,led_array[i]['hue'],led_array[i]['sat'],lumin)
        else:
            led_strip.set_hsv(i,0,0,0)
        if (i % 7 == 0):
            time.sleep(0.75)

def upward_rows(led_array = None):
    for i in range(1, 51):
        if (led_array != None):
            led_strip.set_hsv(50-i, led_array[50-i]['hue'], led_array[50-i]['sat'], lumin)
        else:
            led_strip.set_hsv(50-i,0,0,0)
        if (i % 7 == 0):
            time.sleep(0.75)
            
def downward_spiral(led_array = None):
    for i in range(0, 50):
        if (led_array != None):
            led_strip.set_hsv(i, led_array[i]['hue'], led_array[i]['sat'], lumin)
        else:
            led_strip.set_hsv(i,0,0,0)
        time.sleep(0.1)
        
def upward_spiral(led_array = None):
    for i in range(1, 51):
        if (led_array != None):
            led_strip.set_hsv(50-i, led_array[50-i]['hue'], led_array[50-i]['sat'], lumin)
        else:
            led_strip.set_hsv(50-i,0,0,0)
        time.sleep(0.1)
        
def horizontal(led_array = None):
    for i in range(0,7):
        for j in range(0,50):
            if (j % 7 == i):
                if (led_array != None):
                    led_strip.set_hsv(j, led_array[j]['hue'], led_array[j]['sat'], lumin)
                else:
                    led_strip.set_hsv(j,0,0,0)
        time.sleep(0.075)
        
def spiral_from_centre(led_array = None):
    for i in range(0,25):
        if(led_array != None):
            led_strip.set_hsv(24-i, led_array[24-i]['hue'], led_array[24-i]['sat'], lumin)
            led_strip.set_hsv(25+i, led_array[25+i]['hue'], led_array[25+i]['sat'], lumin)
        else:
            led_strip.set_hsv(24-i,0,0,0)
            led_strip.set_hsv(25+i,0,0,0)
        time.sleep(0.1)
            
animation = [random, downward_rows, upward_rows, downward_spiral, upward_spiral, horizontal, spiral_from_centre]

lumin = 0.5

led_strip.start()

while True:
    
    time.sleep(2)

    starting_hue = uniform(0,1)
    final_hue = uniform(starting_hue+0.1,starting_hue+1)
    gradient_change = (final_hue - starting_hue)/49

    starting_sat = uniform(0.2,1)
    final_sat = uniform(0,1)
    sat_change = (final_sat - starting_sat)/49
    
    leds = []
    for led in range(0, number_of_leds):
        leds.append({
            'hue': starting_hue+(led * gradient_change),
            'sat': starting_sat + (led * sat_change)})
        
    animate_on = animation[randint(0,6)]
    animate_on(leds)

    time.sleep(45)
    
    animate_off = animation[randint(0,6)]
    animate_off()
    
    time.sleep(8)
