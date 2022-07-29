import json
from .lib.AIO import aio
from .lib.ThermalSensor.Process_raw import iterate

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
  # Step for uploading data
  _step(
    method = _method,
    callback = _send,
  )
  # Other steps could be added below, such as 8x8 LED matrix

def main():
  print("Beginning pi ...")
  while True: 
    step()

if __name__ == "__main__":
  main()
