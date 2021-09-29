import time
import board
import digitalio
import neopixel

interrupter = digitalio.DigitalInOut(board.D7)
interrupter.direction = digitalio.Direction.INPUT
interrupter.pull = digitalio.Pull.UP

dot = neopixel.NeoPixel(board.NEOPIXEL, 1)
dot.brightness = 0.1
counter = 0

photo = False
state = False

max = 4
start = time.time()
while True:
    photo = interrupter.value
    if photo and not state:
        counter += 1
        dot.fill((0, 255, 0))
    state = photo
    remaining = max - time.time()

    if remaining <= 0:
        print("Interrupts:", str(counter))
        max = time.time() + 4
        dot.fill((170, 0, 0))