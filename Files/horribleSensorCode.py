import time
import board
import adafruit_hcsr04
import neopixel
import simpleio

sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.D5, echo_pin=board.D6)
dot = neopixel.NeoPixel(board.NEOPIXEL, 1)
AHHH = sonar.distance

while True:
    print("well SOMETHING is running")
    try:
        print((sonar.distance,))
        AHHH = sonar.distance
    except RuntimeError:
        print("N/A")
    if AHHH >= 5 and AHHH < 20:
        red = simpleio.map_range(distance, 5, 20, 255, 0)
        blue = simpleio.map_range(distance, 5, 20, 0, 255)
        green = 0
    if AHHH >= 20 and AHHH < 35:
        red = 0
        blue = simpleio.map_range(distance, 5, 20, 255, 0)
        green = simpleio.map_range(distance, 5, 20, 0, 255)
    dot.fill(red, blue, green)

    time.sleep(0.1)