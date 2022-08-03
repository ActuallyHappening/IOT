import time
import uasyncio as asio

from . import MachineCommands
from . import TimeCommands
from . import ServerCommands
from .command import Command as CommandClass

prebuilt = dict()


def importSet(commands):
    for name, command in commands.items():
        prebuilt[name] = command
        if command.name is None:
            # Set name of command to handle used to call it :)
            command.name = str(name)


importSet(MachineCommands.commands)
importSet(TimeCommands.commands)
importSet(ServerCommands.commands)


async def _execute(commands, *, time=..., logger=print, **overflow):
    if len(overflow) > 0:
        logger(f"OH oh, overflow detected in func _execute: {overflow=}")
    if type(commands) is not list:
        # Executing a single task, just put it in a list for simplicity
        commands = [commands]
    # Execute given list of commands
    logger(f"## Executing ({len(commands)} num. tasks) ...")
    for command in commands:
        if type(command) is not CommandClass:
            logger("## ERROR: Command is not of type CommandClass")
            return
        logger(
            f"#\tMaking Task {str(command.name)+' ' if hasattr(command,'name') else '__'}...")
    if time is ...:
        logger(f"#> Note: {time=}, is not set, running until completion")
    logger(f"## Holding tasks ({time=} seconds) ...")
    await asio.gather(*[command.asioDo(time=time, logger=logger) for command in commands])
    logger("## Released tasks.")


def execute(*args, **kwargs):
    asio.run(_execute(*args, **kwargs))
