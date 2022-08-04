async def do(cmd: str):
    parsed = cmd.lower().split(" ")
    tlc = parsed[0]
    _cmd = cmd[1:]
    if tlc == "ble":
        from lib.ble import __execute__ as ble
        await ble(_cmd)
    elif tlc == "aio":
        from lib.aio import __execute__ as aio
        await aio(_cmd)
    elif tlc == "wifi":
        from lib.wifi import __execute__ as wifi
        await wifi(_cmd)
    elif tlc == "gpio":
        from lib.gpio import __execute__ as gpio
        await gpio(_cmd)
    elif tlc == "motor":
        from lib.gpio.hbridge import __execute__ as motor
        await motor(_cmd)
    else:
        raise ValueError(f"Invalid tlc for cmd: {cmd}")