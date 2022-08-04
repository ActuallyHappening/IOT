try:
  import uasyncio as asio
except ImportError:
  import asyncio as asio # type: ignore

async def parse_processed_cmd(cmd: str):
    parsed = cmd.lower().strip().split(" ")
    tlc = parsed[0]
    _cmd = " ".join(parsed[1:])
    if tlc == "ble":
        from lib.ble import __execute__ as ble
        await ble(_cmd)
    elif tlc == "aio":
        from lib.aio import __execute__ as aio
        await aio(_cmd)
    elif tlc == "wifi":
        from lib.wifi import __execute__ as wifi
        await wifi(_cmd)
    elif tlc == "gpio":
        from lib.gpio import __execute__ as gpio
        await gpio(_cmd)
    elif tlc.startswith("motor"):
        from lib.gpio.hbridge import __execute__ as motor
        await motor(_cmd)
    else:
        raise ValueError(f"Invalid tlc for cmd: {cmd}")

async def execute(cmd: str):
    # Check for 'for' loops:
    parsed = cmd.strip().lower().split(" ")
    tlc = parsed[0]
    if tlc == "forall":
        if len(parsed) < 2:
          raise ValueError(f"Invalid forall command: {cmd}: Too few args")
        if parsed[1].startswith("motor"):
            # e.g. execute('forall motors forward') or execute('forall motor step 10')
            # This is implementation aware! Not a good design practice!
            from lib.gpio.hbridge import motors
            
            motorCmd = parsed[2:] # forward <n> <n> <v?>
            
            # 0 forall motor forward
            # 1 forall motor forward  2
            # 1 forall motor step     10
            # 2 forall motor step     10  2   <motornum> <step>
            # 2 forall motor forward  69  42  <pin1> <pin2>
            
            if len(motorCmd) == 1:
                
                for motor in motors:
                    await parse_processed_cmd(f"motor {motorCmd[1]} {motor}") 
            if len(motorCmd) == 2:
                # e.g. execute('forall motors backward')
                for motor in motors:
                    await parse_processed_cmd(f"motor {motorCmd[1]} {motor}")
            elif len(motorCmd) == 4:
                # e.g. execute('forall motor step 10')
                for motor in motors:
                    await parse_processed_cmd(f"motor {motorCmd[1]} {motorCmd[2]} {motor}")
            else:
              raise ValueError(f"Invalid forall command for second arg motor: {cmd}: Wrong arg number to motor\nUsage: forall motors forward | forall motors step 10")
        else:
          raise ValueError(f"Invalid tlc forall for second arg {parsed[1]}: {cmd}")

    
def do(*x):
  asio.run(execute(*x))