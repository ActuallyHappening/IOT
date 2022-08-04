from cmd import do
try:
  import uasyncio as asio
except ImportError:
  import asyncio as asio # type: ignore

def main():
  do("forall motor stop")
  do("ble begin")
  
if __name__ == "__main__":
  main()