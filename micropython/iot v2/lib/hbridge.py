import machine
import uasyncio as asio
import gpio
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
    if motorN >= len(motors) or motorN < 0:
        raise ValueError(f"Unknown motor for motorN for cmd (motor) int({motorN}): {cmd}")
    return motors[motorN]

def _get_motor_num(motorN: str, cmd: str = "<unknown cmd>") -> int:
    try:
        motorNum = int(motorN)
    except ValueError as exc:
        raise ValueError(f"Invalid motor number for cmd (motor): {cmd}")
    return motorNum

async def __execute__(cmd: str):
    parsed = cmd.lower().split(" ")
    tlc = parsed[0]
    num = len(parsed)
    if tlc == "forward":
        if num == 1:
            # 'forward' with implicit motor = 1st
            await forward(motor1)
        elif num == 2:
            # 'forward 2' with explicit motor = nth
            try:
                motorNum = int(parsed[1])
            except ValueError as exc:
                raise ValueError(f"Invalid motor number for cmd: {cmd}") from exc
            if motorNum == 1:
                await forward(motor1)
            elif motorNum == 2:
                await forward(motor2)
            else:
                raise ValueError(f"Invalid motor number for cmd: {cmd}")
    else: raise ValueError(f"Invalid command: {cmd}: Unknown command")

async def forward(motor: "Tuple[int, int]") -> None:
    await gpio_do(f"on {motor[0]}")
    await gpio_do(f"off {motor[1]}")

async def backward(motor: "Tuple[int, int]") -> None:
    await gpio_do(f"off {motor[0]}")
    await gpio_do(f"on {motor[1]}")

async def stop(motor: "Tuple[int, int]") -> None:
    await gpio_do(f"off {motor[0]}")
    await gpio_do(f"off {motor[1]}")

async def step(motor: Tuple[int, int], time: int = 1) -> None:
    await forward(motor)
    await asio.sleep(time)
    await stop(motor)
    