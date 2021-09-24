import time
import board
import digitalio

interrupter = digitalio.DigitalInOut(board.D7)
interrupter.direction = digitalio.Direction.INPUT
interrupter.pull = digitalio.Pull.UP

counter = 0

photo = False
state = False

max = 4
start = time.time()
while True:
    photo = interrupter.value
    if photo and not state:
            counter += 1
    state = photo

    remaining = max - time.time()

    if remaining <= 0:
        print("Interrupts:", str(counter))
        max = time.time() + 4