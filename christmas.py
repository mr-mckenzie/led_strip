import plasma
from plasma import plasma_stick
import time
from random import uniform
from random import randint

number_of_leds = 50

led_strip = plasma.WS2812(number_of_leds, 0, 0, plasma_stick.DAT, color_order=plasma.COLOR_ORDER_RGB)

led_strip.start()

candy_cane_sat = 0
candy_cane_list = []
bulb_list = []

time.sleep(2)

while True:

    for led in range (0, number_of_leds):
        led_strip.set_hsv(led, 0.96, candy_cane_sat, 0.5)
        candy_cane_list.append({"hue": 0.96, "sat": candy_cane_sat, "lumin": 0.5}) 
        time.sleep(0.125)
        if (led % 7 == 0):
            candy_cane_sat = (candy_cane_sat + 1)%2
        
    time.sleep(15)
    candy_count = 0
    
    while candy_count < 20:
        for led in range (0,number_of_leds):
            led_strip.set_hsv(led, candy_cane_list[led]["hue"], candy_cane_list[led]["sat"], candy_cane_list[led]["lumin"])
        
        for led in range(0,7):
            candy_cane_list.pop()        
            if candy_count < 12:
                new_sat = (candy_cane_list[6]["sat"] + 1)%2
                candy_cane_list.insert(0, {"hue": 0.96, "sat": new_sat, "lumin": 0.5})
            else:
                candy_cane_list.insert(0, {"hue": 0, "sat": 0, "lumin": 0})
        candy_count += 1
        time.sleep(0.5)
        
    time.sleep(15)

    for led in range (0, number_of_leds):
        if (led % 4 == 0):
            led_strip.set_hsv(led, 0.96, 0.75, 0.5)
            bulb_list.append({"hue": 0.96, "sat": 0.75, "lumin": 0.5, "on_off": "on"}) 
        elif (led % 4 == 1):
            led_strip.set_hsv(led, 0.18, 0.75, 0.5)
            bulb_list.append({"hue": 0.18, "sat": 0.75, "lumin": 0.5, "on_off": "on"})
        elif (led % 4 == 2):
            led_strip.set_hsv(led, 0.4, 0.9, 0.5)
            bulb_list.append({"hue": 0.4, "sat": 0.9, "lumin": 0.5, "on_off": "on"})
        else:
            led_strip.set_hsv(led, 0.55, 0.75, 0.5)
            bulb_list.append({"hue": 0.55, "sat": 0.75, "lumin": 0.5, "on_off": "on"})
            time.sleep(0.75)
            
    time.sleep(5)
        
    counter = 0

    while counter < 75:
        random_led = randint(0,number_of_leds - 1)
        ledDetails = bulb_list[random_led]
        if (ledDetails["on_off"] == "off"):
            led_strip.set_hsv(random_led, bulb_list[random_led]["hue"], bulb_list[random_led]["sat"], bulb_list[random_led]["lumin"])
            bulb_list[random_led]["on_off"] = "on"
        else:
            led_strip.set_hsv(random_led, 0,0,0)
            bulb_list[random_led]["on_off"] = "off"
        time.sleep(0.35)
        counter += 1
