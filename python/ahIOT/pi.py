import json
from lib.AIO import Aio
from lib.ThermalSensor.Extract_raw import iterate

def main():
  while True: 
    Aio.send_stream_data(list(iterate()))

if __name__ == "__main__":
  main()
