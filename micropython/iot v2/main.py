from cmd import do
import time
try:
  import uasyncio as asio
except ImportError:
  import asyncio as asio # type: ignore

from lib.ble import begin, dualLog, post

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

_ping = True;

def ble_received(msg: str):
  global _ping;
  if msg.startswith("pingstop"):
    _ping = False;
    post("6")
    return
  if msg.startswith("pingstart"): 
    _ping = True;
    post("6")
    return
  try:
    do(msg)
  except Exception as e:
    dualLog(f"Exception caught on callback level: {e}", True)
    post("100")
    raise e
  else:
    post("2")

def ping_status():
  global _ping;
  while True:
    if not _ping:
      continue
    dualLog("Regular Pinging ...", False)
    post("5")
    time.sleep(8)

def main():
  do("forall motor stop")
  # do("ble begin") # Can't do this, as handler callback needs to be passed in
  try:
    dualLog("Starting BLE ...", True)
    
    asio.run(begin(handler=ble_received))
    
    ping_status() # blocking
    
    dualLog("Finished ping ...", True)
    post("4")
  except Exception as e:
    dualLog(f"!!! Exiting ... {e}", True)
    post("0")
    raise e
  
if __name__ == "__main__":
  print("Executing main.py as __main__ ...")
  main()