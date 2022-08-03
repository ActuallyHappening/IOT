import machine
import uasyncio as asio


async def off(pin: int):
    led = machine.Pin(pin, machine.Pin.OUT)
    led.off()

async def on(pin: int):
    led = machine.Pin(pin, machine.Pin.OUT)
    led.on()

async def blink(cmd: str):
    '''Blink like "2" or "2 4", first num is pin and optional second is time in seconds'''
    parsed = cmd.lower().split(" ")
    num = len(parsed)
    try:
      pinNum = int(parsed[0])
    except ValueError as exc:
        raise ValueError(f"Invalid pin number for cmd: {cmd}") from exc
    if num == 1:
        await on(pinNum)
        await asio.sleep(2)
        await off(pinNum)
    elif num == 2:
        blinkLen = int(parsed[1])
        await on(pinNum)
        await asio.sleep(blinkLen)
        await off(pinNum)
    else: raise ValueError(f"Invalid command: {cmd}: Too many args")
    
async def __execute__(cmd: str):
    parsed = cmd.lower().split(" ")
    tlc = parsed[0]
    num = len(parsed)
    if tlc == "blink":
      if num == 1:
        await blink("2 4")
      else:
        await blink(" ".join(cmd[1:]))
    else:
      try:  
        pinNum = int(parsed[1])
      except ValueError as exc:
        raise ValueError(f"Invalid pin number for cmd: {cmd}") from exc
      if tlc == "on": await on(pinNum)
      elif tlc == "off": await off(pinNum)
      else: raise ValueError(f"Invalid command: {cmd}: Unknown command")