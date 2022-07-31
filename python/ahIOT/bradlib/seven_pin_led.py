# https://www.youtube.com/watch?v=c7ebs0WU34w
# Seven Segment Display with RPi

import RPi.GPIO as GPIO
from time import sleep

def setup():
    GPIO.setwarnings(False)  # Do not show any warnings
    GPIO.setmode(GPIO.BCM)  # Programming the GPIO by BCM pin number
    
    # Initialize GPIO Pins as Outputs
    GPIO.setup(24, GPIO.OUT) # A
    GPIO.setup(25, GPIO.OUT)  # B
    GPIO.setup(17, GPIO.OUT) # C
    GPIO.setup(4, GPIO.OUT) # D
    GPIO.setup(22, GPIO.OUT) # E
    GPIO.setup(23, GPIO.OUT) # F
    GPIO.setup(18, GPIO.OUT) # G

    # String of characters storing PORT values for each digit
      

# Assigning GPIO logic by taking 'pin' value
def PORT(pin):
    if(pin&0x01 == 0x01):
        GPIO.output(24,1)            # if  bit0 of 8bit 'pin' is true, pull PIN13 high
    else:
        GPIO.output(24,0)            # if  bit0 of 8bit 'pin' is false, pull PIN13 low
    if(pin&0x02 == 0x02):
        GPIO.output(25,1)             # if  bit1 of 8bit 'pin' is true, pull PIN6 high
    else:
        GPIO.output(25,0)            #if  bit1 of 8bit 'pin' is false, pull PIN6 low
    if(pin&0x04 == 0x04):
        GPIO.output(17,1)
    else:
        GPIO.output(17,0)
    if(pin&0x08 == 0x08):
        GPIO.output(4,1)
    else:
        GPIO.output(4,0)   
    if(pin&0x10 == 0x10):
        GPIO.output(22,1)
    else:
        GPIO.output(22,0)
    if(pin&0x20 == 0x20):
        GPIO.output(23,1)
    else:
        GPIO.output(23,0)
    if(pin&0x40 == 0x40):
        GPIO.output(18,1)
    else:
        GPIO.output(18,0)

# Assigning the conditions
def loop():
    dat = [0x3F,0x06,0x5B,0x4F,0x66,0x6D,0x7D,0x07,0x7F,0x6F]
    while True:
        # For even numbers
        for x in range(10):
            if x % 2 == 0:
                pin = dat[x]
                PORT(pin)
                sleep(0.8)
        sleep(1.2)

        # For odd numbers
        for y in range(10):
            if y % 2 != 0:
                pin1 = dat[y]
                PORT(pin1)
                sleep(0.8)
        sleep(1.2)

        # For 0-9 numbers
        for z in range(10):
            pin2 = dat[z]
            PORT(pin2)
            sleep(0.8)
        sleep(1.2)

# To destroy/clean-up all the pins
def destroy():     
	GPIO.cleanup()              

if __name__ == '__main__':
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        print("Keyboard Interrupt Detected")
        destroy()