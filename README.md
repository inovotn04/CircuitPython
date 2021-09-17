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
Makes the on-board neopixel on the metro express blink, in my case, blink different, random, colours. I used a bunch of random values between 0, 255 to control each of the colour values with integers hooked up to 

```python
random.randint(0, 255)
```
Also it should be noted I turned down the brightness with 
```python
dot.brightness = 0.1
```
so it was a little less blinding and less likely to burn out. Other than that, it was basically the same as coding an off-board LED on an arduino, except with specific colour values and mildly different code.

### Evidence
![Look at it go!! So many random colors...](https://github.com/jmuss07/Circuit-Python/blob/main/Images/Random_Color.gif?raw=true)

image credit goes to [Josie Muss](https://github.com/jmuss07/Circuit-Python)

### Reflection
Twas' but making a neopixel blink, no challenges were encountered. Just turn down the brightness so it doesn't burn out.




## CircuitPython_Servo

### Description & Code
Makes a 180 degree micro servo move in different directions based on interacting with wires connected to different ports. Uses the 'touchio' and 'servo' libraries which allow you to take input from interactions with the input ports, and of course move the servo. Here's a sample of the kinda most vital part of code:
```python
while True:
    if touchA3.value:
        print("A3 Touch")
        for angle in range(0, 180, 5):
            my_servo.angle = angle
        time.sleep(0.3)
```

### Evidence
![Silly Servos](https://github.com/inovotn04/CircuitPython/blob/main/Images/CapacitivePic1.jpg?raw=true)
![Wow such servo such capacitive touch](https://github.com/inovotn04/CircuitPython/blob/main/Images/CapacitivePic2.jpg?raw=true)
### Wiring
![Simple servo wiring!](https://github.com/jmuss07/Circuit-Python/blob/main/Images/servo.png?raw=true)

image credit goes to [Josie Muss](https://github.com/jmuss07/Circuit-Python)

### Reflection
Had some trouble in regards to code, don't remember what I did exactly to fix it, but just using previous servo code worked, just make sure to reuse code to prevent further problems.



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
