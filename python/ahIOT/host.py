import json
from .lib.AIO import aio
from .lib.ThermalSensor.Extract_raw import iterate, print_frame

def _load():
  try:
    loaded = aio.receive_stream()
    data = json.loads(loaded)
  except json.JSONDecodeError as exc:
    print(f"(Error: Received stream bad: {exc}")
    aio.status_send_code("JSONDecodeError - host.py")

def _print(stream):
  iterate(print_frame, stream)

def _ping():
  aio.host_ping()

def step():
  _ping()
  data = _load()
  _print(data)

def main():
  print("Beginning host ...")
  while True:
    step()

if __name__ == "__main__":
  main()