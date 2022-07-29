# Guidance message that occurs in command line when file is run (needs to be addressed):
# "PWMSoftwareFallback: To reduce servo jitter, use the pigpio pin factory.
# See https://gpiozero.readthedocs.io/en/stable/api_output.html#servo for more info"

from gpiozero import Servo
from time import sleep

servo_left = Servo(4)
servo_right = Servo(22)

while True:
    servo_left.min()
    servo_right.min()
    sleep(1)
    servo_left.mid()
    servo_right.mid()
    sleep(1)
    servo_left.max()
    servo_right.max()
    sleep(1)