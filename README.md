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
Pictures / Gifs of your work should go here.  You need to communicate what your thing does.


### Reflection
Twas' but making a neopixel blink, no challenges were encountered. Just turn down the brightness so it doesn't burn out.




## CircuitPython_Servo

### Description & Code

```python
Code goes here

```

### Evidence

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
