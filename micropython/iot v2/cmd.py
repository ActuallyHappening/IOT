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
        from lib.hbridge import __execute__ as motor
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
            from lib.hbridge import motors
            
            motorCmd = parsed[2:] # forward <n> <n> <v?>
            print(f"Forall motor: {' '.join(motorCmd)}")
            
            # 0 forall motor forward
            # 1 forall motor forward  2
            # 1 forall motor step     10
            # 2 forall motor step     10  2   <motornum> <step>
            # 2 forall motor forward  69  42  <pin1> <pin2>
            
            if len(motorCmd) == 1:
                # forall motor 1:forward
                if motorCmd[0].startswith("step"):
                    raise ValueError(f"Invalid forall motor step command: {cmd}\nCannot step like `motor step <motorN>`")
                for motorN in range(1, len(motors) + 1):
                    await parse_processed_cmd(f"motor {motorCmd[0]} {motorN}")
            if len(motorCmd) == 2:
                # e.g. execute('forall motors 1:step 2:<v>?'), 'step 1.5'
                if not motorCmd[0].startswith("step"):
                    raise ValueError(f"Invalid forall motor !step command: {cmd}\nCannot forward|back|step like `motor stop <motorN> <?? argv[0] ??>`")
                for motor in motors:
                  # step case: execute('forall motor step 10sec') => execute('motor step {motorN} 10seconds')
                    await parse_processed_cmd(f"motor step {motor} {motorCmd[1]}")
            else:
              raise ValueError(f"Invalid forall command for second arg motor: {cmd}: Wrong arg number to motor\nUsage: forall motors forward | forall motors step 0.25")
        else:
          raise ValueError(f"Invalid tlc forall for second arg {parsed[1]}: {cmd}")
    else:
      await parse_processed_cmd(cmd)

    
def do(*x):
  asio.run(execute(*x))