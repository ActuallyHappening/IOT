# from typing import Tuple # micropython doesn't support typing
import machine
import uasyncio as asio
import gpio
from gpio import __execute__ as gpio_do

motor1 = (15, 2)
motor2 = (5, 18)
motors = (motor1, motor2)

async def _do(tlc: str, param1: int = None, param2: int = None) -> None:
  
    # If param2 not exits, then motor uses param1 as motor num
    # If param2 exists, then motor is (param1, param2)
    _motor = None # type Tuple[int, int]| None
    if param1:
      if param2: _motor = (param1, param2)
      else:
        if param1 >= len(motors):
          raise ValueError(f"Invalid motor num {param1}: Len of motors is {len(motors)}")
        else:
          _motor = motors[param1]
    else:
      _motor = motors[0] # implicit motor1 if not given
    print(f"Command received: {tlc} {_motor}")
    if tlc == "forward":
        await forward(_motor)
    elif tlc == "backward":
        await backward(_motor)
    elif tlc == "step":
        await step(_motor)
    elif tlc == "stop":
        await stop(_motor)
    else:
      raise ValueError(f"Invalid tlc cmd: {tlc}")
      

async def __execute__(cmd: str):
    parsed = cmd.lower().split(" ")
    tlc = parsed[0]
    num = len(parsed)
    if num == 1:
        # 'forward' with implicit motor = 1st
        await _do(tlc, int(parsed[1]))
    elif num == 2:
        # 'forward 2' with explicit motor = nth
        try:
            motorNum = int(parsed[1])
        except ValueError as exc:
            raise ValueError(f"Invalid motor number for cmd: {cmd}") from exc
        await _do(tlc, motorNum)
    elif num == 3:
        # 'forward pin1 pin2' with given pins
        try:
            pin1Num = int(parsed[1])
            pin2Num = int(parsed[2])
        except ValueError as exc:
            raise ValueError(f"Invalid pin numbers for cmd: {cmd}") from exc
        await _do(tlc, pin1Num, pin2Num)

async def forward(motor: "Tuple[int, int]") -> None:
    await gpio_do(f"on {motor[0]}")
    await gpio_do(f"off {motor[1]}")

async def backward(motor: "Tuple[int, int]") -> None:
    await gpio_do(f"off {motor[0]}")
    await gpio_do(f"on {motor[1]}")

async def stop(motor: "Tuple[int, int]") -> None:
    await gpio_do(f"off {motor[0]}")
    await gpio_do(f"off {motor[1]}")

async def step(motor: "Tuple[int, int]", time: int = 1) -> None:
    await forward(motor)
    await asio.sleep(time)
    await stop(motor)
    