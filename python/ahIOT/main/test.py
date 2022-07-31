from gpiozero import LED
from time import sleep
import segment7controller

i = 0
while True:
  segment7controller.display_char(str(i % 10))
  i += 1
  sleep(0.2)