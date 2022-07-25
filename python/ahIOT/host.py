import json
from ahIOT.lib.AIO import Aio
from ahIOT.lib.ThermalSensor.Extract_raw import iterate, print_frame

while True:
  try:
    data = json.loads(Aio.receive_stream())
  except json.JSONDecodeError as exc:
    print(f"(Error: Received stream bad: {exc}")
    continue
  iterate(print_frame, data["stream"])