import plasma
from plasma import plasma_stick
import time
import random

number_of_leds = 50

led_strip = plasma.WS2812(number_of_leds, 0, 0, plasma_stick.DAT, color_order=plasma.COLOR_ORDER_RGB)

led_strip.start()

lumin_one_const = 0.5
lumin_two_const = 0.5

time.sleep(3)

while True:
    
    hue_one = random.uniform(0.0, 1.0)
    sat_one = random.uniform(0.5,0.8)

    hue_two = random.uniform(hue_one, 2)
    sat_two = random.uniform(sat_one,1)
    
    lumin_one = lumin_one_const
    lumin_two = lumin_two_const
    

    #fade up to colour one
    start_lumin = 0
    start_step = lumin_one / 30
    while start_lumin < lumin_one:
        for i in range(0,50):
            led_strip.set_hsv(i, hue_one, sat_one, start_lumin)
        
        start_lumin += start_step
        time.sleep(0.05)
        
    time.sleep(10)
    
    #Vertically change to second colour
    z=6
    while z >= 0:
        for i in range(0,50):
            if (i % 7 == z):
                led_strip.set_hsv(i, hue_two, sat_two, lumin_two)
                time.sleep(0.1)
        z -= 1
        time.sleep(1)
            
    time.sleep(5)
    
    
    #Horizontal change
    colour_one = True
    number_of_switches = random.randint(3,25)
    
    for i in range(0,50):
        if (i % number_of_switches == 0):
            colour_one = not(colour_one)
        if (colour_one == True):
            led_strip.set_hsv(i, hue_one, sat_one, lumin_one)
            time.sleep(0.12)
        else:
            led_strip.set_hsv(i, hue_two, sat_two, lumin_two)
            time.sleep(0.12)
    
    time.sleep(10)

    #Fade to black
    while (lumin_one > 0):
        #print(lumin_one)

        for i in range(0,50):
            if (i % number_of_switches == 0):
                colour_one = not(colour_one)
            if (colour_one == True):
                led_strip.set_hsv(i, hue_one, sat_one, lumin_one)
            else:
                led_strip.set_hsv(i, hue_two, sat_two, lumin_two)
        
        lumin_two -= 0.05
        lumin_one -= 0.05
        time.sleep(0.15)
        
    for i in range(0,50):
        led_strip.set_hsv(i, 0,0,0)
    
    time.sleep(5)
    
    #Randomly light up
    unlit_array = []
    for i in range(0,50):
        unlit_array.append(i)
        
    for i in range(0,50):
        random_position = random.randint(0, len(unlit_array)-1)
        #print('random position is ' + str(random_position))
        #print('len is ' + str(len(unlit_array)))
        random_colour = random.randint(0,1)
        if (random_colour == 0):
            led_strip.set_hsv(unlit_array[random_position], hue_two, sat_two, lumin_two_const)
        else:
            led_strip.set_hsv(unlit_array[random_position], hue_one, sat_one, lumin_one_const)
        time.sleep(0.25)
        del unlit_array[random_position]
        
    time.sleep(10)
    
    #switch off spiral downwards
    for i in range(0, 50):
        led_strip.set_hsv(i, 0,0,0)
        time.sleep(0.1)
        
    time.sleep(5)
    
    #Gradient between the two colours
    hue_step = (hue_two - hue_one) / 51
    start_hue = hue_one
    sat_step = (sat_two - sat_one) / 51
    start_sat = sat_one
    
    for i in range(0, 50):
        led_strip.set_hsv(i, start_hue, start_sat, lumin_two_const)
        start_hue += hue_step
        start_sat += sat_step
        time.sleep(0.1)
        
    time.sleep(10)
    
    #switch off in rows
    for i in range(0, 51):
        led_strip.set_hsv(50-i,0,0,0)
        if (i % 7 == 0):
            time.sleep(0.75)
    
    time.sleep(5)
            
    #flash alternatively
    counter = 0
    led_selected = True
    while counter < 60:
        for i in range(0,50):
            if ((led_selected == True and i%2 == 0) or (led_selected == False and i%2==1)):
                led_strip.set_hsv(i, hue_one, sat_one, lumin_one_const)
            else:
                led_strip.set_hsv(i, hue_two, sat_two, lumin_two_const)
        
        led_selected = not(led_selected)
        counter += 1
        time.sleep(0.25)
        
    #Randomly turn off
    unlit_array = []
    for i in range(0,50):
        unlit_array.append(i)
        
    for i in range(0,50):
        random_position = random.randint(0, len(unlit_array)-1)
        led_strip.set_hsv(unlit_array[random_position], 0, 0, 0)
        time.sleep(0.1)
        del unlit_array[random_position]
    
    time.sleep(20)
