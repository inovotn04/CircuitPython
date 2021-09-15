# CircuitPython

## Table of Contents
* [Table of Contents](#TableOfContents)
* [Hello_CircuitPython](#Hello_CircuitPython)
* [CircuitPython_Servo](#CircuitPython_Servo)
* [CircuitPython_LCD](#CircuitPython_LCD)
* [NextAssignmentGoesHere](#NextAssignment)
---

## Hello_CircuitPython

### Description & Code
Description goes here

Here's how you make code look like code:

```python

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
```


### Evidence
![Look at it go!! So many random colors...](https://github.com/jmuss07/Circuit-Python/blob/main/Images/Random_Color.gif?raw=true)

image credit goes to [Josie Muss](https://github.com/jmuss07/Circuit-Python)

### Reflection
Twas' but making a neopixel blink, no challenges were encountered. Just turn down the brightness so it doesn't burn out.




## CircuitPython_Servo

### Description & Code

```python
import board
import servo
import time
import pwmio
import touchio
pwm = pwmio.PWMOut(board.A2, duty_cycle=2 ** 15, frequency=50)

my_servo = servo.Servo(pwm)

touchA3 = touchio.TouchIn(board.A3)
touchA4 = touchio.TouchIn(board.A4)

while True:
    if touchA3.value:
        print("A3 Touch")
        for angle in range(0, 180, 5):
            my_servo.angle = angle
        time.sleep(0.3)
    if touchA4.value:
        print("A4 Touch")
        for angle in range(180, 0, -5):
            my_servo.angle = angle
        time.sleep(0.3)

```

### Evidence
![Silly Servos](https://github.com/inovotn04/CircuitPython/blob/main/Images/CapacitivePic1.jpg?raw=true)
![Wow such servo such capacitive touch](https://github.com/inovotn04/CircuitPython/blob/main/Images/CapacitivePic2.jpg?raw=true)
### Wiring

### Reflection




## CircuitPython_LCD

### Description & Code

```python
Code goes here

```

### Evidence

### Wiring

### Reflection





## NextAssignment

### Description & Code

```python
Code goes here

```

### Evidence

### Wiring

### Reflection
