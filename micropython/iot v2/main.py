from cmd import do
try:
  import uasyncio as asio
except ImportError:
  import asyncio as asio

def main():
  do("forall motor forward")
  
if __name__ == "__main__":
  main()