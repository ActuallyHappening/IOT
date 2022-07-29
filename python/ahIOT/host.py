import json
from typing import List
from .lib.AIO import aio
from .lib.ThermalSensor.Process_raw import print_frame

def _load(strict=True):
  data = None
  try:
    data = aio.receive_stream_data()
  except json.JSONDecodeError as exc:
    print(f"(Error: Received stream bad: {exc}")
    print(f"{loaded=}")
    aio.host_status_send("JSONDecodeError - host.py")
    if strict:
      raise TypeError(f"(Error: JSONDecodeError - host.py :: Strict=True)")
  return data

def _load_stream(stream, *, strict=False):
  """Takes _load() and returns the parsed stream"""
  if type(stream) is not list:
    try:
      stream = json.loads(stream)
    except json.JSONDecodeError as exc:
      print("(Error while loading stream {exc=})")
      if strict: raise TypeError(f"Expected type list, got stream {stream=}")
  return stream

def _print(stream: List[int]):
  print_frame(stream)

def _ping(*x, **y):
  aio.host_ping(*x, **y)

def step() -> bool:
  _ping()
  try:
    raw = _load(strict=True)
    data = _load_stream(raw, strict=True)
  except TypeError as exc:
    print(f"(Error while gathering stream (host.py): {exc})")
    return False
  if data is True:
    print("(Error: No data received)")
    return False
  _print(data)
  return True

def main():
  print("Beginning host ...")
  while True:
    step()

if __name__ == "__main__":
  main()