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