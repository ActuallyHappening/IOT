from blelib import ble_uart_peripheral as ble_DO

__uart = None
_uart_buffer = "";

def dualLog(msg, ble=False, default=True, *, defaultPrint=print, __prefix__=""):
    if default:
        defaultPrint(f"{__prefix__}{msg}")
    if ble and __uart:
        __uart.write(f"{__prefix__}{msg}\n")

async def __execute__(command: str, *, logger=dualLog, **kwargs):
    logger(f"$> <ble.py> execute: {command}")
    parsed = command.lower().split(" ")
    if parsed[0] == "send":
      await send(" ".join(command.split(" ")[1:]), logger=logger, **kwargs)
    elif parsed[0] == "receive":
      return _uart_buffer
    elif parsed[0] == "begin":
      await begin(logger=logger, **kwargs)
    else:
      logger(f"$> <ble.py> FAILED execute: {command}\nNo found command from send|receive|begin, got {parsed[0]}", True)
    logger(f"$< <ble.py> executed: {command}")

def _bluetoothCallback(msg): return print(
    f"$< <ble.py> received: {msg}")

__implicitRetry = False


async def send(msg=..., *, __constructor__=..., logger=dualLog, **kwargs):
    global __implicitRetry
    if msg is ...:
      msg = __constructor__
      if __constructor__ is ...:
        raise ValueError("No message given (no __constructor__ specified either)")

    logger(f"!> <ble.py> send: {msg}")
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

async def begin(*, logger=dualLog, handler=_bluetoothCallback, **kwargs):
    global __uart
    logger("$> <ble.py> Beginning ...")

    __uart = ble_DO._begin(callback=handler)
    __uart.write(
        str("$> Beginning <ble.py>.py (begin) bluetooth ...") + '\n')

    logger("$> Finished <ble.py>.py (begin) bluetooth")