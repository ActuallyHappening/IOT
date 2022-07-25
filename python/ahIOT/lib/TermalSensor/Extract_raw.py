# Source: https://docs.circuitpython.org/projects/mlx90640/en/latest/

import time
import board
import busio
import adafruit_mlx90640
from rich import pretty as p
from rich import print as rprint
p.install()

i2c = busio.I2C(board.SCL, board.SDA, frequency=800000)

mlx = adafruit_mlx90640.MLX90640(i2c)
print("MLX addr detected on I2C", [hex(i) for i in mlx.serial_number])

# if using higher refresh rates yields a 'too many retries' exception,
# try decreasing this value to work with certain pi/camera combinations
mlx.refresh_rate = adafruit_mlx90640.RefreshRate.REFRESH_2_HZ

ascii_chars = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\\|()1{}[]?-_+~<>i!lI;:,\"^`'."

lowest_temp = 15
highest_temp = 45

def map_num_ranges(value, leftMin=lowest_temp, leftMax=highest_temp, rightMin=0, rightMax=int(len(ascii_chars) - 1)):
    # Figure out how 'wide' each range is
    leftSpan = leftMax - leftMin
    rightSpan = rightMax - rightMin

    # Convert the left range into a 0-1 range (float)
    valueScaled = float(value - leftMin) / float(leftSpan)

    # Convert the 0-1 range into a value in the right range.
    return int(rightMin + (valueScaled * rightSpan))

def get_ascii_char_from_num(num):
  """Put in number from 15-45 and get back ascii char from ascii_chars"""
  charNum = map_num_ranges(num)
  print(f"{charNum=}")
  return ascii_chars[]

def get_char(temp, info):
  ctrlChar = "red" if temp > info["avg"] else "green"
  return f"[{ctrlChar}]{get_ascii_char_from_num(int(temp))}[/{ctrlChar}]"

def print_frame(value, x, y, l):
  avg = sum(l) / len(l)
  rprint(get_char(value, {
    "avg": avg
  }), end="")
  if x == 31:
    print()
    if y == 23:
      print()

def main():
  while True:
    iterate(print_frame)

def iterate_frame(frame):
  for y in range(24):
    for x in range(32):
      yield frame[y*32 + x], x, y

def iterate(f):
  frame = get_frame()
  if frame == None:
    return frame
  for value, x, y in iterate_frame(frame):
    f(value, x, y, frame)

def get_frame():
  frame = [0] * (24*32)
  try:
      mlx.getFrame(frame)
  except ValueError:
      # these happen, no biggie - retry
      print("(Error)")
      return None
  return frame

if __name__ == "__main__":
  main()