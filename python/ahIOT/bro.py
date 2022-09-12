import time
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
  import busio
  import board
  import adafruit_mlx90640 as adafruit_mlx90640
except Exception as exc:
  red.on()
  print(f"Exc while importing raw extracting libraries: {exc}")
  yellow.blink(0.5, 0, 1, False)
  raise SystemExit(420)
finally:
  red.on()
  green.off()
  yellow.on()
  blue.off()

_mlx: adafruit_mlx90640.MLX90640 = None
def _init():
  global _mlx
  if _mlx is not None: return
  
  while True:
    i2c = busio.I2C(board.SCL, board.SDA, frequency=5_000_000)
    try:
      _mlx = adafruit_mlx90640.MLX90640(i2c)
    except ValueError as exc:
      print(f"Camera needs to be connected - {exc}")
      time.sleep(1)
    else:
      break

def get_frame():
  while True:
    _init()
    frame = [0] * (24*32)
    try:
      _mlx.getFrame(frame)
    except ValueError as exc:
      print(f"Camera frame error - {exc}")
      red.on()
    else:
      red.off()
      return frame

green.on()
red.off()
yellow.off()
blue.off()
while True:
  _init()
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
    