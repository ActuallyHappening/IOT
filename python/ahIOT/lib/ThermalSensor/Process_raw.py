''' from .  '''
from . import Extract_raw as raw
from .Extract_raw import get_frame
from rich import pretty as p
from rich import print as rprint
p.install()

ascii_chars = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\\|()1{}[]?-_+~<>i!lI;:,\"^`'."

lowest_temp = 15
highest_temp = 45

def map_num_ranges(value, leftMin, leftMax, rightMin=0, rightMax=int(len(ascii_chars) - 1)):
    # Figure out how 'wide' each range is
    leftSpan = leftMax - leftMin
    rightSpan = rightMax - rightMin

    # Convert the left range into a 0-1 range (float)
    valueScaled = float(value - leftMin) / float(leftSpan)

    # Convert the 0-1 range into a value in the right range.
    v = int(rightMin + (valueScaled * rightSpan))
    return max(min(v, rightMax), rightMin)

def get_ascii_char_from_num(num, *, min=lowest_temp, max=highest_temp):
  """Put in number from 15-45 and get back ascii char from ascii_chars"""
  if num < min:
    num = min
  if num > max:
    num = max
  charNum = map_num_ranges(num, min, max)
  # print(f"{charNum=}")
  return ascii_chars[charNum]

def generate_colour(temp, *, avg):
  return "red" if temp > avg else "green"

def get_char(temp, *, list, previous=None, final=False):
  assert len(list) > 0
  assert min(list) - max(list) != 0
  avg = sum(list) / len(list)
  colour = generate_colour(temp, avg=avg)
  beginningColours = f"[/{previous}][{colour}]" if previous is not colour else ""
  beginningColours = f"[{colour}]" if previous is None else beginningColours
  endingColours = f"[/{colour}]" if final else ""
  chosenChar = get_ascii_char_from_num(int(temp), min=min(list), max=max(list))
  return f"{beginningColours}{chosenChar}{endingColours}"

def print_frame_value(value, x, y, *, list, previous=None, dimensions=(32, 24), final=False):
  assert value in list
  toPrint = get_char(value, list=list, previous=previous, final=bool(x == dimensions[0]-1 and y == dimensions[1]-1))
  rprint(toPrint, end="")
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

def print_frame(frame=None):
  iterate(print_frame_value, frame=frame)