import json
from .lib.AIO import Aio
from .lib.ThermalSensor.Extract_raw import iterate

def step(fn = lambda data: Aio.send_stream_data(data)):
  data = list(iterate())
  fn(data)

def main():
  while True: 
    step()

if __name__ == "__main__":
  main()
