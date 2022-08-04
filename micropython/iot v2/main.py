from cmd import do
try:
  import uasyncio as asio
except ImportError:
  import asyncio as asio # type: ignore

from lib.ble import begin

def main():
  do("forall motor stop")
  do("ble begin")
  begin(handler=do)
  
if __name__ == "__main__":
  main()