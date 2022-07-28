import json
from .lib.AIO import Aio
from .lib.ThermalSensor.Extract_raw import iterate

def _step(
  method,
  callback,
):
  data = method()
  callback(data)

def _method():
  return list(iterate())

def _send(data):
  try:
    Aio.send_stream_data(data)
  except json.JSONDecodeError:
    print('JSONDecodeError: Cannot jsonify data :(')
    Aio.status_send_code("JSONDecodeError - pi.py")

def step():
  _step(
    method = _method,
    callback = _send,
  )

def main():
  while True: 
    step()

if __name__ == "__main__":
  main()
