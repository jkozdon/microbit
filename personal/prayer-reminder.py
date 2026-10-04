# Imports go at the top
from microbit import *
import music

set_volume(100)

notes = ['c4:1', 'e', 'g', 'e']
delta =  60 * 1000
next_time = running_time() + delta
step = 3 * 60 * 1000
x_pixels = 5
y_pixels = 5
num_pixels = x_pixels * y_pixels
extra_time = 0
brightness = 5
extra_brightness = 0
while True:
    time = running_time()
    set_pixels = 25
    if time < next_time:
        set_pixels = int(25 * ((time + delta - next_time) / delta))
    pixel = 0
    for y in range(0, y_pixels):
        for x in range(0, x_pixels):
            display.set_pixel(x, y, min(brightness + extra_brightness, 9) if pixel < set_pixels else 0)
            pixel += 1
    if button_a.was_pressed() or button_b.was_pressed():
        next_time = time + delta
        extra_brightness = 0
        extra_time = 0 
    if next_time + extra_time < running_time():
        music.play(notes)
        extra_time += step
        extra_brightness += 1