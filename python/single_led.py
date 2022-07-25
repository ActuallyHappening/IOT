from gpiozero import LED
import time

K = int(input("Sleep for: "))
led = LED(14)

while True:
    led.toggle()
    time.sleep(K)
    led.toggle()
    time.sleep(K)