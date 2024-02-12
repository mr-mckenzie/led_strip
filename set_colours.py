from random import uniform, choice

def get_gradient(number_of_leds):
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
    
    return leds

def get_marbled_colour(number_of_leds):

    random_hue = uniform(0.1,1.1)
    random_sat = uniform(0.4,1)

    leds = []
    for led in range(0, number_of_leds):
        leds.append({
            'hue': uniform(random_hue-0.05,random_hue+0.05),
            'sat': random_sat})
    
    return leds

def get_two_colours(number_of_leds):

    random_sat = uniform(0.4,1)
    random_colour_one = uniform(0,1)
    random_colour_two = uniform(0,1)

    leds = []
    for led in range(0, number_of_leds):
        leds.append({
            'hue': uniform(0,2),
            'sat': random_sat})
    
    return leds

def get_colour_bands(number_of_leds, number_of_bands):
    
    if number_of_bands <= 0:
        number_of_bands = 1

    random_sat = uniform(0.4,1)
    random_colour = uniform(0,1)
    colour_choices = []
    interval = 1/number_of_bands
    for n in range(0,number_of_bands):
        colour_choices.append(random_colour+(n*interval))

    leds = []
    for led in range(0, number_of_leds):
        leds.append({
            'hue': choice(colour_choices),
            'sat': random_sat})
    
    return leds
