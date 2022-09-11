from gpiozero import LED
green = LED(14) # Working at all (typically script loaded)
red = LED(15) # Not working at all

yellow = LED(27) # Collecting from camera
blue = LED(17) # Transmitting data

green.blink(0.5, 0, 1, False)
red.off()
blue.off()
yellow.off()

try:
  blue.on()
  from firebase import send_firebase
  blue.off()
except Exception as exc:
  red.on()
  print(f"Exc while importing firebase: {exc}")
  blue.blink(0.5, 0, 1, False)
  raise SystemExit(69)
finally:
  red.on()
  green.off()
  blue.on()
  yellow.off()

try:
  from lib.ThermalSensor.Extract_raw import get_frame
except Exception as exc:
  red.on()
  print(f"Exc while importing Extract_raw: {exc}")
  yellow.blink(0.5, 0, 1, False)
  raise SystemExit(420)
finally:
  red.on()
  green.off()
  yellow.on()
  blue.off()  

while True:
  try:
    yellow.on()
    d = get_frame()
    yellow.off()
    blue.on()
    send_firebase(d)
    blue.off()
  except Exception as exc:
    red.blink(0.5, 0.5, 2)
    print(f"Error caught top level: {exc}")
    