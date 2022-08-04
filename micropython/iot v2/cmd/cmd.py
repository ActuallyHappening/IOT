from .. import lib

async def do(command: str):
    parsed = command.lower().split(" ")
    if parsed[0] == "ble":
        await lib.ble.__execute__(command[1:])