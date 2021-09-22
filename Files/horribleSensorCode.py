import time
import board
import adafruit_hcsr04
import neopixel
import simpleio

sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.D5, echo_pin=board.D6)
dot = neopixel.NeoPixel(board.NEOPIXEL, 1)
dot.brightness = 0.1

while True:
    try:
        distance = sonar.distance
        print((sonar.distance,))
        if distance >= 5 and distance < 20:
            red = int(simpleio.map_range(distance, 5, 20, 255, 0))
            blue = int(simpleio.map_range(distance, 5, 20, 0, 255))
            green = int(simpleio.map_range(distance, 5, 20, 0, 0))
        if distance >= 20 and distance < 35:
            red = int(simpleio.map_range(distance, 20, 35, 0, 0))
            blue = int(simpleio.map_range(distance, 20, 35, 255, 0))
            green = int(simpleio.map_range(distance, 20, 35, 0, 255))
        print(red, green, blue)
        dot.fill((red, green, blue))
    except RuntimeError:
        print("Sensor bad :(")
    time.sleep(0.1)