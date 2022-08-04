try: import machine
except: print("No machine module")
try: import uasyncio as asio
except: import asyncio as asio # type: ignore

async def off(pin: int):
    print(f"Pin {pin} off")
    led = machine.Pin(pin, machine.Pin.OUT)
    led.off()

async def on(pin: int):
    print(f"Pin {pin} on")
    led = machine.Pin(pin, machine.Pin.OUT)
    led.on()

async def blink(cmd: str):
    '''Blink like "2" or "2 0.5", first num is pin and optional second is time in seconds'''
    parsed = cmd.lower().split(" ")
    num = len(parsed)
    try:
      pinNum = int(parsed[0])
    except ValueError as exc:
        raise ValueError(f"Invalid pin number for cmd: {cmd}") from exc
    if num == 1:
        await on(pinNum)
        await asio.sleep(0.3)
        await off(pinNum)
        await asio.sleep(0.3)
    elif num == 2:
        blinkLen = float(parsed[1])
        await on(pinNum)
        await asio.sleep(blinkLen)
        await off(pinNum)
        await asio.sleep(blinkLen)
    else: raise ValueError(f"Invalid command: {cmd}: Too many args")
    
async def __execute__(cmd: str):
    parsed = cmd.split(" ") # type List[str]
    _cmd: str = " ".join(parsed[1:])
    tlc: str = parsed[0]
    num = len(parsed)
    if tlc == "blink":
      if num == 1:
        await blink("2 4")
      else:
        await blink(_cmd)
    else:
      try:  
        pinNum = int(parsed[1])
      except ValueError as exc:
        raise ValueError(f"Invalid pin number for cmd: {cmd}") from exc
      if tlc == "on": await on(pinNum)
      elif tlc == "off": await off(pinNum)
      else: raise ValueError(f"Invalid command: {cmd}: Unknown command")