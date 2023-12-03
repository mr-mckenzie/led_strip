import plasma
from plasma import plasma_stick
import time
from random import uniform
from random import randint

number_of_leds = 50

def random_bulbs(number_of_colours):
    
    bulbs_list = []
    colours_list = []
    threshold = 1/number_of_colours
    
    for led in range(0, number_of_leds):
        bulbs_list.append({"led": led, "hue": 0, "sat": 0, "lumin": 0.5, "on_off": "off"})
    
    for colour in range(0, number_of_colours):
        colours_list.append({"hue": uniform((threshold*colour),(threshold*(colour+1))), "sat":uniform(0.4, 0.6)})
        
    #print("colours_list =  " + str(colours_list[0]) + str(colours_list[1]))
    
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
    
    candy_cane_colour = uniform(0.85,1.01)

    for led in range (0, number_of_leds):
        led_strip.set_hsv(led, candy_cane_colour, candy_cane_sat, 0.5)
        candy_cane_list.append({"hue": candy_cane_colour, "sat": candy_cane_sat, "lumin": 0.5}) 
        time.sleep(0.125)
        if (led % 3 == 0):
            candy_cane_sat = (candy_cane_sat + 1)%2
        
    time.sleep(15)
    candy_count = 0
    
    while candy_count <= 150:
        for led in range (0,number_of_leds):
            led_strip.set_hsv(led, candy_cane_list[led]["hue"], candy_cane_list[led]["sat"], candy_cane_list[led]["lumin"])
        
        candy_cane_list.pop()        
        if candy_count < 100:
            new_sat = (candy_cane_list[2]["sat"] + 1)%2
            candy_cane_list.insert(0, {"hue": 0.96, "sat": new_sat, "lumin": 0.5})
        else:
            candy_cane_list.insert(0, {"hue": 0, "sat": 0, "lumin": 0})
        candy_count += 1
        time.sleep(0.125)
        
    time.sleep(15)
    
    bulb_list = []
    
                #led_strip.set_hsv(led, 0.55, 0.75, 0.5)
                #led_strip.set_hsv(led, 0.96, 0.75, 0.5)
                #led_strip.set_hsv(led, 0.18, 0.75, 0.5)
                #led_strip.set_hsv(led, 0.4, 0.9, 0.5)
    
    #random number of colours
    number_of_bulbs = randint(2,11)
    
    bulb_list = random_bulbs(number_of_bulbs)
            
    time.sleep(1)
        
    counter = 0
    flash_condition = 0

    while counter < 150:
        for led in range (0, number_of_leds):
            #random_led = randint(0,number_of_leds - 1)
            #ledDetails = bulb_list[random_led]
            if (led%number_of_bulbs == flash_condition):
                if (bulb_list[led]["on_off"] == "off"):
                    led_strip.set_hsv(led, bulb_list[led]["hue"], bulb_list[led]["sat"], bulb_list[led]["lumin"])
                    bulb_list[led]["on_off"] = "on"
                else:
                    led_strip.set_hsv(led, 0,0,0)
                    bulb_list[led]["on_off"] = "off"
        time.sleep(0.25)
        counter += 1
        flash_condition = randint(0,number_of_bulbs-1)

