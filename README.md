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


## CircuitPython Distance Sensor

### Description & Code
Uses the HCSR04 to find the distance and translate said distance to an RGB value on the neopixel. I used the "map" function from the simpleio library to translate it into an RGB value:
```python
red = int(simpleio.map_range(distance, 5, 20, 255, 0))
```
Otherwise the code is pretty much a matter of coordinating all those values, and getting the distance with
```python
distance = sonar.distance
```
which is remarkably easy.
### Evidence
![Gross Little GIF](https://github.com/inovotn04/CircuitPython/blob/main/Images/DistanceSensorEvidence.gif?raw=true)
### Wiring
<img src="https://github.com/Jhouse53/CircuitPython/blob/main/GIF%20and%20Images/UltraSonicSensor%20wiring.PNG?raw=true" width="400">
Image credit goes to [Benton House](https://github.com/Jhouse53/CircuitPython)
### Reflection
DEFINITELY had some problems with this one. For the whole time my code was being frustrating and it would stop working every time that I actually got a distance value. It took a lot of skillful use of the serial monitor using the "print" function in order to deduce exactly what was wrong with it. In the end the main problem I was having is that most of the RGB values returned a 'float' value instead of an integer (the numbers had decimals in them) and apparently the neopixel does not work with float values. All it took was adding that little 'int' at the front of the line of code which translated the distance into RGB to fix it.
P.S. also make sure your 
```python
dot.fill((value))
``` 
has two parentheses in it.


## CircuitPython Photointerrupter

### Description & Code
Thank you [Ghislain Ventre](https://github.com/gventre04/CircuitPython/blob/master/photointerrupter.py) on github for the code. Had to be adapted a bit though, as it's rather outdated and not perfect for the assignment.
Uses a counter and if statements as opposed to time.sleep so a photointerrupter is able to count the amount of times it has been interrupted, while still having the same effect as a delay. Also flickers the neopixel on the board every time it is interrupted.
```python
start = time.time()
while True:
    photo = interrupter.value
    if photo and not state:
            counter += 1
    state = photo
```
This code looks real nice doesn't it

### Evidence
![PhotoPain](https://github.com/inovotn04/CircuitPython/blob/main/Images/PhotoInterrupterGIF.gif?raw=true)

### Wiring


### Reflection
Biggest lesson learned from this is that life is much easier when using other people's code. Not only did it save me a lot of time but simply seeing the code helped me understand how it was used. Make sure you don't mess up your photointerrupter wiring though.

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
