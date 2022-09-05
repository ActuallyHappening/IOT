import json
from typing import Callable, Tuple, Type, TypeVar
from .lib.AIO import aio
from .lib.ThermalSensor.Extract_raw import get_frame


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

def _sendFirebase(data):
  import requests
  from dotenv import dotenv_values
  import os
  env_variables = dotenv_values() | os.environ
  r = requests.put(env_variables["FIREBASE_ENDPOINT"], json={"json":json.dumps(data)})

def step():
  aio.pi_ping()
  # Step for uploading data
  if not _isFirebase: _step(
    method = _method,
    callback = _send,
  )
  # Other steps could be added below, such as 8x8 LED matrix
  if _isFirebase: _step(
    method = _method,
    callback = _send,
  )

def main():
  print("Beginning pi ...")
  while True: 
    step()

if __name__ == "__main__":
  main()
