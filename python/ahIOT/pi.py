from __future__ import annotations
import json
from random import randrange
import sys
from typing import Callable, List, Tuple, Type, TypeVar

from ahIOT.firebase import send_firebase
try:
  from .lib.AIO import aio
  from .lib.ThermalSensor.Extract_raw import get_frame
except NotImplementedError:
  print("Not implemented for this platform :(")

_isFirebase = False

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
  # print(f"[Debug: pi.py] Frame: {frame=}")
  return True, frame

def _send(data):
  # print(f"[Debug: pi.py] Sending data: {data=}")
  try:
    aio.send_stream_data(data)
    return True
  except TypeError:
    print('JSONDecodeError: Cannot jsonify data :(')
    aio.pi_status_send("JSONDecodeError - pi.py")
    return False

def step():
  # Step for uploading data
  if not _isFirebase:
    aio.pi_ping()
    _step(
      method = _method,
      callback = _send,
    )
  else:
    if _isFirebase: _step(
      method = _method,
      callback = send_firebase,
    )

def main():
  print("Beginning pi ...")
  if sys.argv[1] == "firebase":
    global _isFirebase
    _isFirebase = True
    print("Using firebase!")
  while True: 
    step()

if __name__ == "__main__":
  main()
