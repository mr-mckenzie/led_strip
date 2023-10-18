import plasma
from plasma import plasma_stick
import time
import random

number_of_leds = 50

# SPAIN
#hue_one = 46/360
#sat_one = 0.98
#lumin_one_const = 0.49

#hue_two = 359/360
#sat_two = 0.85
#lumin_two_const = 0.37

#SCOTLAND
#hue_one = 210/360
#sat_one = 1
#lumin_one_const = 0.5

#hue_two = 0
#sat_two = 0
#lumin_two_const = 0.5

led_strip = plasma.WS2812(number_of_leds, 0, 0, plasma_stick.DAT, color_order=plasma.COLOR_ORDER_RGB)

led_strip.start()

lumin_one_const = 0.5
lumin_two_const = 0.5

while True:
    
    hue_one = random.random()
    sat_one = random.uniform(0.5,0.8)

    hue_two = random.random()
    sat_two = random.uniform(0.5,0.8)
    
    lumin_one = lumin_one_const
    lumin_two = lumin_two_const
    
    for i in range(0,12):
        led_strip.set_hsv(i, hue_two, sat_two, lumin_two)
        time.sleep(0.1)

    for i in range(12,37):
        led_strip.set_hsv(i, hue_one, sat_one, lumin_one)
        time.sleep(0.1)

    for i in range(37, number_of_leds):
        led_strip.set_hsv(i, hue_two, sat_two, lumin_two)
        time.sleep(0.1)
    

    time.sleep(20)

    while (lumin_one > 0):
        print(lumin_one)

        for i in range(0,12):
            led_strip.set_hsv(i, hue_two, sat_two, lumin_two)

        for i in range(12,37):
            led_strip.set_hsv(i, hue_one, sat_one, lumin_one)

        for i in range(37, number_of_leds):
            led_strip.set_hsv(i, hue_two, sat_two, lumin_two)
        
        lumin_two -= 0.05
        lumin_one -= 0.05
        time.sleep(0.15)
        
    for i in range(0,50):
        led_strip.set_hsv(i, 0,0,0)
    
    time.sleep(15)
    
    unlit_array = []
    for i in range(0,50):
        unlit_array.append(i)
        
    for i in range(0,50):
        random_position = random.randint(0, len(unlit_array)-1)
        print('random position is ' + str(random_position))
        print('len is ' + str(len(unlit_array)))
        random_colour = random.randint(0,1)
        if (random_colour == 0):
            led_strip.set_hsv(unlit_array[random_position], hue_two, sat_two, lumin_two_const)
        else:
            led_strip.set_hsv(unlit_array[random_position], hue_one, sat_one, lumin_one_const)
        time.sleep(0.25)
        del unlit_array[random_position]
        
    time.sleep(30)
    
    for i in range(50):
        led_strip.set_hsv(i, 0,0,0)
        time.sleep(0.1)
    
    time.sleep(120)
