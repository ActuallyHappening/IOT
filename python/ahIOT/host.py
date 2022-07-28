import json
from typing import List
from .lib.AIO import aio
from .lib.ThermalSensor.Process_raw import print_frame

def _load():
  data = False
  try:
    loaded = aio.receive_stream_data()
    data = json.loads(loaded)
  except json.JSONDecodeError as exc:
    print(f"(Error: Received stream bad: {exc}")
    print(f"{loaded=}")
    aio.host_status_send("JSONDecodeError - host.py")
  return data

def _print(stream: List[int]):
  print_frame(frame=stream)

def _ping(*x, **y):
  aio.host_ping(*x, **y)

def step():
  _ping()
  data = _load()
  if data is False:
    print("(Error: No data received)")
    return
  _print(data)

def main():
  print("Beginning host ...")
  while True:
    step()

if __name__ == "__main__":
  main()