from .lib.aio import __execute__ as aio
from .lib.ble import __execute__ as ble
from .lib.gpio import __execute__ as gpio
from .lib.wifi import __execute__ as wifi
from .lib.gpio.hbridge import __execute__ as motor

async def do(cmd: str):
    parsed = cmd.lower().split(" ")
    tlc = parsed[0]
    _cmd = cmd[1:]
    if tlc == "ble":
        await ble(_cmd)
    elif tlc == "aio":
        await aio(_cmd)
    elif tlc == "wifi":
        await wifi(_cmd)
    elif tlc == "gpio":
        await gpio(_cmd)
    elif tlc == "motor":
        await motor(_cmd)
    else:
        raise ValueError(f"Invalid tlc for cmd: {cmd}")