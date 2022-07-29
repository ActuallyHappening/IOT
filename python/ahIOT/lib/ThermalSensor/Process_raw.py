''' from .  '''
from . import Extract_raw as raw
from .Extract_raw import get_frame
from rich import pretty as p
from rich import print as rprint
p.install()

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
    v = int(rightMin + (valueScaled * rightSpan))
    return max(min(v, rightMax), rightMin)

def get_ascii_char_from_num(num):
  """Put in number from 15-45 and get back ascii char from ascii_chars"""
  charNum = map_num_ranges(num)
  # print(f"{charNum=}")
  return ascii_chars[charNum]

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

def iterate_frame(frame):
  for y in range(24):
    for x in range(32):
      yield frame[y*32 + x], x, y

def iterate(f, frame=None):
  if frame == None:
    frame = get_frame()
    if frame == None: return frame # retry, return None
  for value, x, y in iterate_frame(frame):
    f(value, x, y, frame)