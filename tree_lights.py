from pimoroni_i2c import PimoroniI2C
import plasma
from plasma import plasma_stick
import time
from random import choice, uniform, random


# # # # # # # # # # # # # #
# A Christmas Light Theme #
# # # # # # # # # # # # # #

# set number of LEDs
LEDS = 66

HUES = [0.07, #Orange
        0.35, #Green
        0.25, #Green
        0.77, #Purple
        0.85, #Purple
        1.00  #Red
        ]

# WS2812 / NeoPixel™ LEDs
led_strip = plasma.WS2812(LEDS, 0, 0, plasma_stick.DAT, color_order=plasma.COLOR_ORDER_RGB)

def smooth_adjust(input,lower_limit, upper_limit, sensitivity):
    adjusted_input = input + uniform(0,sensitivity)*choice([-1, 1])
    if (adjusted_input > upper_limit):
        return (input - uniform(0,sensitivity))
    elif (adjusted_input < lower_limit):
        return (input + uniform(0,sensitivity))
    else:
        return adjusted_input

# Start updating the LED strip
led_strip.start()

print("Merry Christmas!")

while True:
    
    colour = random()
    colour_spread = uniform(0.02,0.8)
    counter = 0
    LED_MAP = []
    sat_lower = 0.75
    sat_upper = 1
    v_lower = 0.4
    v_upper = 1
    
    for x in range(0,LEDS):
        LED_MAP.append(
        {"colour": colour+(uniform(0,colour_spread)*choice([-1, 1])),
        "sat": uniform(sat_lower, sat_upper),
        "v": uniform(v_lower, v_upper)
        })
        
    while (counter < 20):
        for i in range(0,LEDS):
            led_strip.set_hsv(i, LED_MAP[i]["colour"], LED_MAP[i]["sat"], LED_MAP[i]["v"])
            if i<LEDS-1:
                LED_MAP[i]["colour"] = LED_MAP[i+1]["colour"]
            else:
                LED_MAP[i]["colour"] = LED_MAP[0]["colour"]
            LED_MAP[i]["sat"] = smooth_adjust(LED_MAP[i]["sat"], sat_lower, sat_upper, 0.05)
            LED_MAP[i]["v"] = smooth_adjust(LED_MAP[i]["v"], v_lower, v_upper, 0.2)
        counter += 1
        time.sleep(1.25)
    

