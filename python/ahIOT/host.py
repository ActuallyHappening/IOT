import json
from typing import List
from .lib.AIO import aio
from .lib.ThermalSensor.Process_raw import print_frame

def _load(strict=True):
  data = None
  try:
    loaded = aio.receive_stream_data()
    data = json.loads(loaded)
  except json.JSONDecodeError as exc:
    print(f"(Error: Received stream bad: {exc}")
    print(f"{loaded=}")
    aio.host_status_send("JSONDecodeError - host.py")
    if strict:
      raise TypeError(f"(Error: JSONDecodeError - host.py :: Strict=True)")
  return data

def _load_stream(data, *, strict=False):
  """Takes _load() and returns the stream"""
  if data is None:
    raise TypeError("(Error: No data received)")
  if "stream" not in data:
    raise TypeError("(Error: No stream found in data)")
  stream = data["stream"]
  if type(stream) is not list:
    raise TypeError(f"Expected type list, got {type(stream)} in stream ({stream})")
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