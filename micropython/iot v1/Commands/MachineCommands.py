import machine
import uasyncio as asio

from .command import Command, _timeoutWrapper
from extensions import constants


@_timeoutWrapper
async def led_state(led, *, state=1, logger=print, **overflow):
    if len(overflow) > 0:
        logger(f"OH oh, overflow detected in func led_state: {overflow=}")
    logger(f"#> Setting LED {led=} to {state=}")
    led.value(state)


@_timeoutWrapper
async def led_on(led, *, **_kwargs):
    await led_state(led, state=1, **_kwargs)


@_timeoutWrapper
async def led_off(led, *, **_kwargs):
    await led_state(led, state=0, **_kwargs)


@_timeoutWrapper
async def pin_state(pin, *, state=1, logger=print, **_kwargs):
    try:
        led = machine.Pin(pin, machine.Pin.OUT)
    except ValueError as exc:
        logger(f"#> Error (Pin probably invalid): {exc=}")
        return
    await led_state(led, state=state, logger=logger, **_kwargs)


@_timeoutWrapper
async def pin_on(pin, *, **_kwargs):
    await pin_state(pin, state=1, **_kwargs)


@_timeoutWrapper
async def pin_off(pin, *, **_kwargs):
    await pin_state(pin, state=0, **_kwargs)


@_timeoutWrapper
async def blink_led(led, *, period=0.5, logger=print, finishState=False, **overflow):
    if len(overflow) > 0:
        logger(f"OH oh, overflow detected in func blink_led: {overflow=}")
    logger(
        f"blink_led called with args {led=}, {period=}, {logger=}, {finishState=}")
    logger(f"Blinking LED {led=} every {period=} seconds")
    try:
        while True:
            led.on()
            await asio.sleep(period)
            led.off()
            await asio.sleep(period)
    finally:
        led.value(finishState)
        logger(f"#< Closing blink_led with {finishState=}, and {led=}")


async def blink_pin(number, logger=print, **kwargs):
    logger(f"blink_pin called with args {number=}, {kwargs=}")
    try:
        led = machine.Pin(number, machine.Pin.OUT)
    except ValueError as exc:
        logger(f"#> Error (Pin probably invalid): {exc=}")
        return
    await blink_led(led, logger=logger, **kwargs)


async def blink_builtin(*, logger=print, **kwargs):
    logger(f"blink_builtin called with args {kwargs=}")
    await blink_pin(constants["machine"]["TEST_BUILTIN"], logger=logger, **kwargs)


async def blink_red(**kwargs):
    await blink_pin(constants["machine"]["TEST_RED"], **kwargs)


async def blink_yellow(**kwargs):
    await blink_pin(constants["machine"]["TEST_YELLOW"], **kwargs)


async def blink_green(**kwargs):
    await blink_pin(constants["machine"]["TEST_GREEN"], **kwargs)


async def blink_blue(**kwargs):
    await blink_pin(constants["machine"]["TEST_BLUE"], **kwargs)


commands = {
    "Blink Builtin": Command(blink_builtin),
    "Blink Red": Command(blink_red),
    "Blink Yellow": Command(blink_yellow),
    "Blink Green": Command(blink_green),
    "Blink Blue": Command(blink_blue),
    "Pin On": Command(pin_on),
    "Pin Off": Command(pin_off),
    "Led On": Command(led_on),
    "Led Off": Command(led_off),
    "Blink Pin": Command(blink_pin),
}
