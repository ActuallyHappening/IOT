import json
from .lib.AIO import aio
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
    aio.send_stream_data(data)
  except json.JSONDecodeError:
    print('JSONDecodeError: Cannot jsonify data :(')
    aio.pi_status_send_code("JSONDecodeError - pi.py")

def step():
  aio.pi_ping()
  _step(
    method = _method,
    callback = _send,
  )

def main():
  print("Beginning pi ...")
  while True: 
    step()

if __name__ == "__main__":
  main()
