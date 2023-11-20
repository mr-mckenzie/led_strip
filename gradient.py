import plasma
from plasma import plasma_stick
from random import uniform
from random import randint
from random import choice
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
        
def spiral_from_ends(led_array = None):
    for i in range(0,25):
        if(led_array != None):
            led_strip.set_hsv(49-i, led_array[49-i]['hue'], led_array[49-i]['sat'], lumin)
            led_strip.set_hsv(0+i, led_array[0+i]['hue'], led_array[0+i]['sat'], lumin)
        else:
            led_strip.set_hsv(49-i,0,0,0)
            led_strip.set_hsv(0+i,0,0,0)
        time.sleep(0.1)
        

def drip_downward(led_array = None):
    for i in range(0,7):
        for j in range(0,50):
            if (j % 7 == i):
                if (led_array != None):
                    led_strip.set_hsv(j, led_array[j]['hue'], led_array[j]['sat'], lumin)
                else:
                    led_strip.set_hsv(j,0,0,0)
            time.sleep(0.008)

def fade(led_array = None):
    lumin_change = 0.02
    if (led_array == None):
        fading_lumin = lumin
        while fading_lumin >= 0:
            for i in range (0,50):
                led_strip.set_hsv(i,0,0,fading_lumin)
            time.sleep(0.1)
            fading_lumin -= lumin_change
    else:
        fading_lumin = 0
        while fading_lumin <= lumin:
            for i in range (0,50):
                led_strip.set_hsv(i,led_array[i]['hue'],led_array[i]['sat'], fading_lumin)
            time.sleep(0.1)
            fading_lumin += lumin_change
        
# def random_animate (led_array):
#    for i in range(0, 51):
#        if i > 0 :
#            led_strip.set_hsv(i-1, led_array[i-1]['hue'], led_array[i-1]['sat'], lumin)
#        if i <= 49:
#            led_strip.set_hsv(i, led_array[i]['hue'], led_array[i]['sat'], 0.1)
#        time.sleep(0.05)
        
def colour_wheel(led_array):
    hue_change = 0.75
    while hue_change >= 0:
        for i in range (0,50):
            led_strip.set_hsv(i,led_array[i]['hue']+hue_change,led_array[i]['sat'], lumin)
        time.sleep(0.2)
        hue_change -= 0.02
        
def group_spiral(led_array):
    last_led = 50
    group_size = 5
    
    while last_led > 0:
        for i in range(0,last_led):
            for j in range (0,group_size):
                if j <= i:
                    led_strip.set_hsv(i-j, led_array[last_led-1-j]['hue'], led_array[last_led-1-j]['sat'], lumin)
            if i >= group_size:
                led_strip.set_hsv(i-group_size,0,0,0)
            time.sleep(0.1)
        last_led -= group_size
        
        
                
animation = [random, downward_rows, upward_rows, downward_spiral, upward_spiral, horizontal, spiral_from_centre, spiral_from_ends, drip_downward, fade, colour_wheel, group_spiral]

lumin = 0.5

led_strip.start()

while True:
    
    time.sleep(2)

    starting_hue = uniform(0,1)
    final_hue = uniform(starting_hue+0.15,starting_hue+0.70)
    gradient_change = choice([1, -1]) * (final_hue - starting_hue)/49

    starting_sat = uniform(0.4,1)
    final_sat = uniform(0.4,1)
    sat_change = (final_sat - starting_sat)/49
    
    leds = []
    for led in range(0, number_of_leds):
        leds.append({
            'hue': starting_hue + 1 + (led * gradient_change),
            'sat': starting_sat + (led * sat_change)})
        
    animate_on = animation[randint(0,11)]
    animate_on(leds)

    time.sleep(45)
    
    animate_off = animation[randint(0,8)]
    animate_off()
    
    time.sleep(8)