import plasma
from plasma import plasma_stick
from random import uniform
from random import randint
from random import choice
import time
#from transitions import turn_off_led_at_index, turn_of_all_leds, turn_on_led_at_index, turn_on_all_leds

number_of_leds = 50

lumin = 0.35

led_strip = plasma.WS2812(number_of_leds, 0, 0, plasma_stick.DAT, color_order=plasma.COLOR_ORDER_RGB)

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
        
## THESE ARE ON ONLY ON ANIMATIONS
def colour_wheel(led_array, turn_on = True):
    hue_change = 0.75
    while hue_change >= 0:
        for i in range (0,50):
            led_strip.set_hsv(i,led_array[i]['hue']+hue_change,led_array[i]['sat'], lumin)
        time.sleep(0.2)
        hue_change -= 0.02
        
def group_spiral(led_array, turn_on = True):
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
        
def shuffle_bubble_sort(led_array, turn_on = True):
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
        
        
def shuffle_cocktail_sort(led_array, turn_on = True):
    randomised_array = led_array
    for led in range(0,100):
        random_popped_led = randomised_array.pop(randint(0,49))
        randomised_array.insert(randint(0,49),random_popped_led)

    turn_on_all_leds(randomised_array, lumin)
           
    time.sleep(2.5)
    
    n = len(led_array)
    swapped = True
    start=0
    end=n
    increment=1
    while swapped == True:
        swapped = False
        for index in range(start,end, increment):
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
        if increment == 1:
            increment = -1
            start = n
            end = 0
        else:
            increment = 1
            start = 0
            end = n
            
def shuffle_gnome_sort(led_array, turn_on = True):
    randomised_array = led_array
    for led in range(0,100):
        random_popped_led = randomised_array.pop(randint(0,49))
        randomised_array.insert(randint(0,49),random_popped_led)

    turn_on_all_leds(randomised_array, lumin)
           
    time.sleep(2.5)
    
# procedure gnomeSort(a[]):
#     pos := 0
#     while pos < length(a):
#         if (pos == 0 or a[pos] >= a[pos-1]):
#             pos := pos + 1
#         else:
#             swap a[pos] and a[pos-1]
#             pos := pos - 1


    n = len(led_array)
    position = 0

    while position < n:
        if position == 0 or randomised_array[position]['hue'] >= randomised_array[position-1]['hue']:
            turn_on_led_at_index(position, randomised_array, lumin/2)
            turn_on_led_at_index(position-1, randomised_array, lumin/2)
            time.sleep(0.05)
            turn_on_led_at_index(position, randomised_array, lumin)
            turn_on_led_at_index(position-1, randomised_array, lumin)
            position += 1
            
        else:
            this_led = randomised_array[position]
            next_led = randomised_array[position-1]
            randomised_array[position] = next_led
            randomised_array[position-1] = this_led

            turn_on_led_at_index(position, randomised_array, lumin)
            turn_on_led_at_index(position-1, randomised_array, lumin)
            position -= 1

            time.sleep(0.05)

animations = [random, downward_rows, upward_rows, downward_spiral, upward_spiral, horizontal, spiral_from_centre, spiral_from_ends, drip_downward, fade, colour_wheel, group_spiral, shuffle_bubble_sort, shuffle_cocktail_sort, shuffle_gnome_sort]

led_strip.start()
#print("Starting")

while True:
    #print("HERE")
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
        
    animate_on = animations[randint(0,14)]
    animate_on(leds, True)
    #random(leds, True)

    time.sleep(45)
    #time.sleep(5)

    animate_off = animations[randint(0,8)]
    #animate_off()
    random(leds, False)

    #time.sleep(8)
    time.sleep(2)

