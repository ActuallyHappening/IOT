import json
from .lib.AIO import aio
from .lib.ThermalSensor.Extract_raw import iterate, print_frame

def main():
  while True:
    try:
      loaded = aio.receive_stream()
      data = json.loads(loaded)
    except json.JSONDecodeError as exc:
      print(f"(Error: Received stream bad: {exc}")
      continue
    iterate(print_frame, data["stream"])

if __name__ == "__main__":
  main()