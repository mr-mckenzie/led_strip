import plasma
from plasma import plasma_stick
import time
from random import random, uniform

#number of LEDs
number_of_leds = 50

frames_per_second = 60

# WS2812 / NeoPixel™ LEDs
led_strip = plasma.WS2812(number_of_leds, 0, 0, plasma_stick.DAT, color_order=plasma.COLOR_ORDER_RGB)

random_colour = 360 * random()

upper_led = 48
lower_led = 44

led_strip.start(frames_per_second)

spark = False
spark_start = 0
spark_position = 0
spark_chance = 0
    
while True:
    x = 0
    led_strip.set_hsv(upper_led,0,0,0)
    while x < 80:
        for i in range(lower_led, upper_led):
            random_sat = uniform(0.4,1)
            random_val = random()

            led_strip.set_hsv(i, random_colour, random_sat, random_val)

        if spark == False:
            spark_chance = random()
            if (round(spark_chance, 2) > 0.8):
                print('spark')
                spark = True
                spark_colour = random() * 360
                spark_sat = uniform(0.4,1)
                spark_val = 1
                spark_offset = 1
                if round(spark_chance > 0.9):
                    spark_start = lower_led - 1
                    spark_position = lower_led - 1
                else:
                    spark_start = upper_led + 1
                    spark_position = upper_led + 1
                    spark_offset = -1
        if spark == True and x%1 == 0:
            led_strip.set_hsv(spark_position, random_colour, spark_sat, spark_val)
            if abs(spark_start - spark_position) > 0:
                led_strip.set_hsv(spark_position + spark_offset, 0,0,0)
            if abs(spark_start - spark_position) <= 3:
                    spark_position -= spark_offset
                #print('spark continues')
            else:
                led_strip.set_hsv(spark_position+spark_offset,0,0,0)
                led_strip.set_hsv(spark_position,0,0,0)
                spark = False
                #print('spark ends')
        if x == 79:
                led_strip.set_hsv(spark_position+spark_offset,0,0,0)
                led_strip.set_hsv(spark_position,0,0,0)
        time.sleep(0.08)
        x += 1
    lower_led -= 1
    upper_led -= 1
    print('cycle complete')
    
    #something breaks here!