from cmd import do
try:
  import uasyncio as asio
except ImportError:
  import asyncio as asio # type: ignore

from lib.ble import begin, dualLog, send

"""
Possible codes that AIO expects:
0 - Offline

>0 - ONLINE
1 - Online
2 - Online, received well
3 - Online, just started
4 - Online, just exiting?
5 - Online, regular ping

>99 - ONLINE - ERROR
100 - Online, ERROR

"""

def ble_received(msg):
  try:
    do(msg)
  except Exception as e:
    dualLog(f"Exception caught on callback level: {e}", True)
    send("100")
    raise e
  else:
    send("2")

async def ping_status():
  while True:
    dualLog("Regular Pinging ...", True)
    send("5")
    await asio.sleep(8)

def main():
  # do("forall motor stop")
  # do("ble begin") # Can't do this, as handler callback needs to be passed in
  try:
    dualLog("Starting BLE ...", True)
    
    asio.run(begin(handler=ble_received))
    
    # asio.run(ping_status()) # blocking
    
    dualLog("Finished ping ...", True)
    send("4")
  except Exception as e:
    dualLog(f"!!! Exiting ... {e}", True)
    send("0")
    raise e
  
if __name__ == "__main__":
  print("Executing main.py as __main__ ...")
  main()