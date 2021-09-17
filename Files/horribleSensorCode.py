import time
import board
import adafruit_hcsr04
import neopixel
sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.D5, echo_pin=board.D6)

while True:
    try:
        print((sonar.distance,))
    except RuntimeError:
        print("N/A")
    if distance>=5 and distance<20:
        blue=simpleio.map_range(distance,5,20,0,255)
    if distance>=20 and distance<35:

    time.sleep(0.1)