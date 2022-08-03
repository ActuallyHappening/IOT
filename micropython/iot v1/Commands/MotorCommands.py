import uasyncio as asio

from .command import Command, _timeoutWrapper


@_timeoutWrapper
async def MotorStart(*, logger=print, **kwargs):
    logger("#<> Nothing called :)")


@_timeoutWrapper
async def MotorStop(*, time=10, logger=print, **overflow):
    if len(overflow) > 0:
        logger(f"OH oh, overflow detected in func Wait: {overflow=}")
    logger(f"#> Waiting {time=} seconds")
    time.sleep(time)

commands = {
    "Motor Start": Command(Nothing),
    "Motor Stop": Command(Wait),
    "Motor Step": Command(Wait),
}
