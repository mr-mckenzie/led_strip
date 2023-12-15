import plasma
from plasma import plasma_stick
import time
from random import uniform
from random import randint

number_of_leds = 50

def random_bulbs(number_of_colours):
    
    bulbs_list = []
    colours_list = []
    colour_range = uniform(0.05,0.8)
    colour_offset = uniform(0,1)
    threshold = 1/number_of_colours
    threshold_buffer = threshold/10
    
    random_sat = uniform(0.5,0.85)
    #print("sat = " + str(random_sat))
    
    for led in range(0, number_of_leds):
        bulbs_list.append({"led": led, "hue": 0, "sat": 0, "lumin": 0.5, "on_off": "off"})
    
    for colour in range(0, number_of_colours):
        colours_list.append({"hue": uniform((threshold*colour)+threshold_buffer,(threshold*(colour+1))-threshold_buffer)*colour_range + colour_offset, "sat":random_sat})
    
    for led in range(0,number_of_leds):
        for colour in range(0, number_of_colours):
            if (led % number_of_colours == colour):
                bulbs_list[led]["hue"] = colours_list[colour]["hue"]
                bulbs_list[led]["sat"] = colours_list[colour]["sat"]
                
    return bulbs_list


led_strip = plasma.WS2812(number_of_leds, 0, 0, plasma_stick.DAT, color_order=plasma.COLOR_ORDER_RGB)

led_strip.start()

candy_cane_sat = 0

time.sleep(2)

while True:
    
    candy_cane_list = []
    
    candy_cane_colour = uniform(0.93,1.01)
    #introduce a chance of selecting a non-red colour:
    if (randint(0,100) == 13):
        cand_cane_colour = uniform(0.01,0.93)

    for led in range (0, number_of_leds):
        led_strip.set_hsv(led, candy_cane_colour, candy_cane_sat, 0.4)
        candy_cane_list.append({"hue": candy_cane_colour, "sat": candy_cane_sat, "lumin": 0.4}) 
        time.sleep(0.125)
        if (led % 3 == 0):
            candy_cane_sat = (candy_cane_sat + 1)%2
        
    time.sleep(10)
    candy_count = 0
    
    while candy_count <= 150:
        for led in range (0,number_of_leds):
            led_strip.set_hsv(led, candy_cane_list[led]["hue"], candy_cane_list[led]["sat"], candy_cane_list[led]["lumin"])
        
        candy_cane_list.pop()     
        if candy_count < 100:
            new_sat = (candy_cane_list[2]["sat"] + 1)%2
            candy_cane_list.insert(0, {"hue": candy_cane_colour, "sat": new_sat, "lumin": 0.4})
        else:
            candy_cane_list.insert(0, {"hue": candy_cane_colour, "sat": 0, "lumin": 0})
        candy_count += 1
        #time.sleep(0.125)
        
    time.sleep(5)
    
    bulb_list = []
    
    #set a random number of colours
    number_of_bulbs = randint(3,6)
    #print("number of bulbs = " + str(number_of_bulbs))
    
    #set the random colours
    bulb_list = random_bulbs(number_of_bulbs)
        
    counter = 0
    flash_condition = 0
    flash_range = randint(1,10)
    #print("flash range = " + str(flash_range))
    flash_length = 0.25  
    
    led_chunk = randint(3,7)
    
    for led in range(0,number_of_leds):
        led_strip.set_hsv(led, bulb_list[led]["hue"], bulb_list[led]["sat"], bulb_list[led]["lumin"])
        bulb_list[led]["on_off"] = "on"
        if (led % led_chunk == 0):
            time.sleep(0.35)
    
    time.sleep(5)
        
    
    for i in range (1, 100):
        random_led = randint(0,49)
        if (bulb_list[random_led]["on_off"] == "off"):
            led_strip.set_hsv(random_led, bulb_list[random_led]["hue"], bulb_list[random_led]["sat"], bulb_list[random_led]["lumin"])
            bulb_list[random_led]["on_off"] = "on"
        else:
            led_strip.set_hsv(random_led, 0,0,0)
            bulb_list[random_led]["on_off"] = "off"
        time.sleep(0.02)
        
    time.sleep(0.5)

    while counter < 500:
        for led in range (0, number_of_leds):
            if (led%flash_range == flash_condition):
                if (bulb_list[led]["on_off"] == "off"):
                    led_strip.set_hsv(led, bulb_list[led]["hue"], bulb_list[led]["sat"], bulb_list[led]["lumin"])
                    bulb_list[led]["on_off"] = "on"
                else:
                    led_strip.set_hsv(led, 0,0,0)
                    bulb_list[led]["on_off"] = "off"
        if (counter % 25 == 0):
            flash_length = uniform(0.1,0.5)
            flash_range = randint(1,10)
            #print("flash range = " + str(flash_range))
            
        time.sleep(flash_length)
        counter += 1
        flash_condition = (flash_condition + 1)%flash_range