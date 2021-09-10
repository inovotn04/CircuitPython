import board
import servo
import time
import pwmio

pwm = pwmio.PWMOut(board.A2, duty_cycle=2 ** 15, frequency=50)

my_servo = servo.Servo(pwm)

while True:
    for angle in range(0, 180, 5):
        my_servo.angle = angle
        print ("steeping")
        time.sleep(0.3)
    for angle in range(180, 0, -5):
        my_servo.angle = angle
        print ("slooping")
        time.sleep(0.3)