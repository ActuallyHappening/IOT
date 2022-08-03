import time
from .command import Command, _timeoutWrapper
import uasyncio as asio


@_timeoutWrapper
async def time_interval(interval, *, asioCallback, logger=print, forever=True, **overflow):
    """
    Every interval seconds, `await callback()`;
    If `False` is returned and forever is `False`, exit / `return` from loop
    """
    __passage__ = 0  # Passage of time in seconds
    while True:
        await asio.sleep(interval)
        __passage__ += interval
        if await asioCallback(__passage__=__passage__) is False and forever is False:
            return


async def time_logger(interval, *, __prefix__="Time Logged", logger=print, **kwargs):
    async def aCallback(*, __passage__):
        logger(f"{__prefix__}: {__passage__}")
    await time_interval(interval=interval, asioCallback=aCallback, forever=True, logger=logger, **kwargs)


async def time_trigger(interval, *, logger=print):
    async def aCallback(__passage__):
        logger(f"Time Logged: {__passage__}")
        return False  # Exit since forever=False
    await time_interval(interval=interval, asioCallback=aCallback, forever=False)


async def second_logger(*, __prefix__="Seconds Logged", logger=print, **kwargs):
    await time_logger(interval=1, __prefix__=__prefix__, logger=logger, **kwargs)


async def second_timer(*, __prefix__="Second Triggered", logger=print, **kwargs):
    await time_trigger(interval=1, __prefix__=__prefix__, logger=logger, **kwargs)

commands = {
    "Seconds Logger": Command(second_logger),
    "Seconds Timer": Command(second_timer),
}
