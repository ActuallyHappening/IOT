from .command import Command, _timeoutWrapper
from Bluetooth import ble_uart_peripheral as ble_DO


def _bluetoothCallback(msg): return print(
    f"$< BluetoothCommands received: {msg}")


__uart = None


def dualUartPrint(msg, *, defaultPrint=print, shouldDefaultPrint=True, __prefix__=""):
    if shouldDefaultPrint:
        defaultPrint(f"{__prefix__}{msg}")
    if __uart:
        __uart.write(f"{__prefix__}{msg}\n")


__implicitRetry = False



@_timeoutWrapper
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


@_timeoutWrapper
async def begin(*, logger=dualUartPrint, handler=_bluetoothCallback, **kwargs):
    global __uart
    logger("$> BluetoothCommands Beginning ...")

    __uart = ble_DO._begin(callback=handler)
    __uart.write(
        str("$> Beginning BluetoothCommands.py (begin) bluetooth ...") + '\n')

    logger("$> Finished BluetoothCommands.py (begin) bluetooth")


def ThetaHandler(msg, logger=dualUartPrint, **kwargs):
    logger(f"$< BluetoothCommands received: {msg}")


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

commands = {
    "Bluetooth Begin": Command(begin),
    "Bluetooth Send": Command(send),
    "Bluetooth Project Theta": Command(ProjectTheta),
}
