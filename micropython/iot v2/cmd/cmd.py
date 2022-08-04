from .. import lib

async def do(cmd: str):
    parsed = cmd.lower().split(" ")
    tlc = parsed[0]
    _cmd = cmd[1:]
    if tlc == "ble":
        await lib.ble.BLE.__execute__(_cmd)
    elif tlc == "aio":
        await lib.aio.AIO.__execute__(_cmd)
    elif tlc == "wifi":
        await lib.wifi.WIFI_TODO.__execute__(_cmd)
    elif tlc == "gpio":
        await lib.gpio.GPIO.__execute__(_cmd)
    elif tlc == "motor":
        await lib.gpio.hbridge.__execute__(_cmd)
    else:
        raise ValueError(f"Invalid tlc for cmd: {cmd}")
