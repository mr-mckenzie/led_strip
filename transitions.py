import plasma
from plasma import plasma_stick
from random import randint
import time

number_of_leds = 50
lumin = 0.5

led_strip = plasma.WS2812(number_of_leds, 0, 0, plasma_stick.DAT, color_order=plasma.COLOR_ORDER_RGB)

#helper function to start strip
#def start_LED_stick(led_strip):
        #led_strip.start()

#helper off functions
def turn_off_led_at_index(index):
    led_strip.set_hsv(index, 0,0,0)

def turn_of_all_leds():
    for led_index in range(0,number_of_leds):
        turn_off_led_at_index(led_index)

#helper on functions
def turn_on_led_at_index(index, colour_array, luminosity):
    led_strip.set_hsv(index,colour_array[index]['hue'],colour_array[index]['sat'],luminosity)

def turn_on_all_leds(colour_array, luminosity):
    for led_index in range(0,number_of_leds):
        turn_on_led_at_index(led_index, colour_array, luminosity)

def random(led_array, turn_on):
    lit_array = []
    for i in range(0,number_of_leds):
        lit_array.append(i)
        
    for i in range(0,number_of_leds):
        random_position = randint(0, len(lit_array)-1)
        if (turn_on == True):
            turn_on_led_at_index(lit_array[random_position], led_array, lumin)
        else:
            turn_off_led_at_index(lit_array[random_position])
        time.sleep(0.075)
        del lit_array[random_position]

def downward_rows(led_array, turn_on):
    for i in range(0, number_of_leds):
        if (turn_on == True):
            turn_on_led_at_index(i, led_array, lumin)
        else:
            turn_off_led_at_index(i)
        if (i % 7 == 0):
            time.sleep(0.75)

def upward_rows(led_array, turn_on):
    for i in range(number_of_leds-1, -1, -1):
        if (turn_on == True):
            turn_on_led_at_index(i, led_array, lumin)
        else:
            turn_off_led_at_index(i)
        if (i % 7 == 0):
            time.sleep(0.75)
            
def downward_spiral(led_array, turn_on):
    for i in range(0, 50):
        if (turn_on == True):
            turn_on_led_at_index(i, led_array, lumin)
        else:
            turn_off_led_at_index(i)
        time.sleep(0.1)
        
def upward_spiral(led_array, turn_on):
    for i in range(1, 51):
        if (turn_on == True):
            turn_on_led_at_index(50-i, led_array, lumin)
        else:
            turn_off_led_at_index(50-i)
        time.sleep(0.1)
        
def horizontal(led_array, turn_on):
    for i in range(0,7):
        for j in range(0,50):
            if (j % 7 == i):
                if (turn_on == True):
                    turn_on_led_at_index(j, led_array, lumin)
                else:
                    turn_off_led_at_index(j)
        time.sleep(0.075)
        
def spiral_from_centre(led_array, turn_on):
    for i in range(0,25):
        if(turn_on == True):
            turn_on_led_at_index(24-i, led_array, lumin)
            turn_on_led_at_index(25+i, led_array, lumin)
        else:
            turn_off_led_at_index(24-i)
            turn_off_led_at_index(25+i)
        time.sleep(0.1)
        
def spiral_from_ends(led_array, turn_on):
    for i in range(0,25):
        if(turn_on == True):
            turn_on_led_at_index(49-i, led_array, lumin)
            turn_on_led_at_index(0+i, led_array, lumin)
        else:
            turn_off_led_at_index(49-i)
            turn_off_led_at_index(0+i)
        time.sleep(0.1)
        

def drip_downward(led_array, turn_on):
    for i in range(0,7):
        for j in range(0,50):
            if (j % 7 == i):
                if (turn_on == True):
                    turn_on_led_at_index(j, led_array, lumin)
                else:
                    turn_off_led_at_index(j)
            time.sleep(0.008)

def fade(led_array, turn_on):
    lumin_change = 0.02
    if (turn_on == False):
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
                turn_on_led_at_index(i, led_array, fading_lumin)
            time.sleep(0.1)
            fading_lumin += lumin_change
        
## THESE ARE ON ONLY
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
        
def shuffle_bubble_sort(led_array):
    randomised_array = led_array
    for led in range(0,100):
        random_popped_led = randomised_array.pop(randint(0,49))
        randomised_array.insert(randint(0,49),random_popped_led)

    turn_on_all_leds(randomised_array, lumin)

    time.sleep(2.5)
        
    n = len(led_array)
    swapped = True
    while swapped == True:
        swapped = False
        for index in range(0,n):
            if index < n-1:
                this_led = randomised_array[index]
                next_led = randomised_array[index+1]
                if this_led['hue'] > next_led['hue']:
                    randomised_array[index] = next_led
                    randomised_array[index+1] = this_led
                    swapped = True
                    
                    turn_on_led_at_index(index, randomised_array, lumin)
                    turn_on_led_at_index(index+1, randomised_array, lumin)

        time.sleep(0.2)
        
        
def shuffle_cocktail_sort(led_array):
    randomised_array = led_array
    for led in range(0,100):
        random_popped_led = randomised_array.pop(randint(0,49))
        randomised_array.insert(randint(0,49),random_popped_led)

    turn_on_all_leds(randomised_array, lumin)
           
    time.sleep(2.5)
    
    n = len(led_array)
    swapped = True
    while swapped == True:
        swapped = False
        for index in range(0,n):
            if index < n-1:
                this_led = randomised_array[index]
                next_led = randomised_array[index+1]
                if this_led['hue'] > next_led['hue']:
                    randomised_array[index] = next_led
                    randomised_array[index+1] = this_led
                    swapped = True

                    turn_on_led_at_index(index, randomised_array, lumin)
                    turn_on_led_at_index(index+1, randomised_array, lumin)

        time.sleep(0.2)
        for index in range(n,0, -1):
            if index < n-1:
                this_led = randomised_array[index]
                next_led = randomised_array[index+1]
                if this_led['hue'] > next_led['hue']:
                    randomised_array[index] = next_led
                    randomised_array[index+1] = this_led
                    swapped = True
                    
                    turn_on_led_at_index(index, randomised_array, lumin)
                    turn_on_led_at_index(index+1, randomised_array, lumin)
        time.sleep(0.2)
