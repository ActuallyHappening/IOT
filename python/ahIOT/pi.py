import json
from typing import Callable, Tuple, TypeVar
from .lib.AIO import aio
from .lib.ThermalSensor.Extract_raw import get_frame

T_Data = TypeVar('T_Data')
def _step(
  method: Callable[[], Tuple[bool, T_Data]],
  callback: Callable[[T_Data], Tuple[bool]],
) -> bool:
  status, data = method()
  if status is False: return False
  finished_successfully = callback(data)
  if not finished_successfully: return False
  return True

def _method():
  frame = get_frame()
  if frame is None:
    return False
  return True, get_frame

def _send(data):
  try:
    aio.send_stream_data(data)
    return True
  except json.JSONDecodeError:
    print('JSONDecodeError: Cannot jsonify data :(')
    aio.pi_status_send_code("JSONDecodeError - pi.py")
    return False

def step():
  aio.pi_ping()
  # Step for uploading data
  _step(
    method = _method,
    callback = _send,
  )
  # Other steps could be added below, such as 8x8 LED matrix

def main():
  print("Beginning pi ...")
  while True: 
    step()

if __name__ == "__main__":
  main()
