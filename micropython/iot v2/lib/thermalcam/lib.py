
import time
# import board
import machine
from machine import SoftI2C
from . import cam_lib as adafruit_mlx90640

print("Initializing Thermal Camera ...")
print(adafruit_mlx90640)

scl = machine.Pin(22)
sda = machine.Pin(21)

class CoolI2C(SoftI2C):
    """Used to implement a CircuitPython compatible i2c"""
    def try_lock(self):
        return True
    def unlock(self):
        pass

def attempt():
  while True:
    try:
      main()
    except Exception as e:
      print(f"Exception {e}")
      time.sleep(1)

def main():
  i2c = CoolI2C(scl=scl, sda=sda)

  try: mlx = adafruit_mlx90640.MLX90640(i2c)
  except Exception as e:
    print(f"Failed to initialize MLX90640 {e}")
    return
  print("MLX addr detected on I2C", [hex(i) for i in mlx.serial_number])

  # if using higher refresh rates yields a 'too many retries' exception,
  # try decreasing this value to work with certain pi/camera combinations
  mlx.refresh_rate = adafruit_mlx90640.RefreshRate.REFRESH_2_HZ

  frame = [0] * 768
  while True:
      try:
          mlx.getFrame(frame)
      except ValueError:
          # these happen, no biggie - retry
          continue

      for h in range(24):
          for w in range(32):
              t = frame[h*32 + w]
              print("%0.1f, " % t, end="")
          print()
      print()