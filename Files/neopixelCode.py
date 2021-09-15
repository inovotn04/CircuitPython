import board
import neopixel
import time
import random

dot = neopixel.NeoPixel(board.NEOPIXEL, 1)

randvalue1 = 0
randvalue2 = 0
randvalue3 = 0

print("Make it red!")
dot.brightness = 0.1
while True:
    dot.fill((randvalue1, randvalue2, randvalue3))
    randvalue1 = random.randint(0, 255)
    randvalue2 = random.randint(0, 255)
    randvalue3 = random.randint(0, 255)
    print(randvalue1, randvalue2, randvalue3)
    time.sleep(1)