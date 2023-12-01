import plasma
from plasma import plasma_stick
import time
from random import uniform
from random import randint

number_of_leds = 50

led_strip = plasma.WS2812(number_of_leds, 0, 0, plasma_stick.DAT, color_order=plasma.COLOR_ORDER_RGB)

led_strip.start()

candyCaneSat = 0
candyCaneList = []


for led in range (0, number_of_leds):
    led_strip.set_hsv(led, 0.96, candyCaneSat, 0.5)
    time.sleep(0.125)
    if (led % 7 == 0):
        if (candyCaneSat == 0):
            candyCaneSat = 1
        else:
            candyCaneSat = 0
    
time.sleep(45)

for led in range (0, number_of_leds):
    if (led % 4 == 0):
        led_strip.set_hsv(led, 0.96, 0.75, 0.5)
        candyCaneList.append({"hue": 0.96, "sat": 0.75, "lumin": 0.5, "on_off": "on"}) 
    elif (led % 4 == 1):
        led_strip.set_hsv(led, 0.18, 0.75, 0.5)
        candyCaneList.append({"hue": 0.18, "sat": 0.75, "lumin": 0.5, "on_off": "on"})
    elif (led % 4 == 2):
        led_strip.set_hsv(led, 0.4, 0.9, 0.5)
        candyCaneList.append({"hue": 0.4, "sat": 0.9, "lumin": 0.5, "on_off": "on"})
    else:
        led_strip.set_hsv(led, 0.55, 0.75, 0.5)
        candyCaneList.append({"hue": 0.55, "sat": 0.75, "lumin": 0.5, "on_off": "on"})
        time.sleep(0.125)


while True:
    random_led = randint(0,number_of_leds - 1)
    ledDetails = candyCaneList[random_led]
    if (ledDetails["on_off"] == "off"):
        led_strip.set_hsv(random_led, candyCaneList[random_led]["hue"], candyCaneList[random_led]["sat"], candyCaneList[random_led]["lumin"])
        candyCaneList[random_led]["on_off"] = "on"
    else:
        led_strip.set_hsv(random_led, 0,0,0)
        candyCaneList[random_led]["on_off"] = "off"
    time.sleep(0.25)  
