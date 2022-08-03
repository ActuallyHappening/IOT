import uasyncio as asio

from .command import Command, _timeoutWrapper


@_timeoutWrapper
async def Nothing(*, logger=print, **kwargs):
    logger("#<> Nothing called :)")


@_timeoutWrapper
async def Wait(*, time=10, logger=print, **overflow):
    if len(overflow) > 0:
        logger(f"OH oh, overflow detected in func Wait: {overflow=}")
    logger(f"#> Waiting {time=} seconds")
    time.sleep(time)

commands = {
    ...: Command(Nothing),
    "Nothing": Command(Nothing),
    "Wait": Command(Wait),
}
