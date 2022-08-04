from cmd import do
try:
  import uasyncio as asio
except ImportError:
  import asyncio as asio # type: ignore

from lib.ble import begin

def ble_received(msg):
  do(msg)

def main():
  do("forall motor stop")
  # do("ble begin")
  asio.run(begin(handler=ble_received))
  
if __name__ == "__main__":
  main()