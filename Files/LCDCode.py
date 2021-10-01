import board
import time
import touchio

from lcd.lcd import LCD
from lcd.i2c_pcf8574_interface import I2CPCF8574Interface

touchA2 = touchio.TouchIn(board.A2)
touchA4 = touchio.TouchIn(board.A4)
counter = 0
salad1 = 0
salad2 = 0
direction = 0
# get and i2c object
i2c = board.I2C()
# some LCDs are 0x3f... some are 0x27.
lcd = LCD(I2CPCF8574Interface(i2c, 0x3f), num_rows=2, num_cols=16)

lcd.print("HUMANITY WILL   FALL")
while True:
    if touchA2.value and salad1 == 0:
        print("A2 Touch")
        if direction == 1:
            print(direction)
            counter += 1
            lcd.clear()
            lcd.print(str(counter))
            lcd.print("\nCounting Up")
        if direction == 0:
            print(direction)
            counter -= 1
            lcd.clear()
            lcd.print(str(counter))
            lcd.print("\nCounting Down")
        time.sleep(0.1)
    salad1 = touchA2.value
    if touchA4.value and salad2 == 0 and direction == 0:
        direction = 1
        print("A4 Touch")
        lcd.clear()
        lcd.print("Direction switched")
        time.sleep(0.1)
    if touchA4.value and salad2 == 0 and direction == 1:
        direction = 1
        print("A4 Touch")
        lcd.clear()
        lcd.print("Direction switched")
        time.sleep(0.1)
    salad2 = touchA4.value