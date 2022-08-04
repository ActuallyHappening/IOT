from blelib import ble_uart_peripheral as ble_DO

__uart = None
_uart_buffer = "";

def dualUartPrint(msg, *, defaultPrint=print, shouldDefaultPrint=True, __prefix__=""):
    if shouldDefaultPrint:
        defaultPrint(f"{__prefix__}{msg}")
    if __uart:
        __uart.write(f"{__prefix__}{msg}\n")

async def __execute__(command: str, *, logger=dualUartPrint, **kwargs):
    logger(f"$> BluetoothCommands execute: {command}")
    parsed = command.lower().split(" ")
    if parsed[0] == "send":
      await send(command, logger=logger, **kwargs)
    elif parsed[0] == "receive":
      return _uart_buffer
    elif parsed[0] == "begin":
      await begin(logger=logger, **kwargs)
    logger(f"$< BluetoothCommands execute: {command}")

def _bluetoothCallback(msg): return print(
    f"$< BluetoothCommands received: {msg}")

__implicitRetry = False


async def send(msg=..., *, __constructor__=..., logger=dualUartPrint, **kwargs):
    global __implicitRetry
    if msg is ...:
      msg = __constructor__
      if __constructor__ is ...:
        raise ValueError("No message given (no __constructor__ specified either)")

    logger(f"!> BluetoothCommands send: {msg}")
    if __uart:
        __uart.write(f"{msg}\n")
    else:
        if __implicitRetry:
            logger("!!> No uart connected: Already retried! FAILED BLUETOOTH")
            __implicitRetry = False
            return
        logger(f"!> No uart connected: Implicitely beginning bluetooth ...")
        await begin(logger=logger)
        __implicitRetry = True
        await send(msg, logger=logger, **kwargs)

async def begin(*, logger=dualUartPrint, handler=_bluetoothCallback, **kwargs):
    global __uart
    logger("$> BluetoothCommands Beginning ...")

    __uart = ble_DO._begin(callback=handler)
    __uart.write(
        str("$> Beginning BluetoothCommands.py (begin) bluetooth ...") + '\n')

    logger("$> Finished BluetoothCommands.py (begin) bluetooth")


def ThetaHandler(msg, logger=dualUartPrint, **kwargs):
    global _uart_buffer
    logger(f"$< BluetoothCommands received: {msg}")
    _uart_buffer = msg


async def ProjectTheta(*, logger=dualUartPrint, handler=..., __constructor__=..., **kwargs):
    """
    Setting handler and __constructor__ will favour the handler over the __constructor__
    """
    logger("$> BluetoothCommands Project Theta ...")
    if handler is ...:
      if __constructor__ is ...:
        handler = ThetaHandler
      else:
        handler = __constructor__

    await begin(logger=logger, handler=handler, **kwargs)
    await send("PROJECT THETA is a go :)", logger=logger, **kwargs)

    logger("$> Finished BluetoothCommands.py (Project Theta) bluetooth")
