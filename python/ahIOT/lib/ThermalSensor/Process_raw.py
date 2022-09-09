''' from .  '''
from typing import List, Tuple
from . import Extract_raw as raw
from .Extract_raw import get_frame
pretty_print = print
try:
  from rich import pretty as p
  from rich import print as _pretty_print
  pretty_print = _pretty_print
except ImportError:
  print(f"Warning: Cannot find package `rich`, printing is now not as pretty")
p.install()

ascii_chars = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\\|()1{}[]?-_+~<>i!lI;:,\"^`'."

lowest_temp = 15
highest_temp = 45

defaultDimensions = (32, 24)

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
  assert len(list) > 0 # Div by 0 when calculating average
  assert min(list) - max(list) != 0 # Div by 0 when calculating / range
  
  avg = sum(list) / len(list)
  colour = generate_colour(temp, avg=avg)
  beginningColours = f"[/{previous}][{colour}]" if previous is not colour else ""
  beginningColours = f"[{colour}]" if previous is None else beginningColours
  endingColours = f"[/{colour}]" if final else ""
  chosenChar = get_ascii_char_from_num(int(temp), min=min(list), max=max(list))
  return f"{beginningColours}{chosenChar}{endingColours}"

def print_frame_value(value, x, y, list, *, previous=None, dimensions=defaultDimensions, final=False):
  assert value in list
  final = final or bool(x == dimensions[0]-1 and y == dimensions[1]-1)
  toPrint = get_char(value, list=list, previous=previous, final=final)
  pretty_print(toPrint, end="")
  if x == dimensions[0]-1:
    print() # newline every line of chars
    if y == dimensions[1]-1:
      print() # newline at end of frame

def iterate_frame(frame, *, dimensions=defaultDimensions):
  for y in range(dimensions[1]):
    for x in range(dimensions[0]):
      yield frame[y*dimensions[0] + x], x, y

def iterate(f, frame:List[int]|None=None, *, dimensions:Tuple[int, int]|None=defaultDimensions):
  if frame is None:
    frame = get_frame()
    if frame is None: return frame # retry, return None
  if dimensions is None and len(frame) == defaultDimensions[0] * defaultDimensions[1]:
    dimensions = defaultDimensions
  for value, x, y in iterate_frame(frame, dimensions=dimensions):
    f(value, x, y, frame, dimensions=dimensions)

def print_frame(frame=None):
  iterate(print_frame_value, frame=frame)