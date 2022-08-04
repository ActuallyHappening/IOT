# from typing import Tuple # micropython doesn't support typing
try:
    from __future__ import annotations
except: ...
try:
  import uasyncio as asio
except:
  import asyncio as asio # type: ignore
from gpio import __execute__ as gpio_do

motor1 = (15, 2)
motor2 = (5, 18)
motor3 = (13, 12)
motors = (motor1, motor1, motor2, motor3) # 0 index is implicit motor

async def _do(tlc: str, *, p1: int = motors[0][0], p2: int = motors[0][1], v: float = 0.5) -> None:
    """Executes a motor command, tlc = 'forward' | 'backward' | 'step' | 'stop'
    """
    
    _motor = (p1, p2)
    
    print(f"Command received (motor): {tlc} {_motor}")
    
    if tlc == "forward":
        await forward(_motor)
    elif tlc == "backward":
        await backward(_motor)
    elif tlc == "step":
        await step(_motor, time=v)
    elif tlc == "stop":
        await stop(_motor)
    else:
      raise ValueError(f"Invalid tlc cmd: {tlc}")

def _get_motor(motorN: int, cmd: str = "<unknown cmd>") -> "Tuple[int, int]":
    if motorN < 1 or motorN > len(motors):
        raise ValueError(f"Unknown motor for motorN for cmd (motor) int({motorN}): {cmd}")
    return motors[motorN]

def _get_motor_num(motorN: str, cmd: str = "<unknown cmd>") -> int:
    try:
        motorNum = int(motorN)
    except ValueError as exc:
        raise ValueError(f"Invalid motor number for cmd (motor): {cmd}")
    return motorNum

async def __execute__(cmd: str):
    """Executes a motor command, tlc = 'forward' | 'backward' | 'step' | 'stop'
    e.g. execute('forward 1') or execute('step 2 1.5') or execute('step 15 5 2.5')
    
    X       step
    X       forward
    X       backward
    X       step
    
    X       step <motorN>
    Y   forward <motorN>
    Y   backward <motorN>
    Y   stop <motorN>
    
    Y   step <motorN> <v>
    Y   forward <pin1> <pin2>
    Y   backward <pin1> <pin2>
    Y   stop <pin1> <pin2>
    
    Y   step <pin1> <pin2> <v>
    """
  
    parsed = cmd.split(" ")
    tlc = parsed[0]
    num = len(parsed)
    if num == 1:
        raise ValueError(f"Invalid command (motor): {cmd}: Too few args <strict>")
    elif num == 2:
        # 'forward 2' with explicit motor = nth
        # 'backward 2' with explicit motor = nth
        if tlc.startswith("step"):
          raise ValueError(f"Invalid command (motor): {cmd}: Too few args <strict>")
        motor = _get_motor(_get_motor_num(parsed[1], cmd), cmd)
        await _do(tlc, p1=motor[0], p2=motor[1])
    elif num == 3:
        # 'forward pin1 pin2' with given pins
        # OR 'step motorN v' with given motor and v (time in seconds)
        if tlc.startswith("step"):
          try:
              pin2 = float(parsed[2])
          except ValueError:
              raise ValueError(f"Invalid v for cmd (motor): {cmd}")
          motor = _get_motor(_get_motor_num(parsed[1], cmd), cmd)
          await _do(tlc, p1=motor[0], p2=motor[1], v=pin2)
        else:
          try:
              pin1 = int(parsed[1])
              pin2 = int(parsed[2])
          except ValueError as exc:
              raise ValueError(f"Invalid pin numbers for cmd !step (motor): {cmd}")
          await _do(tlc, p1=pin1, p2=pin2)
    elif num == 4:
        # 'step pin1 pin2 v' with given pins and v (time in seconds)
        if not tlc.startswith("step"):
            raise ValueError(f"Invalid command !step (motor): {cmd}: Too many args <strict>")
        try:
          p1 = int(parsed[1])
          p2 = int(parsed[2])
          v = float(parsed[3])
        except ValueError as exc:
          raise ValueError(f"Invalid pin/v numbers for cmd: {cmd}")
        await _do(tlc, p1=p1, p2=p2, v=v)

async def forward(motor: "Tuple[int, int]") -> None:
    await gpio_do(f"on {motor[0]}")
    await gpio_do(f"off {motor[1]}")

async def backward(motor: "Tuple[int, int]") -> None:
    await gpio_do(f"off {motor[0]}")
    await gpio_do(f"on {motor[1]}")

async def stop(motor: "Tuple[int, int]") -> None:
    await gpio_do(f"off {motor[0]}")
    await gpio_do(f"off {motor[1]}")

async def step(motor: "Tuple[int, int]", time: float = 1) -> None:
    await forward(motor)
    await asio.sleep(time)
    await stop(motor)
    